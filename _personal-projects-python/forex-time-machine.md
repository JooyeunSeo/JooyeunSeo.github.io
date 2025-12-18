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

# Intro
<hr>

Forex Time Machine은 과거 특정 시점과 현재의 환율을 빠르게 비교할 수 있는 웹 서비스입니다. <a href="https://exchangerate.host/" target="_blank">exchangerate.host</a> API를 통해 환율 데이터를 수집하며, 오늘 날짜 기준 최대 1년치 환율 히스토리를 기반으로 두 시점 간 변화를 직관적으로 확인할 수 있습니다.

사용자가 비교하고 싶은 두 날짜를 선택하면 해당 구간이 1년치 환율 추이 그래프에서 자동으로 하이라이트됩니다. 이를 통해 과거와 현재의 환율 변동을 한눈에 파악할 수 있습니다. 

해외 주식 투자, 유학 비용 계산, 해외 결제 등 환율 변동이 직접적인 영향을 미치는 상황에서 빠르고 효율적인 정보 제공을 목표로 합니다.

*※ 무료 API 키는 월 최대 100회 요청 제한이 있기 때문에 한도 초과 시 서비스가 일시적으로 동작하지 않을 수 있습니다.*
<br><br><br>

# Design
<hr>

### Overview

애플리케이션의 설계 원칙은 다음과 같다.

- API 요청 최소화를 위해 1년치 환율 데이터는 캐싱한다.
- 과거·현재 환율 계산과 그래프 데이터의 일관성을 유지하기 위해 단일 데이터 소스(timeframe API)를 사용한다.
- 페이지 이동 없이 하나의 화면에서 `입력 → 검증 → 계산 → 시각화`가 완료된다.
- 서버는 계산과 검증을 담당하고, 클라이언트는 결과 표시와 상호작용(UI)에 집중한다.

### Information Architecture

<figure>
  <a href="https://mermaid.live/edit#pako:eNqNU39P4kAQ_SqTTbxoDsUW6ZVGuZhSIgkqKVAvR81loQts0u6S3VZB4Lvfdgs91Jy6f2x2frw3M6_TNZrwiCAHTWP-PJljkULXD1nIQJ2jI7h6fcDtdry7wVv31VUBkNl4JvBiDm5MCUtHISoecPxAxjDsnIToscjMT29UvRw3PZYSAT08I5fVcbN6EB-ORio-lCrcYYsszeOPB_G2xreoXMR4Be0YyzncEil3VJdjUW0-4ZhGOKWcARGCi0N-P6f3icziFAJKnkvQKbicPREhc5jMkgSL1S5wQ2XKBZ3gGFJBWARasx2psj-Qru_5ged_Kl2fCFVaSVc8XikWrFXHWgsIysHytrf_clp5josncwLeUnUrf75JcPOxvaVqnM0I-Dgl4OJ4ksUlm571u75V6kDPGVCZqZIvZdJBW_3RcVmzr-TR8p98SRTv18Dz7667n8riLdWaMBz_ue51lDh7E5T5SiLv_XQqpZxKSYaBT8GAFcHiSy22u_cP_2uvB6enTRjqO9hzBLm56TC9extoa_OWR3S6KhYZvoFPIr6B4SEgKNJbe5qW9haq3tB0A-57_y2VcgOert_Xt7uHu9r0C8P_oAdUQTNBI-RMcSxJBSVEJDi30ToHhyidk4SEyFHPiEyx-l1CFLKtwi0w-815gpxUZAopeDablzzZQolNWhSrD5iU3nyZiHB5xlLkmHZDkyBnjZbIscyzer1Wu7B-mJZhNex6Ba2QY9RrZ8a5YZo1FbMN27S3FfSiy56fNUzLss16w7io2WajZm3_AqzeaTE" target="_blank" title="Mermaid Live Editor">
    <img src="/assets/images/personal-projects/forex_time_machine_IA.png" alt="IA">
  </a>
</figure>

사용자 요청부터 결과 표시까지의 데이터 흐름은 다음과 같다.

1. 사용자가 통화(from/to), 환전할 금액, 과거 날짜, 최근 날짜를 입력한다.
2. Flask 서버는 POST 요청을 수신하고 입력값을 파싱한다.
3. 서버에서 날짜 유효성 검증을 수행한다.
   - 실패: 오류 메시지를 띄우고 그 전 입력값은 유지한 채 템플릿을 다시 렌더링한다.
   - 성공: 캐시된 1년치 환율 데이터가 존재하는지 확인한다.
4. 캐싱된 데이터가 존재할 경우 그대로 사용하고, 없을 경우 외부 환율 API를 호출한다.
5. API 데이터를 기반으로 다음 작업을 수행한다.
   - 날짜별 환율 리스트를 구성한다.
   - 사용자가 선택한 두 날짜의 환전 금액을 계산한다.
   - 두 시점 간 증감률을 계산한다.
   - Plotly 그래프를 생성한다.
