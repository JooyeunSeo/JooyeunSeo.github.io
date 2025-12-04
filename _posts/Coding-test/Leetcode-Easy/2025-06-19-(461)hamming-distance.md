---
excerpt: "'LeetCode: Hamming Distance' 풀이 정리"
title: "\0461. Hamming Distance"
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

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return *the **Hamming distance** between them.*

**Example 1:**

- Input: x = 1, y = 4
- Output: 2
- Explanation:
    <pre>
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    </pre>
    The above arrows point to positions where the corresponding bits are different.

**Example 2:**

- Input: x = 3, y = 1
- Output: 1

**Constraints:**

- 0 <= x, y <= 2<sup>31</sup> - 1

**Note:** This question is the same as <a href="https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/" target="_blank">2220. Minimum Bit Flips to Convert Number.</a>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0

        while x != 0 or y != 0:
            if (x & 1) != (y & 1):  # x와 y의 마지막 비트가 다르면 해밍 거리에 +1
                result += 1
            x >>= 1
            y >>= 1

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.59** MB \| Beats **10.46%**

어떤 숫자와 1을 `AND` 연산하면 가장 오른쪽 비트가 0일 경우 0을, 1일 경우 1을 반환하는 원리를 이용했다. 그리고 `>>` 연산자로 오른쪽으로 1비트씩 이동하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/hamming-distance/solutions/6763094/2-lines-easy-to-follow-by-kodirjon_akhme-6rdx/" target="_blank">1st</a>

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        return bin(xor).count('1')
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log(max(𝑥+𝑦))) ← 더 큰 수의 비트 수    
<i class="fa-solid fa-memory"></i> **space complexity:** O(1)           

`XOR` 연산으로도 풀 수 있다. 두 비트가 다르면 1, 같으면 0을 반환하기 때문에 xor에는 서로 다른 비트의 위치에만 1로 표시되는 숫자가 생성된다. <mark>bin()</mark> 함수로 이 숫자를 이진 문자열로 변환한 뒤 1의 개수를 세면 된다.

### <a href="https://leetcode.com/problems/hamming-distance/solutions/6793925/simple-python-solution-beats-100-by-user-mvrz/" target="_blank">2nd</a>

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        x, y = bin(x)[2:], bin(y)[2:]

        # 길이가 짧은 쪽의 앞에 0(패딩)을 추가하여 길이 맞추기
        x = max(0,len(y)-len(x))*"0" + x
        y = max(0,len(x)-len(y))*"0" + y

        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1

        return cnt
```
비트 연산 없이 하려면 두 숫자를 이진 문자열로 변환한 뒤 인덱스 별로 비교하는 방법을 사용할 수 있다.