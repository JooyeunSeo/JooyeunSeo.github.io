---
date: 2025-06-09
layout: splash
excerpt: "Extract the 10 most noticeable colors in the image."
title: "Color Picker"
header:
  teaser: "https://images.unsplash.com/photo-1739145974146-c310088417ca?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://images.unsplash.com/photo-1739145974146-c310088417ca?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%ED%85%8C%EC%9D%B4%EB%B8%94-%EC%9C%84%EC%97%90-%EB%8B%A4%EC%96%91%ED%95%9C-%EC%83%89%EC%83%81%EC%9D%98-%ED%8E%98%EC%9D%B8%ED%8A%B8-%EB%AD%89%EC%B9%98-m4BWEyDqwCM)"
  actions:
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/color_picker"
    - label: "Check the Code"
      url: "https://github.com/JooyeunSeo/Dynamic-Web-Page"  
---

# Overview
<hr>

이 웹 애플리케이션은 사용자가 이미지를 업로드하면 데이터 과학 기법을 활용하여 이미지 내에서 가장 비중이 높은 10가지 주요 색상을 추출하고 시각화하는 도구입니다. 추출된 색상은 HEX 코드와 함께 점유 비율(%)로 표시되며, 각 색상 항목을 클릭하면 즉시 클립보드에 복사되는 기능을 제공합니다. 모든 이미지 처리와 분석은 서버 측에서 수행되며, 사용자는 브라우저를 통해 간편하게 결과물을 확인할 수 있습니다.
<br><br><br>

# System & Interface Design
<hr>

### Information Architecture