6. 계산 결과와 그래프를 하나의 페이지에 즉시 표시한다.

### UI/UX
   - **통화 선택:** 지원되는 169개 통화 중 원하는 통화를 빠르게 찾을 수 있도록 Select2 기반 검색형 드롭다운을 사용한다.
   - **금액 입력:** 숫자 자동 포맷팅(쉼표 적용)을 적용하여 가독성을 높이고, 숫자와 소수점(.) 외 입력은 제한한다.
   - **환전 금액 표시:** 세 자리마다 쉼표를 적용하고 소수점은 최대 2자리까지 표시한다.
   - **실시간 결과 갱신:** 그래프, 환율 비교 결과, 환전 금액을 모두 하나의 페이지에서 즉시 갱신한다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Programming Language:** Python
- **Backend:** Flask
- **Templates:** Jinja2(HTML rendering)
- **Frontend:** JavaScriptHTML, CSS, JavaScript, Select2(Dropdown Search)
- **HTTP Client:** requests
- **Data Visualization:** Plotly
- **Caching:** Flask-Caching(FileSystemCache)
- **Security:** werkzeug.security

### Coding

1. **API 호출**
   - `url`: "https://api.exchangerate.host/timeframe"
   - `params`
      - 'source'(from currency), 'currencies'(to currency), 'start_date', 'end_date'
      - 개인 'access_key'는 하드코딩하지 않고 환경변수에서 불러온다.
   - API 응답 데이터 구조는 다음과 같다.
   ```json
   {
     'success': True,
     'start_date': '2025-05-18',
     'end_date': '2025-11-18',
     'source': 'KRW',
     'quotes': {
       '2025-05-18': {'KRWJPY': 0.103854},
       '2025-05-19': {'KRWJPY': 0.104347},
       '2025-05-20': {'KRWJPY': 0.103559},
       ...
     }
   }
   ```
   - 해당 데이터를 이용하여 과거·현재 환율 계산과 그래프 생성을 처리한다.
2. **캐싱 구현**
   - `Flask-Caching`과 `@cache.memoize`를 활용하여 통화쌍 기준 1년치 환율 데이터를 캐싱한다.     
   - TTL은 하루 단위(86400초)로 설정한다.
   - 하루 동안 동일한 통화쌍에 대한 요청이 반복될 경우 저장된 캐시를 재사용하고, 캐시가 존재하지 않거나 TTL이 만료된 경우에만 API를 새로 호출한다.
   - 캐시 저장 방식은 `FileSystemCache`를 사용한다.
      - 로컬 환경에서는 지정된 디렉토리에 저장된다.
      - 배포 환경에서는 `/tmp/cache` 디렉토리에 저장되며, 서버 재시작 시 초기화된다.
3. **지원 통화 코드 관리**
   - API가 지원하는 통화 코드, 통화 이름, 국기 이모지를 JSON 파일로 관리한다.
   - JSON 구조 예시는 다음과 같다.
   ```json
   { 
     "AED": {"name": "United Arab Emirates Dirham", "flag": "\uD83C\uDDE6\uD83C\uDDEA"}, 
     "AFN": {"name": "Afghan Afghani", "flag": "\uD83C\uDDE6\uD83C\uDDEB"},
     "ALL": {"name": "Albanian Lek", "flag": "\uD83C\uDDE6\uD83C\uDDF1"},
      ...
   }
   ```
   - 서버에서 해당 JSON 파일을 로드한 후 Flask 템플릿으로 전달하여 드롭다운(select) 옵션을 생성한다.
4. **환율 계산**
   - 날짜별 환율 데이터를 순회하며 다음 작업을 수행한다.
      - 과거 날짜와 최근 날짜에 해당하는 환율로 각 환전액 계산: `환전 금액 = 입력한 금액 × 해당 날짜 환율`
      - 사용자 가독성을 위해 역환율 값으로 계산: `역환율 = 1 / 환율`
      - 두 날짜 간 증감률(%) 계산: `((최근 금액 - 과거 금액) / 과거 금액) × 100`
5. **날짜 데이터 처리**
   - 오늘 날짜와 1년 전 날짜는 다음과 같이 계산한다.
      - 오늘 날짜: `datetime.now()`
      - 1년 전 날짜: `today - timedelta(days=366)`
   - API 요청 및 Plotly 차트 생성을 위한 날짜는 `"YYYY-MM-DD"` 형식의 문자열로 변환한다.
   - 날짜 비교 및 유효성 검증을 위해 문자열을 `datetime` 객체로 변환하여 처리한다.
6. **Plotly 그래프 생성**
   - Plotly의 `go.Scatter`를 사용해 1년치 환율 추이 꺾은선 그래프를 생성한다.
   - 사용자가 선택한 과거 날짜와 최근 날짜 구간은 `layout.shapes`를 사용해 시각적으로 하이라이트 처리한다.
   - 생성된 그래프는 HTML div 형태로 반환하여 템플릿에 삽입한다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem

