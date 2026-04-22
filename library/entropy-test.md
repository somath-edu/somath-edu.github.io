---
layout: chapter
title: 학습 엔트로피 자가 진단
permalink: /entropy-test.html
prev_link: /entropy-ch1.html
next_link: /entropy-ch2.html
---

<div class="test-intro">
  <p>현재 당신(혹은 아이)의 학습 상태는 얼마나 무질서할까요? 아래 10가지 항목 중 해당되는 것을 체크해 보세요. 인지하는 것이 질서의 시작입니다.</p>
</div>

<div class="quiz-container">
  <div class="checklist" id="entropy-checklist">
    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb1">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">설명 불가</span>
        <span class="check-desc">방금 배운 내용을 책을 덮고 설명하라고 하면 꿀 먹은 벙어리가 된다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb2">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">시작 지연</span>
        <span class="check-desc">"공부하자"라고 마음먹고 실제 책을 펴기까지 10분 이상 딴짓을 한다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb3">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">물건 찾기</span>
        <span class="check-desc">필기구, 노트, 프린트물을 찾는 데 시간을 자주 허비한다. (책상이 어지럽다.)</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb4">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">메타인지 오류</span>
        <span class="check-desc">눈으로 보고 "안다"고 착각하지만, 막상 문제를 풀면 틀린다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb5">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">맥락 부재</span>
        <span class="check-desc">단편적인 지식은 외우지만, 전체적인 단원의 흐름은 모른다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb6">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">만성 불안</span>
        <span class="check-desc">공부를 안 하면 불안한데, 막상 앉아 있어도 집중이 안 된다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb7">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">멀티태스킹</span>
        <span class="check-desc">공부 중 스마트폰 알림을 즉시 확인하거나, 음악을 들어야 마음이 편하다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb8">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">용두사미</span>
        <span class="check-desc">계획은 거창하게 세우지만, 3일을 넘기지 못하고 흐지부지된다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb9">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">응용 불가</span>
        <span class="check-desc">교과서 문제는 풀지만, 조금만 비틀어 낸 응용문제는 손도 못 댄다.</span>
      </div>
    </div>

    <div class="check-item-card" onclick="toggleCheck(this)">
      <div class="checkbox-box">
        <input type="checkbox" class="entropy-cb" id="cb10">
        <span class="checkmark"></span>
      </div>
      <div class="check-text">
        <span class="check-title">번아웃</span>
        <span class="check-desc">시험 기간이 끝나면 머리가 텅 빈 것 같고, 다시 공부할 의욕이 생기지 않는다.</span>
      </div>
    </div>
  </div>

  <div id="result-container" class="result-box hidden">
    <div class="result-header">
      진단 결과: <span id="result-status">상태</span>
    </div>
    <div class="result-score">
      나의 무질서 점수: <span id="score-display">0</span> / 10
    </div>
    <div class="result-description" id="result-desc">
      결과 설명이 여기에 표시됩니다.
    </div>
  </div>

</div>

<style>
.test-intro {
  text-align: center;
  margin-bottom: 3rem;
  font-size: 1.1rem;
  color: #666;
  line-height: 1.6;
}

.quiz-container {
  max-width: 600px;
  margin: 0 auto;
}

.checklist {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.check-item-card {
  display: flex;
  align-items: flex-start;
  padding: 20px;
  background: #fff;
  border: 1px solid #eee;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
  user-select: none;
}

.check-item-card:hover {
  border-color: #d88e88;
  background: #fffcfb;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(216, 142, 136, 0.08);
}

.check-item-card.checked {
  border-color: #d88e88;
  background: #fdf8f8;
}

.checkbox-box {
  margin-right: 20px;
  margin-top: 4px;
}

.checkbox-box input {
  display: none;
}

.checkmark {
  display: inline-block;
  width: 24px;
  height: 24px;
  border: 2px solid #ddd;
  border-radius: 50%;
  position: relative;
  transition: all 0.2s ease;
}

.check-item-card.checked .checkmark {
  background: #d88e88;
  border-color: #d88e88;
}

.check-item-card.checked .checkmark::after {
  content: "✓";
  color: white;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-size: 14px;
  font-weight: bold;
}

.check-text {
  flex: 1;
}

.check-title {
  display: block;
  font-weight: 700;
  font-size: 1.1rem;
  color: #2c2c2c;
  margin-bottom: 4px;
}

.check-desc {
  font-size: 0.95rem;
  color: #777;
  line-height: 1.5;
}

.result-box {
  margin-top: 4rem;
  padding: 30px;
  border-radius: 16px;
  text-align: center;
  border: 2px solid #eee;
  transition: all 0.3s ease;
}

.result-box.hidden {
  display: none;
}

.result-box.stable { border-color: #6d8e6d; background: #f7faf7; }
.result-box.warning { border-color: #e5b05c; background: #fdfbf5; }
.result-box.danger { border-color: #c95c5c; background: #fdf5f5; }

.result-header {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 10px;
}

.stable .result-status { color: #6d8e6d; }
.warning .result-status { color: #e5b05c; }
.danger .result-status { color: #c95c5c; }

.result-score {
  font-size: 1rem;
  color: #666;
  margin-bottom: 20px;
}

.result-score span {
  font-weight: 700;
  color: #2c2c2c;
}

.result-description {
  font-size: 1.1rem;
  line-height: 1.7;
  color: #444;
  margin-bottom: 30px;
  word-break: keep-all;
}


</style>

<script>
function toggleCheck(card) {
  const checkbox = card.querySelector('input[type="checkbox"]');
  checkbox.checked = !checkbox.checked;
  
  if (checkbox.checked) {
    card.classList.add('checked');
  } else {
    card.classList.remove('checked');
  }
  
  updateResults();
}

function updateResults() {
  const checkboxes = document.querySelectorAll('.entropy-cb');
  const checkedCount = Array.from(checkboxes).filter(cb => cb.checked).length;
  const resultBox = document.getElementById('result-container');
  const statusSpan = document.getElementById('result-status');
  const scoreSpan = document.getElementById('score-display');
  const descDiv = document.getElementById('result-desc');
  
  scoreSpan.innerText = checkedCount;
  resultBox.classList.remove('hidden', 'stable', 'warning', 'danger');
  
  if (checkedCount <= 2) {
    resultBox.classList.add('stable');
    statusSpan.innerText = "저엔트로피 상태 (안정)";
    descDiv.innerText = "학습 효율이 매우 높습니다. 지식이 체계적으로 정리되어 있으며, 최소한의 노력으로 최대의 효과를 내고 있습니다. 지금의 흐름을 유지하며 'Part 2'의 기술을 더해 속도를 높여보세요.";
  } else if (checkedCount <= 6) {
    resultBox.classList.add('warning');
    statusSpan.innerText = "중엔트로피 상태 (주의)";
    descDiv.innerText = "열심히는 하지만 효율이 떨어지기 시작했습니다. 무질서가 스멀스멀 피어오르고 있어요. 지금 바로 정돈하지 않으면 곧 '고엔트로피'의 늪에 빠지게 됩니다. 엔트로피를 낮추는 기술이 시급합니다.";
  } else {
    resultBox.classList.add('danger');
    statusSpan.innerText = "고엔트로피 상태 (위험)";
    descDiv.innerText = "비상사태입니다. 뇌는 이미 혼란의 도가니에 빠져 있습니다. 아무리 시간을 쏟아부어도 '밑 빠진 독에 물 붓기'일 뿐입니다. 지금은 새로운 지식을 넣는 것을 멈추고, 먼저 '비우고 정리하는' 작업부터 시작해야 합니다.";
  }
}
</script>
