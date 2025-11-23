---
date: 2025-11-21
layout: splash
excerpt: "설명"
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
**Note:** The file is large, so Google Drive may display a warning before download. This is normal.

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
   - 로컬 환경에서는 FileSystemCache에, 배포 환경에서는 Flask-Caching 내장 메모리(SimpleCache)에 1일(86400초) 동안 저장
3. 환율 계산 로직
   - API에서 반환된 데이터 구조 예시:
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
       '2025-05-21': {'KRWJPY': 0.104563},
       ...
     }
   }
   ```
   - 날짜별 환율 데이터를 파싱하고, 과거/현재 환전 금액 계산(e.g. `amount * 0.103854`)
   - 사용자 편의를 위한 역환율을 계산(e.g. `1 / (amount * 0.103854)`)
   - 두 날짜 간 증감률(%) 계산: `((b_amount - a_amount) / a_amount) * 100`
4. 날짜 데이터 처리
   - 오늘 날짜(datetime.now())와 1년 전 날짜(today - timedelta(days=366))는 `strftime("%Y-%m-%d")`을 사용해 문자열로 변환해야 API 호출 및 Plotly 차트 생성에 활용할 수 있다. 
   - 웹 폼에서 사용자가 선택한 날짜 값은 문자열로 전달된다. (e.g. "2025-05-18")
   - 과거/최근 날짜 순서를 비교 연산자로 비교하려면 `datetime.strptime`으로 문자열을 다시 datetime 객체로 변환해야 한다.
5. Plotly 그래프 생성
   - `go.Scatter`로 1년치 환율 라인 차트를 생성
   - 차트 내에서 선택한 두 날짜 구간을 `layout.shapes`로 하이라이트 처리
   - `pyo.plot(..., output_type='div')`로 HTML div를 반환해 템플릿에 삽입
<br><br><br>

# Result

<br><br><br>

# Future Improvements

<br><br><br>

# Conclusion

(HTTP 요청과 REST API에 대해 배운 내용을 활용해서 API에서 나온 데이터를 이용)
<br>

### reference
**API Documentation:** <https://exchangerate.host/documentation>     
**API Supported Currencies:** <https://exchangerate.host/currencies>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}