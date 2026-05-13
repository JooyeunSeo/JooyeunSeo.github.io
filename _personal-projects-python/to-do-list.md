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

# Overview
<hr>

이 서비스는 사용자 단위로 데이터를 분리하여 관리합니다. 모든 할 일은 인증된 사용자와 연결되어 저장되며, 로그인 상태에 따라 개별적인 데이터가 로드됩니다.

메인 페이지는 단일 GET 요청으로 로드됩니다. 서버는 사용자의 인증 여부를 확인한 후, 해당 사용자의 데이터를 진행 중, 완료, 기한 초과의 세 가지 그룹으로 분류하여 화면에 표시합니다. 할 일의 추가, 수정, 순서 변경, 삭제와 같은 주요 작업은 사용자 경험을 저해하지 않도록 AJAX 비동기 요청을 통해 페이지 이동 없이 처리합니다.
<br><br><br>

# System & Interface Design
<hr>

이 서비스는 사용자 단위로 할 일 데이터를 분리하여 관리하도록 설계되었습니다. 모든 할 일은 인증된 사용자와 연결되어 저장되며, 로그인 상태에 따라 조회되는 데이터가 달라집니다.

메인 페이지는 하나의 GET 요청으로 로드되며, 서버는 인증 여부를 확인한 뒤 사용자에 해당하는 할 일 목록만 조회합니다.    
조회된 데이터는 할 일의 완료 상태와 마감일을 기준으로 진행 중, 완료, 기한 초과의 세 가지 그룹으로 분류되어 화면에 표시됩니다.

할 일의 추가, 수정, 순서 변경, 삭제와 같은 주요 작업은 페이지 이동 없이 비동기 요청을 통해 처리되도록 구성하였습니다.

### Information Architecture

<figure>
  <a href="https://mermaid.live/edit#pako:eNqNVGFv2jAQ_SuWpUqtBAWSQELUMVHCpEndWkFppZFqcuIjWA1JZifrGPDfd3GyLqXaVn-J7Xv3_O6dnR0NUw7Upas4fQrXTObkauYnfkJwnJyQd8eDLObT2evtKkEVQSRZtiYLBXLp00ksIMnJ6T0EZPHxzKcPFa4ci96ycxGMpkkOktywCC46wajTBBhLjM9AFXFO7gQ8lYBm3FyWgFumHsl1BpLlIk1UCboIZGfUJmPOSYdMucjx40EMOZASXYdv0yiKgYTpJitD9e4MUslRUY5A9VAfBwn_pydoyd0bXJmD_K59qSYv7Jj3dljMuMjX6JgIdTFksobw8bkioUiBvpIYhQMnInl_aORrt65SxrX5utA_ZgRbnfpV8OaRZpkyiZlSYrU9ymiTG6xaJFG9mtQ28Xp9jQXwApp0Vkk3zrK44kL1LIlAHbVt3td994TKYrYln0CpuvnIPMLaREIkfCuEBN55o__e-HZ8OZ5P_9sB7xLd91jOAqbghf9eb3mKsmrvglgrOmsCDA3Qlb0C_E_gh6vr-7-JW_RIuz3CC9BgKO8BCSRLwjW2oNqea9y-cUWA77HvL6Kf05wcI_qaf2E0-Mv3hveI8TrZ0BCvUuJVq7n5Ok_bw0L90mr1GrzXgbEO7PFlVgSWDv22mywyjor2yE9bNJKCU3fFYgUtugG5YeWa7kpWn2IBG-yPi1MOK4Z_AJ_6yQHzMpZ8SdMNdXNZYKZMi2j9zFPoEzzBsNub512J3QE5SYskp-7AMTUJdXf0B3Ut-9x27IFh2UPLsWxr0KJb6vaM4Xm_P7Cdbr9ndm3HcA4t-lMf2z0fmn3T6ZrDoWHYPcswD78Ae0OIFA" target="_blank" title="Mermaid Live Editor">
    <img src="/assets/images/personal-projects/to_do_list_IA.png" alt="IA">
  </a>
</figure>

위 구조는 사용자가 페이지에 접근한 이후의 데이터 흐름과 액션 반영 과정을 나타냅니다.

1. **인증 확인:** 페이지 접근 시 서버는 로그인 상태를 확인합니다.
2. **데이터 로드:** 인증된 사용자의 할 일 목록만 조회하여 상태별로 화면에 구성합니다.
3. **사용자 액션:** 추가, 수정, 순서 변경, 삭제 요청을 POST(AJAX) 방식으로 서버에 전달합니다.
4. **실시간 반영:** 서버는 DB를 즉시 업데이트하며, 변경 사항은 페이지 재로딩 없이 화면에 반영됩니다.

### Data Model

사용자 중심의 관리를 위해 User와 Task 두 개의 주요 엔티티를 활용합니다.

