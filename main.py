prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    },
    # 여기에 최소 2개 이상의 딕셔너리를 더 추가해 주세요!
]

# 1. 메뉴 출력 함수
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

# 2. 프롬프트 목록 출력 함수 (들여쓰기 및 위치 수정)
def show_list():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    print("\n=== 프롬프트 목록 ===")
    for index, prompt in enumerate(prompts):
        star = "★" if prompt.get('favorite') else "☆"
        print(f"[{index}] {star} {prompt['title']} ({prompt['category']})")

# -----------------------------------------------------
# 3. 프로그램 실행 루프 (항상 맨 아래에 위치)
# -----------------------------------------------------
while True:
    show_menu()
    choice = input("선택: ")
    
    if choice == "1":
        # TODO: 프롬프트 추가 함수 호출
        print("프롬프트 추가 기능은 아직 준비 중입니다.")
        pass
    elif choice == "2":
        # 수정됨: 2번 선택 시 목록 보기 함수 호출
        show_list()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")