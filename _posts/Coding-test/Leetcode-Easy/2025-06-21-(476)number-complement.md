---
excerpt: "'LeetCode: Number Complement' 풀이 정리"
title: "\0476. Number Complement"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Bit Manipulation
---

## <i class="fa-solid fa-file-lines"></i> Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

- For example, The integer `5` is `"101"` in binary and its **complement** is "010" which is the integer `2`.

Given an integer `num`, return *its complement*.

**Example 1:**

- Input: num = 5
- Output: 2
- Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

**Example 2:**

- Input: num = 1
- Output: 0
- Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

**Constraints:**

- 1 <= num < 2<sup>31</sup>

**Note:** This question is the same as <a href="https://leetcode.com/problems/complement-of-base-10-integer/description/" target="_blank">1009. Complement of Base 10 Integer</a>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bitcheck = 1

        while bitcheck <= num:
            num ^= bitcheck
            bitcheck <<= 1

        return num
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.50** MB \| Beats **8.47%**

`XOR` 연산을 활용하여 풀 수 있다. 두 입력이 서로 다르면 `1`, 같으면 `0`을 출력하기 때문에 num의 각 자리에 1을 XOR 연산하면 반대되는 비트값으로 변환된다.

num = "1010"   
bitcheck = 1
{: style="color: blue;"}
<pre>
num         1010   1011   1001   1101
bitcheck       1     10    100   1000
            ----   ----   ----   ----
            1011   1001   1101   0101
</pre>

return num = "0101"
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/number-complement/solutions/6810303/number-complement-by-ixy8n6uys3-m28f/" target="_blank">1st</a>

```python
class Solution:
    def findComplement(self, num):
        bits = num.bit_length()   # e.g. 5(101) → 3
        mask = (1 << bits) - 1    # e.g. 1000 - 1 = 111
        return num ^ mask         # e.g. 101 ^ 111 = 010
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

num의 이진수 길이만큼 1비트로 채워진 mask를 생성하는 방법으로, 반복문 없이 한 번의 연산으로 끝나기 때문에 더 빠르다는 장점이 있다. <mark>bit_length()</mark> 함수는 정수를 2진수로 표현할 때 필요한 비트 수를 리턴하기 때문에 num의 가장 높은 1비트의 위치를 알 수 있다.