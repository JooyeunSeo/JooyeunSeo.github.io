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

### <a href="https://analytics.google.com/analytics/web/provision/?authuser=0#/provision" target="_blank">Google Analytics</a>

블로그에 접속한 방문자를 분석하는 도구

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
  provider: "google-gtag" # false (default), "google", "google-universal", "google-gtag", "custom"
  google:
    tracking_id: "Your Tracking Code"
    anonymize_ip: false   # false (default)
```
- `_config.yml`의 analytics 부분 수정
- tracking_id에 복사한 측정 ID를 넣어서 파일 수정
- Github에 push해서 웹 서버에 반영하기

### <a href="https://search.google.com/search-console/welcome?hl=ko&utm_source=wmx&utm_medium=deprecation-pane&utm_content=home" target="_blank">Google Search Console</a>

- 검색 엔진 최적화(SEO) 지원 및 웹사이트 트래픽과 성과를 분석할 수 있는 도구
- 검색 엔진의 결과 페이지에서 상위에 노출되도록 돕는 작업

*[SEO]: Search Engine Optimization

1. 속성 유형
   1. **URL 접두어** 선택
   2. Github 블로그 주소 입력
2. 소유권 확인
   1. 확인 방법 중 **HTML 태그** 선택
   2. Google에서 제공하는 HTML 메타 태그의 **content** 속성 값 복사
   3. `_config.yml`의 **SEO Related** 복사한 값 붙여넣기
       ```yml
       google_site_verification : EnOYENSsmtyv_O5Bwtaj8kTBAAxDQ4sjRbWJKT8tYjs
       ```
   4. 
3. 사이트맵 제출
   1. `jekyll-sitemap` 플러그인 필요(mininal-mistakes 테마에서 기본으로 제공되는 플러그인에 이미 있음)
   2. 