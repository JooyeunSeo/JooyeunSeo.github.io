---
date: 2025-12-14
layout: splash
excerpt: "A simple to-do tracking service. Add tasks, check them off when completed, and set due dates. Overdue tasks are automatically marked when not finished on time."
title: "To-do List"
header:
  teaser: "https://cdn.pixabay.com/photo/2021/03/28/13/02/lists-6131220_1280.jpg"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://cdn.pixabay.com/photo/2021/03/28/13/02/lists-6131220_1280.jpg
  caption: "Photo credit: [**Pixabay**](https://pixabay.com/ko/illustrations/%EA%B8%B0%EC%9A%B8%EA%B8%B0-%ED%95%A0-%EA%B2%83-%EC%A2%85%EC%9D%B4-6131220/)"
  actions:
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/todo_list"
    - label: "Check the Code"
      url: "https://github.com/JooyeunSeo/Dynamic-Web-Page"  
---

# Intro
<hr>

이 프로젝트는 로그인한 사용자가 개인적인 할 일 목록을 직관적으로 관리할 수 있도록 만든 Todo List 웹 서비스입니다.

사용자는 할 일을 추가하고 완료 여부를 전환하며, 마감일을 기준으로 현재 해야 할 작업을 한눈에 확인할 수 있습니다.    
완료한 항목은 클릭 한 번으로 상태를 변경할 수 있고, 마우스 드래그를 통해 할 일의 순서를 자유롭게 조정할 수 있습니다.

마감일이 설정되었지만 아직 완료하지 않은 할 일은 목록 하단에 따로 정리되어 표시되기 때문에, 해야 할 일을 자주 놓치거나 관리가 어려운 사용자에게도 도움이 되도록 설계되었습니다.

웹 환경에서 간단한 할 일을 빠르게 기록하고 진행 상황을 시각적으로 관리하는 것을 목표로 합니다.
<br><br><br>

# Design
<hr>

### Overview 

이 서비스는 사용자 단위로 할 일 데이터를 분리하여 관리하도록 설계되었다.       
모든 할 일은 인증된 사용자와 연결되어 저장되며, 로그인 상태에 따라 조회되는 데이터가 달라진다.

메인 페이지는 하나의 GET 요청으로 로드되며, 서버는 인증 여부를 확인한 뒤 사용자에 해당하는 할 일 목록만 조회한다.    
조회된 데이터는 할 일의 완료 상태와 마감일을 기준으로 진행 중, 완료, 기한 초과의 세 가지 그룹으로 분류되어 화면에 표시된다.

할 일의 추가, 수정, 순서 변경, 삭제와 같은 주요 작업은 페이지 이동 없이 비동기 요청을 통해 처리되도록 구성하였다.

### Information Architecture

<figure>
  <a href="https://mermaid.live/edit#pako:eNqNVGFv2jAQ_SuWpUqtBAWSQELUMVHCpEndWkFppZFqcuIjWA1JZifrGPDfd3GyLqXaVn-J7Xv3_O6dnR0NUw7Upas4fQrXTObkauYnfkJwnJyQd8eDLObT2evtKkEVQSRZtiYLBXLp00ksIMnJ6T0EZPHxzKcPFa4ci96ycxGMpkkOktywCC46wajTBBhLjM9AFXFO7gQ8lYBm3FyWgFumHsl1BpLlIk1UCboIZGfUJmPOSYdMucjx40EMOZASXYdv0yiKgYTpJitD9e4MUslRUY5A9VAfBwn_pydoyd0bXJmD_K59qSYv7Jj3dljMuMjX6JgIdTFksobw8bkioUiBvpIYhQMnInl_aORrt65SxrX5utA_ZgRbnfpV8OaRZpkyiZlSYrU9ymiTG6xaJFG9mtQ28Xp9jQXwApp0Vkk3zrK44kL1LIlAHbVt3td994TKYrYln0CpuvnIPMLaREIkfCuEBN55o__e-HZ8OZ5P_9sB7xLd91jOAqbghf9eb3mKsmrvglgrOmsCDA3Qlb0C_E_gh6vr-7-JW_RIuz3CC9BgKO8BCSRLwjW2oNqea9y-cUWA77HvL6Kf05wcI_qaf2E0-Mv3hveI8TrZ0BCvUuJVq7n5Ok_bw0L90mr1GrzXgbEO7PFlVgSWDv22mywyjor2yE9bNJKCU3fFYgUtugG5YeWa7kpWn2IBG-yPi1MOK4Z_AJ_6yQHzMpZ8SdMNdXNZYKZMi2j9zFPoEzzBsNub512J3QE5SYskp-7AMTUJdXf0B3Ut-9x27IFh2UPLsWxr0KJb6vaM4Xm_P7Cdbr9ndm3HcA4t-lMf2z0fmn3T6ZrDoWHYPcswD78Ae0OIFA" target="_blank" title="Mermaid Live Editor">
    <img src="/assets/images/personal-projects/to_do_list_IA.png" alt="IA">
  </a>
