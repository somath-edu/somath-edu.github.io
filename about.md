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
        font-size: 1.6rem;
        font-weight: 700;
        color: #5D4037;
        margin-bottom: 20px;
        word-break: keep-all;
        line-height: 1.5;
    }

    .sub-message {
        font-size: 1rem;
        color: #795548;
        max-width: 600px;
        margin: 0 auto;
        word-break: keep-all;
        opacity: 0.85;
    }

    /* 4. Donation Card (Redesigned) */
    .donation-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 40px;
        animation: fadeIn 1.2s ease-out;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 32px;
        padding: 40px 30px;
        width: 100%;
        max-width: 420px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.08);
        text-align: center;
        box-sizing: border-box;
    }

    .card-title-mini {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #A1887F;
        margin-bottom: 25px;
        font-weight: 600;
    }

    .qr-frame {
        background: white;
        padding: 15px;
        border-radius: 20px;
        box-shadow: inset 0 0 0 1px rgba(0,0,0,0.05), 0 10px 20px rgba(0,0,0,0.03);
        margin: 0 auto 30px;
        width: 200px;
        height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .qr-image {
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 10px;
    }

    .kakaopay-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background-color: #FFEB00;
        color: #3C1E1E;
        text-decoration: none;
        padding: 20px;
        border-radius: 18px;
        font-weight: 800;
        font-size: 1.15rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        width: 100%;
        box-shadow: 0 10px 20px rgba(255, 235, 0, 0.25);
        box-sizing: border-box;
        white-space: nowrap;
    }

    .kakaopay-btn:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(255, 235, 0, 0.35);
    }

    .kakaopay-text-logo {
        font-weight: 900;
        font-size: 1.2rem;
        letter-spacing: -0.5px;
    }

    .support-footer {
        margin-top: 30px;
        font-size: 0.85rem;
        color: #A1887F;
        line-height: 1.6;
    }

    /* 5. Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Responsive Adjustments */
    @media (max-width: 600px) {
        .coffee-page { padding: 30px 15px; }
        .hero-img { height: 260px; }
        .hero-title { font-size: 1.5rem; }
        .hero-overlay { padding: 25px; }
        .main-message { font-size: 1.3rem; }
        .glass-card { padding: 35px 20px; }
        .kakaopay-btn { font-size: 1rem; padding: 16px; }
        .qr-frame { width: 180px; height: 180px; }
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

    <!-- Donation Card -->
    <section class="donation-section">
        <div class="glass-card">
            <div class="card-title-mini">Kakaopay Donation</div>
            
            <div class="qr-frame">
                <img src="/assets/donation/qr-code.png" class="qr-image" alt="KakaoPay QR Code">
            </div>

            <a href="https://qr.kakaopay.com/FSSJrWbkG" class="kakaopay-btn" target="_blank">
                <span class="kakaopay-text-logo">pay</span>
                카카오페이로 보내기
            </a>
            
            <div class="support-footer">
                <p>QR 코드를 스캔하거나 위 버튼을 눌러주세요.</p>
                <p style="font-weight: 600; margin-top: 5px;">* 보내주시는 소중한 응원, 마음 깊이 새기겠습니다.</p>
            </div>
        </div>
    </section>

    <!-- Footer Quote -->
    <footer style="margin-top: 100px; text-align: center; border-top: 1px solid #f0ece9; padding-top: 40px; padding-bottom: 40px;">
        <p style="font-family: 'Playfair Display', serif; font-style: italic; color: #D7CCC8; font-size: 0.95rem;">
            "Entropy decreases where care increases."
        </p>
    </footer>
</div>
