# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 박재성
# 프로젝트 주제:  직원 실적 분석 및 성과급 계산기

# [1단계] 데이터 구조 수정: 처음에는 비어있는 리스트로 시작합니다.
employee_data = []

# [2단계] 함수 정의: 실적 점수를 바탕으로 등급 판정 (네가 작성한 코드 그대로!)
def calculate_grade(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"

# [2단계] 함수 정의: 등급을 바탕으로 성과급 계산 (네가 작성한 코드 그대로!)
def calculate_bonus(grade):
    if grade == "S":
        return 1000000
    elif grade == "A":
        return 500000
    elif grade == "B":
        return 200000
    else:
        return 0

# [1단계]와 [2단계](함수 정의)는 기존 코드 그대로 둡니다.

# [3단계] 메인 실행 흐름 (메뉴 시스템 도입)
while True:
    print("\n=== 직원 성과급 관리 프로그램 ===")
    print("1. 직원 정보 입력")
    print("2. 전체 직원 조회")
    print("3. 직원 정보 삭제")
    print("4. 프로그램 종료")
    
    choice = input("원하는 메뉴의 번호를 입력하세요: ")

    if choice == "1":
        # [기능 1] 직원 입력 및 2차원 리스트 추가
        input_name = input("직원의 이름을 입력하세요: ")
        input_score = int(input("실적 점수를 입력하세요: "))
        employee_data.append([input_name, input_score])
        print(f"👉 {input_name} 직원의 데이터가 등록되었습니다.")

    elif choice == "2":
        # [기능 2] 전체 직원 조회
        print("\n=== [전체 직원 평가 결과] ===")
        if not employee_data: # 리스트가 비어있는지 확인
            print("등록된 직원 정보가 없습니다.")
        else:
            # 💡 [미션 1] 방금 성공했던 'for emp in employee_data:' 출력 코드를 여기에 넣어보세요!
            for emp in employee_data:
                grade = calculate_grade(emp[1]) 
                bonus = calculate_bonus(grade)
    
                print(f"\n--- [평가 결과] ---")
                print(f"이름: {emp[0]}")
                print(f"실적 점수: {emp[1]}점")
                print(f"평가 등급: {grade}") 
                print(f"성과급: {bonus}원")

    elif choice == "3":
        # [기능 3] 직원 정보 삭제
        delete_name = input("삭제할 직원의 이름을 입력하세요: ")
        found = False
        
        # 2차원 리스트를 돌며 이름이 일치하는 행을 찾습니다.
        for emp in employee_data:
            if emp[0] == delete_name:
                # 💡 [미션 2] 리스트에서 해당 직원 상자(emp)를 완전히 지우는 파이썬 명령어를 완성해 보세요.
                # 힌트: 리스트이름.remove(지울데이터)
                employee_data.remove(emp)
                print(f"👉 {delete_name} 직원의 정보가 삭제되었습니다.")
                found = True
                break # 찾아서 지웠으므로 반복문 종료
                
        if not found:
            print("존재하지 않는 이름입니다.")

    elif choice == "4":
        print("프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
        break # while 무한 루프를 빠져나가 프로그램이 종료됩니다.

    else:
        print("잘못된 번호입니다. 1~4번 사이의 번호를 입력해 주세요.")


# [4단계] 2차원 리스트 탐색 및 결과 출력
for emp in employee_data:
    # emp[0]은 이름, emp[1]은 실적점수
    grade = calculate_grade(emp[1]) 
    bonus = calculate_bonus(grade)
    
    print(f"\n--- [평가 결과] ---")
    print(f"이름: {emp[0]}")
    print(f"실적 점수: {emp[1]}점")
    print(f"평가 등급: {grade}") 
    print(f"성과급: {bonus}원")
