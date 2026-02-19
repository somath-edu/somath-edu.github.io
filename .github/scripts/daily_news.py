import os
import time
import datetime
import re
import google.generativeai as genai

# API 설정 및 가장 안정적인 1.5-flash 모델 적용
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

TARGET_DIR = "library"
# 폴더가 없으면 스스로 생성하여 구조를 잡습니다.
os.makedirs(TARGET_DIR, exist_ok=True) 

# 오늘 날짜로 파일명 깔끔하게 정리
today = datetime.datetime.now().strftime("%Y-%m-%d")
base_name = f"{today}-suneung"

# --- 1. 수능 국어 원본 ---
print("1. 수능 국어 지문 인쇄 중...")
prompt_ko = f"""
당신은 수능 국어 일타 강사입니다. 수능 비문학(독서) 영역에 출제될 법한 철학, 과학, 경제 분야의 핵심 개념 하나를 선정하여 논리적인 지문을 작성해 주세요.
[엄격한 규칙]
1. 최상단에 마크다운 Front Matter를 반드시 넣으세요. 이때 `layout: newspaper`를 지정하세요.
   예시:
   ---
   layout: newspaper
   title: "오늘의 수능 비문학: [여기에 생성된 주제 입력]"
   permalink: /{today}-suneung-ko
   ---
2. 분량은 실제 수능 지문 1개 분량으로 체계적으로 작성하세요.
"""
ko_content = model.generate_content(prompt_ko).text
with open(os.path.join(TARGET_DIR, f"{base_name}-ko.md"), 'w', encoding='utf-8') as f:
    f.write(ko_content)

# 생성된 글에서 '제목'만 쏙 뽑아냅니다. (홈 화면 업데이트용)
match = re.search(r'title:\s*"(.*?)"', ko_content)
today_topic = match.group(1) if match else "새로운 수능 지식"

print(">> 로봇 휴식 중... (10초)")
time.sleep(10)

# --- 2. 수능 영어 (직독직해) ---
print("2. 수능 영어 신문 인쇄 중...")
prompt_en = f"""
당신은 수능 영어 전문가입니다. 아래 지문을 수능 영어 독해 지문 스타일의 세련된 영문 기사로 번역하세요.
[엄격한 규칙]
1. 최상단 Front Matter에 `layout: newspaper`를 지정하고, permalink 끝에 '-en'을 붙이세요.
2. 영어를 공부하는 학생이 '직독직해' 훈련을 할 수 있도록 문장 구조를 명확히 하세요.
3. 하단에 '오늘의 핵심 영단어' 5개를 정리하세요.
[원본 지문]
{ko_content}
"""
en_content = model.generate_content(prompt_en).text
with open(os.path.join(TARGET_DIR, f"{base_name}-en.md"), 'w', encoding='utf-8') as f:
    f.write(en_content)

print(">> 로봇 휴식 중... (10초)")
time.sleep(10)

# --- 3. 국한문 혼용 (한자 공부) ---
print("3. 국한문 고전 신문 인쇄 중...")
prompt_classic = f"""
당신은 조선시대의 대학자입니다. 아래 지문을 서당에서 제자들을 가르치는 '강학' 스타일의 옛날 신문으로 변환하세요.
[엄격한 규칙]
1. 최상단 Front Matter에 `layout: newspaper`를 지정하고, permalink 끝에 '-classic'을 붙이세요.
2. 주요 개념어와 명사는 반드시 [한글(漢字)] 형태로 표기하여 한자 공부가 되게 하세요.
3. 문체는 조선시대 문어체(~이라, ~하도다)를 사용하세요.
4. 하단에 '오늘의 필수 한자' 5개의 훈과 음을 정리하세요.
[원본 지문]
{ko_content}
"""
classic_content = model.generate_content(prompt_classic).text
with open(os.path.join(TARGET_DIR, f"{base_name}-classic.md"), 'w', encoding='utf-8') as f:
    f.write(classic_content)

# --- 4. 홈 화면 (index.html) 헤드라인 업데이트 ---
print("4. 홈 화면(index.html) 정돈 중...")
index_path = "index.html"
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        index_html = f.read()

    # 홈 화면에 있는 '[오늘의 주제]' 텍스트를 오늘 생성된 진짜 제목으로 자동 교체합니다.
    updated_html = re.sub(
        r'<strong>\[오늘의 주제\]</strong>.*?</p>',
        f'<strong>[오늘의 주제]</strong> {today_topic}</p>',
        index_html
    )
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print(f"✅ 홈 화면 업데이트 완료! 오늘의 주제: {today_topic}")
else:
    print("⚠️ index.html 파일이 최상단에 없어 헤드라인 업데이트는 건너뜁니다.")

print("📰 3가지 버전의 신문 발행 및 시스템 업데이트가 체계적으로 완료되었습니다.")
