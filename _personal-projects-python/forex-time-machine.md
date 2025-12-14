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

Forex Time Machine은 과거 특정 시점과 현재의 환율을 빠르게 비교할 수 있는 웹 서비스입니다.
<a href="https://exchangerate.host/" target="_blank">exchangerate.host</a>의 API를 통해 환율 데이터를 수집하며, 최대 1년치 히스토리를 기반으로 두 시점 간 변화를 직관적으로 확인할 수 있습니다.

사용자가 비교하고 싶은 두 날짜를 선택하면 해당 기간이 1년치 환율 추이 그래프에서 자동으로 하이라이트되어 과거와 현재의 변동을 한눈에 파악할 수 있습니다.
해외 주식, 유학, 해외 결제 등 환율 변동이 직접적인 영향을 미치는 상황에서 빠르고 효율적으로 정보를 제공하는 것을 목표로 합니다.       
(참고: 무료 API 키는 한 달 최대 100회 요청까지만 가능하므로, 서비스가 일시적으로 작동하지 않을 수도 있습니다.)
<br><br><br>

# Design

1. 전체 아키텍처
   1. 사용자가 통화(from/to)와 비교 날짜(past/recent), 금액을 입력
   2. Flask 서버에서 입력값 유효성 검증
   3. 외부 API로부터 환율 데이터 요청
   4. 1년치 Timeframe 데이터는 캐싱하여 API 사용량과 응답시간 최적화
   5. 동일 금액을 두 날짜 기준으로 환전한 뒤 금액 증감률 계산
   6. Plotly로 1년치 라인 차트 생성 후 HTML로 임베딩
   7. 새로운 페이지 이동 없이 하나의 화면에서 즉시 결과 표시
2. API 요청
   - 최신 환율은 즉시 요청
      - 사용자 입력 통화쌍(from/to)이 캐시에 없다면 캐싱 없이 즉시 API 호출
      - 비교 날짜(past/recent)에 해당하는 환율은 항상 최신으로 받아온다.
   - 받아온 1년치 Timeframe 데이터는 캐싱
      - 환율 히스토리는 분 단위로 변하지 않으므로 캐싱이 적합
      - 하루 동안 동일한 통화 간의 환전 요청이 들어오면 저장된 캐시를 사용하여 속도와 비용 최적화
   - API 반환 구조는 `{ "date": "2025-01-01", "value": rate }` 형태로 통일하여 저장 후 활용
3. 사용자 입력 검증(Validation)
   - 두 날짜 입력은 다음 조건을 반드시 만족해야 한다:
      - 과거 날짜 < 최근 날짜 (동일 날짜인 경우도 오류로 처리)
      - 오늘 이후 날짜는 선택 불가
      - 과거 날짜는 오늘로부터 최대 1년 이내만 허용
   - 오류 발생 시 Flask의 `flash()`로 즉시 UI에 메시지를 표시하여 어떤 부분에서 잘못 입력했는지 알린다.    
   (이미 사용자가 입력한 통화 및 금액 정보는 그대로 유지한 채 템플릿을 다시 렌더링)
4. Plotly 차트
   - 1년치 Timeframe 데이터를 기반으로 꺾은선 그래프(line chart) 생성
   - 사용자가 선택한 두 날짜 구간은 배경 하이라이트 처리
   - Y축은 원본값(e.g. 1 JPY → KRW) 대신 사용자에게 더 직관적인 역환율(e.g. 1 KRW → JPY) 기준으로 변환해 표시
   - 마우스 hover 시 해당 날짜의 상세 환율(역환율 기준)을 바로 확인 가능
5. UI/UX
   - 통화 선택: 지원되는 169개 통화 중 원하는 통화를 빠르게 찾을 수 있도록 Select2 기반 검색형 드롭다운 사용
   - 금액 입력: 숫자 자동 포맷팅(쉼표 적용)으로 가독성을 높이고, 숫자와 소수점(.) 외에는 입력 차단
   - 환전 금액 표시: 세자리마다 쉼표 적용 및 소수점 2자리까지 표시
   - 실시간 결과 갱신: 그래프, 비교 결과, 환전 금액을 모두 하나의 페이지에서 즉시 갱신
<br><br><br>

# Implementation

### Tech Stack

- **Programming Language:** Python
- **Backend:** Flask
- **Templates:** Jinja2 (HTML rendering)
- **Frontend:** JavaScriptHTML, CSS, JavaScript, Select2 (드롭다운 검색)
- **HTTP Client:** requests
- **Data Visualization:** Plotly
- **Caching:** Flask-Caching (FileSystemCache)
- **Security:** werkzeug.security

### Coding

1. API 호출
   - url: "https://api.exchangerate.host/timeframe"
   - params: "access_key"(개인키), "source"(사용자 통화), "currencies"(목표 통화), "start_date", "end_date"
