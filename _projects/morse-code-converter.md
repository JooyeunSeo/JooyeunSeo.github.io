---
date: 2025-01-26
layout: splash
excerpt: "This converter will translate string to morse code."
title: "Morse Code Converter"
header:
  teaser: "https://www.worldhistory.org/img/r/p/1500x1500/17222.png.webp?v=1679479979-1679480090"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://www.worldhistory.org/img/r/p/1500x1500/17222.png.webp?v=1679479979-1679480090
  caption: "Photo credit: [**World History Encyclopedia**](https://www.worldhistory.org/image/17222/telegraph-morse-key/)"
  actions:
    - label: "Download Zip"
      url: "https://drive.google.com/uc?id=1RHljR59QBC3nqtZn3bR15MdO2PmU1LZo&export=download"
    - label: "Visit the Website"
      url: "https://dynamic-web-page-2bzr.onrender.com/morse_code_converter"
---

# Intro

모스 부호 변환기는 Udemy Academy의 *100개의 프로젝트로 Python 개발 완전 정복* 부트캠프에서 최종적으로 진행하는 전문 포트폴리오 프로젝트의 첫 번째 과제다. 이 프로젝트를 통해 부트캠프 초반부에 연습했던 텍스트 기반 프로그램을 직접 만들어 볼 수 있었다.   

사용자가 영어 알파벳이나 숫자로 입력한 문자열을 모스 부호로 변환하여 출력하는 간단한 프로그램으로, 여러 방법으로 실행 가능하다.

1. 파일을 다운받아서 터미널에서 실행
2. `Try now` 링크를 따라 동적 웹사이트에서 실행
<br>

<cite>Morse code</cite> - From Wikipedia
{: .small}
<a href="https://en.wikipedia.org/wiki/Morse_code" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/800px-International_Morse_Code.svg.png" width="50%" alt="morse code chart">
</a>
<br><br><br>

# Design

- 사용자의 운영체제를 확인한다.
   - 운영체제에 따라 터미널에서 화면을 지우고 커서를 맨 위로 다시 돌리는 명령어가 다르기 때문
- 딕셔너리에 모든 알파벳 및 숫자를 키로, 키에 해당하는 모스부호를 값으로 짝지어서 저장한다.
- 프로그램 루프
   1. 변환된 모스 부호를 저장하는 리스트와 허용되지 않은 문자를 저장하는 리스트를 초기화한다.
   2. 사용자에게 문자열을 입력받는다.
   3. 문자열을 공백 기준으로 단어끼리 구분한 뒤, 각 단어를 문자별로 하나씩 순회하는 것을 반복한다.
      - CLI 프로그램에서는 해당 문자가 `/`일 경우 "\n"으로 변환하여 저장
      - 해당 문자가 딕셔너리에 있는 키일 경우 모스 부호로 변환하여 저장
      - 해당 문자가 딕셔너리에 없는 키일 경우 따로 저장
   4. 변환 결과를 출력한다.
      - 모스 부호를 저장한 리스트의 모든 요소를 이어붙여서 출력
      - 각 단어 사이는 **세 칸**을 띄우고, 각 글자(모스 부호) 사이는 **한 칸**으로 띄워서 구분
      - 허용되지 않은 문자를 저장한 리스트에 요소가 있다면 모스 부호 밑에 어떤 문자들을 삭제했는지 알리는 문구를 출력
   5. CLI 프로그램에서는 사용자가 계속 이용하고 싶은지 그만하고 싶은지 확인한다.
      - 계속하기를 선택한 경우, 화면을 지우고 다시 루프 실행
      - 그만하기를 선택한 경우, 인사 메시지와 함께 루프 종료
- 웹페이지에서는 reset 버튼으로 작성한 내용을 지우고 다시 작성한 후 제출할 수 있다.
<br><br><br>

# Implementation

### Language

- Python 부트캠프를 진행 중이기 때문에 python을 메인으로 사용했다.  
- 동적 웹사이트에서 코드를 실행하기 위해 Flask, Jinja2 프레임워크와 HTML/CSS 등의 웹 개발 언어를 사용했다.

### Coding

<br>**입력 문자열 처리**

- for문으로 사용자가 입력한 문자열을 순회
- 알파벳 소문자와 대문자를 섞어서 입력해도 모두 대문자로 통일(딕셔너리 길이 절약)
- 각 라인을 구분
   - 텍스트 기반 프로그램: `/`을 `\n`으로 변환해서 저장
   - 웹페이지: 각 라인을 `splitlines()`으로 구분한 후, 한 라인의 순회가 끝날 때마다 `<br>` 추가
