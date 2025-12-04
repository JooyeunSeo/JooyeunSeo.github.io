---
excerpt: "1009. Complement of Base 10 Integer"
title: "\0'LeetCode: Complement of Base 10 Integer' 풀이 정리"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Bit Manipulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

- For example, The integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `n`, return *its complement*.

**Example 1:**

- Input: n = 5
- Output: 2
- Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

**Example 2:**

- Input: n = 7
- Output: 0
- Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

**Example 3:**

- Input: n = 10
- Output: 5
- Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

**Constraints:**

- 0 <= n < 10<sup>9</sup>

**Note:** This question is the same as <a href="https://jooyeunseo.github.io/leetcode-easy/(476)number-complement/" target="_blank">476. Number Complement</a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">A binary number plus its complement will equal 111....111 in binary. Also, N = 0 is a corner case.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bits = n.bit_length()
        mask = (1 << bits) - 1 if bits > 1 else 1
        return n ^ mask
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.62** MB \| Beats **73.96%**    

476번과 다르게 n이 `0`인 케이스가 있어서 주의해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/complement-of-base-10-integer/solutions/256740/javacpython-find-1111111-n-by-lee215-vgm0/" target="_blank">1st</a>

```python
class Solution:
    def bitwiseComplement(self, N):
        X = 1
        while N > X:
            X = X * 2 + 1;
        return N ^ X
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

mask를 1부터 시작해서 n의 자리수만큼의 111...111 비트를 만드는 방법으로, 예외처리를 따로 하지 않아도 되서 깔끔한 것 같다.