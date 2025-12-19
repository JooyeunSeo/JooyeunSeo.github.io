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
      url: "https://drive.google.com/uc?id=1PnwnDFCwp31jiDiM9agAz5RV12m1PbUn&export=download" 
---

# Intro
<hr>

이 프로그램은 Selenium을 활용하여 닌텐도 코리아 eShop에 등록된 닌텐도 스위치 게임 정보를 자동으로 수집합니다.    
크롬 브라우저에서 실행되며, 동적으로 렌더링되는 웹 페이지를 직접 제어하여 데이터를 가져옵니다.

사용자는 베스트셀러, 신작, 세일 중과 같은 카테고리를 선택할 수 있고, 발매일 기준 또는 가격 기준으로 게임 목록을 정렬할 수 있습니다.

수집된 데이터는 Tkinter 기반의 GUI를 통해 표 형태로 시각화되며 썸네일 이미지와 함께 게임 제목, 가격, 발매일 등의 정보를 한눈에 확인할 수 있습니다.      
또한 결과를 CSV 파일로 저장할 수 있어 이후 데이터 분석이나 개인적인 기록 용도로도 활용할 수 있습니다.
<br><br><br>

# Design
<hr>

### Overview 

이 프로젝트는 데스크톱 GUI 애플리케이션 형태로 구현되었다.
Selenium을 이용해 웹 페이지에서 데이터를 수집하고, Tkinter를 통해 사용자에게 직관적인 인터페이스를 제공한다.

데이터 수집, 정렬, 시각화, 파일 저장까지의 전 과정이 하나의 애플리케이션 내에서 이루어지도록 설계되었다.

### Information Architecture

<figure>
  <a href="https://mermaid.live/edit#pako:eNqVVO9P4jAA_VeaJhpNULeBwhaPixkD8SYYBnp3zA-FFVhuW5euUzjgf7_-QB14yl0_LHvte2-vb02XcEwCDC04icjzeIYoA27PT_wE8HFwAL7sDmC7bafTf7-gJFk-mlKUzoAdhThhQx9ejurqHRz1f4UJwxS0Bu3jy7NR3YePSiWGNzzj1HYSshBFwBtTjBNBOitwBsMh53iYARsxPCV0IRiXI1o_FA-xRvgOuikLiRQ_FsS2FPfy5EUjrSKchHm8y23IMH00ijC4D_HzbhBHet2iXxjY3n1RjZPg8_p6Vw-u09vfH0XPEaaqwAc8UhNhMgUuWmD6rr7m0c52Njvk0gYNn5Ti-I3f0pd89Y6keQqceZix7KtgrIsMJHdpRyTDBUep2S2sZQi7Dp4zcIem-CPLsnQUjIJhBz2FU_S3X3a9odOtAC0UY9BADP1P7873vtPrXLl7i3fm_IgmKFLNvyDAe0w3sbd6b4veO-JcJwEB3wjFCGBvRtJC3_uyef1u76rl7I3mMUJ5BpXMJWMeqxnyE-otMobjd9FuhiIbP5-SJfP8Y1lNt_vwURoPnJzUwUCBgQS2ArYETQWaErQVaEvQ0hVq6QKufuBsJQ6ZWitvrXXI6m2qLBnXCl0rurFZMwpW5a05YdF42WVDTjnzlF8PK-CoSUda3XzahNvt3n3UhDK9JUE4WWzunAwcgh4O-KcHsASnNAygNUFRhkswxjRGAsOlkPuQzXCMfWjx1wBPUB4xH_rJmutSlPwkJIYWozlXUpJPZ68-eRrwu68RIn4m4tdZyn8ppjbJEwYt47xiShdoLeEcWifm6UWlUjnXTM2sXuiGXivBBbR0XT_VTUPTq7pZq1b0qrEuwd_yw_qpoWk1TTsv17SLslYxy-s_HHi5oA" target="_blank" title="Mermaid Live Editor">
    <img src="/assets/images/personal-projects/nintendo_game_info.IA.png" alt="IA">
  </a>
</figure>

위 다이어그램은 본 애플리케이션의 전체 구조를 나타낸다.

1. 카테고리 선택
   - 사용자는 `베스트셀러`, `신작`, `세일 중` 중 하나를 선택하여 해당 게임 목록을 가져오도록 설정한다.
2. 정렬 기능 선택
   - 발매일순, 가격 오름차순, 가격 내림차순 중 하나를 선택할 수 있다.
   - 선택된 정렬 옵션은 데이터 수집 완료 후 테이블 갱신 시 적용된다.
3. 크롤링 시작
   - Run 버튼을 누르면 Selenium WebDriver가 선택된 카테고리 페이지를 열고 게임 정보를 수집한다.
   - 여러 페이지로 구성된 목록도 자동으로 순회하며 데이터를 수집한다.
4. 결과 표시
   - GUI 하단 영역에 썸네일, 제목, 현재 가격, 정가, 발매일 정보가 테이블 형식으로 표시된다.
   - 데이터가 많을 경우 스크롤을 통해 전체 목록을 확인할 수 있다.
5. 결과 저장
   - `Make CSV` 버튼을 통해 수집된 게임 정보를 CSV 파일로 저장할 수 있다.
   - 해당 버튼은 데이터 수집이 완료된 이후에만 활성화된다.

## UI

- **상단:** 애플리케이션 제목과 간단한 설명을 표시한다.
- **중단:** 카테고리 선택, 정렬 옵션, 실행 버튼 및 CSV 파일로 저장하기 버튼을 배치한다.
- **하단:** 게임 정보 테이블을 표시하며, 썸네일 이미지를 포함하고 스크롤을 지원한다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Programming Language:** Python
- **Graphics Library:** Tkinter
- **Web Crawling:** Selenium, Requests
- **Image Handling:** Pillow
- **Data Handling:** pandas