본 프로젝트 구현 과정에서 두 가지 핵심적인 문제를 경험했다.

첫 번째는 <u>환율 API 호출의 비효율성</u>이었다.    
초기에는 exchangerate.host의 convert 엔드포인트에 날짜를 지정하는 방식으로 환율을 계산했다. 이 방식은 입력 금액이 작을 경우 결과가 0으로 반환되는 정밀도 문제가 있었고, 이미 그래프 생성을 위해 timeframe API로 1년치 데이터를 요청하고 있음에도 동일한 통화쌍에 대해 API를 중복 호출하는 구조였다.

두 번째는 <u>JavaScript 라이브러리 간 실행 순서 충돌</u>이었다.     
Select2(통화 선택), 숫자 입력 포맷팅 스크립트, Plotly(그래프 렌더링)를 함께 사용하면서, 라이브러리 로딩과 초기화 순서가 명확히 분리되지 않아 일부 기능이 정상적으로 동작하지 않는 문제가 발생했다.

### Analysis

첫 번째 문제의 원인은 단일 데이터 소스를 활용하지 못한 설계에 있었다.      
timeframe API는 기준일로부터 최대 1년치 일별 환율 데이터를 제공하므로, 해당 데이터만으로도 사용자가 선택한 과거 날짜와 최근 날짜의 환율을 모두 계산할 수 있었다. 그럼에도 불구하고 계산과 그래프를 서로 다른 엔드포인트에 의존하면서 구조가 복잡해지고 불필요한 API 호출이 발생하고 있었다.

두 번째 문제는 JavaScript 코드 자체의 오류가 아니라, 라이브러리 간 의존성과 실행 타이밍에 대한 관리 부족에서 비롯되었다.     
Select2는 DOM 로드 이후에 초기화되어야 하고, Plotly 그래프는 서버에서 전달된 데이터와 대상 DOM 요소가 준비된 상태에서만 렌더링이 가능했다. 이러한 전제 조건이 명확히 분리되지 않은 채 스크립트가 실행되면서 충돌이 발생했다.

### Solution

첫 번째 문제는 `timeframe` API 단일 사용 전략으로 해결했다. 이를 통해 다음과 같은 개선 효과를 얻었다.

- 동일 통화쌍에 대한 API 중복 호출 제거
- 소수점 정밀도 문제 없는 안정적인 계산
- 그래프 데이터와 계산 결과 간의 일관성 확보

두 번째 문제는 JavaScript 로딩과 실행 책임을 명확히 분리하여 해결했다.       
Select2 라이브러리는 모든 페이지에서 공통으로 사용되므로 base 템플릿에서 의존성 순서에 맞게 로드하고, Select2 초기화 및 금액 입력 처리 로직(숫자 및 소수점만 허용, 세 자리 단위 쉼표 포맷팅)은 페이지별 스크립트 블록에서 DOM 로드 이후에 실행되도록 구성했다.

Plotly 그래프의 경우, 서버에서 전달된 데이터와 대상 HTML 요소가 모두 준비된 이후에만 렌더링될 수 있도록 그래프가 위치한 템플릿 영역 바로 앞에서 라이브러리를 로드했다.

그 결과, 사용자 입력 → 데이터 처리 → 시각화로 이어지는 전체 흐름이 서로 간섭 없이 안정적으로 동작하도록 개선할 수 있었다.
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

이 프로젝트를 진행하면서, API 기반 데이터를 받아와 다양한 방식으로 가공하고, 사용자 편의를 위해 통화 코드를 이모지와 함께 보기 좋게 정리하여 제공하는 과정을 경험했습니다. 또 과거와 현재 환율 데이터를 계산하고, 이를 Plotly 그래프로 시각화하면서 정보를 직관적으로 전달하는 방법을 실습할 수 있었습니다.

새롭게 배운 점으로는, 캐싱 전략을 적용해 불필요한 API 호출을 줄이고 데이터 로딩 속도를 높이는 방법과 이전에 써보지 못했던 JavaScript 기능들을 활용하는 것들이 있습니다. 특히 여러 스크립트를 동시에 사용하는 과정에서 select2(드롭다운)와 plotly(그래프) JS 간 충돌 문제가 있었는데, JS 로딩 순서와 블록 구조를 관리하는 것으로 해결할 수 있었습니다. 이를 통해 웹 애플리케이션에서 프론트엔드 라이브러리 간 의존성을 안전하게 다루는 방법을 익힐 수 있었습니다.

이번 프로젝트를 통해 단순히 데이터를 보여주는 것뿐만 아니라, 사용자가 직관적으로 이해할 수 있는 UI를 설계하는 것과 효율적인 백엔드 구조를 고려하는 것의 중요성을 직접 느낄 수 있었습니다.
<br>

### reference
**API Documentation:** <https://exchangerate.host/documentation>      
**API Supported Currencies:** <https://exchangerate.host/currencies>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}