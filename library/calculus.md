---
layout: page
title: 미적분 I - 서브교과서
permalink: /calculus.html
---

<style>
  /* Calculus Book Theme - Modern Dark Reader */
  .book-toc-wrapper {
    font-family: var(--font-sans);
    max-width: 640px;
    margin: 20px auto;
    padding: 30px 20px;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    backdrop-filter: blur(10px);
  }

  .main-title {
    font-family: var(--font-serif);
    font-size: 2rem;
    text-align: center;
    margin-bottom: 8px;
    color: var(--text-main);
  }
  
  .sub-title {
    text-align: center;
    font-size: 0.9rem;
    color: var(--accent-blue);
    margin-bottom: 40px;
    font-weight: 600;
    letter-spacing: 1px;
  }

  .part-header {
    margin-top: 40px;
    margin-bottom: 20px;
    padding-left: 10px;
    border-left: 3px solid var(--accent-blue);
  }
  
  .part-label {
    font-size: 0.75rem;
    color: var(--text-sub);
    text-transform: uppercase;
    letter-spacing: 2px;
    display: block;
  }
  
  .part-name {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text-main);
  }

  .chapter-item {
    display: flex;
    align-items: center;
    padding: 16px;
    margin-bottom: 10px;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 12px;
    text-decoration: none;
    color: var(--text-main);
    transition: all 0.2s ease;
    border: 1px solid transparent;
  }

  .chapter-item:active {
    background: rgba(255, 255, 255, 0.05);
    border-color: var(--accent-blue);
    transform: scale(0.98);
  }

  .chapter-num {
    font-family: var(--font-serif);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-sub);
    margin-right: 15px;
    opacity: 0.5;
  }

  .chapter-text {
    flex: 1;
    font-size: 1rem;
    font-weight: 500;
  }

  .chevron {
    color: var(--text-sub);
    font-size: 0.8rem;
  }
</style>

<div class="book-toc-wrapper">
  <h1 class="main-title">Calculus I</h1>
  <p class="sub-title">SUB TEXTBOOK</p>

  <div class="part-header">
    <span class="part-label">Part I</span>
    <div class="part-name">함수의 극한과 연속</div>
  </div>

  <a href="/wiki/chapter01/limits/" class="chapter-item">
    <span class="chapter-num">01</span>
    <span class="chapter-text">함수의 극한</span>
    <span class="chevron">→</span>
  </a>
  
  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">02</span>
    <span class="chapter-text">함수의 연속</span>
    <span class="chevron">→</span>
  </a>

  <div class="part-header">
    <span class="part-label">Part II</span>
    <div class="part-name">다항함수의 미분법</div>
  </div>

  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">03</span>
    <span class="chapter-text">미분계수와 도함수</span>
    <span class="chevron">→</span>
  </a>

  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">04</span>
    <span class="chapter-text">도함수의 활용 (1)</span>
    <span class="chevron">→</span>
  </a>

  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">05</span>
    <span class="chapter-text">도함수의 활용 (2)</span>
    <span class="chevron">→</span>
  </a>

  <div class="part-header">
    <span class="part-label">Part III</span>
    <div class="part-name">다항함수의 적분법</div>
  </div>

  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">06</span>
    <span class="chapter-text">부정적분</span>
    <span class="chevron">→</span>
  </a>

  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">07</span>
    <span class="chapter-text">정적분</span>
    <span class="chevron">→</span>
  </a>

  <a href="/wiki/" class="chapter-item">
    <span class="chapter-num">08</span>
    <span class="chapter-text">정적분의 활용</span>
    <span class="chevron">→</span>
  </a>

</div>
