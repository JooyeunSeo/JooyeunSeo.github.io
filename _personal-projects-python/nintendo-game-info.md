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

# Overview
<hr>

이 프로그램은 Selenium을 활용하여 닌텐도 코리아 eShop에 등록된 게임 정보를 자동으로 수집하는 자동화 도구입니다. 크롬 브라우저 환경에서 실행되며, 자바스크립트로 동적 렌더링되는 웹 페이지를 직접 제어하여 정확한 데이터를 가져옵니다.

사용자는 베스트셀러, 신작, 세일 중인 게임 등 원하는 카테고리를 선택할 수 있으며, 발매일이나 가격을 기준으로 목록을 자유롭게 정렬할 수 있습니다. 수집된 데이터는 Tkinter 기반의 GUI를 통해 표 형태로 시각화되어 썸네일 이미지, 제목, 가격, 발매일 등을 한눈에 확인 가능합니다. 또한, 결과를 CSV 파일로 내보낼 수 있어 개인적인 데이터 분석이나 기록 용도로 활용하기에 용이합니다.
<br><br><br>

# System & Interface Design
<hr>

본 프로젝트는 데스크톱 GUI 애플리케이션으로 구현되었습니다. 데이터 수집부터 정렬, 시각화, 파일 저장까지의 모든 프로세스가 하나의 인터페이스 내에서 완결되도록 설계되었습니다.

### Information Architecture

<figure>
  <a href="https://mermaid.live/edit#pako:eNqVVO9P4jAA_VeaJhpNULeBwhaPixkD8SYYBnp3zA-FFVhuW5euUzjgf7_-QB14yl0_LHvte2-vb02XcEwCDC04icjzeIYoA27PT_wE8HFwAL7sDmC7bafTf7-gJFk-mlKUzoAdhThhQx9ejurqHRz1f4UJwxS0Bu3jy7NR3YePSiWGNzzj1HYSshBFwBtTjBNBOitwBsMh53iYARsxPCV0IRiXI1o_FA-xRvgOuikLiRQ_FsS2FPfy5EUjrSKchHm8y23IMH00ijC4D_HzbhBHet2iXxjY3n1RjZPg8_p6Vw-u09vfH0XPEaaqwAc8UhNhMgUuWmD6rr7m0c52Njvk0gYNn5Ti-I3f0pd89Y6keQqceZix7KtgrIsMJHdpRyTDBUep2S2sZQi7Dp4zcIem-CPLsnQUjIJhBz2FU_S3X3a9odOtAC0UY9BADP1P7873vtPrXLl7i3fm_IgmKFLNvyDAe0w3sbd6b4veO-JcJwEB3wjFCGBvRtJC3_uyef1u76rl7I3mMUJ5BpXMJWMeqxnyE-otMobjd9FuhiIbP5-SJfP8Y1lNt_vwURoPnJzUwUCBgQS2ArYETQWaErQVaEvQ0hVq6QKufuBsJQ6ZWitvrXXI6m2qLBnXCl0rurFZMwpW5a05YdF42WVDTjnzlF8PK-CoSUda3XzahNvt3n3UhDK9JUE4WWzunAwcgh4O-KcHsASnNAygNUFRhkswxjRGAsOlkPuQzXCMfWjx1wBPUB4xH_rJmutSlPwkJIYWozlXUpJPZ68-eRrwu68RIn4m4tdZyn8ppjbJEwYt47xiShdoLeEcWifm6UWlUjnXTM2sXuiGXivBBbR0XT_VTUPTq7pZq1b0qrEuwd_yw_qpoWk1TTsv17SLslYxy-s_HHi5oA" target="_blank" title="Mermaid Live Editor">
    <img src="/assets/images/personal-projects/nintendo_game_info.IA.png" alt="IA">
  </a>
</figure>

