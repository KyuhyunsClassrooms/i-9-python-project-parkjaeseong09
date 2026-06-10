# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20909
# 프로젝트 주제:  직원 실적 분석 및 성과급 계산기

# [1단계] 데이터 구조 만들기 (가상의 직원 데이터)
employee_data = [
    ["A101", "김민준", "영업팀", 95],
    ["A102", "이서연", "마케팅팀", 82],
    ["A103", "박도윤", "개발팀", 73],
    ["A104", "최아린", "영업팀", 50]
]

# [2단계] 함수 정의: 실적 점수를 바탕으로 등급 판정 (학생이 작성한 코드)
def calculate_grade(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"

# [2단계] 함수 정의: 등급을 바탕으로 성과급 계산 (학생이 작성한 코드 - 숫자의 쉼표 제거)
def calculate_bonus(grade):
    if grade == "S":
        return 1000000
    elif grade == "A":
        return 500000
    elif grade == "B":
        return 200000
    else:
        return 0

# [3단계] 핵심 반복문 설계하기 (메인 실행 흐름)
search_id = input("조회할 직원의 사번을 입력하세요: ")
found = False  # 직원을 찾았는지 확인하는 변수

# 2차원 리스트를 한 줄씩 반복문으로 탐색합니다.
for emp in employee_data:
    # 입력한 사번과 일치하는 직원을 리스트에서 찾았을 때만 아래 코드가 실행됩니다.
    if emp[0] == search_id:
        found = True
        
        # 1. 점수를 바탕으로 등급 계산 함수 호출
        grade = calculate_grade(emp[3])
        
        # 2. 등급을 바탕으로 성과급 계산 함수 호출 (올바른 위치로 이동)
        bonus = calculate_bonus(grade)
        
        # [5단계] 출력 형식 만들기
        print(f"\n--- [조회 결과] ---")
        print(f"사번: {emp[0]}")
        print(f"이름: {emp[1]}")
        print(f"부서: {emp[2]}")
        print(f"실적 점수: {emp[3]}점")
        print(f"평가 등급: {grade}") 
        print(f"성과급: {bonus}원")
        
        # 💡 중요: 사번을 찾아서 출력한 '후에만' 반복을 멈추도록 if문 안쪽에 줄을 맞췄습니다.
        break

# [예외 상황 처리] 리스트를 다 돌았는데도 사번을 못 찾았을 때
if not found:
    print("존재하지 않는 사번입니다.")