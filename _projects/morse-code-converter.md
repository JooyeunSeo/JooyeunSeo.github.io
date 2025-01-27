---
layout: splash
excerpt: "This converter will translate string to morse code"
title: "Morse Code Converter"
header:
  teaser: "https://www.worldhistory.org/img/r/p/1500x1500/17222.png.webp?v=1679479979-1679480090"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://www.worldhistory.org/img/r/p/1500x1500/17222.png.webp?v=1679479979-1679480090
  caption: "Photo credit: [**World History Encyclopedia**](https://www.worldhistory.org/image/17222/telegraph-morse-key/)"
  actions:
    - label: "Download Zip"
      url: "https://github.com/JooyeunSeo/JooyeunSeo.github.io/raw/main/download/Morse_Code_Converter.zip"
    - label: "Try now"
      url: "https://dynamic-web-page-2bzr.onrender.com/morse_code_converter"
---

# Intro

모스 부호 변환기는 Udemy Academy의 *100개의 프로젝트로 Python 개발 완전 정복* 부트캠프에서 최종적으로 진행하는 전문 포트폴리오 프로젝트의 첫 번째 과제다.
과제를 통해 부트캠프 초반부에 연습했던 텍스트 기반 프로그램을 직접 만들어 볼 수 있었다.

사용자가 텍스트를 입력하면 이를 모스 부호로 변환하는 간단한 프로그램으로, 두 가지 방법으로 준비했다.

- 파일을 다운받아서 터미널에서 실행
- 파일 다운로드 없이 동적 웹사이트에서 실행
<br><br><br>

# Implementation

### 기술 스택

Python 부트캠프를 진행 중이기 때문에 python을 메인으로 사용했다.  
동적 웹사이트에서 코드를 실행하기 위해 추가적으로 Flask, Jinja2 프레임워크와 HTML/CSS 등의 웹 개발 언어를 사용했다.

### 함수 작성

<cite>Morse code</cite> - From Wikipedia
{: .small}
<a href="https://en.wikipedia.org/wiki/Morse_code" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/800px-International_Morse_Code.svg.png" width="50%" alt="morse code chart">
</a>

파이썬 딕셔너리에 모든 알파벳 및 숫자와 모스 부호를 짝지어서 저장하고 for문에서 입력한 문자열을 하나씩 순회하며 딕셔너리의 키와 일치하는지 확인하는 방법을 썼다. 알파벳 순서와 모스 부호 간에 통일성이나 패턴이 크게 있지 않아서 이 방법이 가장 적합하다고 생각했다. 

이후 아래와 같이 여러 가지 경우를 고려해서 코드를 발전시켰다.

1. 알파벳 소문자와 대문자를 섞어서 입력해도 모두 **대문자로 통일**(딕셔너리 길이 절약)
2. 각 글자 사이는 **한 칸**씩 띄워서 구분, 각 단어 사이는 **세 칸**씩 띄워서 구분, `/`는 줄바꿈으로 인식
   1. `.split()`으로 단어끼리 구분
   2. `/`은 `\n`으로 변환해서 저장
   3. `/`가 아닌 글자는 딕셔너리에 있는 키일 경우 해당 키의 값에 `" "`(1칸 공백) 추가한 결과 저장
3. **허용되지 않은 문자**(한글, 특수문자 등) 입력 시 무시하고 어떤 문자가 삭제됐는지 알리는 메시지를 변환 결과와 함께 출력
4. 계속 프로그램을 이용할지 묻고, y를 입력할 경우 터미널을 지우고 맨 위부터 새로 출력

3번의 경우 처음에는 알파벳이나 숫자 외의 문자를 입력하면 다시 입력하라는 메시지를 반환했는데, 직접 테스트해보니 허용되지 않는 문자가 하나만 실수로 섞여도 다시 입력하라는 결과만 뜨는게 불편하다고 느꼈다. 그래서 허용되지 않는 글자들은 그냥 무시해버리고 대신 변환된 모스 부호 밑에 어떤 문자들이 지워졌는지 알리는 식으로 변경했다.

동적 웹사이트에서 구현한 코드는 텍스트 기반 프로그램의 코드에서 조금 변경했다.

- `\n`을 `<br>`으로 변경
- 사용자가 엔터키로 줄바꿈한 부분을 `.splitlines()` 함수로 분할
- 버튼을 눌러 제출할 수 있기 때문에 str_to_morse 함수 외 모두 삭제
<br>

### Flask 라우트 설계

웹페이지에서 접속해서 양식에 문자열을 입력하고 변환하는 과정에서 일어나는 GET/POST 요청은 다음과 같다.

