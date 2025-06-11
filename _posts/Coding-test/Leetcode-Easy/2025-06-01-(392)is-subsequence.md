---
excerpt: "'LeetCode: Is Subsequence' 풀이 정리"
title: "\0392. Is Subsequence"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise.*

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Example 1:**

- Input: s = "abc", t = "ahbgdc"
- Output: true

**Example 2:**

- Input: s = "axc", t = "ahbgdc"
- Output: false

**Constraints:**

- 0 <= s.length <= 100
- 0 <= t.length <= 10<sup>4</sup>
- `s` and `t` consist only of lowercase English letters.

**Follow up:** Suppose there are lots of incoming `s`, say s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub> where k >= 10<sup>9</sup>, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code? 

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t or not s:     # s와 t가 같거나, s가 빈 문자열이면 무조건 True
            return True
        
        sc = 0                  # s 포인터

        for tc in t:            # t 포인터(ch)
            if tc == s[sc]:
                sc += 1

            if sc > len(s) - 1:     # sc가 s의 마지막 인덱스보다 크다면 모든 문자가 t에 있는 것
                return True
        
        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.33** MB \| Beats **94.21%**

두 개의 포인터를 사용한 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/is-subsequence/solutions/6743977/video-two-pointer-solution-by-niits-7igj/" target="_blank">1st</a>

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛) ← s나 t 중 더 긴 길이    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

좀 더 깔끔하게 작성된 코드를 참고했다.