---
excerpt: "'LeetCode-Valid Palindrome' 풀이 정리"
title: "\0125. Valid Palindrome"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Palindrome
  - Two Pointers
  - isalnum()
  - all()
  - Bitwise
  - Regular Expression
  - re.sub()
---

## <i class="fa-solid fa-file-lines"></i> Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a ***palindrome***, or `false` otherwise.

**Example 1:**

- Input: s = "A man, a plan, a canal: Panama"
- Output: true
- Explanation: "amanaplanacanalpanama" is a palindrome.

**Example 2:**

- Input: s = "race a car"
- Output: false
- Explanation: "raceacar" is not a palindrome.

**Example 3:**

- Input: s = " "
- Output: true
- Explanation: s is an empty string "" after removing non-alphanumeric characters.    
Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**

- 1 <= s.length <= 2 * 10<sup>5</sup>
- s consists only of printable ASCII characters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0           # 가장 앞 문자부터 시작
        back = len(s) - 1   # 가장 끝 문자부터 시작
        
        while front < back:
            # 모든 문자가 비문자(e.g. ".,")일 경우를 위해 front < back 조건을 또 추가해야 한다
            while front < back and not s[front].isalnum():  
                front += 1
            while front < back and not s[back].isalnum():
                back -= 1
            
            if s[front].lower() != s[back].lower():
                return False

            front += 1
            back -= 1

        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **12** ms \| Beats **77.34%**    
<i class="fa-solid fa-memory"></i> Memory: **12.75** MB \| Beats **80.29%**

두 개의 포인터와 <mark>isalnum()</mark>(알파벳 대소문자 또는 숫자일 때만 True를 반환)을 사용했다. 문자열을 따로 저장하지 않기 때문에 공간 복잡도가 𝑂(1)이라는 장점이 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-palindrome/solutions/3864359/python-3-two-solutions-beats-99-33ms-by-tkxec/" target="_blank">1st</a>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]             # 알파벳과 숫자만 남기고 모두 소문자로 변환
        return all (s[i] == s[~i] for i in range(len(s)//2))  # 모든 요소가 True일 경우에만 True를 반환
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)   

<mark>~</mark> 연산자와 <mark>all()</mark>을 활용한 답안을 참고했다. **~i**는 **-(i+1)**과 같은 값이 되기 때문에 리스트의 인덱스로 넣을 경우 끝에서부터 i번째 요소를 가져오게 된다.

<pre>
~0  →  -(0 + 1)  →  -1
~1  →  -(1 + 1)  →  -2
~2  →  -(2 + 1)  →  -3
~3  →  -(3 + 1)  →  -4
</pre>

### <a href="https://leetcode.com/problems/valid-palindrome/solutions/6170976/video-transforming-the-input-string-by-n-8qyj/" target="_blank">2nd</a>

```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]  
```
isalnum()처럼 간편한 함수를 사용하지 못할 경우를 대비한 답안도 참고했다. <mark>정규 표현식</mark>(regular expression)과 <mark>re.sub()</mark>를 활용했으며, 이 함수는 문자열에서 정규식 패턴을 찾아서 다른 문자로 치환한다. 문자열을 새로 만들기 때문에 𝑂(𝑛)의 추가 공간을 사용한다.

<div class="notice--info" markdown="1">
💡 **[^a-zA-Z0-9]**

- `[]` : 문자 클래스([] 안에 포함된 문자 중 하나라도 일치하면 매칭됨)
- `a-z` : a부터 z
- `A-Z` : A부터 Z
- `0-9` : 0부터 9
- `^` : 부정(캐럿이 [] 내부에서 맨 앞에 있으면 *이 문자를 제외한 모든 문자* 를 의미)

→ 알파벳(a-z, A-Z)과 숫자(0-9)를 제외한 모든 문자를 의미
</div>