- **카테고리 설정:** 사용자가 베스트셀러, 신작, 세일 중 카테고리 중 하나를 선택합니다.
- **정렬 옵션 선택:** 발매일순, 가격 오름차순/내림차순 중 데이터 표시 기준을 설정합니다.
- **데이터 수집(Crawling):** Run 버튼 클릭 시 Selenium WebDriver가 작동하여 페이지네이션을 따라가며 모든 게임 정보를 수집합니다.
- **결과 시각화:** 수집된 정보를 썸네일과 함께 테이블 형식으로 GUI에 출력합니다.
- **파일 내보내기:** Make CSV 버튼을 통해 수집된 리스트를 파일로 저장합니다.

## UI

- **상단:** 서비스 타이틀 및 사용 가이드 배치
- **중단:** 컨트롤러 영역(카테고리·정렬 선택, 실행 및 저장 버튼)
- **하단:** 데이터 출력 영역(이미지 포함 테이블, 스크롤 지원)
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Language:** Python
- **Library:** Tkinter(GUI), Selenium 및 Requests(크롤링), Pillow(이미지), Pandas(데이터)

### Key Implementation Details

1. 동적 크롤링: Selenium을 통해 팝업 창 자동 닫기, 페이지 이동(a.action.next), 상세 항목(제목, 가격, 세일 가격, 발매일 등) 파싱을 수행합니다.
2. 브라우저 최적화: `--headless` 모드와 `user-agent` 위장을 통해 리소스 소모를 줄이고 자동화 탐지를 회피했습니다.
3. 데이터 전처리: 날짜 문자열을 정수 튜플로 변환하고, 가격의 특수문자(`₩`, `,`)를 제거하여 정렬 가능한 수치 데이터로 가공했습니다.
4. 이미지 렌더링: requests로 다운로드한 이미지를 Pillow로 리사이징한 후, Tkinter 메모리 관리(GC)를 위해 참조 리스트(self.image_refs)에 저장하여 화면에 표시합니다.
5. 한글 인코딩: CSV 저장 시 `utf-8-sig` 설정을 적용하여 엑셀 등에서 한글 깨짐 현상을 방지했습니다.
<br><br><br>

# Problem Solving Process
<hr>

더 상세한 정보를 얻기 위해 각 게임의 상세 페이지를 반복 호출하자, 웹사이트 측에서 과도한 트래픽으로 인식하여 IP를 차단하거나 자동화 접속을 제한하는 현상이 발생했습니다.

짧은 시간 내에 급격히 증가한 요청 횟수가 주요 원인이었으며, 상용 웹사이트의 보안 정책상 단순한 옵션 조정만으로는 회피가 어려웠습니다.

### Solution

수집 범위를 목록 페이지에서 제공하는 정보로 한정하는 전략적 수정을 거쳤습니다. 이를 통해 크롤링 속도를 높이고 서비스의 안정적인 동작을 확보했습니다.
<br><br><br>

# Result
<hr>

<img src="/assets/images/personal-projects/nintendo_game_info.Result.gif" width="40%">
<br><br><br>

# Future Improvements
<hr>

- **데이터 수집 중 로딩 애니메이션 표시**
- **필터링 기능 강화**    
가격대 또는 발매일 범위 등
<br><br><br>

# Conclusion
<hr>

이번 프로젝트를 통해 동적 웹 페이지를 처리하고 페이지네이션을 구현하는 등 실전적인 웹 크롤링 기술을 습득할 수 있었습니다. 특히 실제 웹 서비스의 보안 정책에 대응하며 발생한 문제 해결 과정을 통해, 무분별한 수집보다는 서비스 환경을 고려한 효율적인 설계가 중요하다는 점을 배웠습니다.

필요한 데이터를 선별하여 수집하고, 이를 정제하여 사용자에게 가치 있는 정보(CSV, GUI)로 전환하는 경험은 향후 데이터 자동화 업무를 수행하는 데 큰 자산이 될 것입니다.
<br>

### reference

**닌텐도 코리아 eShop:** <https://store.nintendo.co.kr/digital>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}