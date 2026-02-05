---
layout: page
title: 엔트로피 학습법
permalink: /entropy.html
---

<style>
  /* 전체 컨테이너: 책 느낌의 명조체 적용 */
  .book-style-wrapper {
    font-family: "KoPub Batang", "Merriweather", "Georgia", "Batang", serif;
    color: #2c2c2c;
    max-width: 680px;
    margin: 0 auto;
    padding: 20px 10px;
    line-height: 1.6;
  }

  /* 서문 텍스트 */
  .intro-text {
    text-align: center;
    color: #555;
    margin-bottom: 60px;
    font-size: 1.05rem;
    font-weight: 400;
  }

  /* Part 제목: 굵고 크게 */
  .part-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-top: 50px;
    margin-bottom: 25px;
    padding-bottom: 10px;
    border-bottom: 2px solid #333;
    color: #111;
  }

  /* 챕터 한 줄 (제목 ...... Read) */
  .chapter-row {
    display: flex;
    align-items: baseline; /* 글자 밑라인 맞춤 */
    margin-bottom: 18px;
    width: 100%;
  }

  /* 챕터 제목 */
  .chapter-title {
    font-size: 1.15rem;
    font-weight: 500;
    color: #333;
    flex-shrink: 0; /* 줄어들지 않음 */
  }

  /* 가운데 점선 (남는 공간 다 차지) */
  .dots {
    flex-grow: 1;
    border-bottom: 1px dotted #999;
    margin: 0 12px;
    position: relative;
    top: -5px; /* 점선 위치 살짝 위로 */
  }

  /* Read 버튼 */
  .read-btn {
    font-size: 0.9rem;
    color: #d9480f; /* 포인트 컬러 (오렌지 계열) */
    text-decoration: none;
    font-weight: bold;
    flex-shrink: 0;
    transition: all 0.2s;
  }

  .read-btn:hover {
    color: #ff6b6b;
    text-decoration: underline;
  }

  /* 모바일 최적화 */
  @media (max-width: 500px) {
    .chapter-title { font-size: 1rem; }
    .part-title { font-size: 1.3rem; }
  }
</style>

<div class="book-style-wrapper">

  <p class="intro-text">
    학습할수록 머릿속이 복잡해지나요?<br>
    심리적 엔트로피를 낮추고 몰입을 극대화하는<br>
    <strong>가장 과학적인 학습 전략</strong>을 제안합니다.
  </p>

  <div class="part-title">Part 1. 진단: 무질서해진 머릿속</div>

  <div class="chapter-row">
    <span class="chapter-title">01. 학습 엔트로피의 정체</span>
    <span class="dots"></span>
    <a href="/entropy-ch1.html" class="read-btn">Read →</a>
  </div>

  <div class="chapter-row">
    <span class="chapter-title">02. 외부의 적: 디지털과 환경</span>
    <span class="dots"></span>
    <a href="/entropy-ch2.html" class="read-btn">Read →</a>
  </div>

  <div class="chapter-row">
    <span class="chapter-title">03. 내부의 적: 인지 과부하</span>
    <span class="dots"></span>
    <a href="/entropy-ch3.html" class="read-btn">Read →</a>
  </div>

  <div class="part-title">Part 2. 처방: 질서를 만드는 힘</div>

  <div class="chapter-row">
    <span class="chapter-title">04. 단순함이 능력이다</span>
    <span class="dots"></span>
    <a href="/entropy-ch4.html" class="read-btn">Read →</a>
  </div>

  <div class="chapter-row">
    <span class="chapter-title">05. 환경 설계: 몰입의 공간</span>
    <span class="dots"></span>
    <a href="/entropy-ch5.html" class="read-btn">Read →</a>
  </div>

  <div class="chapter-row">
    <span class="chapter-title">06. 지식 압축: 청킹과 구조화</span>
    <span class="dots"></span>
    <a href="/entropy-ch6.html" class="read-btn">Read →</a>
  </div>
  
  <div class="chapter-row">
    <span class="chapter-title">07. 루틴: 지속 가능한 시스템</span>
    <span class="dots"></span>
    <a href="#" class="read-btn">Read →</a>
  </div>

</div>
