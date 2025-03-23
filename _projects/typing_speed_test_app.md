---
date: 2025-02-28
layout: splash
excerpt: "This game tests your typing speed and accuracy. <br>Type as many words as you can in 1 minute, and challenge yourself to beat your highest score."
title: "Typing Speed Test App"
header:
  teaser: "https://cdn.pixabay.com/photo/2017/03/16/10/23/hands-on-keyboard-2148723_1280.jpg"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://cdn.pixabay.com/photo/2017/03/16/10/23/hands-on-keyboard-2148723_1280.jpg
  caption: "Photo credit: [**Pixabay**](https://pixabay.com/ko/photos/%ED%82%A4%EB%B3%B4%EB%93%9C%EC%97%90-%EC%86%90-%EA%B1%B4%EB%B0%98-%EC%BB%B4%ED%93%A8%ED%8C%85-2148723/)"
  actions:
    - label: "Download zip"
      url: "https://drive.google.com/uc?id=1QZQCzXNcJ_hXPOvZedR8R_uJXghEi-bQ&export=download"
---
**Note:** The file is large, so Google Drive may display a warning before download. This is normal.

---

# Intro

*100개의 프로젝트로 Python 개발 완전 정복* 부트캠프 프로젝트로 타이핑 속도 테스트 앱을 제작했다. Tkinter로 GUI를 구축하고, Pygame을 사용하여 배경음악과 효과음을 추가했다. 게임을 시작하면 1분 카운트다운과 함께 현재 입력해야 할 단어와 그 다음에 입력할 단어가 화면에 표시된다. 프로그램은 사용자가 제한 시간 내에 입력한 단어 개수(WPM, Words Per Minute)와 정확도를 측정하며, WPM이 최고점을 갱신할 때마다 화면에 기록이 갱신되고 점수가 저장된다.
<br><br><br>

# Design

- GUI 및 UX(User Experience)
   - Tkinter 라이브러리로 GUI를 구성하며, 각 클래스마다 레이아웃(프레임)을 설정하여 필요한 기능을 분리한다.
   - 타이머
      - 게임을 시작한 순간부터 카운트다운을 시작하여 남은 시간을 실시간으로 표시한다.
      - 타이머 이미지를 함께 추가해서 시각적 요소를 제공한다.
   - 기록 업데이트
      - 한 단어를 입력할 때마다 wpm, 정확도, 총 단어 개수, 틀린 단어 개수를 실시간으로 반영하여 사용자에게 알린다.
      - 최고 WPM 점수를 갱신했을 경우 저장하여 사용자가 자신의 기록을 지속적으로 개선하도록 동기를 부여한다.
   - Pygame 라이브러리로 배경음악과 효과음 추가
      - 키를 누를 때 타이핑 효과음을 출력하여 몰입감을 상승시킨다.
      - 맞는 단어와 틀린 단어를 입력했을 때 효과음을 다르게하여 즉각적으로 피드백을 제공한다.    
      (맞는 단어를 입력하고 최고 기록도 갱신했을 때 나는 효과음도 따로 구분)
      - 시간이 5초 남았을 때부터 초침이 째깍거리는 소리를 넣어 긴장감을 더한다.
      - 시간 종료 시 타이머가 울리는 소리로 게임이 종료됐음을 인지하도록 한다.
   - 텍스트 색상 및 크기
      - 현재 입력해야하는 단어는 한 눈에 들어올 수 있도록 형광 노란색, 크고 굵은 글씨로 설정한다.
      - 다음에 입력할 단어는 회색, 작고 얇은 글씨로 설정해서 현재 단어를 방해하지 않으면서 다음 단어를 알리도록 한다.
      - 시간이 5초 남았을 때부터 타이머의 숫자를 빨간색으로 변경하여 직관적으로 경고를 한다.
- 클래스 구조
   - App: 전체 애플리케이션을 관리하는 메인 클래스이며, tkinter의 root 윈도우에 해당한다.
   - Top: 상단 UI를 구성하는 클래스로, 애플리케이션의 제목을 표시한다.
   - Records: 타이머 및 기록(WPM, 정확도, 입력한 총 단어 수, 틀린 단어 수) 관련 UI를 담당하는 클래스다.
   - HighestWPM : 사용자의 최고 기록을 저장하고 업데이트한다.
   - Typing: 이 클래스에서는 사용자가 입력해야 할 단어를 보여주고 입력을 받아서 처리한 뒤 정확성을 평가한다.
   - Setting: 게임 시작 및 강제 종료, 게임 설명 및 음량 조절 등의 설정을 다룬다.
