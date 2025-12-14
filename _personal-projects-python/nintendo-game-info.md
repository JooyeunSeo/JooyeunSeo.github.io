---
date: 2025-07-02
layout: splash
excerpt: "Explore Nintendo Switch's top, new, and discounted games. Sort them your way and save the list as a CSV file."
title: "Nintendo Game Info"
header:
  teaser: "https://cdn.pixabay.com/photo/2019/06/26/02/56/nintendo-4299421_1280.jpg"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://cdn.pixabay.com/photo/2019/06/26/02/56/nintendo-4299421_1280.jpg
  caption: "Photo credit: [**Pixabay**](https://pixabay.com/ko/illustrations/%EB%8B%8C%ED%85%90%EB%8F%84-nintendo-%EC%8A%A4%EC%9C%84%EC%B9%98-4299421/)"
  actions:
    - label: "Download Zip"
      url: "https://drive.google.com/uc?id=13yBoSRfw5jC38StDljQY_nxzrpi_VoeM&export=download" 
---

# Intro

이 프로그램은 Selenium을 활용해 닌텐도 코리아 eShop에 등록된 닌텐도 스위치 게임 정보를 자동으로 수집한다. 사용자는 원하는 카테고리(베스트셀러, 신작, 세일 중)와 정렬 방식(발매일 기준, 가격 기준)을 선택할 수 있으며, GUI를 통해 수집된 데이터를 표 형태로 확인할 수 있다. 또한 데이터를 CSV 파일로 저장할 수 있어, 추후 데이터 분석에 활용하기에도 유용하다.
<br><br><br>

# Design

1. 카테고리 선택
   - 사용자는 `베스트셀러`, `신작`, `세일 중` 중 하나를 선택하여 해당 게임 목록을 가져오도록 설정한다.
2. 정렬 기능 선택
   - 발매일순, 가격 오름차순, 가격 내림차순 중 하나를 선택할 수 있다.
   - 사용자가 지정한 정렬 옵션은 데이터가 수집된 후 테이블 갱신 시 적용된다.
3. 크롤링 시작
   - Run 버튼을 누르면 셀레니움이 해당 페이지를 열고 게임 정보를 수집한다.
   - 여러 페이지에 걸쳐 있는 데이터도 자동으로 수집된다.
4. 결과 표시
   - GUI 창 하단에 썸네일, 제목, 가격, 정가, 발매일 등이 테이블 형식으로 시각화된다.
   - 목록이 길 경우 생성되는 스크롤을 통해 아래위로 이동하며 전체 리스트를 볼 수 있다.
5. 결과를 파일로 저장
   - Make CSV 버튼을 눌러 수집한 게임 정보를 CSV 파일로 저장할 수 있다.
   - 해당 버튼은 데이터 수집 및 정렬 이후에 활성화된다.
<br><br><br>

# Implementation

### Tech Stack

- **Programming Language:** Python
- **Graphics Library:** Tkinter
- **Web Crawling:** Selenium, Requests
- **Image Handling:** Pillow
- **Data Handling:** pandas

### Coding

- **Selenium**을 사용하여 **동적**(JavaScript)으로 렌더링되는 웹페이지 조작
   - 페이지 순회 및 크롤링 흐름
      1. 페이지 열기
      2. 첫 접속 시에만 등장하는 팝업창 닫기
      3. 현재 페이지의 각 게임 요소(최대 20개)에 대해 정보 파싱
         - 썸네일 이미지(url): `img.product-image-photo`
         - 제목: `a.product-item-link`
         - 현재가: `span.price`
         - 정가(세일 중일 때만 존재): `span.old-price span.price`
         - 발매일: `div.category-product-item-released`
      4. 다음 페이지로 가는 버튼(`a.action.next`)이 존재한다면 `.click()`으로 클릭
      5. 마지막 페이지에 도달하면 다음 페이지 버튼이 없으므로 NoSuchElementException 발생 → 루프 종료
   - ChromeOptions로 탐지 회피 및 크롤링 안정성 확보
      - `--headless`:  브라우저 GUI 없이 백그라운드에서 실행되어 사용자 개입 없이 자동화 가능
      - `"user-agent"` : 일반 사용자 브라우저로 접근하는 것처럼 위장
      - `"--lang=ko_KR"`, : 웹사이트에 요청 시 우선 언어를 지정하여 웹페이지 구조와 크롤링 결과의 일관성 보장
      - `"--disable-blink-features=AutomationControlled"`, `"--disable-extensions"`, `"excludeSwitches": ["enable-automation"]` : 자동화 탐지 우회
      - `--window-size=1920x1080`: 항상 데스크탑 전용 UI가 로드되도록 지정
- 문자열 데이터 가공 후 정렬
   - 날짜: `"YY.MM.DD"` 형식을 split(".") 후 tuple(map(int, ...)) 형태로 변환
   - 가격: `"₩00,000"` 형식에서 "₩"와 ","을 제거한 뒤 int형으로 변환
   - sort() 함수를 이용해 정렬하고, 내림차순일 경우 reverse=True 옵션 적용
- 게임 썸네일 이미지 최적화
   1. **requests**로 **정적**인 이미지 다운로드
   2. Pillow로 사이즈 조정 후, Tkinter에서 사용 가능한 ImageTk.PhotoImage 객체로 변환
   3. 이미지 레퍼런스가 GC(가비지 컬렉션)에 의해 삭제되지 않도록 참조 유지 리스트(self.image_refs)를 관리
- Pandas 라이브러리로 CSV 저장
   1. 리스트 안에 딕셔너리들이 들어있는 형태의 데이터를 pandas.DataFrame 객체로 변환
   2. tkinter의 파일 저장 다이얼로그를 통해 사용자가 직접 파일 이름과 저장 위치를 지정(확장자는 .csv로 고정)
   3. DataFrame.to_csv() 메서드로 CSV 파일로 저장(`utf-8-sig` 인코딩으로 한글 깨짐 방지)
<br><br><br>

# Result

<img src="/assets/images/personal-projects/nintendo_game_info.gif" width="40%">
<br><br><br>

# Future Improvements

- **스크래핑 시 로딩 애니메이션 표시**
- **게임 상세 페이지 접속 후 추가 정보 수집**   
한국어 지원 여부, 장르, Nintendo Switch 1/2 지원 여부 등
- **필터링 기능 강화**   
가격대 또는 발매일 범위 등
<br><br><br>

# Conclusion

이번 프로젝트를 통해 웹사이트에서 원하는 정보를 자동으로 가져오는 방법을 배우게 되었다. 특히 상용 웹사이트에서 자주 등장하는 동적 콘텐츠를 처리하거나 페이지네이션(다음 페이지 탐색) 같은 기능을 직접 구현해보면서 웹 크롤링의 실제 작동 방식을 경험했다.   
크롤링을 반복 실행하는 과정에서 사이트에서 차단되는 문제가 발생했는데, 이를 해결하기 위해 User-Agent 설정이나 실행 옵션 등을 조정하며 더 안정적인 크롤링 방법을 고민하고 적용해볼 수 있었다.   
또한 웹사이트 구조를 분석해 필요한 데이터만 뽑아 정렬하고 저장하는 작업을 통해, 단순한 코드 작성이 아닌 실제로 활용 가능한 프로그램을 만드는 감각도 함께 키울 수 있었다.   
이 경험은 앞으로 데이터 수집이나 정리 자동화 같은 작업을 할 때 큰 도움이 될 것 같다.
<br>

### reference

**닌텐도 코리아 eShop:** <https://store.nintendo.co.kr/digital>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}