---
excerpt: "'LeetCode: Divide Two Integers' 풀이 정리"
title: "\029. Divide Two Integers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Math
  - Bit Manipulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two integers dividend and divisor, divide two integers **without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return *the **quotient** after dividing* `dividend` *by* `divisor`.

**Note:** Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: [−2<sup>31</sup>, 2<sup>31</sup> − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 2<sup>31</sup> - 1, and if the quotient is **strictly less than** -2<sup>31</sup>, then return -2<sup>31</sup>.

**Example 1:**

- Input: dividend = 10, divisor = 3
- Output: 3
- Explanation: 10/3 = 3.33333.. which is truncated to 3.

**Example 2:**

- Input: dividend = 7, divisor = -3
- Output: -2
- Explanation: 7/-3 = -2.33333.. which is truncated to -2.

**Constraints:**

- -2<sup>31</sup> <= dividend, divisor <= 2<sup>31</sup> - 1
- divisor != 0

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX, MIN = 2 ** 31 - 1, -2 ** 31
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1  # 부호
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            max_divisor = divisor   # 현재 뺄 수 있는 가장 큰 수
            mul = 1                 # 1, 2, 4, 8...
            while dividend >= (max_divisor << 1): 
                max_divisor <<= 1   # 2배씩 키우기
                mul <<= 1
            dividend -= max_divisor
            result += mul
        
        result = sign * result
        if result > MAX:
            return MAX
        elif result < MIN:
            return MIN
        else:
            return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.36** MB \| Beats **57.95%**    

dividend에서 divisor를 뺀 횟수를 몫으로 만들 수 있다. 다만 반복해서 divisor씩 빼는 것은 너무 느려서 시간 초과가 뜨기 때문에 한 번에 많은 수를 빼야 한다. 곱셈을 사용할 수 없기 때문에 비트 연산으로 divisor 값을 2배씩 키우며 뺄 수 있는 한 최대한 키우는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/divide-two-integers/solutions/142849/cjavapython-should-not-use-long-int-by-l-bb5h/" target="_blank">1st</a>

```python
class Solution:
    def divide(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

여기서는 반대로 dividend를 줄여가면서 비교하는 방법을 썼다. 또 범위 체크도 실제로 오버플로가 일어나는 경우의 수는 `dividend = -2147483648`이고 `divisor = -1`인 1가지 밖에 없기 때문에 더 간단하게 할 수 있다.