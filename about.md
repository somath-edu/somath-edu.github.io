---
layout: page
title: Support - 커피 한 잔의 응원
permalink: /about/
---

<style>
    /* 1. Global & Font Setup */
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&family=Playfair+Display:ital,wght@0,400;1,400&family=Noto+Sans+KR:wght@300;400;500&display=swap');
    
    .coffee-page {
        font-family: 'Noto Sans KR', sans-serif;
        color: #4A3B32;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px 20px;
        line-height: 1.8;
    }

    /* 2. Hero Section */
    .hero-container {
        position: relative;
        text-align: center;
        margin-bottom: 60px;
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(74, 59, 50, 0.1);
        animation: fadeIn 1s ease-out;
    }

    .hero-img {
        width: 100%;
        height: 450px;
        object-fit: cover;
        display: block;
        transition: transform 0.5s ease;
    }

    .hero-container:hover .hero-img {
        transform: scale(1.02);
    }

    .hero-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 40px;
        background: linear-gradient(to top, rgba(74, 59, 50, 0.8), transparent);
        color: white;
        text-align: left;
    }

    .hero-title {
        font-family: 'Nanum Myeongjo', serif;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 10px 0;
        word-break: keep-all;
    }

    .hero-subtitle {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.1rem;
        opacity: 0.9;
    }

    /* 3. Message Section */
    .message-box {
        text-align: center;
        margin-bottom: 40px;
        padding: 0 10px;
    }

    .main-message {
        font-family: 'Nanum Myeongjo', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #6B4F3F;
        margin-bottom: 20px;
        word-break: keep-all;
    }

    .sub-message {
        font-size: 1rem;
        color: #777;
        max-width: 600px;
        margin: 0 auto;
        word-break: keep-all;
    }

    /* 4. Donation Card (Glassmorphism) */
    .donation-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
        margin-top: 30px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 30px 20px;
        width: 100%;
        max-width: 400px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        text-align: center;
        position: relative;
        box-sizing: border-box;
    }

    .kakaopay-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background-color: #FFEB00;
        color: #3C1E1E;
        text-decoration: none;
        padding: 15px 20px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        width: 100%;
        box-shadow: 0 8px 20px rgba(255, 235, 0, 0.2);
        margin-bottom: 25px;
        box-sizing: border-box;
    }

    .kakaopay-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(255, 235, 0, 0.3);
    }

    .kakaopay-logo {
        height: 20px;
    }

    /* QR Placeholder Overlay */
    .qr-container {
        background: #fdfaf5;
        border: 1px dashed #D4A373;
        border-radius: 16px;
        padding: 15px;
        margin: 0 auto;
        width: 150px;
        height: 150px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        cursor: help;
        box-sizing: border-box;
    }

    .qr-container span {
        font-size: 0.75rem;
        color: #D4A373;
        margin-top: 8px;
        font-weight: 500;
    }

    .qr-placeholder-icon {
        font-size: 2rem;
        opacity: 0.4;
    }

    /* 5. Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Small screens */
    @media (max-width: 600px) {
        .coffee-page { padding: 20px 15px; }
        .hero-img { height: 240px; }
        .hero-title { font-size: 1.4rem; }
        .hero-overlay { padding: 20px; }
        .main-message { font-size: 1.2rem; }
        .sub-message { font-size: 0.95rem; }
        .glass-card { padding: 25px 15px; }
        .kakaopay-btn { font-size: 1rem; padding: 12px 15px; }
    }
</style>

<div class="coffee-page">
    <!-- Hero Section -->
    <div class="hero-container">
        <img src="/assets/images/coffee_donation.png" class="hero-img" alt="Digital Library Coffee Support">
        <div class="hero-overlay">
            <h1 class="hero-title">Archive S : Digital Library Support</h1>
            <p class="hero-subtitle">Cultivating Knowledge, One Cup at a Time.</p>
        </div>
    </div>

    <!-- Message -->
    <section class="message-box">
        <h2 class="main-message">"더 나은 디지털 도서관 콘텐츠 제작을 위해<br>커피 한 잔의 힘을 보태주세요."</h2>
        <p class="sub-message">
            Archive S는 파편화된 지식을 정갈하게 갈무리하고, 수학교육의 새로운 가능성을 탐구하는 디지털 공간입니다. 
            당신이 보내주신 따뜻한 응원은 더 깊이 있는 도서관 콘텐츠와 학습 도구들을 개발하는 데 소중히 사용됩니다.
        </p>
    </section>

    <!-- Donation Action -->
    <section class="donation-section">
        <div class="glass-card">
            <!-- 
                TIP: 카카오페이 송금 링크가 생기면 아래 href를 교체하세요. 
                예: https://qr.kakaopay.com/281006011... 
            -->
            <a href="https://qr.kakaopay.com/FSSJrWbkG" class="kakaopay-btn" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/f/f2/KakaoPay_logo.svg" class="kakaopay-logo" alt="KakaoPay">
                카카오페이로 후원하기
            </a>

            <div class="qr-container" title="준비 중입니다. 곧 여러분만의 코드를 담아드릴게요!">
                <div class="qr-placeholder-icon">🔲</div>
                <span>Scan QR to Support</span>
                
                <!-- 
                    TIP: QR 코드 이미지 파일이 준비되면 아래 img 태그를 활성화하세요.
                    <img src="/assets/images/my_kakaopay_qr.png" style="width:100%; height:100%; position:absolute; top:0; left:0; border-radius:14px; padding:10px; background:white;"> 
                -->
            </div>
            
            <p style="margin-top: 25px; font-size: 0.85rem; color: #999;">
                * 후원해주시는 모든 분들의 따뜻한 마음을 소중히 기억하겠습니다.
            </p>
        </div>
    </section>

    <!-- Footer Quote -->
    <footer style="margin-top: 100px; text-align: center; border-top: 1px solid #eee; padding-top: 40px;">
        <p style="font-family: 'Playfair Display', serif; font-style: italic; color: #aaa; font-size: 0.9rem;">
            "Entropy decreases where care increases."
        </p>
    </footer>
</div>