[![](https://mermaid.ink/img/pako:eNplU11PE0EU_Ss381RiwYW17bIPTSyGB6PRuPTF9GWyHdoN2906uyUiIaGymgDFj1ikkjbWSAqYEosFggn-oc7sf3D2g0LCPt27c87Zc-6dXUW6XSRIRQ55VSOWTh4ZuERxpWCBeKqYuoZuVLHlQh6wA3mHUEjMmQax3Im7GC3AzJvYWQKN0GVC70JyASSH9SViFeGJXTJ0oWebNoWHFjZXHMMRuhEtP5nNairwzhn7fckP14HvvWM_2uxLGxLPn2kLcF8PiJNVQ6jR2I4Wkea0F_Pgv-_69QGwwUfwGw3euQLe7vr7R9w7hdGfdd7rRBxsunEPfPvAbxxFryM5oZcXJvY-se99YMdNvt0OvXQ9tt2HRJC2DE-J4-ASiT0Q0yFjQe90NDy_LZjN5m6HYjsD0fjeIJa8geZi6M8rvt8EvrHJN-phGPbX4-0j4BdNfiFmsWBXYVqauE2MhsAuPO51hJPBaHglmC3_W-tutPjY_9ASPkJH3QbbabLDOiRubN4bG-j1-daBv3V5HdYqRsXN0oJ5RWB_94T9Oga_fsZ6J5B4jJexplOjen15YnR4_o8Nz4LdsuE5f9sPN_F1M8y7YGPHBb7bYD3h83NbrAAlUYkaRaQuYjHsJKoQWsFBj1YD5QJyy6RCCkgVZZEs4prpFlDBWhM8cQ1f2nYFqS6tCSa1a6XyWKdWLWL3-icYQ0RGQufsmuUiNaWEEkhdRa-ROjMrT80qaTmdzkiiTslJtILUaWVKkZQHMylJUWQpLSvptSR6E35UmprNpDMzUiYlyfK0klEya_8BHQhwbw?type=png)](https://mermaid.live/edit#pako:eNplU11PE0EU_Ss381RiwYW17bIPTSyGB6PRuPTF9GWyHdoN2906uyUiIaGymgDFj1ikkjbWSAqYEosFggn-oc7sf3D2g0LCPt27c87Zc-6dXUW6XSRIRQ55VSOWTh4ZuERxpWCBeKqYuoZuVLHlQh6wA3mHUEjMmQax3Im7GC3AzJvYWQKN0GVC70JyASSH9SViFeGJXTJ0oWebNoWHFjZXHMMRuhEtP5nNairwzhn7fckP14HvvWM_2uxLGxLPn2kLcF8PiJNVQ6jR2I4Wkea0F_Pgv-_69QGwwUfwGw3euQLe7vr7R9w7hdGfdd7rRBxsunEPfPvAbxxFryM5oZcXJvY-se99YMdNvt0OvXQ9tt2HRJC2DE-J4-ASiT0Q0yFjQe90NDy_LZjN5m6HYjsD0fjeIJa8geZi6M8rvt8EvrHJN-phGPbX4-0j4BdNfiFmsWBXYVqauE2MhsAuPO51hJPBaHglmC3_W-tutPjY_9ASPkJH3QbbabLDOiRubN4bG-j1-daBv3V5HdYqRsXN0oJ5RWB_94T9Oga_fsZ6J5B4jJexplOjen15YnR4_o8Nz4LdsuE5f9sPN_F1M8y7YGPHBb7bYD3h83NbrAAlUYkaRaQuYjHsJKoQWsFBj1YD5QJyy6RCCkgVZZEs4prpFlDBWhM8cQ1f2nYFqS6tCSa1a6XyWKdWLWL3-icYQ0RGQufsmuUiNaWEEkhdRa-ROjMrT80qaTmdzkiiTslJtILUaWVKkZQHMylJUWQpLSvptSR6E35UmprNpDMzUiYlyfK0klEya_8BHQhwbw)

1. 라우팅 처리
   - GET 요청 시 이미지 업로드 폼을 사용자에게 제공합니다.
   - POST 요청 시 업로드된 이미지의 유효성을 검증하고 색상 분석 로직을 실행합니다.
2. 이미지 처리
   - FileStorage 객체를 수신하여 Pillow로 이미지화한 뒤, 효율적인 연산을 위해 NumPy 배열로 변환합니다.
3. 색상 추출
   - KMeans 클러스터링 알고리즘을 적용하여 이미지 픽셀의 색상 분포를 분석하고, 군집별 중심 색상을 추출합니다.
4. 결과 렌더링
   - 상단에는 업로드한 이미지 미리보기를 표시합니다.
   - 하단에는 분석된 10가지 색상 블록과 비율을 나열하며, 클릭 시 클립보드 복사 및 토스트 메시지 알림 기능을 수행합니다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Backend:** Python, Flask, Jinja2
- **Frontend:** HTML/CSS, JavaScript(AJAX, Clipboard API)
- **Libraries:** Pillow(이미지 처리), NumPy(픽셀 배열 처리 및 벡터 연산), scikit-learn(KMeans 클러스터링), Base64(이미지 인코딩)

### Key Implementation Details

1. 이미지 전처리: 모든 업로드 파일은 RGB 형식으로 강제 변환되며, thumbnail() 함수를 통해 성능 최적화를 위한 리사이징 과정을 거칩니다.
2. 픽셀 벡터화: 이미지 배열을 `(height × width, 3)` 형태로 재구성하여 각 픽셀의 RGB 값을 벡터 형태로 정렬한 뒤 군집화 모델에 입력합니다.
3. 색상 군집화 및 비율 산출: `KMeans(n_clusters=10)`를 사용하여 색상을 그룹화하고, np.bincount를 활용해 각 군집이 전체 이미지에서 차지하는 비중을 계산합니다.
4. 메모리 내 처리: 이미지를 디스크에 저장하지 않고 `io.BytesIO`와 `Base64` 인코딩을 사용하여 메모리에서 즉시 Data URL로 변환합니다. 이는 응답 속도를 높이고 서버 보안을 강화하는 데 기여합니다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem 1. 고해상도 이미지 처리 시 성능 저하

고해상도 이미지를 그대로 분석할 경우 픽셀 수가 너무 많아 KMeans 연산 시간이 급격히 늘어나고 서버 부하가 발생했습니다.

### Solution

`img.thumbnail((130, 130))`을 적용하여 색상 분포의 특징은 유지하면서도 연산 대상 픽셀 수를 획기적으로 줄여 처리 속도를 대폭 개선했습니다.

-----------

### Problem 2. 비정상 이미지 포맷 및 런타임 에러

투명도가 포함된 PNG(RGBA)나 흑백 이미지, 혹은 손상된 파일 업로드 시 배열 차원 불일치로 인해 서버 에러가 발생했습니다.

### Solution

`.convert('RGB')`를 통해 채널을 통일하고, ndim 검증 로직을 추가하여 규격에 맞지 않는 파일은 사전에 차단하도록 예외 처리를 강화했습니다.

------------

### Problem 3. 효율적인 이미지 미리보기 구현

업로드된 이미지를 사용자에게 다시 보여주기 위해 서버 스토리지에 임시 파일을 저장하는 방식은 관리 비용과 보안 측면에서 비효율적이었습니다.

### Solution

Base64 인코딩을 활용하여 이미지 데이터를 문자열 형태(Data URL)로 템플릿에 직접 전달함으로써 별도의 저장 시스템 없이 메모리 내에서 처리를 완결했습니다.
<br><br><br>

# Result
<hr>

![](/assets/images/personal-projects/color_picker.gif)
<br><br><br>

# Future Improvements
<hr>

- **추출할 색상 수 선택 기능 추가**   
현재는 항상 10개의 색상을 추출하지만, 사용자 입력을 통해 색상 수를 조절할 수 있도록 개선
- **추출 색상 다운로드 기능 추가**   
결과 색상 목록을 팔레트 이미지로 다운로드 할 수 있도록 확장
<br><br><br>

# Conclusion
<hr>

이번 프로젝트를 통해 Pillow와 NumPy를 활용한 이미지 데이터 수치화와 KMeans 클러스터링 알고리즘의 실전 적용 과정을 경험했습니다. 데이터 과학 기법이 단순한 수치 분석을 넘어 이미지 분석과 같은 웹 서비스에 어떻게 활용될 수 있는지 이해할 수 있었습니다. 특히 성능 최적화와 예외 처리를 거치며 사용자에게 신뢰성 있는 정보를 빠르게 전달하는 구조를 설계하는 역량을 키울 수 있었던 뜻깊은 프로젝트였습니다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}