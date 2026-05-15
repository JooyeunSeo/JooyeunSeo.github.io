---
date: 2025-05-19
layout: splash
excerpt: "Don’t stop, just write. Hesitation is deletion."
title: "Write or Vanish"
header:
  teaser: "https://images.unsplash.com/photo-1609967804992-c9ad515d6049?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://images.unsplash.com/photo-1609967804992-c9ad515d6049?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%EB%B6%88-%EA%B5%AC%EB%8D%A9%EC%9D%B4%EC%97%90-%EB%B6%88%ED%83%80%EB%8A%94-%EB%82%98%EB%AC%B4-jANTjqcrAQA)"
  actions:
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/write_or_vanish"
    - label: "Check the Code"
      url: "https://github.com/JooyeunSeo/Dynamic-Web-Page"  
---

# Overview
<hr>

글을 써야 하는데... 하얀 건 화면이고 검은 건 커서뿐인가요? 멍하니 모니터만 바라보며 소중한 시간을 흘려보내는 분들을 위해 준비했습니다. Write or Vanish는 여러분의 집중력을 극한까지 끌어올리는 자비 없는 글쓰기 앱입니다.

규칙은 간단합니다. 멈추지 마세요. 5초 이상 멈추는 순간 당신의 글은 영원히 사라지게 됩니다.

긴장감 넘치는 시스템 속에서 오직 타이핑에만 집중해 보세요. 유명한 Squibler의 'Dangerous Writing Prompt'에서 영감을 받아 파이썬 Flask와 바닐라 자바스크립트로 직접 구현해 보았습니다.
<br><br><br>

# System & Interface Design
<hr>

앱의 구조는 사용자의 '긴박한 경험'을 중심으로 설계되었습니다.

- **초기 상태:** 시간 설정(10초~30분) 후 Start 버튼 클릭. (이때 타임바와 입력창은 조용히 대기합니다.)
- **세션 시작:** 입력창 활성화 및 자동 포커스. 타임바가 줄어들며 운명의 카운트다운이 시작됩니다.
- **세션 진행:** 1초마다 실시간 갱신. 입력이 멈추면 경고 단계(색상 변화, 진동)를 거쳐 5초 뒤 텍스트가 삭제됩니다.
- **세션 종료:** 성공 시 글을 안전하게 보관할 수 있는 복사/공유 버튼이 나타납니다.

### Information Architecture

