---
layout: page
title: Entropy Learning Method
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

  /* ▼▼▼ [수정] 테마 강제 화살표 아이콘 제거 코드 ▼▼▼ */
  .chapter-item:after {
    content: none !important;
    display: none !important;
  }
  
  .chapter-item {
    background: none !important;
    padding-right: 0 !important;
  }
</style>

<div class="book-toc-wrapper">
  <h1 class="main-title">Entropy Study</h1>
  <p class="sub-title">"The Art of Transforming Disorder into Order through Learning"</p>

  <div class="part-header">
    <span class="part-label">Part I</span>
    <div class="part-name">Diagnosis: The Disordered Mind</div>
  </div>

  <a href="/entropy-ch1.html" class="chapter-item">
    <span class="chapter-num">01</span>
    <span class="chapter-text">The True Nature of Learning Entropy</span>
    <span class="dots"></span>
    <span class="page-mark">p.12</span>
  </a>
  
  <a href="/entropy-ch2.html" class="chapter-item">
    <span class="chapter-num">02</span>
    <span class="chapter-text">External Adversaries: Digitalization and Environment</span>
    <span class="dots"></span>
    <span class="page-mark">p.28</span>
  </a>

  <a href="/entropy-ch3.html" class="chapter-item">
    <span class="chapter-num">03</span>
    <span class="chapter-text">Internal Adversaries: Cognitive Overload</span>
    <span class="dots"></span>
    <span class="page-mark">p.45</span>
  </a>

  <div class="part-header">
    <span class="part-label">Part II</span>
    <div class="part-name">Prescription: The Power of Creating Order</div>
  </div>

  <a href="/entropy-ch4.html" class="chapter-item">
    <span class="chapter-num">04</span>
    <span class="chapter-text">The Power of Simplicity</span>
    <span class="dots"></span>
    <span class="page-mark">p.62</span>
  </a>

  <a href="/entropy-ch5.html" class="chapter-item">
    <span class="chapter-num">05</span>
    <span class="chapter-text">Environmental Design: The Space for Immersion</span>
    <span class="dots"></span>
    <span class="page-mark">p.78</span>
  </a>

  <a href="/entropy-ch6.html" class="chapter-item">
    <span class="chapter-num">06</span>
    <span class="chapter-text">Knowledge Compression: Chunking and Structuring</span>
    <span class="dots"></span>
    <span class="page-mark">p.94</span>
  </a>

  <a href="/entropy-ch7.html" class="chapter-item">
    <span class="chapter-num">07</span>
    <span class="chapter-text">Routine: A Sustainable System</span>
    <span class="dots"></span>
    <span class="page-mark">p.112</span>
  </a>

  <div class="part-header">
    <span class="part-label">Part III</span>
    <div class="part-name">Practice: Real-Life Application</div>
  </div>

  <a href="/entropy-ch8.html" class="chapter-item">
    <span class="chapter-num">08</span>
    <span class="chapter-text">Utilizing AI Note-Taking Methods</span>
    <span class="dots"></span>
    <span class="page-mark">p.130</span>
  </a>

  <a href="/entropy-ch9.html" class="chapter-item">
    <span class="chapter-num">09</span>
    <span class="chapter-text">The Illusion of Love, The Poison of Greed</span>
    <span class="dots"></span>
    <span class="page-mark">p.145</span>
  </a>

  <a href="/entropy-ch10.html" class="chapter-item">
    <span class="chapter-num">10</span>
    <span class="chapter-text">The Body as a Vessel, Relationships as a Channel</span>
    <span class="dots"></span>
    <span class="page-mark">p.158</span>
  </a>
  
  <a href="/entropy-ch11.html" class="chapter-item">
    <span class="chapter-num">11</span>
    <span class="chapter-text">Misconceptions and Truth</span>
    <span class="dots"></span>
    <span class="page-mark">p.172</span>
  </a>

</div>