1. 페이지에 접속 시 GET 요청으로 페이지 렌더링
   - URL 매개변수에서 함수의 리턴값(변환된 모스 부호)을 추출해서 화면에 출력
   - 맨 처음 접속했을 때는 함수의 리턴값을 저장한 매개변수가 없기 때문에 아무것도 출력되지 않은 상태
2. 사용자가 문자열을 입력하고 submit 버튼을 누르면 POST 요청으로 제출된 데이터를 처리
   - 데이터를 함수에 매개변수로 전달해서 함수를 실행하고 그 결과를 저장
3. 사용자가 입력한 값과 함수의 결과를 URL 매개변수로 추가하여 GET 요청으로 리다이렉트
   - 다시 1번 과정 실행
   - 이번에는 화면에 함수의 실행 결과가 출력됨
<br>

### HTML 템플릿 설계

`<textarea>` form 안에 문자열을 입력한 후 `submit` 버튼을 누르면 바로 옆에서 결과를 출력하도록 했다. `reset` 버튼을 누를 경우 작성한 내용을 모두 지울 수 있다.

개선하고자 했던 부분은 다음과 같다. 

1. 리다이렉트 후에도 사용자가 form에 입력한 문자열을 유지해서 어떤 것을 입력했는지 볼 수 있게 하기
   - Jinja2 템플릿 구문 `{%raw%}{{ user_input or '' }}{%endraw%}` 활용
   - 유저가 입력한 값이 있으면 `<textarea>`에 출력, 아니면 빈 문자열 출력
2. 함수 실행 전에는 결과값이 None으로 출력되는 것을 아무것도 출력되지 않는 것으로 변경하기
   - Jinja2 템플릿 구문 `{%raw%}{% if result is not none %} ... {% endif %}{%endraw%}` 활용
   - 실제로 함수가 실행되어 리턴값이 있을 때만 내용이 출력되고, 그 전에는 빈 상태로 나타남
3. 1번에서처럼 form에 입력한 문자열을 유지하니까 `reset` 버튼을 눌러도 다 지워지지 않고 전에 입력한 내용이 남아있는 문제가 새로 발생 
   - JavaScript로 해당 form(id로 식별)의 모든 입력값을 초기화하는 스크립트 작성
   - reset 버튼에 onclick 속성으로 JavaScript 코드를 지정해서 클릭 이벤트를 처리
<br><br><br>

# Result

### 터미널

<img src="/assets/images/personal-projects/morse_code_converter_1.png" 
     width="80%">

<img src="/assets/images/personal-projects/morse_code_converter_2.png" 
     width="80%">
<br><br>

### str_to_morse 함수 (웹)

<img src="/assets/images/personal-projects/morse_code_converter_3.png" 
     width="80%">

<img src="/assets/images/personal-projects/morse_code_converter_4.png" 
     width="80%">     
<br><br><br>

# Lessons Learned

파이썬에서 문자열을 다루는 방법을 익힐 수 있었다. 또 웹사이트에서 파이썬 코드를 구현하기 위해 많이 찾아보고 배우게 됐다. Flask의 GET/POST 요청에 대해 더 깊게 이해하고 Jinja2 템플릿에서 동적인 데이터와 HTML를 처리해볼 수 있었다.
<br><br><br>

# Future Improvements

지금은 알파벳과 숫자만 지원하고 있지만, 한글이나 일본어를 모스 부호로 번역하는 프로그램으로 발전시켜보고 싶다. 또 추가하고 싶은 기능은 변환된 모스 부호를 beep 음으로 재생하는 것이다. <a href="https://morsecode.world/international/translator.html" target="_blank">https://morsecode.world/international/translator.html</a>에서 아이디어를 얻었다.

그리고 동적 웹사이트에서 구현한 코드의 경우 현재는 문자열을 입력하고 제출 버튼을 누르면 결과가 뜨는 방식이다. 더 나아가서 입력을 하면 바로 변환 결과를 보여주는 동적 기능을 넣으면 훨씬 좋은 프로그램이 될 것 같다. Ajax를 사용하면 된다고 하는데 나중에 JavaScript에 대해 배우게 되면 이 부분을 업데이트하려고 한다. 
<br><br><br>

# Conclusion

프로그램 자체는 매우 간단했지만, 코드를 잘 짜는 것뿐만 아니라 프로그램을 실행하는 사람의 편의를 처음으로 고려해볼 수 있는 기회였다.  
그리고 웹페이지에서 구현한 프로그램이 많이 부족하다고 느꼈다. 웹 개발에 대해서는 아직 이 부트캠프에서 간단히 배운 게 전부여서 앞으로 틈틈히 더 공부해서 보강하려고 한다.