- 각 단어는 `.split()`으로 구분
- 각 글자는 딕셔너리에 있는 키인지 확인
   - 키일 경우, 해당 키의 값 뒤에 `" "`(1칸 공백)을 붙인 후 리스트에 추가
   - 키가 아닐 경우, 다른 리스트에 따로 추가    

처음에는 허용되지 않은 문자가 있을 경우 다시 입력하라는 메시지를 반환했는데, 직접 테스트해보니 허용되지 않는 문자가 하나만 실수로 섞여도 변환된 모스 부호를 볼 수 없는 것이 불편했다. 그래서 허용되지 않는 글자들은 그냥 무시해버리고 대신 변환된 모스 부호 밑에 어떤 문자들이 지워졌는지 알리는 식으로 변경했다.

동적 웹사이트에서 구현한 코드는 `\n` 부분을 모두 `<br>`으로 변경했다. 또 submit 버튼을 눌러 제출할 수 있기 때문에 모스 부호로 변환하는 부분을 제외하고 모두 삭제했다.
<br><br>

**Flask route에서 GET/POST 요청 처리**

1. 페이지에 접속 시 GET 요청으로 페이지 렌더링
   - URL 매개변수에서 함수의 리턴값(변환된 모스 부호)을 추출해서 화면에 출력한다.
   - 맨 처음 접속했을 때는 함수의 리턴값을 저장한 매개변수가 없기 때문에 아무것도 출력되지 않는다.
2. 사용자가 문자열을 입력하고 submit 버튼을 누르면 POST 요청으로 제출된 데이터를 처리
   - 데이터를 함수에 매개변수로 전달해서 함수를 실행하고 그 결과를 저장한다.
3. 사용자가 입력한 값과 함수의 결과를 URL 매개변수로 추가하여 GET 요청으로 리다이렉트
   - 다시 1번 과정을 실행하게 된다.
   - 이번에는 화면에 함수의 실행 결과가 출력된다.
<br><br>

**HTML template 생성**

- 사용자는 `<textarea>` form에 문자열 입력
- `submit` 버튼을 누르면 바로 옆에서 결과를 출력
- `reset` 버튼을 누르면 작성한 내용을 모두 삭제
- 리다이렉트 후에도 사용자가 form에 입력한 문자열을 유지해서 어떤 것을 입력했는지 볼 수 있도록 변경
   - Jinja2 템플릿 구문 `{%raw%}{{ user_input or '' }}{%endraw%}`을 활용했다.   
   (유저가 입력한 값이 있으면 `<textarea>`에 출력, 아니면 빈 문자열을 출력)
- 함수 실행 전에는 결과값이 None으로 출력되는 것을 아무것도 출력되지 않는 것으로 변경
   - Jinja2 템플릿 구문 `{%raw%}{% if result is not none %} ... {% endif %}{%endraw%}`을 활용   
   (실제로 함수가 실행되어 리턴값이 있을 때만 내용이 출력되고, 그 전에는 출력하지 않음)

리다이렉트 후에도 form에 입력한 문자열을 유지하니까 `reset` 버튼을 눌러도 다 지워지지 않고 전에 입력한 내용이 남아있는 문제가 새로 발생했었다. 그래서 form(id로 식별)의 모든 입력값을 초기화하는 JavaScript 스크립트를 추가하고, reset 버튼에 onclick 속성으로 해당 스크립트를 지정해서 클릭 이벤트를 처리하는 방법으로 해결했다.
<br><br><br>

# Result

### CLI Program

<img src="/assets/images/personal-projects/morse_code_converter_1.png" 
     width="80%">

<img src="/assets/images/personal-projects/morse_code_converter_2.png" 
     width="80%">
<br><br>

### Webpage

<img src="/assets/images/personal-projects/morse_code_converter_3.png" 
     width="80%">

<img src="/assets/images/personal-projects/morse_code_converter_4.png" 
     width="80%">     
<br><br><br>

# Future Improvements

- **한국어, 일본어 등 다양한 언어 추가**
- **변환된 모스 부호를 beep 음으로 재생하는 기능 추가**    
모스 부호를 소리로도 직접 들을 수 있는 기능으로, <a href="https://morsecode.world/international/translator.html" target="_blank">https://morsecode.world/international/translator.html</a>에서 아이디어를 얻었다.
<br><br><br>

# Conclusion

프로그램 자체는 매우 간단했지만, 코드를 잘 짜는 것뿐만 아니라 프로그램을 실행하는 사람의 편의를 처음으로 고려해볼 수 있는 기회였다.  
그리고 웹페이지에서 구현한 프로그램이 많이 부족하다고 느꼈다. 웹 개발에 대해서는 아직 이 부트캠프에서 간단히 배운 게 전부여서 앞으로 틈틈히 더 공부해서 보강하려고 한다.

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}
