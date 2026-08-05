import sys

# 기본 데이터 (최소 3개 이상의 프롬프트)
prompts = [
    {
        "id": 1,
        "title": "파이썬 코드 리뷰어",
        "category": "개발",
        "description": "파이썬 코드를 분석하고 개선점을 제안받습니다.",
        "content": "당신은 10년 차 시니어 파이썬 개발자입니다. 다음 코드를 리뷰하고 PEP 8 스타일 가이드, 성능, 가독성 측면에서 구체적인 개선점과 리팩토링된 코드를 제시해주세요:\n[코드 입력]",
        "is_favorite": True
    },
    {
        "id": 2,
        "title": "전문 번역가 (한영)",
        "category": "번역",
        "description": "한국어 문장을 자연스러운 비즈니스 영어로 번역합니다.",
        "content": "당신은 전문 원어민 번역가입니다. 다음 한국어 텍스트를 문맥에 맞는 자연스럽고 격식 있는 비즈니스 영어로 번역해주세요. 직역을 피하고 원어민이 자주 쓰는 표현을 사용해주세요:\n[텍스트 입력]",
        "is_favorite": False
    },
    {
        "id": 3,
        "title": "블로그 포스팅 아이디어 생성기",
        "category": "마케팅",
        "description": "특정 주제에 대한 매력적인 블로그 글 주제를 뽑아줍니다.",
        "content": "당신은 창의적인 콘텐츠 마케터입니다. '[주제 입력]'에 관련된 흥미롭고 클릭을 유도할 수 있는 블로그 포스팅 제목과 핵심 내용 요약 아이디어를 5가지 제시해주세요.",
        "is_favorite": False
    }
]

next_id = 4  # 다음 부여될 ID

def print_menu():
    print("\n" + "="*30)
    print(" 🎯 프롬프트 관리 프로그램 🎯 ")
    print("="*30)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기 및 즐겨찾기")
    print("0. 프로그램 종료")
    print("="*30)

def add_prompt():
    global next_id
    print("\n[ 프롬프트 추가 ]")
    title = input("제목: ")
    category = input("카테고리: ")
    description = input("간단한 설명: ")
    print("프롬프트 내용 (입력을 마치려면 빈 줄에서 Enter를 두 번 누르세요):")
    
    content_lines = []
    while True:
        line = input()
        if line == "":
            break
        content_lines.append(line)
    content = "\n".join(content_lines)

    new_prompt = {
        "id": next_id,
        "title": title,
        "category": category,
        "description": description,
        "content": content,
        "is_favorite": False
    }
    prompts.append(new_prompt)
    print(f"\n✅ '{title}' 프롬프트가 성공적으로 추가되었습니다! (ID: {next_id})")
    next_id += 1

def print_prompt_list(target_prompts):
    if not target_prompts:
        print("\n등록된 프롬프트가 없습니다.")
        return

    print("\n{:<5} | {:<3} | {:<10} | {:<25}".format("ID", "즐겨찾기", "카테고리", "제목"))
    print("-" * 60)
    for p in target_prompts:
        fav_icon = "★" if p["is_favorite"] else "☆"
        print("{:<5} | {:<4} | {:<10} | {}".format(p["id"], fav_icon, p["category"], p["title"]))

def view_all_prompts():
    print("\n[ 전체 프롬프트 목록 ]")
    print_prompt_list(prompts)

def view_by_category():
    print("\n[ 카테고리별 조회 ]")
    # 등록된 모든 카테고리 추출 (중복 제거)
    categories = list(set([p["category"] for p in prompts]))
    
    print("현재 등록된 카테고리:", ", ".join(categories))
    target_category = input("조회할 카테고리명을 입력하세요: ")

    filtered = [p for p in prompts if p["category"].lower() == target_category.lower()]
    print(f"\n'{target_category}' 카테고리 조회 결과:")
    print_prompt_list(filtered)

def search_prompts():
    print("\n[ 프롬프트 검색 ]")
    keyword = input("검색어 입력 (제목, 설명, 내용에서 검색): ").lower()
    
    filtered = [p for p in prompts if 
                keyword in p["title"].lower() or 
                keyword in p["description"].lower() or 
                keyword in p["content"].lower()]
    
    print(f"\n'{keyword}' 검색 결과: 총 {len(filtered)}건")
    print_prompt_list(filtered)

def view_detail_and_favorite():
    print("\n[ 상세 보기 및 즐겨찾기 ]")
    try:
        target_id = int(input("상세보기 할 프롬프트 ID를 입력하세요: "))
    except ValueError:
        print("❌ 숫자로 된 ID를 입력해주세요.")
        return

    # ID로 프롬프트 찾기
    target_prompt = next((p for p in prompts if p["id"] == target_id), None)

    if not target_prompt:
        print(f"❌ ID {target_id}에 해당하는 프롬프트를 찾을 수 없습니다.")
        return

    fav_icon = "★" if target_prompt["is_favorite"] else "☆"
    
    print("\n" + "="*40)
    print(f"[{fav_icon}] {target_prompt['title']} (ID: {target_prompt['id']})")
    print(f"▶ 카테고리: {target_prompt['category']}")
    print(f"▶ 설명: {target_prompt['description']}")
    print("-" * 40)
    print(target_prompt['content'])
    print("="*40)

    # 즐겨찾기 토글 옵션
    toggle = input("\n즐겨찾기 상태를 변경하시겠습니까? (y/n): ").lower()
    if toggle == 'y':
        target_prompt["is_favorite"] = not target_prompt["is_favorite"]
        new_status = "등록" if target_prompt["is_favorite"] else "해제"
        print(f"✅ 즐겨찾기가 {new_status}되었습니다.")

def main():
    while True:
        print_menu()
        choice = input("원하시는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            add_prompt()
        elif choice == '2':
            view_all_prompts()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            search_prompts()
        elif choice == '5':
            view_detail_and_favorite()
        elif choice == '0':
            print("\n프로그램을 종료합니다. 감사합니다! 👋")
            sys.exit()
        else:
            print("\n❌ 잘못된 입력입니다. 0~5 사이의 번호를 입력해주세요.")

if __name__ == "__main__":
    main()