---
date: 2025-05-04
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

*100개의 프로젝트로 Python 개발 완전 정복*의 과제로 간단한 To-do 리스트 웹사이트를 제작했다. 새로운 항목을 추가하고, 완료한 일은 클릭 한 번으로 상태를 변경할 수 있다. 마감일을 설정한 경우, 기한이 지난 미완료 항목은 자동으로 '기한 초과'로 분류된다. 또한 마우스 클릭과 드래그로 리스트의 순서를 자유롭게 조정할 수 있다.
<br><br><br>

# Design

### Overview

1. 사용자 관리
   - 회원가입 (/register)
   - 로그인, 로그아웃 (/login, /logout)
   - 로그인해서 인증된 사용자만 개인 리스트 사용 가능
2. 메인 페이지 (/todo_list)
   1. 할 일 조회 및 분류 (GET 요청)
      - 로그인한 사용자 DB에 연결된 할 일을 불러옴
      - 각 할 일의 마감일 due_date는 UTC로 저장되며, 사용자의 세션에 저장된 시간대를 기준으로 변환해 화면에 표시
      - 현재 시간과 비교해 다음과 같이 세 분류로 나뉨:
         1. 진행 중: 미완료이고 마감일이 없거나 아직 지나지 않은 할 일
         2. 완료: DB의 `is_done` 컬럼의 값이 True(할 일을 추가할 때는 기본 False로 저장됨)인 할 일
         3. 기한 초과: 마감일이 지났음에도 아직 완료되지 않은 할 일
   2. 할 일 생성 (POST 요청)
      - WTForms 양식에 텍스트와 마감일을 입력
      - 마감일은 UTC로 변환하여 DB에 저장하기 때문에 사용자가 어느 위치에서 접근하든 해당 시간대에 맞는 정보 제공
3. 할 일 순서 변경 (/todo_list/reorder_tasks)
   - 사용자가 마우스로 진행 중인 할 일들의 순서를 변경 가능
4. 할 일 마감일 수정 (/todo_list_/update_due_date/\<int:task_id\>)
   - 사용자가 마감일을 수정하면 DB에 반영(해당 task_id를 기반으로 데이터를 조회)
   - 시간대는 마감일을 추가할 때와 동일한 과정으로 변환되어 표시됨
5. 할 일 텍스트 수정 (/todo/update_text/\<int:task_id\>)
   - 사용자가 텍스트를 수정하면 DB에 반영
6. 할 일 완료 or 완료 취소 처리 (/todo_list/toggle_done/\<int:task_id\>)
   - 사용자가 체크박스 클릭 시 진행 중/완료 여부를 토글(클릭할 때마다 is_done 컬럼의 bool 값을 반전시킴)
7. 할 일 삭제 (/todo_list/delete/\<int:task_id\>)
   - 사용자가 할 일을 삭제하면 DB에 반영

### Database

- User (사용자 테이블)
   - `id`, `name`, `email`, `password`
   - 유저 1명은 여러 개의 할 일을 추가할 수 있으며, 각각의 할 일은 하나의 유저와 연결
- Task (할 일 테이블)
   - `id`, `text`, `is_done`, `due_date`, `tasker_id`, `order`
   - 각 할 일은 텍스트, 완료 여부, 마감일, 순서, 그리고 할 일을 생성한 사용자(`tasker`)와 연결됨
   - due_date는 Flask-WTF의 DateTimeLocalField를 사용해 사용자 브라우저의 로컬 시간 기준으로 입력됨
   - order 필드는 사용자가 변경한 할 일의 순서를 저장

### UI 
- 체크박스: 진행 중인 일은 **□** 으로, 완료된 일은 **▣** 으로 표시
- 텍스트: 진행 중인 일은 **검정색**, 완료된 일은 가로 취소선에 **<font color="Grey"><del>회색</del></font>**, 기한 만료된 일은 **<font color="Red">빨간색</font>**으로 표시
- 각 할 일의 분류에 따라 개수를 세서 화면에 표시
<br><br><br>

# Implementation

### Tech Stack

- **Backend:** Flask, Flask-Login, SQLAlchemy, Flask-WTF (with WTForms)
- **Templates:** Jinja2 (HTML rendering)
- **Database:** SQLite
- **Time Zones:** zoneinfo (Python 3.9+)
- **Frontend:** JavaScript (AJAX)

### Coding

