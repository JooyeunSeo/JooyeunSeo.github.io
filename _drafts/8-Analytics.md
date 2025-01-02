---
excerpt: "Analytics"
title: "Analytics"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
---

## <a href="https://mmistakes.github.io/minimal-mistakes/docs/configuration/#analytics" target="_blank">Analytics</a>

블로그에 접속한 방문자를 분석하는 툴 적용하기

## <a href="https://analytics.google.com/analytics/web/provision/?authuser=0#/provision" target="_blank">Google Analytics</a>

1. 계정 생성
  - 계정 이름: 블로그와 관련된 이름으로 정하기
  - 계정 데이터 공유 설정: 모두 체크
2. 속성 만들기
  - 속성 이름: 블로그 이름
  - 보고 시간대: 대한민국
  - 통화: 미국 달러
3. 비즈니스 세부정보
  - 업종 카테고리: 인터넷 및 통신
  - 비즈니스 규모: 작음
4. 비즈니스 목표 선택
5. 약관 동의에 모두 체크 후 만들기
6. 데이터 수집
  - 플랫폼: 웹
  - 웹사이트 URL: 블로그 주소
  - 스트림 이름: 블로그 이름
7. 데이터 스트림 세부정보에서 **측정 ID** 복사하기   

## _config.yml

```yml
analytics:
  provider: "google-gtag" # false (default), "google", "google-universal", "google-gtag", "custom"
  google:
    tracking_id: "Your Tracking Code"
    anonymize_ip: false # false (default)
```
- tracking_id에 복사한 측정 ID를 넣어서 파일 수정
- Github에 push해서 웹 서버에 반영하기