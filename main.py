# 프롬프트 목록 데이터 (최소 3개 이상)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "파이썬 코드 리뷰어",
        "content": "작성된 파이썬 코드의 가독성을 높이고 버그를 찾아주세요.",
        "category": "프로그래밍",
        "favorite": False
    },
    {
        "title": "마케팅 카피라이터",
        "content": "신제품 홍보를 위한 인스타그램 광고 문구를 작성해 주세요.",
        "category": "마케팅",
        "favorite": True
        
    }
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

# 2. 프롬프트 목록 출력 함수
def show_list():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    print("\n=== 프롬프트 목록 ===")
    for index, prompt in enumerate(prompts):
        star = "★" if prompt.get('favorite') else "☆"
        print(f"[{index}] {star} {prompt['title']} ({prompt['category']})")

def add_prompt():
    print("\n[새 프롬프트 추가]")
    title = input("제목: ")
    content = input("내용: ")
    category = input("카테고리: ")
    
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("성공적으로 추가되었습니다!")

def show_by_category():
    if not prompts:
        print("\n등록된 프롬프트가 없습니다.")
        return

    categories = sorted(list(set(p['category'] for p in prompts)))
    print(f"\n현재 등록된 카테고리: {', '.join(categories)}")
    category = input("조회할 카테고리를 입력하세요: ").strip()

    print(f"\n=== '{category}' 카테고리 조회 결과 ===")
    found = False
    for index, p in enumerate(prompts):
        if p['category'].lower() == category.lower():
            star = "★" if p['favorite'] else "☆"
            print(f"[{index}] {star} {p['title']} ({p['category']})")
            found = True
            
    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")

def search_prompt():
    keyword = input("\n검색할 키워드를 입력하세요 (제목 또는 내용): ")
    print(f"\n=== '{keyword}' 검색 결과 ===")
    
    found = False
    for index, p in enumerate(prompts):
        if keyword in p['title'] or keyword in p['content']:
            star = "★" if p['favorite'] else "☆"
            print(f"[{index}] {star} {p['title']} ({p['category']})")
            found = True
            
    if not found:
        print("검색 결과가 없습니다.")

def view_detail():
    show_list()
    if not prompts: return
        
    try:
        index = int(input("\n상세보기 할 프롬프트 번호를 입력하세요: "))
        if 0 <= index < len(prompts):
            p = prompts[index]
            print("\n=== 프롬프트 상세 ===")
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {'★' if p['favorite'] else '☆'}")
            print(f"내용:\n{p['content']}")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자만 입력해주세요.")

def toggle_favorite():
    show_list()
    if not prompts: return
        
    try:
        index = int(input("\n즐겨찾기를 설정/해제 할 프롬프트 번호를 입력하세요: "))
        if 0 <= index < len(prompts):
            prompts[index]['favorite'] = not prompts[index]['favorite']
            status = "설정" if prompts[index]['favorite'] else "해제"
            print(f"즐겨찾기가 {status} 되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자만 입력해주세요.")

def show_favorite_list():
    fav_prompts = [(index, p) for index, p in enumerate(prompts) if p.get('favorite')]
    if not fav_prompts:
        print("\n즐겨찾기한 프롬프트가 없습니다.")
        return

    print("\n=== 즐겨찾기 목록 ===")
    for index, prompt in fav_prompts:
        print(f"[{index}] ★ {prompt['title']} ({prompt['category']})")

# -----------------------------------------------------
# 프로그램 실행 루프 (항상 맨 아래에 위치)
# -----------------------------------------------------
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("선택: ")
        
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            view_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorite_list()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")