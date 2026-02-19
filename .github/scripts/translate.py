import os
import google.generativeai as genai

# 금고에서 API 열쇠 꺼내기
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 최신 제미나이 모델 
model = genai.GenerativeModel('gemini-2.5-flash')

TARGET_DIR = "library"

# library 폴더 내부를 꼼꼼히 살핍니다.
for filename in os.listdir(TARGET_DIR):
    # .md 파일이면서 이미 번역된 파일(-en.md)이 아닌 것만 골라냅니다.
    if filename.endswith(".md") and not filename.endswith("-en.md"):
        ko_path = os.path.join(TARGET_DIR, filename)
        
        # 영어 파일명 규칙 (예: entropy-ch1.md -> entropy-ch1-en.md)
        en_filename = filename.replace(".md", "-en.md")
        en_path = os.path.join(TARGET_DIR, en_filename)

        # 영문판이 없을 때만 새롭게 작업을 시작해 중복 에너지를 막습니다.
        if not os.path.exists(en_path):
            print(f"구조 분석 및 번역 시작: {filename}")
            
            with open(ko_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 제미나이에게 내리는 정밀한 질서 유지 명령 (permalink 수정 규칙 추가)
            prompt = f"""
            당신은 전문 번역가입니다. 아래 제공된 한국어 문서를 영어로 번역하세요.
            
            [엄격한 구조 유지 규칙]
            1. 마크다운 형식과 문서 최상단의 설정값(--- 로 둘러싸인 Front Matter) 구조를 절대 깨뜨리지 마세요.
            2. 본문의 철학적인 깊이를 살려 논리적이고 정돈된 영어로 번역하세요.
            3. [가장 중요] Obsidian 내부 링크 `[[ ]]` 및 이미지 링크 `![[ ]]` 안의 파일명은 절대 번역하지 마세요.
            4. 일반 링크 `[텍스트](경로)` 에서도 괄호() 안의 경로는 원본 그대로 유지하세요.
            5. [주소 충돌 방지] 최상단 Front Matter 설정값 중 `permalink:` 뒤에 오는 주소 끝에 반드시 `-en`을 추가하세요. 
               (예: `permalink: /entropy-ch1.html` -> `permalink: /entropy-ch1-en.html`)
            
            [본문]
            {content}
            """
            
            try:
                response = model.generate_content(prompt)
                with open(en_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print(f"체계화 및 번역 완료: {en_filename}")
            except Exception as e:
                print(f"오류 발생 ({filename}): {e}")
