---
excerpt: "Google Analytics와 Google search Console 설정"
title: "Analytics Setting & SEO"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
---

## <a href="https://analytics.google.com/analytics/web/provision/?authuser=0#/provision" target="_blank">Google Analytics</a>

블로그에 접속한 방문자를 추적하여 분석하는 도구

1. 계정 생성
  - **계정 이름:** 블로그와 관련된 이름으로 정하기
  - **계정 데이터 공유 설정:** 모두 체크
2. 속성 만들기
  - **속성 이름:** 블로그 이름
  - **보고 시간대:** 대한민국
  - **통화:** 미국 달러
3. 비즈니스 세부정보
  - **업종 카테고리:** 인터넷 및 통신
  - **비즈니스 규모:** 작음
4. 비즈니스 목표 선택
5. 약관 동의에 모두 체크 후 만들기
6. 데이터 수집
  - **플랫폼:** 웹
  - **웹사이트 URL:** 블로그 주소
  - **스트림 이름:** 블로그 이름
7. 데이터 스트림 세부정보에서 **측정 ID** 복사하기   

```yml
analytics:
  provider: "google-gtag"
  # false (default), "google", "google-universal", "google-gtag", "custom"
  google:
    tracking_id: "Your Tracking Code"
    anonymize_ip: false   # false (default)
```
- `_config.yml`의 analytics 부분 수정
- tracking_id에 복사한 측정 ID를 넣어서 파일 수정
- Github에 push해서 웹 서버에 반영하기

## <a href="https://search.google.com/search-console/welcome?hl=ko&utm_source=wmx&utm_medium=deprecation-pane&utm_content=home" target="_blank">Google Search Console</a>

- 검색 엔진 최적화(SEO) 지원 및 웹사이트 트래픽과 성과를 분석할 수 있는 도구
- 검색 엔진의 결과 페이지에서 상위에 노출되도록 돕는 작업

*[SEO]: Search Engine Optimization

1. 속성 유형
   1. **URL 접두어** 선택
   2. Github 블로그 주소 입력
2. 소유권 확인
   1. 확인 방법 중 **HTML 태그** 선택
   2. Google에서 제공하는 HTML 메타 태그의 **content** 속성 값 복사
   3. `_config.yml`의 **SEO Related**에 복사한 값 붙여넣기
       ```yml
       google_site_verification : EnOYENSsmtyv_O5Bwtaj8kTBAAxDQ4sjRbWJKT8tYjs
       ```
   4. Github에 push 후 Google Search Console 화면에서 `확인` 버튼 누르기
   5. `소유권이 확인됨`이 뜨면 완료
3. 검색 엔진에 사이트의 구조를 안내하는 사이트맵 제출
   1. `jekyll-sitemap` 플러그인 필요
      - mininal-mistakes 테마에서 기본으로 제공되는 플러그인에 이미 있음
      - `_config.yml`의 **plugins:**에도 플러그인이 추가되어 있어야 한다.
      - `/_site`에 `sitemap.xml` 파일이 생성되어 있는지 확인하기
   2. Google Search Console의 메뉴에서 **Sitemaps** 선택
   3. **새 사이트맵 추가**에 `sitemap.xml` 입력 후 제출
   4. '성공'으로 처리될 때까지 기다리기

## robots.txt

SEO 최적화를 위한 추가 설정

1. 프로젝트의 루트 디렉토리에 `robots.txt` 생성
    ```
    User-agent: *
    Disallow: /private/
    Sitemap: https://yourdomain.com/sitemap.xml
    ```
    - **User-agent:** \* 으로 모든 검색 엔진 크롤러에게 적용
    - **Disallow:** : 설정한 경로를 크롤링하지 않도록 지시(모두 허용하려면 `/` 입력)
    - **Sitemap:** 사이트맵 파일의 위치를 지정
2. `_config.yml`에 파일 추가   
    ```yml
     # Reading Files
     include:
       - .htaccess
       - _pages
       - robots.txt  # robots.txt 파일 추가
     exclude:
       ...
    ```
3. `_site`에 `robots.txt`이 빌드된 것을 확인 후 배포하기

## Connect Google Search Console to Google Analytics

두 플랫폼의 데이터를 연동하여 Google Analytics에서 동시에 분석할 수 있다.

1. Google Analytics 홈페이지에서 왼쪽 하단의 **관리** 클릭
2. '제품 링크'에서 **Search Console 링크** 클릭
3. 연결 설정
   1. Search Console 속성 선택: 해당 블로그
   2. 웹 스트림 선택: 해당 블로그
   3. 연결 확인