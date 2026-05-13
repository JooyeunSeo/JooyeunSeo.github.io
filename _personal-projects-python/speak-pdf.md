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
{: .small}
<br>

# Overview
<hr>

Speak PDF는 사용자가 선택한 PDF 파일의 텍스트를 음성으로 변환해주는 데스크톱 애플리케이션입니다. Google Cloud Text-to-Speech(TTS) API를 활용하여 자연스러운 음성을 생성하며, Tkinter 기반의 직관적인 인터페이스를 통해 파일 선택부터 미리보기, 음성 설정, 오디오 저장까지 한 번에 처리할 수 있도록 개발했습니다.
<br><br><br>

# System & Interface Design
<hr>

### Class Diagram

메인 App 클래스를 중심으로 기능별 프레임(Title, PDFUpload, PDFPreview, TTS)을 모듈화하여 설계했습니다.

[![](https://mermaid.ink/img/pako:eNp9VE1v4jAQ_SuWT7ALCEhCQw6VVq1WWmkPlUovq0iRwYOxmtiW7bR0Ef99baeAA9rmkDjzZt68-UgOeCMp4AJvamLMIydMk6YUyF3Bgn4ohQ6dwV_fV9zWgKy_R9anx58vqpaEIkW3VRuOffhJwxuH94Cr7hyzrp6RtSayeIbKOQ8UsbthBxxLEUvrpMTifpM11MhKVdX-dIOspbWyicEryksdMe2z1VwwtOU1VF5OBG12UhqoPDQYRnYpvPjKUwH9ooaoM71CuLGIN4RB3JNfwqJNqzUI63QwuG5XFzDoHrEas5PvIWLA6T4G_CQ6ILYK2Nue9brxblq9_igu1nKPjCX6RtkJBEGvoZXLg6xP5hxiuQrIa3A2PV1uQyriaWryMfBxvRrJG1SkpVz2YyRjYWytG5MG0za3Vfkd_zYefy5UgR6ksIQL00cvu_GFx2mY_3PxrbvGuvuFfjK5D_4FWmnOGGiDzl_D8ELn3XoZXxQlFkxvb06OXd6Th28t0kQwwCPMNKe42JLawAg3oBvi33EYcIntDhooceGOFLakrW2JS3F0cYqIP1I2uLC6dZFatmx35mlDps__ydnqNpeCfpCtsLiYL-8CCS4OeI-LdJpMlmmWZtl8OsuTLBvhD1yMZ-kkyfJ8nqSpsyZJOj-O8N-QdzrJF8kiu5vNFnm-XGbJ4vgPGhhwjA?type=png)](https://mermaid.live/edit#pako:eNp9VE1v4jAQ_SuWT7ALCEhCQw6VVq1WWmkPlUovq0iRwYOxmtiW7bR0Ef99baeAA9rmkDjzZt68-UgOeCMp4AJvamLMIydMk6YUyF3Bgn4ohQ6dwV_fV9zWgKy_R9anx58vqpaEIkW3VRuOffhJwxuH94Cr7hyzrp6RtSayeIbKOQ8UsbthBxxLEUvrpMTifpM11MhKVdX-dIOspbWyicEryksdMe2z1VwwtOU1VF5OBG12UhqoPDQYRnYpvPjKUwH9ooaoM71CuLGIN4RB3JNfwqJNqzUI63QwuG5XFzDoHrEas5PvIWLA6T4G_CQ6ILYK2Nue9brxblq9_igu1nKPjCX6RtkJBEGvoZXLg6xP5hxiuQrIa3A2PV1uQyriaWryMfBxvRrJG1SkpVz2YyRjYWytG5MG0za3Vfkd_zYefy5UgR6ksIQL00cvu_GFx2mY_3PxrbvGuvuFfjK5D_4FWmnOGGiDzl_D8ELn3XoZXxQlFkxvb06OXd6Th28t0kQwwCPMNKe42JLawAg3oBvi33EYcIntDhooceGOFLakrW2JS3F0cYqIP1I2uLC6dZFatmx35mlDps__ydnqNpeCfpCtsLiYL-8CCS4OeI-LdJpMlmmWZtl8OsuTLBvhD1yMZ-kkyfJ8nqSpsyZJOj-O8N-QdzrJF8kiu5vNFnm-XGbJ4vgPGhhwjA)

### Information Architecture

사용자 경험(UX)을 고려하여 좌측에는 시각적 정보(PDF 미리보기)를, 우측에는 기능적 제어(TTS 설정 및 텍스트 확인)를 배치했습니다.

[![](https://mermaid.ink/img/pako:eNp1U21P01AU_is395MmA8e64ugHEwNqSCRZ3PCD3UKu62UsrC_pWgQXEtRhFOZbHDpJtwwyEAyGIROXuF-0e_sfPG3HNkJs0ttz2-d5zjnPuS3ijK5QLOGsSYwllJxJaQiuhEVM64bsVkpsz-n96bD6EeLbTffL2_RNNDZ2B80beZ0ocnzmPnLLZV7rIl5quK9q6YAffPaRDyEAmA8FMfbZQaz1AfFam512-PcNxM433G_VPjFYC_bToJ55QyEWnZ9FMty91hnfbvSB3tWX9tPETbqSo89kvl_mnT0Jue-rkMLXP-2wwxN23u51Wsj95PBt5z8aj4iWpTLfbfkKyWRiVOVXhTsl6LLJGzt9PtWUlBaEPtUXSVAr0LnG9dpmP4756zLUc9WvS5KvMJ3PZZYTBiXLsr8Cv-RudZH7os0Of6YvUw5Mipt6hhYKSGatM29WtS7fbXs-860ma7yBaKTfobif696qZZKMJcfX5mywAQaE3M13QHS3OohfVPjFKLmP9pkPdD2bp2CSHESgrNuK79rd-Cxyq52r3AE-cIms0CRVDZnXSzAQpBrC4CA1Nnj9YIR5iQ3mnCdrUG2WqJQ7Xa9eXm2ySgVWxOsnfGDpyHA8TuCsrlmmni8GQMT_HkGbbK-5HuD6nwEKx7MLZcGoYX63AN5rOUF6YheobOlZ6GXB8DYLJi3YKk1fk7jSzqDpubggF-C5QGwlp0uI_3b4_iaC18PGA6lRsx_D0U7SVUseDoe1diDiXz_2x4TYyzbfPYadwxoHaRyCXzqnYGmR5As0hFVqqsTb46Inn8LWElVpCksQKnSR2HkrhVPaOvAMoj3RdRVLlmkD09Tt7NJAx_b_yJkcgbM3hIDZ1JzWbc3CUmRK8DWwVMSrWIqGhfGpqBgVxUh4IiaIYgivYWlsIjouiLFYRIhG4a0gRCPrIfzcTxsej00Kk-Lt8JQQmxCioiCu_wNzafHr?type=png)](https://mermaid.live/edit#pako:eNp1U21P01AU_is395MmA8e64ugHEwNqSCRZ3PCD3UKu62UsrC_pWgQXEtRhFOZbHDpJtwwyEAyGIROXuF-0e_sfPG3HNkJs0ttz2-d5zjnPuS3ijK5QLOGsSYwllJxJaQiuhEVM64bsVkpsz-n96bD6EeLbTffL2_RNNDZ2B80beZ0ocnzmPnLLZV7rIl5quK9q6YAffPaRDyEAmA8FMfbZQaz1AfFam512-PcNxM433G_VPjFYC_bToJ55QyEWnZ9FMty91hnfbvSB3tWX9tPETbqSo89kvl_mnT0Jue-rkMLXP-2wwxN23u51Wsj95PBt5z8aj4iWpTLfbfkKyWRiVOVXhTsl6LLJGzt9PtWUlBaEPtUXSVAr0LnG9dpmP4756zLUc9WvS5KvMJ3PZZYTBiXLsr8Cv-RudZH7os0Of6YvUw5Mipt6hhYKSGatM29WtS7fbXs-860ma7yBaKTfobif696qZZKMJcfX5mywAQaE3M13QHS3OohfVPjFKLmP9pkPdD2bp2CSHESgrNuK79rd-Cxyq52r3AE-cIms0CRVDZnXSzAQpBrC4CA1Nnj9YIR5iQ3mnCdrUG2WqJQ7Xa9eXm2ySgVWxOsnfGDpyHA8TuCsrlmmni8GQMT_HkGbbK-5HuD6nwEKx7MLZcGoYX63AN5rOUF6YheobOlZ6GXB8DYLJi3YKk1fk7jSzqDpubggF-C5QGwlp0uI_3b4_iaC18PGA6lRsx_D0U7SVUseDoe1diDiXz_2x4TYyzbfPYadwxoHaRyCXzqnYGmR5As0hFVqqsTb46Inn8LWElVpCksQKnSR2HkrhVPaOvAMoj3RdRVLlmkD09Tt7NJAx_b_yJkcgbM3hIDZ1JzWbc3CUmRK8DWwVMSrWIqGhfGpqBgVxUh4IiaIYgivYWlsIjouiLFYRIhG4a0gRCPrIfzcTxsej00Kk-Lt8JQQmxCioiCu_wNzafHr)

- **PDF 업로드 및 미리보기:** `pdf2image`를 통해 PDF 페이지를 이미지로 렌더링하여 사용자에게 시각적 피드백을 제공합니다.
- **음성 설정:** 페이지 범위 지정, 4가지 음성 옵션(한/영, 남/여) 선택, 재생 및 일시정지 기능을 제공합니다.
- **텍스트 출력:** PDF에서 추출된 원문 텍스트를 실시간으로 확인할 수 있습니다.
<br><br><br>

# Implementation
<hr>

### Tech Stack

**Language:** Python
**GUI:** Tkinter
**PDF Processing:** PyMuPDF(fitz), pdf2image
**Audio:** Pygame
**API:** Google Cloud TTS (Wavenet voice)
**Concurrency:** Threading
<br>

### Key Implementation Details

- Google TTS API 연동: SynthesisInput, VoiceSelectionParams를 설정하여 요청을 보내고, 응답으로 받은 바이너리 데이터를 MP3 파일로 저장하여 재생합니다.
- 멀티스레딩(Multithreading): 네트워크 통신과 오디오 재생은 시간이 소요되는 작업입니다. 이를 메인 스레드에서 처리하면 UI가 멈추는(Freeze) 현상이 발생하므로, threading 모듈을 사용하여 백그라운드에서 처리하도록 구현했습니다.
- 오디오 제어: `pygame.mixer`를 활용해 재생 상태를 추적하고, 하나의 버튼으로 일시정지(Pause)와 재개(Resume)를 전환하는 토글 로직을 구현했습니다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem

일부 PDF에서 텍스트를 추출하는 과정에서 단어 사이의 공백이 사라지고 "ThisIsExample"처럼 글자가 붙어서 추출되는 현상이 발생했습니다.

### Solution

PyPDF2 대신 PDF의 내부 레이아웃을 더 정교하게 분석하는 PyMuPDF(fitz)로 라이브러리를 교체했습니다. `page.get_text()` 메서드를 통해 줄바꿈과 공백이 보존된 고품질의 텍스트를 얻을 수 있었습니다.
<br><br><br>

# Result
<hr>

<div style="width: 90%;">{% include video id="1090098376" provider="vimeo" %}</div>
<br><br><br>

# Future Improvements
<hr>

- **GUI에서 오류 알림**   
API 인증 오류가 발생 시 UI 상에서 메시지 띄우기
- **정밀한 재생 제어**   
재생 바 등을 통해 재생 위치를 조정하는 기능 추가
- **파일 저장 포맷 다양화**   
MP3 외에 WAV, 또는 자막을 입힌 영상(mp4) 저장 옵션 제공하기
- **보이스 선택 시 샘플 오디오 미리 듣기 추가**
<br><br><br>

# Conclusion
<hr>

이번 프로젝트를 통해 Google Cloud API의 인증 체계와 클라이언트-서버 간의 데이터 주고받는 과정을 깊이 있게 이해할 수 있었습니다. 특히 GUI 프로그램에서 사용자 경험을 결정짓는 핵심은 '응답성'이라는 것을 깨달았으며, 이를 위해 멀티스레딩을 적재적소에 활용하는 법을 익혔습니다. 앞으로는 더 복잡한 문서 구조(표, 이미지 내 텍스트 등)도 정확히 인식할 수 있도록 OCR 기능을 추가해보고 싶습니다.
<br>

### reference

**Text-to-Speech documentation:** <https://cloud.google.com/text-to-speech/do>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}