</figure>

위 플로우 차트는 사용자가 페이지에 접근한 이후 화면에 할 일이 표시되고 각 사용자 행동이 서버와 데이터베이스에 반영되는 전체 흐름을 나타낸다.

1. 사용자가 페이지에 접근하면 GET 요청을 통해 서버는 로그인 상태를 확인한다.
2. 인증된 사용자의 경우, 해당 사용자와 연결된 할 일만 조회하여 화면을 구성한다.
3. 화면에 표시된 각 할 일에 대해 사용자는 추가, 수정, 순서 변경, 삭제 등의 작업을 수행할 수 있다.
4. 모든 사용자 액션은 POST 요청을 통해 서버로 전달되며, 데이터베이스에 즉시 반영된다.
5. 변경된 데이터는 이후 페이지 재로딩 또는 재요청 시 다시 조회되어 화면에 반영된다.

### Data Model

사용자 단위로 분리된 할 일 목록을 제공하기 위해 User와 Task 두 개의 주요 엔티티로 구성된다.

- User (`id`, `name`, `email`, `password`)
   - 사용자를 식별하기 위한 기본 정보와 인증 정보를 저장한다.
   - 하나의 사용자는 여러 개의 할 일을 가질 수 있으며, 각 할 일은 반드시 하나의 사용자에 속한다.
- Task (`id`, `text`, `is_done`, `due_date`, `tasker_id`, `order`)
   - 개별 할 일에 대한 내용을 저장한다.
   - `tasker_id`를 통해 할 일을 생성한 사용자와 연결되며, 이를 기준으로 로그인한 사용자에게 해당하는 할 일만 조회된다.
   - `is_done` 필드는 할 일의 완료 여부를 나타내며, 진행 중 / 완료 상태 분류에 사용된다.
   - `due_date`는 사용자가 입력한 로컬 시간 기준의 값을 UTC로 변환하여 저장한다.
   - `order` 필드는 사용자가 직접 변경한 할 일의 순서를 저장하며, 동일 사용자 내에서의 목록 정렬에 사용된다.

### UI 

사용자가 할 일의 상태를 직관적으로 인식할 수 있도록 시각적 요소를 설계하였다.

- **진행 중인 할 일:** **□** 아이콘과 **검정색** 텍스트로 표시한다.
- **완료된 할 일:** **▣** 아이콘과 **<font color="Grey"><del>가로 취소선이 적용된 회색</del></font>** 텍스트로 표시한다.
- **기한이 초과된 할 일:** 체크 상태 변경이 불가능하며, **<font color="Red">빨간색</font>** 텍스트로 강조하여 즉시 인식할 수 있도록 한다.
- **할 일 삭제:** 오른쪽 ✘ 아이콘을 클릭하면 해당 할 일을 삭제할 수 있다.
- **할 일 순서 변경:** 왼쪽 **☰** 아이콘을 마우스로 클릭 후 드래그 앤 드롭으로 할 일 목록의 순서를 자유롭게 변경할 수 있다.
- 진행 중, 완료, 기한 초과된 할 일의 개수를 상단에 표시하여 현재 작업 상태를 한눈에 파악할 수 있도록 한다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Backend:** Flask, Flask-Login, SQLAlchemy, Flask-WTF (with WTForms)
- **Templates:** Jinja2 (HTML rendering)
- **Database:** SQLite
- **Frontend:** JavaScript, AJAX

### Coding

1. **사용자 인증 및 세션 관리**
   - Flask-Login을 사용하여 사용자 인증과 세션 관리를 구현하였다.
   - 인증된 사용자에 대해서만 `user_id` 기준으로 자신에게 연결된 할 일 목록에 접근할 수 있다.
2. **입력 양식 처리**
   - Flask-WTF을 사용하여 할 일 입력 및 수정 폼을 구성하였다.
   - CSRF 보호 기능을 통해 폼 제출 요청의 안전성을 확보한다.
   - 모든 필드는 자동으로 유효성 검사를 수행하며, 검증에 실패할 경우 데이터베이스에 반영되지 않는다.
   - 폼은 Jinja2 템플릿에서 렌더링된다.
