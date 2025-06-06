---
excerpt: "정규 표현식 정리"
title: "Regular Expression"
header:
  teaser: "https://cdn.pixabay.com/photo/2017/09/05/10/20/business-2717066_1280.jpg"
categories:
  - Cheatsheet
tags:
  - Regular Expression
---

## Meta Symbol

| Symbol | explanation       |
|:------:|-------------------|
|  `.`   | newline 문자(\\n)를 제외한 임의의 문자 하나를 의미  |
|  `*`   | \* 앞에 있는 패턴의 0회 이상의 반복을 의미  |
|  `[]`  | [] 안에 지정된 문자 class 내의 임의의 한 문자를 의미 ([] 내의 연산자 문자는 대부분 의미 상실)<br>`-` : 문자의 범위 표시<br>`^`첫 번째에 오는 경우 여집합을 의미<br>`\` : 특수한 메타문자 또는 C 언어의 이스케이프 문자열로 간주 |
|  `^`   | 정규식 내에서 첫 문자로 사용 시 라인의 시작을 의미<br>[] 내에서는 여집합을 표현하기 위해 사용 |
|  `$`   | 정규식 내에서 첫 문자로 사용 시 라인의 끝을 의미  |
|  `{}`   | {} 직전 패턴의 반복 매칭 횟수의 범위를 지정<br>{} 내에 이름이 포함됐을 경우 변수 대체나 동적 값 삽입을 의미(Python의 문자열 포매팅, Jinja2 템플릿 언어, 쉘 스크립트 등)  |
|  `\`   | 메타기호의 의미를 없애거나 정규 표현식에서 특수한 의미를 지닌 문자를 생성<br>*e.g. `\*`는 \*의 메타 의미를 없앤 문자 자체를 나타내고, `\n`은 newline 문자를 의미*   |
|  `+`   | + 앞에 있는 패턴의 1회 이상의 반복을 의미  |
|  `?`   | ? 앞에 있는 패턴의 0회 또는 1회 반복을 의미  |
|  `|`   | \| 양쪽에 있는 좌측 패턴과 우측 패턴 중 어느 하나를 의미   |
|  `""`  | "" 내에 있는 모든 문자를 문자 그대로 해석(C 언어 이스케이프 문자열을 제외한 모든 문자는 메타 의미를 잃음)  |
|  `/`   | / 뒤에 있는 정규식까지 일치하는 경우에만 / 앞에 있는 정규식을 의미  |
|  `()`  | 일련의 정규식들을 하나의 정규식으로 그룹화    |

<br>
`+`, `?`, `{}`, `|`, `()`는 **확장 정규 표현식(Extended Regular Expressions, ERE)**에서만 사용 가능   
(기본 정규 표현식에서는 해당 기호들에 백슬래시를 추가하여 사용해야 한다)
<br>

### Meta Character

| Character  | explanation       |
|:----------:|-------------------|
|  **\\d**   | 0부터 9까지의 숫자 중 하나  |
|  **\\D**   | 숫자가 아닌 모든 문자 중 하나 |
|  **\\w**   | 알파벳, 숫자, 밑줄(_) 중 하나(`[a-zA-Z0-9_]`와 동일) |
|  **\\W**   | \\w가 아닌 모든 문자 중 하나(`[^\w]`와 동일) |
|  **\\s**   | 공백문자중 하나(`[ \t\n\r\f\v]`와 동일) |
|  **\\S**   | 공백이 아닌 문자 중 하나(`[^\s]`와 동일) |
|  **\\b**   | 단어의 경계(단어 문자와 비단어 문자가 만나는 지점)<br>경계에는 <u>단어의 시작과 끝</u>, <u>공백</u>, <u>구두점</u>(`,`, `.`, `?`, `!`, `:`, `;`, `'`, `"`), <u>구분 기호</u>(`-`, `/`) 등이 해당됨<br>*e.g. `\bword\b`는 앞뒤로 경계가 있는 'word'만 매칭*  |
|  **\\B**   | 단어 경계가 아닌 지점<br>*e.g. `\Bword\B`는 단어의 경계가 아닌 위치에 있는(단어 중간) 'word'만 찾음*  |

- 메타기호 백슬래시(\\)와 조합한 메타문자
- 확장 정규 표현식에서만 사용 가능
<br>

### C escape sequence

| Sequence     | explanation                       |
|:------------:|-----------------------------------|
| **\\a**      | Beep: 삑 소리를 출력                 |
| **\\n**      | Line feed: 줄 바꿈                  |
| **\\t**      | TAB: 다음 TAB 위치로 이동             |
| **\\b**      | Back Space: 인쇄 반대방향으로 1칸 후진  |
| **\\r**      | Carrige Return: 커서를 현재 줄의 맨 앞으로 이동 |
| **\\f**      | Form feed: 출력용지를 1페이지 전진(해당 위치에서 새 페이지로 넘어감)  |
| **\\****\\** | Backslash: \\ 출력                 |
| **\\****'**  | Apostrophe: ' 출력                 |
| **\\****''** | Quote: '' 출력                     |
| **%%**       | Percent: % 출력                   |
| **\\0**      | Null: 아무런 동작도 하지 않음          |

<br>

## useful examples

- `[0-9]`, `[0123456789]`, `\d` : 0부터 9까지의 숫자 중 하나
- `-?[0-9]+`, `-?\d+` : 정수
- `[A-Za-z0-9]` : 모든 영문자와 숫자
- `[^a-z A-Z]` : 영문자(및 공백)가 아닌 모든 문자
- `[^*]` : \*를 제외한 모든 문자
- `[\t\n]` : 공백, 탭, 개행문자 중 하나
- `[\40-\176]` : ASCII 값 40(공백)부터 176(~)까지 모든 인쇄가 가능한 문자
- `a*` : a가 0번 이상 반복될 수 있음
- `a+` : a가 한 번 이상 반복 가능
- `a.*` : a부터 한 라인의 끝까지와 일치(a로 시작하는 모든 문자열)
- `a{1, 3}` : a가 1번 이상, 3번 이하 반복(a, aa, aaa)
- `a{3}` : a가 3번 반복(aaa)
- `(ab|cd)` : ab 또는 cd
- `ab?c` : abc 또는 ac(b는 선택적)
- `ab/cd` : ab 다음에 cd가 이어서 나타날 때만 ab를 처리
- `^abc` : 라인의 시작에 abc가 나타났을 때만 abc를 처리
- `abc$`, `abc/\n` : 라인의 끝에 abc가 나타났을 때만 abc를 처리

<br><br>
<center>References</center>

1. 김강현・박두순, 『컴파일러 구성』, 한국방송통신대학교출판문화원, 2023
{: .small}
