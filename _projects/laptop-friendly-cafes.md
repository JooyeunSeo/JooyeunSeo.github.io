---
date: 2025-04-10
layout: splash
excerpt: "Discover and share information about laptop-friendly cafes in your city. <br>Anyone can sign up to add cafes to the list or leave comments."
title: "Laptop Friendly Cafes"
header:
  teaser: "https://images.unsplash.com/photo-1581387490232-2181c3736353?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://images.unsplash.com/photo-1581387490232-2181c3736353?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%EA%B0%88%EC%83%89-%EB%82%98%EB%AC%B4-%ED%85%8C%EC%9D%B4%EB%B8%94%EC%97%90-%EB%A7%A5%EB%B6%81-%ED%94%84%EB%A1%9C%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EC%82%AC%EB%9E%8C-7weXfu_XTSw)"
  actions:
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/laptop_friendly_cafes?city=Seoul"
    - label: "Check the Code"
      url: "https://github.com/JooyeunSeo/Dynamic-Web-Page"  
---

# Intro

원격 근무에 적합한 카페들을 도시별로 모아놓은 웹사이트로, Wi-Fi나 충전용 콘센트 등 원격 근무에 중요한 편의 시설 정보를 한 눈에 파악할 수 있어서 편리한 서비스다.  
누구나 카페 목록을 열람할 수 있지만, 정보를 추가하거나 수정하려면 회원 가입 및 로그인이 필요하다(단순히 프로젝트의 사용자 인증 기능을 구현하는 용도로, 개인정보를 수집하지 않음).   
로그인한 사용자는 새로운 카페를 등록하거나 기존 정보를 수정 및 삭제할 수 있으며, 댓글을 통해 다른 사용자들과 의견을 나눌 수도 있다.

*100개의 프로젝트로 Python 개발 완전 정복* 부트캠프에서 여러 번 다뤘던 아이디어로, 이번에는 모든 카페 데이터를 SQLite 데이터베이스에서 관리하고 이를 활용하여 웹페이지에 정보를 표시했다. 강의에서 예시로 소개했던 <https://laptopfriendly.co/london> 사이트를 참고했다.
<br><br><br>

# Design

### Overview

1. 사용자 관리
   - 회원가입 (/register)
   - 로그인, 로그아웃 (/login, /logout)
   - 로그인해서 인증된 사용자만 카페 등록, 수정, 삭제 및 댓글 작성이 가능
   - 예외로 관리자(가장 먼저 등록한 유저로, id가 1)는 모든 유저가 남긴 정보에 접근 가능
2. 카페 정보
   - 메인 페이지에서 카페 목록 보기 (/laptop_friendly_cafes)
      - 도시별로 목록 필터링
      - 새 카페 등록 (/laptop_friendly_cafes/add)
   - 카페 상세 페이지 (/laptop_friendly_cafes/show/\<id\>)
      - 해당 카페를 추가한 사용자의 이름과 업로드 날짜 표시
      - 카페 정보 수정 및 삭제 (/laptop_friendly_cafes/edit/\<id\>)
3. 댓글 기능
   - 각 카페의 상세 페이지에서 댓글 작성
   - 댓글 수정 및 삭제 가능
4. 이메일 전송
   - 로그인 여부 상관없이 잘못된 정보를 정정하고 싶을 경우 이메일 문의 페이지에서 가능 (/contact)
   - 파이썬 모듈 smtplib를 통해 g메일 서버에 접속
<br>

### Database

- **User (메인 테이블)**
   - `id`, `name`, `email`, `password`
   - 유저 1명은:
     - 여러 개의 새 카페를 리스트에 추가할 수 있음
     - 한 카페에 여러 개의 댓글을 달 수 있음
- **Cafe**
   - `id`, `name`, `city`, `location`, etc.
   - 각 카페는 리스트에 해당 카페를 추가한 유저(`author`)와 연결되어 있음
   - 카페 1개는 여러 개의 댓글을 보유할 수 있음
- **CafeComment**
   - `id`, `text`
   - 각 댓글은:
      - 해당 댓글을 단 유저(`comment_author`)와 연결되어 있음
      - 해당 댓글에 연결된 카페(`parent_cafe`)와 연결되어 있음
<br><br><br>

# Implementation

