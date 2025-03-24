---
excerpt: "'LeetCode-Valid Phone Numbers' 풀이 정리"
title: "\0193. Valid Phone Numbers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Bash
  - Python
  - Regular Expression
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats:   
(xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

**Example:**

Assume that file.txt has the following content:

<pre>
987-123-4567
123 456 7890
(123) 456-7890
</pre>

Your script should output the following valid phone numbers:

<pre>
987-123-4567
(123) 456-7890
</pre>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```bash
grep -E '^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\)[ ][0-9]{3}-[0-9]{4}$' file.txt
```
<i class="fa-solid fa-clock"></i> Runtime: **60** ms \| Beats **84.67%**    
<i class="fa-solid fa-memory"></i> Memory: **3.49** MB \| Beats **99.41%**

<mark>grep</mark>(Global Regular Expression Print)은 파일에서 특정 패턴에 맞는 라인만 출력하는 명령어다.    
<mark>-E</mark>는 기본 정규 표현식에서 확장된 정규 표현식(Extended Regular Expression, ERE)을 사용하기 위한 옵션이다.    
**xxx-xxx-xxxx**: `^[0-9]{3}-[0-9]{3}-[0-9]{4}$`, **(xxx) xxx-xxxx**: `^\([0-9]{3}\)[ ][0-9]{3}-[0-9]{4}$`   
이고 두 패턴 중 하나만 충족하면 되기 때문에 `|`으로 연결했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-phone-numbers/solutions/6430316/valid-phone-numbers/" target="_blank">1st</a>

```bash
grep -E '^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\)[[:space:]][0-9]{3}-[0-9]{4}$' file.txt
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)            
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)          

**(xxx) xxx-xxxx** 패턴의 공백을 POSIX 문자 클래스로 표현했다. `[:space:]`는 모든 공백문자를 포함하는 표현으로, 스페이스, 탭(\\t), 개행(\\n), 캐리지 리턴(\\r), 폼 피드(\\f), 수직 탭(\\v) 등이 포함된다. 참고로 `[:blank:]`는 스페이스와 탭만 허용한다.

### <a href="" target="_blank">2nd</a>

```bash
python3 -c "
import re
with open('file.txt', 'r') as file:
    for line in file:
        if re.match(r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})', line.strip()):
            print(line.strip())
"
```
`python3 -c "파이썬 코드"`: 커맨드라인에서 (문자로 제공된)파이썬 코드 실행    
`import re`: 정규 표현식을 사용하기 위한 모듈    
`line.strip()`: 문자열의 앞뒤 불필요한 공백을 제거    
`re.match()`: 문자열이 해당 패턴에 일치하는지 확인    
`r"정규 표현식"`: 문자열 안의 이스케이프 문자를 무시하고 그대로 처리하기 위해 Raw String으로 처리