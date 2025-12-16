---
excerpt: "'LeetCode: Greatest Common Divisor of Strings' 풀이 정리"
title: "\01071. Greatest Common Divisor of Strings"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - String
  - Weekly Contest
  - GCD
---

## <i class="fa-solid fa-file-lines"></i> Description

For two strings `s` and `t`, we say "``t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string* `x` *such that* `x` *divides both* `str1` *and* `str2`.

**Example 1:**

- Input: str1 = "ABCABC", str2 = "ABC"
- Output: "ABC"

**Example 2:**

- Input: str1 = "ABABAB", str2 = "ABAB"
- Output: "AB"

**Example 3:**

- Input: str1 = "LEET", str2 = "CODE"
- Output: ""

**Example 4:**

- Input: str1 = "AAAAAB", str2 = "AAA"
- Output: ""

**Constraints:**

- 1 <= str1.length, str2.length <= 1000
- `str1` and `str2` consist of English uppercase letters.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">The greatest common divisor must be a prefix of each string, so we can try all prefixes.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:    # ""이 되는 조건 우선 배제
            return ""
        
        k = gcd(len(str1), len(str2))     # len(str1)과 len(str2) 모두 나누는 길이 중 최대값

        return str1[:k]                   # 앞에서부터 최대 길이만큼 자르기
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.68** MB \| Beats **92.84%**    

`str1 + str2 == str2 + str1`이 성립된다면 두 문자열 길이의 최대공약수만큼 앞에서부터 자르면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/6146832/euclids-algorithm-solution-bonus-solutio-4gxf/" target="_blank">1st</a>

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[:gcd(len(str1), len(str2))]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛+𝑚)    

math 모듈 없이 직접 gcd를 구현할 수 있다.