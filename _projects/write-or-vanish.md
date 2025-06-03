---
date: 2025-05-19
layout: splash
excerpt: "Don’t stop, just write. Hesitation is deletion."
title: "Write or Vanish"
header:
  teaser: "https://images.unsplash.com/photo-1609967804992-c9ad515d6049?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://images.unsplash.com/photo-1609967804992-c9ad515d6049?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%EB%B6%88-%EA%B5%AC%EB%8D%A9%EC%9D%B4%EC%97%90-%EB%B6%88%ED%83%80%EB%8A%94-%EB%82%98%EB%AC%B4-jANTjqcrAQA)"
  actions:
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/write_or_vanish"
    - label: "Check the Code"
      url: "https://github.com/JooyeunSeo/Dynamic-Web-Page"  
---

# Intro

무엇을 써야 할지 생각 나지 않아서 아무 것도 쓰지 못하고 시간을 낭비하는 사람들에게 유용한 웹 애플리케이션이다. 5초 이상 타이핑을 멈추면 지금까지 쓴 내용이 모두 사라지는 긴장감 있는 시스템으로 집중해서 글을 쓸 수 있도록 유도한다. 타이머가 종료되면 클립보드에 복사 또는 공유 버튼이 활성화되어, 완성된 글을 손쉽게 저장하거나 전송할 수 있다.   
*100개의 프로젝트로 Python 개발 완전 정복* 에서 예시로 든 웹 앱 <https://www.squibler.io/dangerous-writing-prompt-app> 을 참고해서 비슷하게 제작했다.
<br><br><br>

# Design

1. 초기 상태
   - 사용자는 드롭다운에서 글쓰기 시간(e.g. 10분)을 선택하고 Start 버튼을 클릭 가능
   - 남은 시간을 나타내는 time bar는 흐릿하게 비활성 상태, 글쓰기 영역은 비활성화
2. 세션 시작(시작 버튼 클릭)
   - 사용자가 지정한 시간이 저장되고, time bar가 활성화됨
   - 글쓰기 영역이 편집 가능해지며 포커스가 자동 설정됨
   - 사용자가 타이핑을 시작하면 입력 중단 감지 타이머가 시작됨
3. 세션 진행
   - 매 1초마다 time bar의 진행 상태가 갱신됨
   - 입력이 멈추면 1초 뒤 경고 단계로 진입하고 색 변화, 흔들림 애니메이션 등이 작동
   - 입력 중단이 5초 이상 지속되면 모든 글이 사라짐
4. 세션 종료
   - 글쓰기 영역이 다시 비활성화됨
   - 작성된 글을 복사하거나 공유할 수 있는 버튼 표시
<br><br><br>

# Implementation

### Tech Stack

- **Backend:** Flask
- **Templates:** Jinja2 (HTML rendering)
- **Frontend:** JavaScript (Vanilla), CSS (Custom style, animation)

### JavaScript

- time bar 갱신 (1초마다 실행)
   1. 매 초마다 남은 시간을 비율로 계산(0%에 가까울수록 종료 직전) → `const pct = ((전체시간 - 경과시간) / 전체시간) * 100;`
   2. time bar의 너비를 줄여서 시각적으로 남은 시간 표시 → `timeBar.style.width = pct + "%";`
   3. 지정한 시간이 모두 지나면 성공적으로 세션 종료 → `if (경과시간 >= 전체시간) endSession(true);`
- 입력 중단 및 재개 감지
   1. 사용자가 키보드를 누를 때마다 함수 호출
   2. 이전의 모든 경고 상태 초기화
      1. idleTimer(입력이 멈추고나서 1초 뒤 경고를 시작하는 타이머) 초기화
      2. 경고를 반복적으로 표시하는 인터벌 중지
      3. 배경색을 흰색으로 되돌리고, 글쓰기 영역에 흔들리는 애니메이션 효과 제거
   3. idleTimer에 1초 뒤 경고 시작 함수를 실행하도록 예약(1초 동안 사용자가 아무 입력도 하지 않으면, 경고 시작)
- 입력 중단을 감지할 시 경고
   1. 붉은색 강도를 점점 진하게(불투명도를 높여서) 변경 → `redIntensity = Math.min(redIntensity + 40, 255);`
   2. 배경색을 점점 진한 붉은색으로 변경 → `writingArea.style.background = rgba(255,100,100,${(redIntensity / 255).toFixed(2)});`
      - 불투명도를 알파값으로 비례 변환: `redIntensity / 255`
      - 변환된 알파값은 소수점 둘째 자리까지 자르기: `.toFixed(2)`
   3. 흔들리는 애니메이션 효과 추가: `writingArea.classList.add("shake");`
- 복사 버튼
   1. 사용자가 작성한 글쓰기 영역의 텍스트 내용을 클립보드에 복사 → `navigator.clipboard.writeText(writingArea.innerText)`
   2. 복사 결과에 따라 알림창 띄우기
      - 성공 시: `.then(() => alert("Your text has been copied."))`
      - 실패 시: `.catch(() => alert("Failed to copy"));`
- 공유 버튼
   1. 공유할 텍스트 내용을 변수에 저장 → `const text = writingArea.innerText;`
   2. Web Share API를 지원하는 브라우저인지 확인 → `navigator.share`
      - 공유가 가능할 경우 공유 창을 열어서 복사 또는 다른 앱으로 보낼 수 있도록 허용: `navigator.share({ text })`
      - 공유 기능이 없는 브라우저일 경우 경고창 띄우기: `: alert("This browser does not support the sharing.");`

### CSS animation

- 애니메이션 정의 (@keyframes shake)
   - 원래 위치: `0%, 100% { transform: translate(0px, 0px); }`
   - 오른쪽으로 2x 이동: `25% { transform: translate(2px, 0); }`
   - 아래로 2px 이동: `50% { transform: translate(0, 2px); }`
   - 왼쪽으로 2px: `75% { transform: translate(-2px, 0); }`
- 애니메이션을 텍스트 영역에 적용 (.shake)
   - 애니메이션이 한 바퀴 도는 데 걸리는 시간: `0.5s`
   - 무한 반복: `infinite`
<br><br><br>

# Result

<div style="width: 80%;">{% include video id="1085417083" provider="vimeo" %}</div>

<br><br><br>

# Future Improvements

- **사용자가 직접 타이머 시간을 설정할 수 있는 기능 추가**
- **작성 내용 자동 저장 및 복구 기능 추가**   
브라우저를 실수로 닫았을 때도 작성 중인 내용을 복구할 수 있도록 로컬 저장소에 자동 저장한다.
<br><br><br>

# Conclusion

JavaScript와 CSS 애니메이션 등 프론트엔드 기술에 대해 많이 배울 수 있는 과제였다. 특히 외부 라이브러리 없이 순수 자바스크립트만으로도 실시간 상호작용 처리가 가능하다는 것을 알게 됐다. 또 브라우저 내장 API 덕분에 텍스트를 클립보드에 복사하거나 다른 앱으로 공유하는 기능을 손쉽게 추가할 수 있었다. 기능은 단순하지만 실제로 누군가가 유용하게 사용할 수 있는 유의미한 결과물을 만들어내서 좋았다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}