<br><br><br>

# Implementation

### Language

파이썬

### Coding

- 타이머
   - `.after()` 함수로 1초가 지날 때마다 남은 시간, 경과 시간 및 타이머의 숫자를 갱신하고, 남은 시간이 0초가 됐을 때 게임이 종료된다.
   - 중간에 Stop 버튼으로 게임을 강제 중지할 경우 `.after_cancel()` 함수로 타이머를 멈춘다.
- `bind()`로 입력 처리
   - 단어 입력창에서 키보드의 키가 눌릴 때마다 딸깍거리는 소리를 재생하는 함수를 호출한다.
   - 단어 입력창에서 스페이스키나 엔터키를 눌렀을 때, 입력된 단어를 체크하고 처리한 후 다음 단어로 넘어가는 함수를 호출한다.
- 수치 계산
   - 남은 시간 = 기준 시간 60초(1분)에서 시작하여 1초가 지날 때마다 -1씩 감소
   - 경과 시간 = 기준 시간에서 남은 시간을 뺀 값 
   - WPM = **맞은 단어 수 /** ( **경과 시간**(초) **/ 60**(초) )
   - 정확도(%) = ( **맞은 단어 수 / 입력 단어 수** ) **\* 100**
- 텍스트 파일 읽고 쓰기
   - 게임 시작 시 텍스트 파일에 저장된 최고 기록을 불러오는 방법을 이용하여 게임을 종료해도 이전 기록을 유지할 수 있다.
   - 단어 입력 후 계산된 WPM이 텍스트 파일에 저장된 기록(초기값은 0)보다 높을 경우 파일의 내용을 갱신한다.
   - 게임에 사용되는 샘플 단어들도 텍스트 파일에서 읽어오기 때문에, 사용자가 원하는 단어를 직접 추가 및 변경할 수 있다.
- application (MacOS)
   - 애플리케이션이 패키징될 때 리소스 파일(이미지, 소리 등)의 경로가 올바르게 작동하도록 절대 경로로 변경한다.
   - 앱에서 최초로 텍스트 파일을 쓰기 모드로 열면 `'Typing Speed Test App'이(가) 데스크탑 폴더의 파일에 접근하려고 합니다.` 라는 창이 뜨면서 허용을 요구한다.   
   이것 때문에 게임을 처음 시작하고 첫 단어를 올바르게 입력하면 바로 최고 WPM이 갱신되면서 게임 도중에 창이 열리는 문제가 발생한다.    
   이 현상을 해결한 방법은 게임 구동 후 처음으로 Start 버튼을 누르면 최고 WPM 점수가 기록된 텍스트 파일을 열어서 안의 내용을 그대로 덮어쓰는 것이다.  
   타이핑을 시작하기 전에 창이 먼저 뜨기 때문에 게임을 방해하지 않으며, 이후로는 `file_access` 변수를 True로 변경하기 때문에 이 작업을 생략할 수 있다.
<br><br><br>

# Result

<div style="width: 70%;">{% include video id="1061218422" provider="vimeo" %}</div>

<br><br><br>

# Future Improvements

- **애니메이션 효과 추가**    
시각적인 효과를 주려고 노력했지만 타이핑에 집중하다보면 잘 눈에 띄지 않는 것 같다. 그래서 더욱 다양한 애니메이션 효과로 UX를 보강하려고 한다.
- **단어의 길이나 복잡도를 기준으로 게임 난이도를 조절할 수 있는 기능 추가**
- **사용자 단어 파일 추가 기능 개선**   
지금도 사용자가 텍스트 파일을 열어서 원하는 단어를 추가할 수 있지만, 애플리케이션에서 바로 엑셀, JSON 등의 파일을 첨부할 수 있다면 더욱 편리할 것이다.
<br><br><br>

# Conclusion

Pygame 라이브러리를 처음 활용했는데, 사운드 효과를 넣으니 프로그램이 더 풍부해져서 좋았다. 또 클래스 구조를 통해 체계적으로 각 레이아웃을 관리하는 방법을 익힐 수 있었다. 앞으로도 더 많은 기능에 대해 공부하고 추가해서 사용자 경험이 개선된 GUI 프로그램을 만들고 싶다.
<br>

### reference

**Tkinter 구현:** <https://www.youtube.com/watch?v=rilvj2hV-aM>    
**영어 단어 샘플:** <https://randomwordgenerator.com/>    
**배경 음악:** Music by <a href="https://pixabay.com/ko/users/sachinda4684-47311951/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=289143">sachinda shehan</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=289143">Pixabay</a>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}