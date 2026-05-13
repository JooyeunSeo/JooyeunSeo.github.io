---
date: 2025-11-24
layout: splash
excerpt: "Compare exchange rates between two dates using real time and historical data from an exchange-rate API"
title: "Forex time Machine"
header:
  teaser: "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1742"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://images.unsplash.com/photo-1580519542036-c47de6196ba5?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1742
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/10%EB%8B%AC%EB%9F%AC%EC%A7%9C%EB%A6%AC-%EC%A7%80%ED%8F%90-1%EC%9E%A5%EA%B3%BC-10%EB%8B%AC%EB%9F%AC-%EC%A7%80%ED%8F%90-1%EC%9E%A5-SAYzxuS1O3M)"
  actions:
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/forex_time_machine"
    - label: "Check the Code"
      url: "https://github.com/JooyeunSeo/Dynamic-Web-Page"
---

# Overview
<hr>

Forex Time Machine은 과거 특정 시점과 현재의 환율을 빠르게 비교할 수 있는 웹 서비스입니다. <a href="https://exchangerate.host/" target="_blank">exchangerate.host</a> API를 통해 환율 데이터를 수집하며, 오늘 날짜 기준 최대 1년치 환율 히스토리를 기반으로 두 시점 간 변화를 직관적으로 확인할 수 있습니다.

사용자가 비교할 두 날짜를 선택하면 1년치 환율 추이 그래프에서 해당 구간이 자동으로 하이라이트됩니다. 이를 통해 해외 주식 투자, 유학 비용 계산, 해외 결제 등 환율 변동이 중요한 상황에서 효율적인 의사결정을 돕습니다.

*※ 무료 API 키의 월간 요청 제한(100회)으로 인해 한도 초과 시 서비스 이용이 일시적으로 제한될 수 있습니다.*
<br><br><br>

# System & Interface Design
<hr>

애플리케이션의 설계 원칙은 다음과 같습니다.

- **데이터 효율성:** API 요청 최소화를 위해 1년치 환율 데이터를 캐싱합니다.
- **일관성 유지:** 계산과 시각화의 정밀도를 위해 단일 데이터 소스(timeframe API)를 사용합니다.
- **사용자 경험:** 페이지 이동 없이 한 화면에서 입력 → 검증 → 계산 → 시각화가 완료됩니다.
- **역할 분담:** 서버는 비즈니스 로직(계산·검증)을 담당하고, 클라이언트는 상호작용 및 결과 표시에 집중합니다.

### Information Architecture

<figure>
  <a href="https://mermaid.live/edit#pako:eNqNU39P4kAQ_SqTTbxoDsUW6ZVGuZhSIgkqKVAvR81loQts0u6S3VZB4Lvfdgs91Jy6f2x2frw3M6_TNZrwiCAHTWP-PJljkULXD1nIQJ2jI7h6fcDtdry7wVv31VUBkNl4JvBiDm5MCUtHISoecPxAxjDsnIToscjMT29UvRw3PZYSAT08I5fVcbN6EB-ORio-lCrcYYsszeOPB_G2xreoXMR4Be0YyzncEil3VJdjUW0-4ZhGOKWcARGCi0N-P6f3icziFAJKnkvQKbicPREhc5jMkgSL1S5wQ2XKBZ3gGFJBWARasx2psj-Qru_5ged_Kl2fCFVaSVc8XikWrFXHWgsIysHytrf_clp5josncwLeUnUrf75JcPOxvaVqnM0I-Dgl4OJ4ksUlm571u75V6kDPGVCZqZIvZdJBW_3RcVmzr-TR8p98SRTv18Dz7667n8riLdWaMBz_ue51lDh7E5T5SiLv_XQqpZxKSYaBT8GAFcHiSy22u_cP_2uvB6enTRjqO9hzBLm56TC9extoa_OWR3S6KhYZvoFPIr6B4SEgKNJbe5qW9haq3tB0A-57_y2VcgOert_Xt7uHu9r0C8P_oAdUQTNBI-RMcSxJBSVEJDi30ToHhyidk4SEyFHPiEyx-l1CFLKtwi0w-815gpxUZAopeDablzzZQolNWhSrD5iU3nyZiHB5xlLkmHZDkyBnjZbIscyzer1Wu7B-mJZhNex6Ba2QY9RrZ8a5YZo1FbMN27S3FfSiy56fNUzLss16w7io2WajZm3_AqzeaTE" target="_blank" title="Mermaid Live Editor">
    <img src="/assets/images/personal-projects/forex_time_machine_IA.png" alt="IA">
  </a>
</figure>

사용자 요청부터 결과 표시까지의 데이터 흐름은 다음과 같습니다.

