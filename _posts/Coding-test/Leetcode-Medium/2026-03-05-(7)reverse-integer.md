---
excerpt: "'LeetCode: Reverse Integer' 풀이 정리"
title: "\07. Reverse Integer"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Math
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

- Input: x = 123
- Output: 321

**Example 2:**

- Input: x = -123
- Output: -321

**Example 3:**

- Input: x = 120
- Output: 21

**Constraints:**

- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1   # 부호 저장
        x = abs(x)                  # 양수로 계산
        rev = 0                     # 뒤집은 숫자 저장

        while x != 0:
            digit = x % 10
            x //= 10
            if rev > (2 ** 31 - 1) // 10:   # 범위 넘어가는지 먼저 체크
                return 0
            rev = rev * 10 + digit

        rev *= sign                         # 부호 적용

        return rev
```
<i class="fa-solid fa-clock"></i> Runtime: **37** ms \| Beats **92.94%**    
<i class="fa-solid fa-memory"></i> Memory: **19.38** MB \| Beats **30.54%**    

overflow를 처리하는 것이 중요한 문제다. rev에 10을 곱해서 다음 자리로 넘어간 값이 최대값을 넘어갈 수 있기 때문에 먼저 범위를 체크해야한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-integer/solutions/7555429/easy-peasy-lemon-squezzy-solution-for-re-hfve/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Handle the sign and reverse the digits using string slicing
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * sign
        
        # Step 2: Check for 32-bit integer overflow
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(log𝑛)    

파이썬에서는 문자열로 바꾸면 더 간단하다.