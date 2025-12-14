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

# Intro

이 웹 애플리케이션은 사용자가 이미지를 업로드하면, 데이터 과학 기법을 활용하여 이미지에서 가장 많이 사용된 10가지 주요 색상을 추출하고 시각적으로 보여주는 도구다. 색상은 HEX 코드와 함께 비율(%)로 표시되며, 각 색상은 클릭 시 클립보드에 복사되는 기능도 제공한다. 이미지 처리와 색상 추출은 서버 측에서 이루어지며, 사용자는 브라우저에서 간편하게 결과를 확인할 수 있다.
<br><br><br>

# Design

1. 라우팅 처리
   - GET 요청 시 이미지 파일 업로드 폼을 보여준다.
   - POST 요청 시 이미지 처리 및 색상 분석을 수행한다.
2. 이미지 처리
   - FileStorage 객체를 받아 PIL을 통해 이미지로 변환 후, numpy 배열로 처리한다.
3. 색상 추출
   - KMeans 클러스터링 알고리즘을 이용해 이미지 픽셀들을 분석하고, 클러스터 중심 색상을 추출한다.
4. 결과 렌더링
   - 웹페이지 상단에 업로드한 이미지가 표시되고, 하단에는 추출된 10가지 색상 블록이 표시된다.
   - 색상 블록을 클릭하면 해당 색상의 HEX 코드가 클립보드에 복사되고, 토스트 메시지로 복사 성공 여부를 알린다.
<br><br><br>

# Implementation

### Tech Stack

- **Programming Language:** Python
- **Backend:** Flask
- **Templates:** Jinja2 (HTML rendering)
- **Frontend:** HTML/CSS, JavaScript (클립보드 복사, toast 메시지)
- **Libraries:**
   - Pillow (이미지 처리)
   - NumPy (픽셀 배열 처리 및 벡터 연산)
   - scikit-learn (KMeans 클러스터링)
   - Base64 (이미지 인코딩)

### Coding

- 이미지 전처리
   - 업로드된 이미지는 `PIL.Image.open`을 통해 RGB 형식으로 강제 변환된다.
   - `thumbnail()` 함수를 사용해 이미지를 축소하여 처리 성능을 개선한다.
- 픽셀 추출 및 배열 변환
   - 이미지를 `np.array()` 배열로 변환한다.
   - 배열을 (height × width, 3) 형태로 재구성하여 각 픽셀의 RGB 값을 벡터 형태로 정렬한다.
- 색상 군집화
   - `KMeans(n_clusters=10)`를 통해 색상 분포를 10개의 중심값으로 그룹화한다.
- 비율 계산
   - `np.bincount(labels)`로 각 클러스터에 속한 픽셀 수를 계산한다.
   - (해당 그룹의 픽셀 수 / 전체 픽셀 수)로 비율을 산출한다.
- 예외 처리
   - RGB 이미지가 아니거나 유효한 색상 분포가 없을 경우 ValueError를 발생시킨다.
- 이미지 인코딩 및 미리보기 처리
  - 업로드된 이미지는 디스크에 저장하지 않고 `io.BytesIO` 객체를 이용해 메모리 내에서 처리된다.
  - `base64.b64encode()` 함수를 통해 이미지를 문자열로 인코딩하고, 클라이언트 측에서는 `data:image/...` 형식의 data URL을 통해 즉시 업로드했던 이미지를 확인할 수 있다.
  - 이미지 파일을 따로 저장하거나 서버에서 static URL을 할당하지 않아도 되기 때문에, 응답 속도가 빠르고 보안상 유리하다.
- 클립보드 복사
   - 추출한 색상 코드를 `<div>` 내에 표시하고, 사용자가 클릭하면 자바스크립트가 해당 HEX값을 클립보드로 복사한다.
   - `navigator.clipboard.writeText()` 브라우저 API를 사용하여 안전하고 간편하게 복사할 수 있다.
<br><br><br>

# Result

![](/assets/images/personal-projects/color_picker.gif)
<br><br><br>

# Future Improvements

- **추출할 색상 수 선택 기능 추가**   
현재는 항상 10개의 색상을 추출하지만, 사용자 입력을 통해 색상 수를 조절할 수 있도록 개선
- **추출 색상 다운로드 기능 추가**   
결과 색상 목록을 팔레트 이미지로 다운로드 할 수 있도록 확장
<br><br><br>

# Conclusion

이 프로젝트에서는 데이터 과학 기술을 실제 이미지 처리에 활용했다. Pillow와 NumPy로 이미지 데이터를 수치화하고, KMeans 클러스터링 알고리즘으로 주요 색상을 추출하는 과정을 구현하며 데이터 과학이 이미지 분석에 어떻게 활용되는지 배울 수 있었다.   
단순한 웹 애플리케이션 개발뿐만 아니라, 이미지를 분석하고 의미 있는 정보를 추출하는 능력을 키우는 데 큰 도움이 됐다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}