---
layout: page
title: 엔트로피 학습법
permalink: /entropy.html
---

<style>
  /* --- 고전 서적 스타일 (Classic Serif) --- */
  .book-toc-wrapper {
    font-family: "KoPub Batang", "Noto Serif KR", serif;
    max-width: 640px;
    margin: 40px auto;
    padding: 50px 40px;
    background-color: #fffcf8; /* 아주 연한 미색 배경 */
    box-shadow: 5px 5px 20px rgba(0,0,0,0.05); /* 은은한 그림자 */
    border: 1px solid #e8e0d5;
    border-radius: 4px;
  }

  .main-title {
    font-family: "Playfair Display", serif;
    font-size: 2.2rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    color: #2c2c2c;
    letter-spacing: -0.5px;
  }
  
  .sub-title {
    text-align: center;
    font-size: 0.95rem;
    color: #8c7b75;
    margin-bottom: 60px;
    font-family: "Pretendard", sans-serif;
    font-weight: 300;
  }

  /* 파트 구분선 */
  .part-header {
    margin-top: 60px;
    margin-bottom: 25px;
    text-align: center;
    position: relative;
  }
  
  .part-label {
    display: inline-block;
    font-family: "Playfair Display", serif;
    font-size: 0.8rem;
    letter-spacing: 2px;
    color: #d88e88; /* 포인트 컬러 */
    border-bottom: 1px solid #d88e88;
    padding-bottom: 3px;
    margin-bottom: 10px;
    text-transform: uppercase;
  }
  
  .part-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: #333;
    word-break: keep-all;
  }

  /* 챕터 리스트 아이템 */
  .chapter-item {
    display: flex;
    align-items: flex-end; /* 점선과 텍스트 하단 정렬 */
    margin-bottom: 14px;
    padding: 5px 0;
    transition: all 0.3s ease;
    text-decoration: none; /* 링크 밑줄 제거 */
    color: #4a4a4a;
    border-bottom: 1px solid transparent; /* 호버 시 흔들림 방지용 */
  }

  .chapter-item:hover {
    transform: translateX(5px);
    color: #d88e88;
  }

  .chapter-num {
    font-family: "Playfair Display", serif;
    font-style: italic;
    font-weight: bold;
    font-size: 1.1rem;
    color: #bbb;
    margin-right: 12px;
    min-width: 25px;
    text-align: right;
  }

  .chapter-text {
    font-size: 1.05rem;
    font-weight: 500;
  }

  /* 점선 (Leader dots) */
  .dots {
    flex-grow: 1;
    border-bottom: 1px dotted #ccc;
    margin: 0 10px 6px 10px; /* 점선 위치 조정 */
  }

  .page-mark {
    font-family: "Playfair Display", serif;
    font-size: 0.85rem;
    font-style: italic;
    color: #aaa;
  }
  
  /* 데스크톱 - 텍스트 줄바꿈 방지 */
  @media (min-width: 641px) {
    .chapter-text { white-space: nowrap; }
  }
  
  /* 모바일 대응 */
  @media (max-width: 640px) {
    .book-toc-wrapper { padding: 30px 20px; }
    .main-title { font-size: 1.8rem; }
    .chapter-text { font-size: 0.95rem; }
    .chapter-item { align-items: baseline; }
    .dots { display: none; } /* 모바일에서는 점선 숨김 */
    .page-mark { display: none; } /* 모바일에서는 페이지 번호 숨김 */
  }

  /* 테마에서 강제로 붙이는 외부 링크 아이콘 제거 */
  .chapter-item:after {
    content: none !important;
    display: none !important;
  }
  
  /* 혹시 아이콘이 이미지나 svg로 들어간 경우 대비 */
  .chapter-item svg, 
  .chapter-item img {
    display: none;
  }
  
  /* 배경 이미지 아이콘 제거 및 패딩 조정 */
  .chapter-item {
    background: none !important;
    padding-right: 0 !important;
  }
</style>

<div class="book-toc-wrapper">
  <h1 class="main-title">Entropy Study</h1>
  <p class="sub-title">"무질서를 질서로 바꾸는 학습의 기술"</p>

  <!-- Part 1 -->
  <div class="part-header">
    <span class="part-label">Part I</span>
    <div class="part-name">진단: 무질서해진 머릿속</div>
  </div>

  <a href="/entropy-ch1.html" class="chapter-item">
    <span class="chapter-num">01</span>
    <span class="chapter-text">학습 엔트로피의 정체</span>
    <span class="dots"></span>
    <span class="page-mark">p.12</span>
  </a>
  
  <a href="/entropy-ch2.html" class="chapter-item">
    <span class="chapter-num">02</span>
    <span class="chapter-text">외부의 적: 디지털과 환경</span>
    <span class="dots"></span>
    <span class="page-mark">p.28</span>
  </a>

  <a href="/entropy-ch3.html" class="chapter-item">
    <span class="chapter-num">03</span>
    <span class="chapter-text">내부의 적: 인지 과부하</span>
    <span class="dots"></span>
    <span class="page-mark">p.45</span>
  </a>

  <!-- Part 2 -->
  <div class="part-header">
    <span class="part-label">Part II</span>
    <div class="part-name">처방: 질서를 만드는 힘</div>
  </div>

  <a href="/entropy-ch4.html" class="chapter-item">
    <span class="chapter-num">04</span>
    <span class="chapter-text">단순함의 힘</span>
    <span class="dots"></span>
    <span class="page-mark">p.62</span>
  </a>

  <a href="/entropy-ch5.html" class="chapter-item">
    <span class="chapter-num">05</span>
    <span class="chapter-text">환경 설계: 몰입의 공간</span>
    <span class="dots"></span>
    <span class="page-mark">p.78</span>
  </a>

  <a href="/entropy-ch6.html" class="chapter-item">
    <span class="chapter-num">06</span>
    <span class="chapter-text">지식 압축: 청킹과 구조화</span>
    <span class="dots"></span>
    <span class="page-mark">p.94</span>
  </a>

  <a href="/entropy-ch7.html" class="chapter-item">
    <span class="chapter-num">07</span>
    <span class="chapter-text">루틴: 지속 가능한 시스템</span>
    <span class="dots"></span>
    <span class="page-mark">p.112</span>
  </a>

  <!-- Part 3 -->
  <div class="part-header">
    <span class="part-label">Part III</span>
    <div class="part-name">실천: 실생활 활용</div>
  </div>

  <a href="/entropy-ch8.html" class="chapter-item">
    <span class="chapter-num">08</span>
    <span class="chapter-text">Ai 노트법 활용</span>
    <span class="dots"></span>
    <span class="page-mark">p.130</span>
  </a>

  <a href="/entropy-ch9.html" class="chapter-item">
    <span class="chapter-num">09</span>
    <span class="chapter-text">사랑이라는 착각, 욕심이라는 독</span>
    <span class="dots"></span>
    <span class="page-mark">p.145</span>
  </a>

  <a href="/entropy-ch10.html" class="chapter-item">
    <span class="chapter-num">10</span>
    <span class="chapter-text">몸이라는 그릇, 관계라는 통로</span>
    <span class="dots"></span>
    <span class="page-mark">p.158</span>
  </a>
  
  <a href="/entropy-ch11.html" class="chapter-item">
    <span class="chapter-num">11</span>
    <span class="chapter-text">오해와 진실</span>
    <span class="dots"></span>
    <span class="page-mark">p.172</span>
  </a>

</div>