### Coding

1. **Selenium 기반 크롤링**
   - Selenium을 사용하여 JavaScript로 동적 렌더링되는 웹페이지를 조작한다.
   - 페이지 순회 및 크롤링 흐름은 다음과 같다.
      1. 사용자가 선택한 카테고리에 맞는 페이지 열기
      2. 첫 접속 시 한 번만 등장하는 팝업 창 닫기
      3. 현재 페이지의 각 게임 요소(최대 20개)에 대해 정보 파싱
         - 썸네일 이미지(url): `img.product-image-photo`
         - 제목: `a.product-item-link`
         - 현재가: `span.price`
         - 정가(세일 중일 경우): `span.old-price span.price`
         - 발매일: `div.category-product-item-released`
      4. 다음 페이지 버튼 `a.action.next` 존재 여부 확인
         - 존재할 경우 클릭하여 페이지 이동 후 반복
         - 존재하지 않을 경우 `NoSuchElementException` 발생 → 루프 종료
2. **ChromeOptions 설정**     
크롤링 안정성과 자동화 탐지 회피를 위해 다음과 같은 옵션을 적용했다.       
   - 브라우저 GUI 없이 백그라운드에서 실행하여 사용자 개입 없이 자동화 수행: `--headless`
   - 일반 사용자 브라우저로 접근하는 것처럼 위장: `user-agent`
   - 요청 시 우선 언어를 지정하여 페이지 구조와 크롤링 결과의 일관성 확보: `--lang=ko_KR`,
   - 항상 데스크톱 전용 UI가 로드되도록 창 크기 고정: `--window-size=1920x1080`
   - 자동화 탐지 우회:
      - `--disable-blink-features=AutomationControlled`
      - `--disable-extensions`
      - `excludeSwitches: ["enable-automation"]`
3. **데이터 가공 및 정렬**
   - 날짜 데이터는 `"YY.MM.DD"` 형식을 `split(".")` 후 정수 튜플로 변환하여 정렬에 사용한다.
   - 가격 데이터는 `"₩"` 및 `","` 제거 후 정수형으로 변환한다.
   - `sort()` 함수를 이용해 오름차순 또는 내림차순 정렬을 적용한다.
4. **썸네일 이미지 처리**
   1. `requests`를 사용해 정적 이미지를 다운로드한다.
   2. Pillow 라이브러리로 이미지 크기를 조정한다.
   3. Tkinter에서 사용 가능한 `ImageTk.PhotoImage` 객체로 변환한다.
   4. GC(가비지 컬렉션)에 의해 이미지가 삭제되지 않도록 참조 리스트(self.image_refs)를 유지한다.
5. **CSV 저장**
   - 리스트 형태의 데이터를 Pandas의 `DataFrame`으로 변환한다.
   - Tkinter의 파일 저장 다이얼로그를 통해 파일명과 저장 위치를 지정할 수 있다.
   - `to_csv()` 메서드로 CSV 파일을 저장한다. (utf-8-sig 인코딩으로 한글 깨짐 방지)
<br><br><br>

# Problem Solving Process
<hr>

### Problem

각 게임의 상세 페이지에 직접 접근하여 더 많은 정보를 수집하려는 과정에서 문제가 발생했다.      
다수의 페이지를 반복적으로 요청하는 과정에서 웹사이트 측에서 자동화 트래픽으로 인식하여 접속이 차단되는 현상이 발생했다.

### Analysis

- 각 게임마다 상세 페이지에 진입하는 방식은 요청 횟수가 급격히 증가한다.
- User-Agent 변경이나 실행 옵션 조정으로 탐지를 회피하려 했으나, 요청 데이터 양이 많아질수록 차단을 완전히 피하기는 어려웠다.
- 상용 웹사이트의 경우 크롤링 빈도와 접근 방식에 민감하게 반응한다는 점을 확인했다.

### Solution

상세 페이지 접근을 포기하고, 목록 페이지에서 접근 가능한 정보만 수집하는 방식으로 방향을 수정했다.      
이를 통해 크롤링 안정성을 확보하고, 차단 없이 프로그램이 정상적으로 동작하도록 설계 방향을 조정했다.
<br><br><br>

# Result
<hr>

<img src="/assets/images/personal-projects/nintendo_game_info.Result.gif" width="40%">
<br><br><br>

# Future Improvements
<hr>

- **스크래핑 시 로딩 애니메이션 표시**
- **게임 상세 페이지 접속 후 추가 정보 수집**   
한국어 지원 여부, 장르, Nintendo Switch 1/2 지원 여부 등
- **필터링 기능 강화**   
가격대 또는 발매일 범위 등
<br><br><br>

# Conclusion
<hr>

이번 프로젝트를 통해 웹사이트에서 원하는 정보를 자동으로 수집하는 전체 과정을 경험할 수 있었습니다.
특히 동적 웹 페이지 처리와 페이지네이션 구현을 직접 다뤄보면서, 웹 크롤링이 단순한 요청 이상의 복합적인 작업이라는 점을 체감할 수 있었습니다.

또한 반복적인 크롤링 과정에서 발생한 차단 문제를 통해, 상용 웹사이트 환경에서의 크롤링 한계와 이를 고려한 설계의 중요성도 함께 배울 수 있었습니다.
필요한 데이터만 선별해 수집하고, 이를 정리하여 실제로 활용 가능한 형태로 만드는 경험은 앞으로의 자동화 작업에 큰 도움이 될 것이라 생각합니다.
<br>

### reference

**닌텐도 코리아 eShop:** <https://store.nintendo.co.kr/digital>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}