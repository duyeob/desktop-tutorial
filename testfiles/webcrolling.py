import requests
from bs4 import BeautifulSoup
import time # 요청 간 지연 시간을 위해 필요

# PQI 사이트의 특정 목록 페이지 URL (예시, 실제 URL 확인 필요)
base_url = 'https://pqi.or.kr/search/list' # 예시
# 필요한 경우 HTTP 헤더 설정 (봇으로 인식되지 않게 User-Agent 등 설정)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

all_cert_data = []
page_num = 1 # 시작 페이지 번호

while True:
    # 페이지 URL 구성 (PQI 사이트의 페이지네이션 방식에 따라 달라짐)
    # 예: 쿼리 파라미터 사용 시 ?page=1, ?page=2
    page_url = f"{base_url}?page={page_num}" # 예시

    print(f"크롤링 중: {page_url}")

    try:
        response = requests.get(page_url, headers=headers)
        response.raise_for_status() # 200 응답 코드가 아니면 예외 발생

        soup = BeautifulSoup(response.text, 'html.parser')

        # --- 여기서부터 PQI 사이트의 HTML 구조에 맞춰 정보 추출 ---
        # 예: 자격증 목록이 특정 div 안에 있고, 각 항목이 li 태그인 경우
        cert_items = soup.select('ul.cert-list li') # CSS 선택자 예시

        if not cert_items:
            # 더 이상 자격증 항목이 없으면 마지막 페이지로 간주
            print("마지막 페이지 도달. 크롤링 종료.")
            break

        for item in cert_items:
            # 각 항목에서 자격증 이름, 발행기관 등 추출 (PQI 구조에 맞춰 수정 필요)
            cert_name = item.select_one('h3.cert-name').text.strip() if item.select_one('h3.cert-name') else 'N/A'
            organizer = item.select_one('span.organizer').text.strip() if item.select_one('span.organizer') else 'N/A'
            # 추가 정보 추출...

            all_cert_data.append({
                '자격증 이름': cert_name,
                '발행기관': organizer,
                # 추출한 다른 정보 추가
            })

        # 다음 페이지로 이동
        page_num += 1

        # 서버 부하 방지를 위한 지연 시간
        time.sleep(1) # 1초 대기 (상황에 따라 조절)

    except requests.exceptions.RequestException as e:
        print(f"요청 오류 발생: {e}")
        break # 오류 발생 시 크롤링 중단
    except Exception as e:
        print(f"데이터 파싱/추출 오류 발생: {e}")
        break

# 수집된 데이터 확인 (예시)
import pandas as pd # 데이터 처리를 위해 pandas 사용 추천

if all_cert_data:
    df = pd.DataFrame(all_cert_data)
    print("\n수집된 데이터 미리보기:")
    print(df.head())

    # CSV 파일 등으로 저장
    # df.to_csv('pqi_certifications.csv', index=False, encoding='utf-8-sig')
    # print("\n데이터가 'pqi_certifications.csv' 파일로 저장되었습니다.")
else:
    print("\n수집된 데이터가 없습니다.")