3. **JavaScript & AJAX**       
페이지 전체를 새로고침하지 않고 사용자 인터랙션을 처리하기 위해 AJAX 기반 비동기 통신을 사용하였다.
   - 할 일 순서 변경
      - SortableJS 라이브러리를 사용하여 할 일 목록에 드래그 앤 드롭 기능을 구현하였다.
      - 순서 변경 시 `onEnd` 이벤트가 발생한다.
      - 변경된 할 일 ID 목록을 배열로 수집하여 서버로 전송한다.
      - 서버는 해당 순서를 기준으로 각 할 일의 `order` 값을 업데이트한다.
   - 할 일 텍스트 수정
      - JavaScript를 통해 텍스트 수정 UI를 활성화한다.
      - 수정 완료 시 AJAX 요청을 통해 변경된 텍스트를 서버로 전달한다.
      - 서버는 해당 할 일의 텍스트를 업데이트하고 데이터베이스에 저장한다.
   - 할 일 완료 상태 변경 & 삭제 처리
      - 사용자가 체크박스를 클릭하면 할 일의 상태가 `진행 중 → 완료` 또는 `완료 → 진행 중`으로 토글되며, 해당 할 일의 `is_done` 값은 반전되어 데이터베이스에 업데이트된다.
      - 오른쪽 ✘ 아이콘을 클릭하면 할 일이 삭제된다. 
      - 모든 변경은 AJAX 요청을 통해 서버에 반영되며, 동시에 각 상태별 할 일 카운트도 자동으로 갱신된다.
   - Flask 세션에 사용자 시간대 저장
      - 페이지 최초 로드 시 JavaScript를 통해 사용자의 브라우저 시간대를 서버로 전송한다.
      - 서버는 해당 시간대를 Flask 세션에 저장한다(e.g. Asia/Seoul).
4. **시간대 관리**
   - 마감일 처리는 사용자 위치에 따라 일관된 경험을 제공하기 위해 UTC 기준으로 설계하였다.
      1. 사용자가 입력한 마감일은 시간대 정보가 없는 naive datetime 형식으로 서버에 전달된다.
      2. 서버는 해당 값을 사용자 세션에 저장된 시간대 기준으로 해석한 뒤 UTC로 변환한다.
      3. UTC로 변환된 시간은 SQLite에 저장될 때 다시 naive datetime 형태로 저장된다.
      4. 데이터를 조회할 때는,
         1. 데이터베이스에서 가져온 naive datetime을 UTC 기준 시간으로 다시 명시적으로 변환한 후
         2. 사용자 세션에 저장된 시간대 기준으로 재변환하여 화면에 표시한다.
   - 이와 같은 방식을 통해 사용자가 다른 시간대에서 접속하더라도, 마감일은 항상 해당 사용자의 현지 시간 기준으로 정확하게 표시된다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem

초기 구현 단계에서는 현재 시간과 마감일을 비교하기 위해 datetime 타입을 사용하고 있었고, 로컬 개발 환경에서는 해당 로직이 정상적으로 동작한다고 판단했다.

그러나 실제 웹 서버에 배포한 이후, 사용자가 설정한 마감일이 로컬 시간과 다르게 표시되는 문제가 발생했다.

### First Analysis & Attempted Solution

이 문제는 시간대 처리가 전혀 없어서 발생한 것이 아니라, 서버 환경의 시간 기준을 명시적으로 고려하지 않았다는 점에서 비롯된 것으로 보였다. 로컬 개발 환경은 KST 기준이었지만 <u>실제 웹 서버는 다른 시간대를 기준으로 동작</u>하고 있고, 이로 인해 사용자 입력 시간과 서버에서 처리되는 시간 사이에 차이가 발생했다고 판단했다.

두 환경 간의 시간 기준을 일관되게 맞추기 위해, 모든 시간을 UTC 기준으로 통일하여 처리하는 구조로 변경했다. 적용한 흐름은 다음과 같다.

1. 사용자가 입력한 마감일은 naive datetime 형태로 서버에 전달된다.
2. 해당 값을 사용자 로컬 시간대 기준으로 해석한 뒤 UTC로 변환한다.
3. UTC로 변환한 값을 데이터베이스에 저장한다.
4. 할 일 목록을 조회하는 GET 요청 시, 저장된 시간을 다시 사용자 시간대 기준으로 변환하여 화면에 표시한다.

이 구조를 적용한 이후, 로컬 환경과 서버 환경 간의 시간 기준 차이로 인한 문제는 해결된 것처럼 보였다.

그러나 이후 실제 웹 환경에서 다시 테스트하던 중, 실제로는 몇 시간 뒤가 마감일인 할 일이 기한 만료 상태로 분류되는 문제를 발견했다. 마감일이 의도한 시간보다 약 9시간 빠르게, 즉 UTC 기준 시간 그대로 화면에 반영되는 현상이 발생하고 있었다.

