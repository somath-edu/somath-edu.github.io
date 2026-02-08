---
layout: page
title: Archive S
permalink: /about/
---

<style>
    /* 디자인 설정 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    
    .author-page { font-family: 'Noto Sans KR', sans-serif; color: #4A3B32; padding: 20px 0; }
    .author-page h2 { font-family: 'Playfair Display', serif; }

    /* 프로필 */
    .profile-box { text-align: center; margin-bottom: 50px; }
    .profile-img { width: 120px; height: 120px; border-radius: 50%; border: 3px solid #fcfbf9; box-shadow: 0 5px 15px rgba(0,0,0,0.1); object-fit: cover; }
    .profile-name { font-family: 'Playfair Display', serif; font-size: 2rem; margin: 10px 0 5px; }
    .profile-job { color: #D4A373; font-weight: bold; letter-spacing: 1px; font-size: 0.9rem; }

    /* 3S 카드 */
    .s-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 50px; }
    .s-card { background: white; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #eee; }
    .s-icon { font-size: 1.5rem; margin-bottom: 10px; display: block; }

    /* 방명록 버튼 효과 */
    .guestbook-btn {
        display: inline-block;
        background-color: #4A3B32;
        color: #fcfbf9 !important; /* 링크 색상 강제 지정 */
        padding: 12px 30px;
        text-decoration: none;
        border-radius: 50px;
        font-weight: bold;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #4A3B32;
    }
    .guestbook-btn:hover {
        background-color: #fff;
        color: #4A3B32 !important;
        cursor: pointer;
        transform: translateY(-2px);
    }
</style>

<div class="author-page">
    <div class="profile-box">
        <img src="/assets/IMG_1754.webp" class="profile-img" alt="Writer">
        <h1 class="profile-name">Archive S</h1>
        <div class="profile-job">Education Archiver : So-Du</div>
        <p>무질서한 지식의 엔트로피를 낮추는 공간입니다.</p>
    </div>

    <div class="s-grid">
        <div class="s-card"><span class="s-icon">📂</span><strong>Storage</strong><br><span style="font-size:0.8rem; color:#888;">기록하고</span></div>
        <div class="s-card"><span class="s-icon">🔗</span><strong>Share</strong><br><span style="font-size:0.8rem; color:#888;">연결하고</span></div>
        <div class="s-card"><span class="s-icon">📈</span><strong>Step-up</strong><br><span style="font-size:0.8rem; color:#888;">성장하다</span></div>
    </div>
    
    <hr style="border:0; height:1px; background:#eee; margin:40px 0;">

    <div style="text-align:center; margin-top: 60px;">
        <h3 style="font-family: 'Playfair Display', serif; color: #4A3B32; margin-bottom: 10px;">Guestbook</h3>
        <p style="color: #666; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.6;">
            고민이 있거나 대화가 필요하신가요?<br>
            <strong>Archive S</strong>가 당신의 이야기를 기다립니다.
        </p>

        <a href="https://github.com/somath-edu/somath-edu.github.io/issues" target="_blank" class="guestbook-btn">
           ✉️ Archive S에게 편지 남기기
        </a>

        <p style="font-size: 0.75rem; color: #aaa; margin-top: 20px;">
            *GitHub 계정으로 로그인 후 'New Issue'를 눌러 글을 남길 수 있습니다.<br>
            *남겨주신 글에 Archive S가 답장을 보내드립니다.
        </p>
    </div>
</div>
