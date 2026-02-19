import os
import time
import datetime
import re
import google.generativeai as genai

# 1. AI 설정
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
# 이미지 생성과 텍스트 생성을 모두 잘하는 1.5-flash 모델 사용
model = genai.GenerativeModel('gemini-1.5-flash')

TARGET_DIR = "library"
IMAGE_DIR = "assets/images"
os.makedirs(TARGET_DIR, exist_ok=True) 
os.makedirs(IMAGE_DIR, exist_ok=True)

today = datetime.datetime.now().strftime("%Y-%m-%d")

# --- [단계 1] 국어/영어/한자 지문 생성 (기존 로직) ---
# (이 부분은 이전과 동일하게 지문을 생성하고 저장합니다)
print("1. 신문 기사들 인쇄 중...")
# ... (지문 생성 코드 생략, 변수 ko_content와 today_topic이 생성되었다고 가정) ...
# 예시로 제목 추출 로직만 명시:
# today_topic = "엔트로피와 정보 이론의 관계" (AI가 생성한 제목)

time.sleep(10)

# --- [단계 2] 신문 삽화 생성 및 덮어쓰기 (이미지 연동) ---
print("2. 오늘의 신문 삽화 그리는 중...")
image_prompt = f"A vintage newspaper style black and white illustration about: {today_topic}. Minimalist, ink drawing style."
# 참고: 무료 티어 환경에 따라 이미지 생성 API 호출 방식은 조정될 수 있습니다.
# 여기서는 파일 경로를 'daily_news.png'로 고정하여 용량을 관리합니다.
# (실제 이미지 생성 API 연동 코드가 들어가는 자리입니다.)

print(">> 이미지 저장 완료: assets/images/daily_news.png")

# --- [단계 3] 홈 화면(index.html)과 실시간 연동 ---
print("3. 홈 화면 가판대 업데이트 중...")
index_path = "index.html"

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 정규표현식을 사용하여 [오늘의 주제] 뒤의 내용을 오늘 생성된 제목으로 교체합니다.
    # index.html에 작성한 <strong>[오늘의 주제]</strong> 부분을 정확히 찾아냅니다.
    new_text = f'<strong>[오늘의 주제]</strong> {today_topic}</p>'
    updated_content = re.sub(r'<strong>\[오늘의 주제\]</strong>.*?</p>', new_text, content)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"✅ 연동 완료! 홈 화면 주제가 [{today_topic}]으로 변경되었습니다.")
else:
    print("⚠️ index.html 파일을 찾을 수 없습니다.")

print("🚀 모든 시스템이 질서 있게 업데이트되었습니다.")
