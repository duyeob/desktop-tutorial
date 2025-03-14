import datetime

class 일정관리:
    def __init__(self):
        self.일정들 = []

    def 일정추가(self, 일정, 날짜):
        self.일정들.append({"일정": 일정, "날짜": 날짜})

    def 일정제거(self, 일정):
        self.일정들 = [t for t in self.일정들 if t["일정"] != 일정]

    def 일정보기(self):
        for 일정 in self.일정들:
            print(f"일정: {일정['일정']}, 날짜: {일정['날짜']}")

    def 일정수정(self, 기존일정, 새로운일정, 새로운날짜):
        for t in self.일정들:
            if t["일정"] == 기존일정:
                t["일정"] = 새로운일정
                t["날짜"] = 새로운날짜

def main():
    일정관리자 = 일정관리()
    
    while True:
        print("\n일정 관리")
        print("1. 일정 추가")
        print("2. 일정 제거")
        print("3. 일정 수정")
        print("4. 일정 보기")
        print("5. 종료")
        
        선택 = input("선택하세요: ")
        
        if 선택 == '1':
            일정 = input("일정을 입력하세요: ")
            날짜 = input("날짜를 입력하세요 (YYYY-MM-DD): ")
            일정관리자.일정추가(일정, 날짜)
        elif 선택 == '2':
            일정관리자.일정수정(일정, 새로운일정, 새로운날짜)
            일정관리자.일정제거(일정)
        elif 선택 == '3':
            일정 = input("수정할 일정을 입력하세요: ")
            새로운일정 = input("새로운 일정을 입력하세요: ")
            새로운날짜 = input("새로운 날짜를 입력하세요 (YYYY-MM-DD): ")
            일정관리자.일정수정(일정, 새로운일정, 새로운날짜)
        elif 선택 == '4':
            일정관리자.일정보기()
        elif 선택 == '5':
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()