1. **입력:** 사용자로부터 통화쌍(from/to), 금액, 두 개의 비교 날짜를 수신합니다.    
2. **검증:** Flask 서버에서 날짜 유효성을 검사하며, 실패 시 오류 메시지와 함께 이전 입력값을 유지합니다.
3. **조회:** FileSystemCache를 확인하여 캐시 데이터가 있으면 재사용하고, 없으면 외부 API를 호출합니다.
4. **처리:** API 데이터를 기반으로 일별 환율 리스트 구성, 환전 금액 및 증감률 계산, Plotly 그래프를 생성합니다.
5. **출력:** 계산 결과와 시각화된 그래프를 페이지에 즉시 렌더링합니다.

### UI/UX

- **검색형 드롭다운:** Select2를 적용하여 169개 통화 중 원하는 항목을 빠르게 검색할 수 있습니다.
- **입력 최적화:** 숫자 자동 포맷팅(세 자리 쉼표)을 적용하고 숫자와 소수점 외의 입력을 제한합니다.
- **직관적 결과:** 환전 결과와 증감률을 명확히 표시하며, 실시간으로 그래프를 갱신합니다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Backend:** Python, Flask, Jinja2
- **Frontend:** HTML/CSS, JavaScript, Select2(드롭다운 메뉴), Plotly(그래프)
- **Library:** Requests, Flask-Caching, Werkzeug(보안)

### Key Implementation Details

1. API 연동: timeframe 엔드포인트를 활용합니다. 보안을 위해 API Access Key는 환경변수로 관리하며, JSON 응답 구조를 파싱하여 계산과 그래프 생성에 활용합니다.
2. 캐싱 전략: `@cache.memoize`를 사용하여 통화쌍별 데이터를 24시간(86400초) 동안 유지합니다. 로컬은 지정 디렉토리, 배포 환경은 /tmp/cache(서버 재시작시 초기화)를 사용합니다.
3. 통화 정보 관리: 국기 이모지와 통화명이 포함된 JSON 파일을 별도로 관리하여 사용자 친화적인 선택창을 구성합니다.
4. 환율 계산:
   - `환전 금액 = 입력액 × 해당 날짜 환율`
   - `역환율 = 1 / 환율` (사용자 가독성을 위함)
   - `증감률 = ((최근 금액 - 과거 금액) / 과거 금액) × 100`
5. 시각화: Plotly의 go.Scatter로 선 그래프를 그리고, layout.shapes를 통해 사용자가 선택한 비교 구간을 강조합니다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem 1. API 호출 효율성 개선

초기에는 환율 계산과 그래프 생성을 위해 서로 다른 API 엔드포인트를 호출했습니다. 이로 인해 불필요한 트래픽이 발생하는 문제가 있었습니다.

### Solution

timeframe API 하나로 모든 데이터를 충당하는 단일 소스 전략을 채택했습니다. 이를 통해 중복 호출을 제거하고 계산 결과와 그래프 데이터의 일관성을 확보했습니다.

-------------

### Problem 2. JavaScript 라이브러리 실행 순서 충돌

Select2, Plotly 등 여러 라이브러리를 함께 사용하면서 DOM 로드 시점과 초기화 순서가 꼬여 기능이 정상 작동하지 않았습니다.

### Solution

스크립트 실행 책임을 명확히 분리했습니다. 공통 의존성은 Base 템플릿에서 로드하고, Select2에서의 금액 입력 포맷(숫자 및 소수점만 허용, 세 자리 단위 쉼표 포맷팅)과 같은 개별 로직은 페이지별 스크립트 블록 내에서 DOM 완성 후 실행되도록 구조화하여 간섭을 제거했습니다.
<br><br><br>

# Result
<hr>

<img src="/assets/images/personal-projects/forex_time_machine_Result.gif">
<br><br><br>

# Future Improvements
<hr>

- **캐싱 최적화**    
Redis나 Memcached 같은 외부 캐시를 도입하여 서버 재시작 시에도 데이터가 유지되도록 개선
- **API 호출 제한 대응**    
무료 API의 요청 한도 초과 시 사용자에게 안내 메시지를 띄우고, 요청 실패 시 캐시 데이터를 활용하도록 처리
- **다중 통화 비교 기능 추가**     
여러 통화를 동시에 비교하거나, 특정 기간 동안의 환율 변동 요약 통계를 제공하여 활용도를 높이기
<br><br><br>

# Conclusion
<hr>

이번 프로젝트를 통해 API 데이터를 가공하여 사용자 중심의 정보를 생성하는 전 과정을 경험했습니다. 특히 캐싱 전략을 통한 성능 최적화와 프론트엔드 라이브러리 간의 의존성 관리 방법을 익힐 수 있었습니다. 단순히 데이터를 나열하는 것을 넘어 사용자가 직관적으로 이해할 수 있는 UI/UX 설계와 효율적인 백엔드 구조의 중요성을 다시 한번 깨닫는 계기가 되었습니다.
<br>

### resources
**API Documentation:** <https://exchangerate.host/documentation>      
**API Supported Currencies:** <https://exchangerate.host/currencies>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}