```markdown
User Input (KST)
2025-12-14 22:00       (naive datetime)
↓
사용자 시간대로 해석
2025-12-14 22:00 KST   (aware datetime)
↓
UTC로 변환
2025-12-14 13:00 UTC   (aware datetime)
↓
DB 저장
2025-12-14 13:00       (naive datetime, 의미상 UTC)
↓
할 일 목록 조회
2025-12-14 13:00       (⚠️ UTC timezone으로 착각)
↓
사용자 시간대로 변환
2025-12-14 13:00 KST   (⚠️ naive datetime에 KST timezone을 그대로 부여)
↓
👎 화면 표시
2025-12-14 13:00 KST
```

### Second Analysis & Final Solution

두 번째 분석 단계에서 문제는 시간대 변환 로직 자체가 아니라, 조회 시점의 datetime 상태에 있다는 것을 확인했다.
데이터베이스에 저장된 datetime 값은 UTC 기준으로 변환된 값이지만, <u>저장 과정에서 시간대 정보가 제거되어 naive datetime 형태로만 남아 있었다.</u> 이 사실을 인지하지 못한 채, 해당 값을 이미 UTC 기준으로 변환된 aware datetime 값이라고 가정하고 바로 사용자 시간대 변환을 적용했기 때문에 발생한 문제였다.

핵심은 데이터베이스에서 조회한 naive datetime 값이 어떤 시간대를 기준으로 해석되어야 하는지를 코드에서 명시하지 않았다는 점이었다.

이 프로젝트에서는 모든 시간을 UTC 기준으로 통일해 저장하고 화면에 표시할 때만 사용자가 위치한 시간대에 맞게 변환하는 것을 목표로 했기 때문에, 데이터베이스에서 가져온 naive datetime 값을 UTC 기준의 aware datetime으로 먼저 복원하는 과정을 추가했다. 이후 해당 값을 사용자 세션에 저장된 시간대를 기준으로 변환하면 정상적으로 표시되는 것을 확인할 수 있다.

```markdown
User Input (KST)
2025-12-14 22:00       (naive datetime)
↓
사용자 시간대로 해석
2025-12-14 22:00 KST   (aware datetime)
↓
UTC로 변환
2025-12-14 13:00 UTC   (aware datetime)
↓
DB 저장
2025-12-14 13:00       (naive datetime)
↓
할 일 목록 조회
2025-12-14 13:00 UTC   (UTC timezone으로 명시)
↓
사용자 시간대로 변환
2025-12-14 22:00 KST   (aware datetime)
↓
👍 화면 표시
2025-12-14 22:00 KST
```
<br><br><br>

# Result
<hr>

![](/assets/images/personal-projects/to_do_list_Result.gif)
<br><br><br>

# Future Improvements
<hr>

- **마감 기한 알림**   
할 일의 기한이 임박하면 사용자에게 알림을 보내는 기능 추가
- **우선순위**   
할 일에 우선순위를 지정하고, 우선순위에 따라 목록을 정렬할 수 있는 기능 구현
<br><br><br>

# Conclusion
<hr>

이번 프로젝트에서는 시간대 처리가 서비스의 정확성을 좌우하는 핵심 설계 요소라는 것을 인식하게 되었습니다. 로컬 개발 환경에서는 정상적으로 동작하던 마감일 로직이 실제 서버 환경에서는 마감일이 아직 지나지 않았음에도 기한이 만료된 것으로 처리되는 문제로 이어졌습니다.

문제를 추적하는 과정에서 데이터베이스에 저장되는 datetime 값이 시간대 정보 없이 naive datetime 형태로 관리된다는 점, 이 값이 조회 시점에서 어떤 기준 시간으로 해석되어야 하는지를 명시하지 않았다는 점이 원인임을 이해하게 되었습니다.

이를 해결하기 위해 사용자 입력 시간을 UTC 기준으로 통일해 저장하고, 조회 시에는 저장된 값을 다시 UTC 기준의 aware datetime으로 복원한 뒤 사용자 세션에 저장된 시간대에 맞게 변환하는 구조로 로직을 수정했습니다.

이 경험을 통해 웹 서비스에서는 서로 다른 시간대에 위치한 사용자와 서버 환경을 전제로 시스템을 설계해야 하며, datetime 값 자체뿐만 아니라 그 값이 어떤 시간대를 의미하는지까지 코드로 명확히 표현하는 것이 중요하다는 점을 배웠습니다.

또한 Flask 세션을 활용해 사용자 시간대 정보를 관리하며, 실제 요구사항에 맞는 시간 처리 구조를 설계해볼 수 있었던 의미 있는 경험이었습니다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}