- **User:** ID, 이름, 이메일, 비밀번호 등 인증 정보를 관리하며 Task와 1:N 관계를 가집니다.
- **Task:** 할 일 내용, 완료 여부(`is_done`), 마감일, 사용자 외래키(`tasker_id`), 정렬 순서(`order`)를 포함합니다. 마감일은 사용자가 입력한 로컬 시간 기준의 값을 UTC로 변환하여 저장하였습니다. 이는 글로벌 대응이 가능하도록 합니다.

### UI 

상태별 시각적 차별화를 통해 직관성을 높였습니다.

- **상태별 분류:** 진행 중(검정), 완료(회색+취소선), 기한 초과(빨강 강조)로 구분하여 표시합니다.
- **인터랙션 요소:** 드래그 앤 드롭 전용 핸들(☰)과 삭제 버튼(✘)을 배치하여 조작 편의성을 제공합니다.
- **대시보드 기능:** 상단에 각 상태별 할 일 개수를 표시하여 전체 진행 상황을 한눈에 파악할 수 있습니다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Backend:** Flask, Flask-Login, Jinja2, SQLAlchemy, Flask-WTF(보안이 강화된 웹 폼)
- **Frontend:** JavaScript, AJAX
- **Database:** SQLite

### Key Implementation Details

1. **사용자 인증 및 세션 관리**
   - Flask-Login을 사용하여 보안 세션을 관리하며, 인증된 사용자만 본인의 `user_id`와 연결된 데이터에 접근하도록 제한하였습니다.
2. **입력 양식 처리**
   - Flask-WTF을 사용하여 폼을 구성하고 CSRF 보호 기능을 적용하였습니다. 모든 입력값은 서버 측 유효성 검사를 거쳐 데이터베이스에 반영됩니다.
3. **AJAX**
   - 순서 변경: SortableJS를 활용해 드래그 앤 드롭 기능을 구현하였습니다. 순서 변경 시 서버로 ID 배열을 전송하여 order 필드를 일괄 업데이트합니다.
   - 상태 및 텍스트 수정: 상태 토글 및 할 일 내용 수정 시 AJAX 요청을 통해 DB를 갱신하고, 상단의 상태별 카운트도 실시간으로 업데이트합니다.
   - 시간대 설정: 최초 로드 시 브라우저의 시간대 정보를 서버 세션(Asia/Seoul 등)에 저장하여 개인화된 시간 서비스를 제공합니다.
4. **시간대 관리 전략**
   - 마감일은 항상 UTC 기준으로 처리합니다. 입력된 로컬 시간은 서버에서 UTC로 변환하여 저장하며, 출력 시에는 다시 사용자의 세션 시간대에 맞춰 복원하여 표시하는 방식을 취하였습니다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem

배포 후, 사용자가 설정한 마감일이 실제 시간과 다르게 표시되거나 기한이 남았음에도 '기한 만료'로 처리되는 문제가 발생하였습니다. 이는 제 로컬 환경(KST)과 서버 환경의 기본 시간대 차이에서 비롯된 문제였습니다.

### Solution

첫 시도로 모든 시간 기준을 UTC로 통일하는 구조를 설계하였습니다.

1. 입력된 naive datetime을 사용자 시간대 기준으로 해석 후 UTC 변환
2. UTC 값을 DB에 저장
3. 조회 시 사용자 시간대로 재변환하여 표시

하지만 이 구조를 적용했음에도 화면에는 여전히 UTC 기준 시간이 그대로 표시되는 현상이 나타났습니다. 원인은 DB에서 꺼내온 데이터의 상태에 있었습니다. SQLite에 저장된 시간은 저장 과정에서 시간대 정보가 제거된 naive datetime 형식이었습니다. 시스템이 이를 어떤 시간대로 해석해야 할지 몰라 변환 로직이 꼬였던 것입니다.

이를 해결하기 위해 DB에서 조회한 값을 'UTC 시간'으로 명시적으로 복원(Aware Datetime 타입으로)하는 단계를 추가하였습니다. 그 후 사용자 시간대로 변환하자 의도한 대로 정확한 현지 시간이 출력되었습니다.

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
할 일에 우선순위를 지정하고 우선순위에 따라 목록을 자동 정렬할 수 있는 기능 구현
<br><br><br>

# Conclusion
<hr>

이번 프로젝트를 통해 시간대(Timezone) 처리가 웹 서비스의 신뢰성에 중요한 영향을 미친다는 것을 체감하였습니다. 단순한 값의 저장을 넘어, 데이터가 어떤 기준을 가지고 있는지를 코드로 명확히 표현하는 것이 얼마나 중요한지 배웠습니다.

특히 Flask 세션과 비동기 통신을 조합하여 사용자 맞춤형 환경을 구축해 본 경험은 향후 더 복잡한 글로벌 서비스를 설계하는 데 있어 소중한 경험이 될 것이라고 생각합니다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}