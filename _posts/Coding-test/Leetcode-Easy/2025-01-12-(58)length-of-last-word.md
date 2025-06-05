---
excerpt: "'LeetCode: Length of Last Word' 풀이 정리"
title: "\058. Length of Last Word"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string s consisting of words and spaces, return the length of the ***last*** word in the string.

A **word** is a maximal substring consisting of non-space characters only.

*[substring]: A substring is a contiguous non-empty sequence of characters within a string.


**Example 1:**

- Input: s = "Hello World"
- Output: 5
- Explanation: The last word is "World" with length 5.


**Example 2:**

- Input: s = "&nbsp;&nbsp;&nbsp;fly&nbsp;me&nbsp;&nbsp;&nbsp;to&nbsp;&nbsp;&nbsp;the&nbsp;moon&nbsp;&nbsp;"
- Output: 4
- Explanation: The last word is "moon" with length 4.


**Example 3:**

- Input: s = "luffy is still joyboy"
- Output: 6
- Explanation: The last word is "joyboy" with length 6.


**Constraints:**

- 1 <= s.length <= 10<sup>4</sup>
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.


## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0                              # 반환할 값을 0으로 초기화

        for i in range(len(s) - 1, -1, -1):     # 맨 마지막 문자에서 맨 처음 문자까지 거꾸로 세기
            if s[i] != " ":                     # 해당 원소값이 공백이 아니면 length + 1
                length += 1
            elif s[i] == " " and length != 0:   # 해당 원소값이 공백이고 length가 이미 카운팅됐다면 반환
                return length
        return length                           # 한 단어로만 이루어진 문자열의 경우 for문 종료 후 반환
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.76** MB \| Beats **6.23%**


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/length-of-last-word/solutions/6249321/efficient-way-100-score-by-vedantwalia-xy77/" target="_blank">1st</a>

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()        # 공백을 기준으로 모든 단어를 나누기
        return len(word[-1])    # 마지막 단어 반환
```

<mark>.split()</mark> 함수로 간단하게 통과하는 방법


### <a href="https://leetcode.com/problems/length-of-last-word/solutions/5774504/video-2-solutions-bonus-by-niits-saqv" target="_blank">2nd</a>

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:                
        end = len(s) - 1        # 맨 뒤에서부터 세는 end 포인터

        while s[end] == " ":    # 원소값이 공백이 아닐 때까지 엔드 포인터를 한 칸씩 전진
            end -= 1
        
        start = end             # 문자가 나오기 시작하면 start 포인터 시작
        while start >= 0 and s[start] != " ":   # 다시 공백이 나올 때까지 스타트 포인터를 한 칸씩 전진
            start -= 1
        
        return end - start      # 엔드 포인터 인덱스에서 스타트 포인터 인덱스를 빼면 문자 길이
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)   

두 개의 포인터를 사용한 코드
<br><br>

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:                
        length = 0
        counting = False                # 지금 단어를 세고 있는지 여부

        for c in s:
            if c != " ":                # 현재 원소의 값이 공백이 아니고
                if not counting:            # 단어를 세고 있지 않으면, counting을 시작하고 length + 1
                    counting = True
                    length = 1
                else:                       # 단어를 세고 있는 중이면, 그대로 length + 1
                    length += 1
            else:
                counting = False        # 현재 원소의 값이 공백이면 counting을 멈추기
        
        return length                   # 마지막으로 counting한 단어의 길이를 반환
```

문자열 뒤가 아니라 앞에서부터 반복하는 코드이다.

찾아야 하는 단어가 문자열 앞쪽에 자리잡은 testcase가 더 많다면 이 방법이 효과적일 수도 있을 것 같은데, leetcode에서는 3ms가 걸려서 위의 코드보다 훨씬 느렸다.