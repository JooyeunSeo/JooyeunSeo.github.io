---
layout: splash
excerpt: "Add logo and text on the image"
title: "Image Watermarking App"
header:
  teaser: "https://images.unsplash.com/photo-1596369325307-cbe5dc05d4d1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://images.unsplash.com/photo-1596369325307-cbe5dc05d4d1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%EA%B0%88%EC%83%89-%EB%AA%A8%EB%9E%98%EC%97%90-%EB%B0%9C%EC%9E%90%EA%B5%AD-IxejHK_ToZA)"
  actions:
    - label: "Download Zip"
      url: "https://github.com/JooyeunSeo/JooyeunSeo.github.io/raw/main/download/!!!!!!!.zip"
---

# Intro

*100개의 프로젝트로 Python 개발 완전 정복* 부트캠프의 이번 프로젝트는 이미지에 워터마크 로고/텍스트를 추가하는 데스크톱 응용 프로그램이다. Tkinter 모듈로 그래픽 유저 인터페이스(GUI)를 생성했다.
<br><br><br>

# Design

<br><br><br>

# Implementation

### Language

파이썬으로 구현

### Coding

<br><br><br>

# Result

<br><br><br>

# Future Improvements

<br><br><br>

# Conclusion



Tkinter


Tkinter에 대해 배운 내용을 이용해서 이미지를 업로드하고 파이썬으로 워터마크 로고/텍스트를 추가할 수 있는 그래픽 유저 인터페이스(GUI) 기반 데스크톱 응용 프로그램을 만들게 됩니다.
보통은 워터마크를 추가하기 위해 Photoshop 같은 이미지 편집 소프트웨어를 사용해야 하지만 여러분의 프로그램은 그걸 자동으로 해낼 것입니다.
활용 사례: 예를 들어 여러분의 사진을 Instagram에 게시하려는데 모든 사진에 여러분의 웹사이트를 추가하고 싶습니다. 이제 여러분의 소프트웨어를 이용해서 모든 이미지에 자신의 웹사이트/로고를 자동으로 추가할 수 있습니다.
이것과 유사한 온라인 서비스도 있으니 참고하시고요. <https://watermarkly.com/>




Tkinter로 만든 데스크탑 애플리케이션은 실행 파일 형태로 변환하여 다운로드 링크로 제공할 수 있습니다. 이렇게 하면 사용자는 Python이나 Tkinter가 설치되지 않은 상태에서도 애플리케이션을 실행할 수 있습니다. 데스크탑 응용 프로그램을 만드는 과정은 크게 두 단계로 나눌 수 있습니다.

1. Python 코드 작성 (Tkinter로 UI 구현)
   - Tkinter를 사용하여 데스크탑 애플리케이션의 GUI를 개발합니다. 
   - 예를 들어, 간단한 틱택토 게임을 만들었다고 가정했을 때, 게임의 GUI(게임판, 버튼 등)를 Tkinter로 만들게 됩니다.
2. PyInstaller 또는 다른 도구로 실행 파일로 변환
   - 작성한 Python 코드(.py 파일)를 실행 파일 형태로 변환해야 합니다.
   - PyInstaller는 Python 코드(.py)를 독립 실행 파일로 변환하는 데 유용한 도구입니다.
      - Windows에서는 .exe 파일을 만들 수 있고, macOS나 Linux에서는 .app 또는 실행 가능한 파일을 만들 수 있습니다.

PyInstaller를 사용한 실행 파일 변환 방법

1. PyInstaller 설치:
    ```bash
    pip install pyinstaller  
    ```
2. Python 코드 실행 파일로 변환:
   - 터미널(또는 커맨드 라인)을 열고, Python 스크립트가 있는 디렉터리로 이동한 후 다음 명령어를 실행합니다:
    ```bash
    pyinstaller --onefile your_program.py
    ```
   - `--onefile` 옵션을 사용하면 모든 파일을 하나의 실행 파일로 묶을 수 있습니다.
3. 변환된 실행 파일 확인:
   - 변환이 끝나면 dist/ 폴더 안에 .exe(Windows) 또는 .app(macOS) 파일이 생성됩니다. 이 파일을 배포할 수 있습니다.
3. 실행 파일 배포
   - 실행 파일을 압축 파일(.zip) 형태로 만들거나, 클라우드 스토리지(Google Drive, Dropbox 등)에 업로드하여 다운로드 링크를 제공할 수 있습니다.
   - 사용자는 이 파일을 다운로드하고, 바로 실행할 수 있습니다.
4. 설치 프로그램 생성 (선택 사항)
Inno Setup 또는 NSIS 같은 도구를 사용하여 설치 프로그램을 만들면, 사용자가 실행 파일을 더 쉽게 설치하고 실행할 수 있습니다. 설치 프로그램은 프로그램을 사용자의 컴퓨터에 설치하고, 시작 메뉴에 추가하거나, 바탕 화면에 바로 가기를 만들 수 있습니다.

장점:
- Python이 설치되어 있지 않은 컴퓨터에서도 실행 가능: Python이나 Tkinter가 설치되지 않은 컴퓨터에서도 실행 파일을 바로 실행할 수 있습니다.
- 배포가 간편: 다운로드 후 바로 실행할 수 있어 설치 과정이 간단합니다.

따라서, Tkinter로 만든 데스크탑 애플리케이션을 배포하려면, Python 코드에서 실행 파일로 변환하고, 이를 다운로드할 수 있도록 제공하는 방식이 가장 효율적입니다.
