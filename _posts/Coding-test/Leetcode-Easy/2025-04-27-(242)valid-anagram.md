---
excerpt: "'LeetCode: Valid Anagram' 풀이 정리"
title: "\0242. Valid Anagram"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Hash Table
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`, and `false` otherwise.

*[anagram]: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

**Example 1:**

- Input: s = "anagram", t = "nagaram"
- Output: true

**Example 2:**

- Input: s = "rat", t = "car"
- Output: false

**Constraints:**

- 1 <= s.length, t.length <= 5 * 10<sup>4</sup>
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_letters = {}
        t_letters = {}
        
        for i in range(len(s)):
            if s[i] in s_letters:
                s_letters[s[i]] += 1
            else:
                s_letters[s[i]] = 1

            if t[i] in t_letters:
                t_letters[t[i]] += 1
            else:
                t_letters[t[i]] = 1

        return s_letters == t_letters
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **83.33%**    
<i class="fa-solid fa-memory"></i> Memory: **14.39** MB \| Beats **14.64%**

딕셔너리로 각 글자 수를 세고 비교하는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-anagram/solutions/6101148/video-4-solutions-by-niits-x6b2/" target="_blank">1st</a>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:    # s로 딕셔너리 생성
            counter[char] = counter.get(char, 0) + 1

        for char in t:    # t를 체크하면서 값을 하나씩 감소
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑘) ← 고유 문자 수(알파벳 소문자로 제한될 경우 26)          

딕셔너리를 하나만 만드는 방법

### <a href="https://leetcode.com/problems/valid-anagram/solutions/6101148/video-4-solutions-by-niits-x6b2/" target="_blank">2nd</a>

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        return Counter(s) == Counter(t)
```
파이썬에 문자열의 글자수를 딕셔너리처럼 세는 기능이 있다.