### Tech Stack

- **Backend:** Flask, Flask-Login, SQLAlchemy
- **Templates:** Jinja2 (HTML rendering)
- **Database:** SQLite
- **Email:** smtplib, email.mime
- **Security:** werkzeug.security

### Coding

1. Flask-Login을 이용한 사용자 인증 및 세션 관리
   - 사용자가 로그인하면 `login_user(user)`를 호출해 사용자 ID를 세션에 저장하고, 로그아웃 시에는 `logout_user()`를 사용하여 세션을 종료
   - `@login_manager.user_loader` 데코레이터와 `load_user()` 콜백 함수로 세션에 저장된 사용자 ID로부터 유저 객체를 다시 불러오기  
   (`current_user`로 현재 로그인된 유저 객체를 로드 가능)
   - 사용자 모델 클래스에 `UserMixin`을 상속해서 `is_authenticated` 메서드 사용(해당 사용자가 로그인되었을 때만 True 반환)
   - 인증이 필요한 라우트는 로그인된 사용자만 접근할 수 있도록 `@login_required` 데코레이터로 보호
2. 비밀번호 보안
   - 사용자가 입력한 비밀번호는 werkzeug.security 모듈로 안전하게 암호화되어 저장   
   (e.g. *pbkdf2:sha256:1000000$EZpLWFTN$5d0bd9153d282b95....*)
   - `generate_password_hash`로 해싱 + 솔팅
      - 임의의 문자열 솔트(salt)를 생성하여 평문과 결합 후, bcrypt 해시 함수에 통과시키는 방법
      - `pbkdf2:sha256` 해싱 알고리즘을 사용하고 솔트 길이는 8로 설정
      - 사용자마다 솔트값이 다르기 때문에 같은 비밀번호를 입력해도 서로 다른 해시가 생성됨
   - `check_password_hash`로 로그인 시 검증 수행
3. 환경변수 설정
   - DB 경로(서버 배포시에는 PostgreSQL, 로컬 개발 환경에서는 디렉토리에 생성된 SQLite 파일 사용)   
   - Flask 앱의 SECRET_KEY(암호화나 서명을 필요로 하는 작업에 사용되는 비밀 키)
   - 이메일 주소, 비밀번호 등 민감한 개인 정보 
4. 데이터베이스
   - SQLAlchemy ORM으로 파이썬 클래스와 객체를 통해 SQL 쿼리 없이 데이터베이스를 조작
      - `model_class=Base`를 사용하여 데이터베이스 모델을 정의하고 관리
      - 모델 간 관계는 `db.relationship()`과 `db.ForeignKey()`로 설정
      - 관계에 `lazy=True`로 설정하여 필요한 시점(실제로 접근할 때)에만 데이터를 로드
   - 테이블 관계 구조
      - User: Cafe, CafeComment의 부모 (1:N 관계)
      - Cafe: User의 자식, CafeComment의 부모 (1:N 관계)
      - CafeComment: User와 Cafe의 자식 (N:1 관계)
   - Flask 애플리케이션의 컨텍스트(Context) 내에서 `db.create_all()`을 호출하여 DB 초기화
<br><br><br>

# Result

![](/assets/images/personal-projects/laptop_friendly_cafes.gif)

모든 카페들은 해당 도시에 따라 카테고리화되며, 메인 화면에서 기본으로 뜨는 도시는 서울로 설정했다.
<br><br><br>

# Future Improvements

- **검색 및 필터 기능**   
도시 뿐만 아니라 와이파이나 콘센트 유무 등 다른 조건으로도 필터링할 수 있도록 업그레이드하고 이름으로 검색하는 기능 추가 
- **이미지 업로드**   
사용자가 직접 찍은 사진도 업로드할 수 있도록 기능 확장
- **지도 API를 활용하여 카페의 위치를 시각적으로 표시**
- **자주 가는 카페 북마크 또는 like 기능 추가**
<br><br><br>

# Conclusion

이번 프로젝트를 통해 사용자 인증, 비밀번호 보안 처리, SQLAlchemy를 활용한 관계형 데이터베이스 설계, Flask의 세션 및 폼 처리 등 실제 서비스에서 필요한 핵심 요소들을 복습하고 직접 구현해볼 수 있어서 유익한 경험이었다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}