# 편의점 물품 재고 관리 프로그램

# 물품 정보를 관리하는 딕셔너리 생성
px = dict()  # 키: 물품명, 값: 재고량

# 최대 물품 수 제한
MAX_ITEMS = 50

# 신규 물품 재고 등록 함수
def add_item():
    if len(px) >= MAX_ITEMS:
        print(" 최대 50개까지만 등록 가능합니다.")
        return

    item_name = input("등록할 물품명을 입력하세요: ")
    if item_name in px:
        print(" 이미 등록된 물품입니다.")
    else:
        quantity = int(input("재고량을 입력하세요: "))  # 입력값을 숫자로 변환
        if quantity >= 0:
            px[item_name] = quantity
            print(f"{item_name} 물품이 {quantity}개 등록되었습니다.")
        else:
            print(" 재고량은 0 이상의 값이어야 합니다.")

# 특정 물품 재고량 증가 함수
def incre():
    item_name = input("재고량을 증가시킬 물품명을 입력하세요: ")
    if item_name not in px:
        print("등록되지 않은 물품입니다.")
    else:
        increase_amount = int(input("증가시킬 수량을 입력하세요: "))  # 입력값을 숫자로 변환
        if increase_amount >= 0:
            px[item_name] += increase_amount
            print(f"{item_name}의 재고량이 {increase_amount}개 증가되었습니다.")
        else:
            print(" 증가할 수량은 0 이상의 값이어야 합니다.")

# 특정 물품 재고량 감소 함수
def decre():
    item_name = input("재고량을 감소시킬 물품명을 입력하세요: ")
    if item_name not in px:
        print(" 등록되지 않은 물품입니다.")
    else:
        decrease_amount = int(input("감소시킬 수량을 입력하세요: "))  # 입력값을 숫자로 변환
        if decrease_amount >= 0:
            if px[item_name] < decrease_amount:
                print(" 재고량이 부족하여 감소할 수 없습니다.")
            else:
                px[item_name] -= decrease_amount
                print(f"{item_name}의 재고량이 {decrease_amount}개 감소되었습니다.")
        else:
            print(" 감소할 수량은 0 이상의 값이어야 합니다.")

# 특정 물품 삭제 함수
def delitem():
    item_name = input("삭제할 물품명을 입력하세요: ")
    if item_name not in px:
        print("에러: 등록되지 않은 물품입니다.")
    else:
        del px[item_name]
        print(f"{item_name} 물품이 삭제되었습니다.")

# 전체 물품 출력 함수
def allitems():
    if len(px) == 0:
        print("현재 등록된 물품이 없습니다.")
    else:
        print("\n--- 전체 물품 목록 ---")
        items_list = list(px.keys())
        if len(items_list) > 0:
            item = items_list[0]
            print(f"{item}: {px[item]}개")
            if len(items_list) > 1:
                item = items_list[1]
                print(f"{item}: {px[item]}개")
                if len(items_list) > 2:
                    item = items_list[2]
                    print(f"{item}: {px[item]}개")
               

# 재고량 0인 물품 출력 함수
def px_zeroitems():
    if len(px) == 0:
        print("현재 등록된 물품이 없습니다.")
    else:
        print("\n--- 재고량 0인 물품 ---")
        item_names = list(px.keys())
        if len(item_names) > 0:
            item = item_names[0]
            if px[item] == 0:
                print(item)
            if len(item_names) > 1:
                item = item_names[1]
                if px[item] == 0:
                    print(item)
                if len(item_names) > 2:
                    item = item_names[2]
                    if px[item] == 0:
                        print(item)
                  

# 프로그램 메시지를 저장하는 변수
msg = """
--- 편의점 물품 재고 관리 프로그램 ---

1. 신규물품 재고 등록
2. 특정물품 재고량 증가
3. 특정물품 재고량 감소
4. 특정 물품 삭제
5. 전체 물품 출력
6. 재고량 0인 물품 출력
7. 종료
"""

# 메인 코드 로 관용문 실행 
if __name__ == "__main__":
    while True: 
        print(msg)  # 프로그램 안내 메시지 출력
        # 사용자에게 메뉴 선택 입력받기
        n = input("메뉴를 선택하세요 (1-7): ")

        if n == '1':
            add_item()
        elif n == '2':
            incre()
        elif n == '3':
            decre()
        elif n == '4':
            delitem()
        elif n == '5':
            allitems()
        elif n == '6':
            px_zeroitems()
        elif n == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("에러: 잘못된 메뉴 선택입니다. 다시 시도하세요.")