2. 캐싱 구현
   - `Flask-Caching`과 `@cache.memoize`를 활용하여 선택된 통화간의 1년치 환율 데이터를 캐싱      
   (캐시가 있다면 저장된 것을 재사용하고, 없는 경우에만 새로 API 호출)
   - `FileSystemCache` 사용
      - 하루 단위 TTL(86400초) 기준으로 캐싱
      - 로컬 환경: cache 디렉토리에 저장됨
      - 배포 환경: `/tmp/cache` 디렉토리에 저장됨(서버 재시작시 초기화)
3. 지원하는 통화 코드 관리
   - API가 지원하는 통화, 이름과 국기 이모지를 다음과 같이 JSON 파일로 저장
   ```json
   { 
     "AED": {"name": "United Arab Emirates Dirham", "flag": "\uD83C\uDDE6\uD83C\uDDEA"}, 
     "AFN": {"name": "Afghan Afghani", "flag": "\uD83C\uDDE6\uD83C\uDDEB"},
     "ALL": {"name": "Albanian Lek", "flag": "\uD83C\uDDE6\uD83C\uDDF1"},
      ...
   }
   ```
   - 서버에서 JSON 파일을 읽은 후 Flask 템플릿에 전달하여 드롭다운(select) 옵션 생성
   - 새로운 통화를 추가할 때 JSON만 수정하면 되므로 유지보수가 용이하다.
4. 환율 계산 로직
   - API에서 가져온 데이터 구조 예시
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
   - 날짜별 환율 데이터를 파싱하고, 과거/현재 환전 금액 계산: `입력한 금액 * 해당 날짜 환율`
   - 사용자 편의를 위한 역환율을 계산: `1 / (입력한 금액 * 해당 날짜 환율)`
   - 두 날짜 간 증감률(%) 계산: `((최근 날짜 환전 금액 - 과거 날짜 환전 금액) / 과거 날짜 환전 금액) * 100`
5. 날짜 데이터 처리
   - 오늘 날짜 `datetime.now()`와 1년 전 날짜 `오늘 날짜 - timedelta(days=366)`는 **strftime("%Y-%m-%d")**을 사용해 문자열로 변환      
   (API 호출 및 Plotly 차트 생성에 활용)
   - 웹 폼에서 사용자가 선택한 날짜 값은 문자열로 전달된다(e.g. "2025-05-18").
   - 과거/최근 날짜 순서를 비교 연산자로 비교하려면 **datetime.strptime**으로 문자열을 다시 datetime 객체로 변환해야 한다.
6. Plotly 그래프 생성
   - `go.Scatter`로 1년치 환율 라인 차트를 생성
   - 차트 내에서 선택한 두 날짜 구간을 `layout.shapes`로 하이라이트 처리
   - `pyo.plot(..., output_type='div')`로 HTML div를 반환해 템플릿에 삽입
<br><br><br>

# Result

<img src="/assets/images/personal-projects/forex_time_machine.gif">
<br><br><br>

# Future Improvements

- **캐싱 최적화**    
Redis나 Memcached 같은 외부 캐시를 도입하여 서버 재시작 시에도 데이터가 유지되도록 개선
- **API 호출 제한 대응**    
무료 API의 요청 한도 초과 시 사용자에게 안내 메시지를 띄우고, 요청 실패 시 캐시 데이터를 활용하도록 처리
- **다중 통화 비교 기능 추가**     
여러 통화를 동시에 비교하거나, 특정 기간 동안의 환율 변동 요약 통계를 제공하여 활용도를 높이기
<br><br><br>

# Conclusion

이 프로젝트를 진행하면서, API 기반 데이터를 받아와 다양한 방식으로 가공하고, 사용자 편의를 위해 통화 코드를 이모지와 함께 보기 좋게 정리하여 제공하는 과정을 경험했습니다. 또 과거와 현재 환율 데이터를 계산하고, 이를 Plotly 그래프로 시각화하면서 정보를 직관적으로 전달하는 방법을 실습할 수 있었습니다.

새롭게 배운 점으로는, 캐싱 전략을 적용해 불필요한 API 호출을 줄이고 데이터 로딩 속도를 높이는 방법과 이전에 써보지 못했던 JavaScript 기능들을 활용하는 것들이 있습니다. 특히 여러 스크립트를 동시에 사용하는 과정에서 select2(드롭다운)와 plotly(그래프) JS 간 충돌 문제가 있었는데, JS 로딩 순서와 블록 구조를 관리하는 것으로 해결할 수 있었습니다. 이를 통해 웹 애플리케이션에서 프론트엔드 라이브러리 간 의존성을 안전하게 다루는 방법을 익힐 수 있었습니다.

이번 프로젝트를 통해 단순히 데이터를 보여주는 것뿐만 아니라, 사용자가 직관적으로 이해할 수 있는 UI를 설계하는 것과 효율적인 백엔드 구조를 고려하는 것의 중요성을 직접 느낄 수 있었습니다.
<br>

### reference
**API Documentation:** <https://exchangerate.host/documentation>      
**API Supported Currencies:** <https://exchangerate.host/currencies>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}