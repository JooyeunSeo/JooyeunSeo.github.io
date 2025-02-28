---
layout: splash
excerpt: "설명"
title: "Typing Speed Test App"
header:
  teaser: "https://cdn.pixabay.com/photo/2017/03/16/10/23/hands-on-keyboard-2148723_1280.jpg"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: https://cdn.pixabay.com/photo/2017/03/16/10/23/hands-on-keyboard-2148723_1280.jpg
  caption: "Photo credit: [**Pixabayh**](https://pixabay.com/ko/photos/%ED%82%A4%EB%B3%B4%EB%93%9C%EC%97%90-%EC%86%90-%EA%B1%B4%EB%B0%98-%EC%BB%B4%ED%93%A8%ED%8C%85-2148723/)"
  actions:
    - label: "Download Zip"
      url: "https://github.com/JooyeunSeo/JooyeunSeo.github.io/raw/main/download/!!!!!!!.zip"
---

# Intro



<br><br><br>

# Design

- GUI 및 UX(User Experience)
   - Tkinter 라이브러리로 GUI를 구성하며, 각 클래스마다 레이아웃을 설정하여 필요한 기능을 분리한다.
   - 타이머
      - 게임을 시작한 순간부터 카운트다운을 시작하여 남은 시간을 실시간으로 표시한다.
      - 타이머 이미지를 함께 추가해서 시각적 요소를 제공한다.
   - 기록 업데이트
      - 매번 단어를 입력할 때마다 wpm, 정확도, 총 단어 개수, 틀린 단어 개수를 실시간으로 반영하여 사용자에게 알린다.
      - 최고 WPM을 갱신했을 경우 저장하여 사용자가 자신의 기록을 지속적으로 개선하도록 동기를 부여한다.
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
start_timer 및 update_timer 메서드를 사용하여 타이머를 관리합니다. 타이머가 0이 될 때까지 1초마다 호출되며, 타이머가 종료되면 적절한 사운드를 재생합니다.
- 입력 처리
사용자가 입력한 텍스트의 정확성을 체크하고, 스페이스바나 Enter 키를 통해 다음 단어로 넘어가는 로직을 구현하여 직관적인 사용자 경험을 제공합니다.
- 수치 계산
   - 경과 시간 = 
   - WPM = **맞은 단어 수 /** ( **경과 시간**(초) **/ 60**(초) )
   - 정확도(%) = ( **맞은 단어 수 / 입력한 총 단어 수** ) **\* 100**
- 텍스트 파일을 읽고 쓰기
   - 게임 시작 시 텍스트 파일에 저장된 최고 기록을 불러오는 방법을 이용하여 게임을 종료해도 이전 기록을 유지할 수 있다.
   - 게임 종료 시 사용자의 WPM이 저장된 기록보다 높을 경우 텍스트 파일의 내용을 갱신한다.
   - 게임에 사용되는 샘플 단어들도 텍스트 파일에서 읽어오기 때문에, 사용자가 원하는 단어를 추가 및 변경할 수 있다.
<br><br><br>

# Result
<div style="width: 50%;">   <!-- 가로 너비를 차지할 비율 -->
    <iframe src="https://www.youtube.com/embed/fKB_bdxIbdI?start=3"
            frameborder="0" allowfullscreen>
    </iframe>
</div>

{% include video id="1061218422" provider="vimeo" %}

<br><br><br>

# Future Improvements



<br><br><br>

# Conclusion

<div style="width: 70%;">
   {% include video id="1SRJl3TDRaKR4A_j9-A_QnN77iXAjEHV3/view?usp=sharing" provider="google-drive" %}
</div>
https://drive.google.com/file/d/1SRJl3TDRaKR4A_j9-A_QnN77iXAjEHV3/view?usp=sharing

### reference

**Tkinter 구현:** <https://www.youtube.com/watch?v=rilvj2hV-aM>    
**영어 단어 샘플:** <https://randomwordgenerator.com/>    
**배경 음악:** Music by <a href="https://pixabay.com/ko/users/djartmusic-46653586/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=301284">Krzysztof Szymanski</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=301284">Pixabay</a>


자신의 타이핑 속도를 테스트하는 Tkinter GUI 데스크톱 응용 프로그램
파이썬을 이용한 GUI 응용 프로그램 구축에 대해 배운 내용과 Tkinter를 사용하여 타이핑 속도를 측정하는 데스크톱 앱을 구축해봅니다.
사용자에게 약간의 샘플 텍스트를 제공하고 사용자가 1분당 몇 단어나 타이핑할 수 있는지 검출합니다.
https://www.typing.com/blog/typing-speed/ 평균 타이핑 속도는 1분당 40단어입니다만 연습하면 1분당 100단어까지 속도를 높일 수 있어요.
웹 버전은 다음 주소에서 사용해볼 수 있습니다.
https://typing-speed-test.aoeu.eu/
시간이 남으면 타이핑 속도 테스트를 텍스트 샘플이 더 많고 최고 점수가 나타나는 타이핑 트레이너로 만들어볼 수도 있습니다. 원하는 대로 프로그램을 디자인해보세요.




