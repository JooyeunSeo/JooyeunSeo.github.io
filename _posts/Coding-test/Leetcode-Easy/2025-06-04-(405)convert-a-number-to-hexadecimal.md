---
excerpt: "'LeetCode: Convert a Number to Hexadecimal' 풀이 정리"
title: "\0405. Convert a Number to Hexadecimal"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Bitwise
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a 32-bit integer `num`, return *a string representing its hexadecimal representation*. For negative integers, <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">two’s complement</a> method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

**Note:** You are not allowed to use any built-in library method to directly solve this problem.

**Example 1:**

- Input: num = 26
- Output: "1a"

**Example 2:**

- Input: num = -1
- Output: "ffffffff"

**Constraints:**

- -2<sup>31</sup> <= num <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        hex_map = "0123456789abcdef"
        # num이 음수일 경우 AND 연산으로 하위 32비트만 남기기 위한 마스크
        # 11111111111111111111111111111111(2) → FFFFFFFF(16)
        mask = 0xFFFFFFFF   

        # 음수 처리
        if num < 0:
            num &= mask

        # 10 → 16진수
        result = ""
        while num > 0:
            digit = num % 16
            result = hex_map[digit] + result
            num //= 16

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.29** MB \| Beats **99.57%**

음의 정수는 앞에 부호로 1을 붙이는데, 파이썬 내부에서는 정수에 비트 수 제한이 없기 때문에 1이 무한대가 된다. 따라서 하위 32비트를 잘라줘야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/convert-a-number-to-hexadecimal/solutions/6723211/easy-solutionbeats-100easy-to-understand-slzc/" target="_blank">1st</a>

```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32 
        hex_con = hex(num)[2:]
        return hex_con
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)        

음수를 32비트 unsigned 정수처럼 변환하기 위한 쉬운 방법이 있어서 참고했다. 32비트 부호 없는 정수 최대 범위인 `2**32`에 음수 정수를 더하는 것이다.