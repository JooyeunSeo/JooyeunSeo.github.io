---
date: 2025-06-03
layout: splash
excerpt: "Turn any PDF into a personal audiobook - perfect for bedtime stories or study sessions."
title: "Speak PDF"
header:
  teaser: "https://images.unsplash.com/photo-1704440286929-c5b8025d10ad?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://images.unsplash.com/photo-1704440286929-c5b8025d10ad?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%EA%B7%B8-%EC%9C%84%EC%97%90-%ED%97%A4%EB%93%9C%ED%8F%B0%EC%9D%B4-%EB%8B%AC%EB%A6%B0-%EC%B1%85-ZVAKWvq8J98)"
  actions:
    - label: "Download Zip"
      url: "https://drive.google.com/uc?id=18_vMwhoYKfEibE8E3UUI9nFXpGd3sqk7&export=download" 
---
**Note:** The file is large, so Google Drive may display a warning before download. This is normal.

---

# Intro

Speak PDF는 사용자가 선택한 PDF 파일의 텍스트를 음성으로 변환해주는 데스크탑 애플리케이션이다. 음성 변환에는 Google Cloud Text-to-Speech(TTS) API를 사용하며, 인터페이스는 Tkinter로 구성되어 있어 파일 선택, 페이지 미리보기, 음성 설정, 오디오 재생 등을 직관적으로 조작할 수 있다.
<br><br><br>

# Design

- **상단 제목 영역:** 프로그램의 제목과 부제목을 표시한다.
- **PDF 업로드:** 사용자가 PDF 파일을 열 수 있는 버튼과, 선택된 파일명을 보여주는 라벨이 있는 영역이다.
- **PDF 미리보기:** PDF의 각 페이지를 이미지로 변환하여 미리보기를 제공하며, 버튼으로 앞/뒤 페이지로 이동하며 확인할 수 있다.
- **음성 설정 영역:**
   1. 음성을 추출할 PDF 페이지 범위를 지정한다.
      - `최소` : 페이지 1, `최대` : 마지막 페이지
      - 최소 페이지 <= 최대 페이지
   2. 원하는 음성을 선택한다(옵션: 영어 남성, 영어 여성, 한국어 남성, 한국어 여성).
   3. 음성을 합성한 뒤 재생한다.
   4. 재생되는 음성을 일시정지/재개할 수 있다.
   5. 음성을 MP3 파일로 저장할 수 있다.
- **텍스트 출력 박스:** 사용자가 PDF에서 추출한 텍스트를 보여주는 영역이다.
<br><br><br>

# Implementation

### Tech Stack

- **Programming Language:** Python
- **GUI:** Tkinter
- **PDF:** PyMuPDF(fitz) and pdf2image(텍스트, 이미지 추출)
- **Audio Playback:** Pygame
- **Multithreading:** threading
- **TTS API:** Google Cloud Text-to-Speech
<br>

### Coding

-  API 연동
   - `google-cloud-texttospeech` 클라이언트 라이브러리를 통해 Google Cloud의 TTS API를 사용한다.
   - JSON 키 파일의 경로를 GOOGLE_APPLICATION_CREDENTIALS 환경 변수에 등록하는 방식으로 인증한다.   
   (유료 API이기 때문에 첨부된 파일에는 키 파일이 제외됨)
   - API 호출 시 요청(HTTP POST Request) 데이터의 구성은 다음과 같다.
      - `SynthesisInput` : 음성으로 변환할 텍스트
      - `VoiceSelectionParams` : 언어 및 목소리 종류(<a href="https://cloud.google.com/text-to-speech/docs/list-voices-and-types" target="_blank">Supported voices and languages</a>에서 모든 옵션 확인 가능)
      - `AudioConfig` : 출력 포맷(MP3)
   - 응답은 MP3 파일을 Base64로 인코딩한 문자열로 도착한다(웹을 통해 데이터를 주고받으려면 텍스트 형태가 안전하기 때문).
   - 파이썬 클라이언트가 문자열을 디코딩해서 다시 바이너리 데이터로 변환한 뒤, MP3 파일로 저장한다.
- 스레딩 (Threading)
   - PDF에서 추출한 텍스트는 매우 길고 API 호출 및 파일 쓰기 작업도 느리기 때문에 모든 것을 메인 스레드에서 실행하면 오디오가 재생된 후 텍스트가 뜨는 현상이 생긴다.
   - 문제를 해결하기 위해 Tkinter 위젯을 조작하는 부분은 메인 스레드에서 수행되고, 네트워크/API 호출과 오디오 재생은 별도의 백그라운드 스레드에서 안전하게 처리한다.
- 오디오 재생
   - Pygame의 mixer.music 모듈을 사용하여 MP3 파일을 재생한다.
   - 일시정지와 재개는 pause()와 unpause() 메서드로 구현되어 있으며, 토글 버튼을 통해 재생 상태를 시각적으로 구분할 수 있다.
- 에러 처리
   - Google TTS API 초기화 실패 시(e.g. 인증 키 누락), 콘솔에 안내 메시지를 출력한다.
   - 사용자가 잘못된 페이지 범위를 선택했을 경우(e.g. from *3* to *1*), 텍스트 출력 박스를 통해 오류 메시지를 제공한다.
<br><br><br>

# Result

<div style="width: 90%;">{% include video id="1090098376" provider="vimeo" %}</div>
<br><br><br>

# Future Improvements

- **GUI에서 오류 알림**   
API 인증 오류가 발생 시 UI 상에서 메시지 띄우기
- **정밀한 재생 제어**   
재생 바 등을 통해 재생 위치를 조정하는 기능 추가
- **파일 저장 포맷 다양화**   
MP3 외에 WAV, 또는 자막을 입힌 영상(mp4) 저장 옵션 제공하기
- **보이스 선택 시 샘플 오디오 미리 듣기 추가**
<br><br><br>

# Conclusion

이 프로그램을 개발하면서 Google Cloud TTS API를 연동해보며 클라우드 인증 과정에 대해 실습할 수 있었다. PDF에서 텍스트를 추출하기 위해 처음에는 PyPDF2 모듈을 사용했지만, 띄어쓰기가 무시되고 "thisisasentence"처럼 글자들이 붙어서 추출되는 문제가 있었다. 그래서 PDF 내부 구조를 더 정교하게 분석하는 PyMuPDF로 교체했더니 훨씬 원본에 가까운 텍스트를 얻을 수 있었다. 또한, 멀티스레딩을 적용해 음성 합성과 오디오 재생을 백그라운드에서 처리함으로써 프로그램의 안정성과 사용자 경험을 모두 향상시킬 수 있었다.
<br>

### reference

**Text-to-Speech documentation:** <https://cloud.google.com/text-to-speech/do>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}