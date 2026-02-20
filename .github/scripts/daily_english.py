import os
import datetime
import google.generativeai as genai

# 1. API 설정
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3-flash-preview')

TARGET_DIR = "library"
os.makedirs(TARGET_DIR, exist_ok=True) 

today = datetime.datetime.now().strftime("%Y-%m-%d")

print("📝 누적 직독직해 학습지 생성 중...")
prompt = f"""
당신은 영어 직독직해 전문가입니다. 실생활에 유용하거나 영감을 주는 영어 문장 1개를 골라, 4단계 누적 확장 방식으로 분석해주세요.
반드시 아래의 마크다운 및 HTML 구조를 100% 똑같이 유지해서 출력하세요. 다른 인사말이나 설명은 절대 금지합니다.

---
layout: worksheet
title: "오늘의 직독직해 연습"
permalink: /daily-english
date: {today}
---

<div class="ws-step">1단계: 주어 & 동사 & 목적어 (Subject & Verb & Object)</div>
<div class="ws-content">
[여기에 1단계 영어 기본 문장 (예: The dog chased the ball.)]<br>
([여기에 1단계 한국어 해석])
</div>
<div class="ws-line"></div>
<div class="ws-line"></div>

<div class="ws-step">2단계: 장소 추가 (Adding Location)</div>
<div class="ws-content">
[여기에 2단계에 추가된 영어 구문만 (예: in the backyard)]<br>
([여기에 1+2단계 누적 한국어 해석])
</div>
<div class="ws-line"></div>
<div class="ws-line"></div>

<div class="ws-step">3단계: 시간 및 빈도 추가 (Adding Time & Frequency)</div>
<div class="ws-content">
[여기에 3단계에 추가된 영어 구문만 (예: all afternoon yesterday)]<br>
([여기에 1+2+3단계 누적 한국어 해석])
</div>
<div class="ws-line"></div>
<div class="ws-line"></div>

<div class="ws-step">4단계: 완전한 이해 (Complete Understanding) - 전체 문장 쓰기 & 자유 연습</div>
<div class="ws-content">
[여기에 1~3단계가 모두 합쳐진 완전한 영어 문장 전체]
</div>
<div class="ws-line"></div>
<div class="ws-line"></div>
<div class="ws-line"></div>
"""

response = model.generate_content(prompt).text

# 파일 저장
file_path = os.path.join(TARGET_DIR, f"{today}-english.md")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(response)

print(f"✅ 오늘의 직독직해 학습지가 성공적으로 인쇄되었습니다!")
