---
layout: page
title: Archive S
permalink: /about/
---

<style>
    /* 1. 기본 폰트 및 배경 설정 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    
    .author-page { font-family: 'Noto Sans KR', sans-serif; color: #4A3B32; padding: 20px 0; max-width: 800px; margin: 0 auto; }

    /* 2. 프로필 섹션 디자인 */
    .profile-box { text-align: center; margin-bottom: 50px; }
    .profile-img { width: 130px; height: 130px; border-radius: 50%; border: 4px solid #fff; box-shadow: 0 10px 25px rgba(0,0,0,0.08); object-fit: cover; transition: transform 0.3s ease; }
    .profile-img:hover { transform: scale(1.05); }
    .profile-name { font-family: 'Playfair Display', serif; font-size: 2.2rem; margin: 15px 0 5px; font-weight: 700; }
    .profile-job { color: #D4A373; font-weight: 700; letter-spacing: 1.5px; font-size: 0.85rem; text-transform: uppercase; margin-bottom: 15px; }
    .profile-desc { font-size: 0.95rem; color: #666; line-height: 1.6; }

    /* 3. 3S 카드 (Storage / Share / Step-up) */
    .s-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; margin-bottom: 60px; }
    .s-card { background: #fff; padding: 25px 15px; border-radius: 15px; text-align: center; border: 1px solid #f0f0f0; box-shadow: 0 4px 12px rgba(0,0,0,0.03); transition: all 0.3s ease; }
    .s-card:hover { transform: translateY(-5px); box-shadow: 0 8px 20px rgba(0,0,0,0.06); }
    .s-icon { font-size: 1.8rem; margin-bottom: 12px; display: block; }
    .s-card strong { font-size: 1.1rem; color: #4A3B32; display: block; margin-bottom: 5px; }

    /* 4. 방명록 섹션 꾸미기 */
    .guestbook-section { margin-top: 80px; padding-top: 40px; border-top: 1px solid #eee; }
    .guestbook-header { text-align: center; margin-bottom: 40px; }
    .guestbook-title { font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #4A3B32; margin-bottom: 10px; }
    
    .guestbook-notice { 
        background-color: #fcfbf9; 
        border-radius: 20px; 
        padding: 35px 25px; 
        margin-bottom: 40px; 
        border: 1px dashed #D4A373;
        text-align: center;
    }

    /* Giscus 영역 여백 */
    .giscus { margin-top: 20px; }
</style>

<div class="author-page">
    <header class="profile-box">
        <img src="/assets/IMG_1754.webp" class="profile-img" alt="Archive S">
        <h1 class="profile-name">Archive S</h1>
        <div class="profile-job">Education Archiver : So-Du</div>
        <p class="profile-desc">무질서한 지식의 엔트로피를 낮추고,<br>교육의 본질을 정갈하게 기록하는 공간입니다.</p>
    </header>

    <div class="s-grid">
        <div class="s-card">
            <span class="s-icon">📂</span>
            <strong>Storage</strong>
            <span style="font-size:0.8rem; color:#999;">흩어진 지식을 갈무리하고</span>
        </div>
        <div class="s-card">
            <span class="s-icon">🔗</span>
            <strong>Share</strong>
            <span style="font-size:0.8rem; color:#999;">너와 나를 지혜로 연결하며</span>
        </div>
        <div class="s-card">
            <span class="s-icon">📈</span>
            <strong>Step-up</strong>
            <span style="font-size:0.8rem; color:#999;">어제보다 나은 오늘로 성장하다</span>
        </div>
    </div>

    <section class="guestbook-section">
        <div class="guestbook-header">
            <h2 class="guestbook-title">Guestbook</h2>
        </div>

        <div class="guestbook-notice">
            <p style="margin: 0; font-size: 1rem; color: #555; line-height: 1.8;">
                세상의 소음으로 마음이 흩어진 순간인가요?<br>
                당신의 생각을 남겨주세요. <br>
                <strong>Archive S</strong>가 따뜻한 시선으로 답장을 보냅니다.
            </p>
        </div>

        <script src="https://giscus.app/client.js"
                data-repo="somath-edu/somath-edu.github.io"
                data-repo-id="R_kgDORFSD4g"
                data-category="General"
                data-category-id="DIC_kwDORFSD4s4C2DWI"
                data-mapping="pathname"
                data-strict="0"
                data-reactions-enabled="1"
                data-emit-metadata="0"
                data-input-position="top"
                data-theme="light"
                data-lang="ko"
                crossorigin="anonymous"
                async>
        </script>

        <p style="text-align: center; font-size: 0.75rem; color: #aaa; margin-top: 30px;">
            * GitHub 계정으로 로그인 후 마음을 남겨주세요.<br>
            * 작성하신 글은 Archive S의 기록으로 소중히 보관됩니다.
        </p>
    </section>
</div>