1. 사용자 인증 및 세션 관리 (Flask-Login 사용)
   - [사용자 인증 참고](https://jooyeunseo.github.io/projects/laptop-friendly-cafes/#coding)
   - 각 유저마다 개인적인 할 일 리스트를 소유할 수 있음
2. Flask-WTF으로 입력 양식 생성
   - TaskForm이라는 폼 클래스를 정의하여 다양한 필드(문자열, 날짜, 체크박스)를 통해 사용자 입력 수집
   - CSRF 보호 기능으로 사용자가 제출한 폼을 안전하게 처리
   - 자동으로 폼 필드의 유효성 검사를 수행하고, 모든 필드가 유효할 때만 True 반환
   - HTML 템플릿에서 폼 렌더링
3. JavaScript의 AJAX
   - 할 일 순서 변경
      1. JavaScript의 SortableJS 라이브러리로 HTML 항목들에 드래그 앤 드롭 기능 추가(마우스로 조작 가능)
      2. 사용자가 목록에서 할 일들의 순서를 변경하면 `onEnd` 이벤트 발생
      3. 순서가 변경된 항목들의 ID를 배열로 수집하여 서버로 AJAX 요청 전송
      4. 서버는 순서 배열을 받아 데이터베이스에서 각 할 일의 `order` 값을 업데이트하여 순서를 반영
   - 할 일 텍스트 수정
      1. JavaScript로 텍스트 수정 폼 활성화
      2. 텍스트 수정 후, AJAX 요청을 통해 서버로 수정된 텍스트를 전달
      3. 서버는 해당 할 일의 텍스트를 업데이트하고, 데이터베이스에 저장
   - 할 일 완료 or 완료 취소 처리
      1. 사용자가 체크박스를 클릭하면 `진행 중→완료 상태` 또는 `완료 상태→진행 중`으로 표시 변경
      2. 상태가 변경되면 AJAX 요청을 통해 서버로 해당 할 일의 상태를 전송
      3. 서버는 요청을 받아 데이터베이스에서 해당 할 일의 `is_done` 값을 반전시키고, 데이터베이스에 반영
   - Flask 세션에 사용자 시간대 저장
      1. 사용자가 웹페이지에 접속할 때 JavaScript로 사용자의 시간대를 서버로 전송
      2. 서버에서 이를 받아 세션에 저장(e.g. Asia/Seoul)
4. 시간대 관리     
   1. 사용자가 입력한 마감일은 시간대 정보가 없는 naive datetime 형식으로 전달됨   
   (e.g. 2025년 5월 6일 15:30 KST → 2025-05-06T15:30)
   2. 서버는 세션에 저장된 시간대를 기준으로 이를 UTC 변환 후 저장   
   (e.g. 2025-05-06T15:30 → 2025년 5월 6일 06:30 UTC)
   3. UTC로 저장된 시간을 세션에 저장된 시간대 기준으로 다시 변환하여 UI에 표시    
   (e.g. 2025-05-06T06:30 UTC → 2025-05-06T15:30 KST)
<br><br><br>

# Result

![](/assets/images/personal-projects/to_do_list.gif)

로그인을 하면 해당 유저의 이름과 할 일 목록을 볼 수 있다.    
체크박스를 누르면 진행 중인 일과 완료된 일로 상태를 스위칭할 수 있고, 진행 중인 할 일은 마우스로 드래그하여 순서를 변경할 수 있다.   
텍스트와 마감일도 자유롭게 변경 가능하며, 마감일이 현재 시간 이전일 경우 자동으로 OVERDUE에 카운트된다.
<br><br><br>

# Future Improvements

- **마감 기한 알림**   
할 일의 기한이 임박하면 사용자에게 알림을 보내는 기능 추가
- **우선순위**   
할 일에 우선순위를 지정하고, 우선순위에 따라 목록을 정렬할 수 있는 기능 구현
<br><br><br>

# Conclusion
간단한 할 일 목록을 만들면서 시간대 처리에서 많은 시간을 소모했다. 로컬 서버에서 테스트할 때는 문제가 없었으나, 실제 웹 서버에서 실행할 경우 마감일이 현재 시간보다 한두 시간 정도 앞서 있음에도 불구하고 기한이 만료된 일로 인식되지 않는 것을 발견했다. 물론 코드 자체에서 원하는 시간대를 명시하면 쉽게 해결할 수 있지만, 사용자가 어느 나라에서 접속하든 현지 시간에 맞춰 서비스를 제공할 수 있는 방법이 필요하다고 판단했다. 이 경험을 통해 웹에서 서비스할 경우 다양한 시간대에 위치한 사용자들이 동일한 시스템을 사용하는 경우를 고려하여 시간대를 처리하는 것이 중요하다는 것을 알게 됐고, 처음으로 Flask 세션도 활용해볼 수 있었다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}