[![](https://mermaid.ink/img/pako:eNp1U11P2lAY_isn5xqYpXz2bs54vaiZyQ5cnNEjNIOWHEo2Z1wYQqLoYozoxgKEC7axBJMOcOEC_1B7-h_2tiA4M3vR9pw-H-_zvj0HOGOoDCs4y2kxh3Y2UjqCa8swTLLLNZMhg6NXVNdKOeT8aorONI2CwSDaZiaRQkjU-qJ3hcTXT-LLTXrF9TEv83SfhEPInlbEpWVPLeSMp85w-gR8i5XKeZPIQBhZ9niGRK8tricr9BwPzj58RyswspIWp23bqkFBPfeog4JogxtF1Xinp_9lbZuUmwTAonuBnFHNbczQYnfd1JcmXuk-fp1y4h5VRBekf9bc6xPkWE00d4dv6Ufw55xR4tY_i0bfbUDQbt3pfRfWHTC8bmp61kM8Zm0ypr6hmbfEHt3Z456XxROotxfA-f0e5VN2KdclIonJMRL9C-d0oEBhFvDFEZT458QenUG3K26rmX6CHSbSxwjwFS-Yc94C_jlyO03nsu_8mCH32wBm8D_yJtXyJOo5--XOFPQgcPUGpuZLidO-ezZA4urYqU6WjZ0PeT6KcibDSiUiar_t8a0XGjKMb0V1-AzWot27n4_bagNmFeWBxhYz-T65t_IURHcIT-e8tnCe1-LPAQlrAJ1K4wD87ZqKlT2aL7EALjBeoN4aH3gGKWzmWIGlsAKvKtujYJbCKf0QeEWqvzaMAlZMXgYmN8rZ3FKnXFSpyTY0CmepsNzlTFcZf2GUdRMrclz2RbBygN9jJZkIJSPRSDSZiMmxiBQLB_A-VqSwFIKVFI-EE_JaOC4nDgP4g2-7FvKQ0bgkxRKJZDIqxw7_AunumOc?type=png)](https://mermaid.live/edit#pako:eNp1U11P2lAY_isn5xqYpXz2bs54vaiZyQ5cnNEjNIOWHEo2Z1wYQqLoYozoxgKEC7axBJMOcOEC_1B7-h_2tiA4M3vR9pw-H-_zvj0HOGOoDCs4y2kxh3Y2UjqCa8swTLLLNZMhg6NXVNdKOeT8aorONI2CwSDaZiaRQkjU-qJ3hcTXT-LLTXrF9TEv83SfhEPInlbEpWVPLeSMp85w-gR8i5XKeZPIQBhZ9niGRK8tricr9BwPzj58RyswspIWp23bqkFBPfeog4JogxtF1Xinp_9lbZuUmwTAonuBnFHNbczQYnfd1JcmXuk-fp1y4h5VRBekf9bc6xPkWE00d4dv6Ufw55xR4tY_i0bfbUDQbt3pfRfWHTC8bmp61kM8Zm0ypr6hmbfEHt3Z456XxROotxfA-f0e5VN2KdclIonJMRL9C-d0oEBhFvDFEZT458QenUG3K26rmX6CHSbSxwjwFS-Yc94C_jlyO03nsu_8mCH32wBm8D_yJtXyJOo5--XOFPQgcPUGpuZLidO-ezZA4urYqU6WjZ0PeT6KcibDSiUiar_t8a0XGjKMb0V1-AzWot27n4_bagNmFeWBxhYz-T65t_IURHcIT-e8tnCe1-LPAQlrAJ1K4wD87ZqKlT2aL7EALjBeoN4aH3gGKWzmWIGlsAKvKtujYJbCKf0QeEWqvzaMAlZMXgYmN8rZ3FKnXFSpyTY0CmepsNzlTFcZf2GUdRMrclz2RbBygN9jJZkIJSPRSDSZiMmxiBQLB_A-VqSwFIKVFI-EE_JaOC4nDgP4g2-7FvKQ0bgkxRKJZDIqxw7_AunumOc)
<br><br><br>

# Implementation
<hr>

### Tech Stack

- **Backend:** Python, Flask, Jinja2
- **Frontend:** JavaScript(Vanilla), CSS

### Key Implementation Details

- 실시간 타임바: `elapsed / duration `비율을 계산해 CSS width를 갱신합니다. 0%가 되는 순간이 여러분의 승리입니다.
- 지능형 입력 감시: 키보드를 누를 때마다 이전의 타이머를 파괴(clearTimeout)하고 새 타이머를 예약합니다. 이 '파괴와 창조'의 반복이 앱의 핵심 엔진입니다.
- 경고 시스템: 입력이 중단되면 `rgba`의 알파값을 40씩 높여 배경을 점점 핏빛으로 물들입니다. 동시에 CSS `@keyframes`으로 화면을 흔들어(Shake) 심리적 압박을 극대화했습니다.
- Web Share API: 완성된 글은 브라우저 내장 API를 통해 모바일 등에서 즉시 외부 앱으로 공유할 수 있습니다.
<br><br><br>

# Problem Solving Process
<hr>

### Problem

분명 입력을 재개했음에도 불구하고 배경이 계속 붉게 변하거나 갑자기 화면이 흔들리는 등 경고 시스템이 오작동하고, 설정한 글쓰기 시간이 아직 남았는데도 갑자기 세션이 종료되는 문제들이 있었습니다.     
원인은 입력이 중단되었다가 다시 시작될 때 이전에 생성된 타이머가 완전히 제거되지 않은 채 백그라운드에서 계속 실행되고 있던 것이었습니다.

### Solution

새로운 입력을 감지하는 즉시, 무조건 현재 활성화된 모든 타이머 인스턴스를 초기화하는 로직을 추가했습니다. 경고 시각 효과 또한 즉시 제거하여 사용자가 다시 입력하는 순간 안전한 상태로 복귀했음을 시각적으로 보장했습니다.
<br><br><br>

# Result
<hr>

<div style="width: 80%;">{% include video id="1085417083" provider="vimeo" %}</div>
<br><br><br>

# Future Improvements
<hr>

- **사용자가 직접 타이머 시간을 설정할 수 있는 기능 추가**
- **작성 내용 자동 저장 및 복구 기능 추가**      
브라우저를 실수로 새로고침했을 때를 대비한 자동 복구
<br><br><br>

# Conclusion
<hr>

외부 라이브러리 없이 순수 자바스크립트(Vanilla JS)만으로도 이 정도의 역동적인 상호작용을 구현할 수 있다는 점이 놀라웠습니다. 특히 Web Share API나 Navigator.vibrate 같은 브라우저 내장 기능을 실습할 수 있는 기회였습니다.

단순한 도구이지만, "제약이 창의성을 만든다"는 말처럼 이 앱이 누군가의 막힌 문장력을 뚫어주는 시원한 해결사가 되길 바랍니다.
<br>

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}