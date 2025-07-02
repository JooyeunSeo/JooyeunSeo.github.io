---
date: 2025-02-15
layout: splash
excerpt: "A GUI tool for adding customizable watermarks to images, supporting text and pattern options."
title: "Image Watermarking App"
header:
  teaser: "https://cdn.pixabay.com/photo/2012/03/01/16/11/animal-20574_1280.jpg"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://cdn.pixabay.com/photo/2012/03/01/16/11/animal-20574_1280.jpg
  caption: "Photo credit: [**Pixabay**](https://pixabay.com/ko/photos/%EB%8F%99%EB%AC%BC-%EB%B0%B0%EA%B2%BD-%EA%B0%9C-%EB%B0%9C-%EB%B0%9C%EC%9E%90%EA%B5%AD-20574/)"
  actions:
    - label: "Download Zip"
      url: "https://drive.google.com/uc?id=1xpQOkPPxZaimN6RMNOcq6oKonFpuPPMN&export=download"
---
**Note:** The file is large, so Google Drive may display a warning before download. This is normal.

---

# Intro

원하는 이미지에 워터마크를 추가하는 데스크톱 응용프로그램이다. Tkinter 모듈로 그래픽 유저 인터페이스(GUI)를 생성했다. 이미지에 전체적으로 패턴을 오버레이하거나 텍스트를 추가할 수 있으며 텍스트의 크기, 색상, 투명도, 위치를 조정할 수 있다. 또 첫 번째 이미지에 워터마크를 넣으면 다른 이미지들에도 일괄 적용되며, 각 사진의 크기에 따라 워터마크 텍스트의 크기도 자동으로 조정되도록 설정했다.
<br><br><br>

# Design

- GUI 인터페이스
   - 사용자가 직접 이미지를 불러올 수 있고, 첫 번째 이미지는 대표로 썸네일에 표시되어 변화를 바로 확인할 수 있다.
   - 텍스트 또는 패턴을 선택하여 이미지에 추가할 수 있다.
      - 텍스트는 문구, 크기, 투명도, 색상, 위치 옵션이 있다.
      - 패턴은 사선, 가로선, 세로선, 점 무늬 옵션이 있고 투명도와 색상은 텍스트의 설정과 동일하다.
   - 원본 크기의 워터마크 적용 이미지를 별도 창에서 확인 가능하며, 창 크기보다 클 경우 가로 및 세로로 스크롤할 수 있다.
   - 워터마크 적용 후 저장 시 이미지의 원래 이름 뒤에 "_watermark"가 붙어서 저장된다.
- 일괄 처리
   - 첫 번째 이미지에 적용한 워터마크를 여러 개의 이미지에 일괄 적용하여 저장할 수 있다.
   - 워터마크 텍스트의 크기는 각 이미지의 크기에 따라 자동으로 적절히 조정된다.
<br><br><br>

# Implementation

### Tech Stack

- **Programming Language:** Python
- **Graphics Library:** Tkinter
- **Packaging:** PyInstaller

### Coding

- Tkinter로 GUI 구현 및 이미지 파일 열기/저장
   - PNG, JPG, JPEG, BMP 확장자를 지원한다.
   - 처리된 이미지들은 사용자가 지정한 폴더에 저장한다.
- PILLOW 라이브러리를 활용한 워터마킹
   - `Image`를 사용해 이미지를 프로그램으로 불러온다.
   - 투명도 값이 추가된 RGBA 모드로 사진을 변경한다.
   - `getexif()`로 이미지 파일에 포함된 EXIF 메타데이터를 체크하여 사진을 올바른 방향으로 회전시킨다.   
   (스마트폰이나 카메라로 찍은 사진이 자동으로 돌아가는 현상을 막기 위함)
   - `ImageDraw`와 `ImageFont`를 활용해 패턴과 텍스트를 원하는 위치에 그린다.
- 사용자의 OS에 맞는 한글 폰트를 설정하여 한글 워터마크 지원
- 같은 스타일의 워터마크를 여러 이미지에 일괄 적용
   - 워터마크 텍스트 크기는 이미지마다 자동으로 변경된다.
      - 첫 번째 이미지의 크기와 텍스트의 크기를 기준으로 비율을 설정하고 저장
      - 두 번째 이미지부터는 해당 이미지의 크기와 미리 설정된 비율에 따라 텍스트의 크기 자동 조정
      - 가로 또는 세로가 극단적으로 더 긴 이미지에 대비해 가로 길이 또는 세로 길이 중 적절한 것을 택해서 비율 계산
   - 반복문으로 불러온 모든 이미지에 워터마크를 적용하고 저장한다.
- 사용자 편의
   - tkinter의 canvas에 첫 번째 사진을 축소해서 넣어서 이미지에 어떻게 워터마크가 적용되는지 바로 확인할 수 있다.
   - 간단한 문구를 통해 이미지 열기/저장이 제대로 되는지 파악할 수 있다.

### 배포

PyInstaller 모듈을 통해 프로그램을 실행 파일 형태로 변환했다. Python이나 필수 라이브러리가 설치되지 않은 컴퓨터에서도 프로그램을 실행 가능하다는 장점이 있기 때문에 시도해보았다.   
다만 Mac OS 이용자만 실행 파일을 사용할 수 있고, Windows 등 다른 OS 사용자는 여전히 Python과 Pillow 라이브러리를 설치 후 파이썬 파일을 직접 실행해야 한다.
<br><br><br>

# Result

<img src="/assets/images/personal-projects/image_watermarking_app.gif" width="80%">
<br><br><br>

# Future Improvements

- 원하는 이미지를 워터마크로 사용할 수 있는 기능 추가
- 워터마크 텍스트에 테두리를 추가하는 옵션 넣기
<br><br><br>

# Conclusion

많은 개체들을 원하는 위치에 어긋나는 것 없이 깔끔하게 배치하는 것이 쉽지 않았다. 또 한글 깨짐 현상, EXIF 메타데이터, RGBA 모드, 워터마크 텍스트의 위치 좌표 계산 및 크기 조절 등 신경써야 할 부분이 너무 많아서 완성하기까지 시간이 아주 오래 걸렸다.   
또 실행 파일로 만들어서 배포하는 것도 처음 시도했는데, 코드에서 변경해야 할 부분이 많았다. 파일 경로를 모두 절대 경로로 바꿔야했고, 원본 이미지를 보여주기 위해 사용한 PILLOW 라이브러리의 `show()` 때문에 프로그램이 다시 열리는 문제가 생겨서 tkinter로 새 창을 여는 것으로 대신했다. 하지만 이번 기회를 계기로 GUI 프로그램 제작에 좀 더 익숙해질 수 있었다.

<br>

### reference

Tkinter 구현1: <https://www.youtube.com/watch?v=dcLcIa-qR8c>   
Tkinter 구현2: <https://www.youtube.com/watch?v=x6fHhNvcGjg>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}