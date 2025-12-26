---
excerpt: "'LeetCode: Fibonacci Number' 풀이 정리"
title: "\0509. Fibonacci Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Dynamic Programming
  - Recursion
  - Memoization
  - Fibonacci Numbers
---

## <i class="fa-solid fa-file-lines"></i> Description

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

> F(0) = 0, F(1) = 1   
> F(n) = F(n - 1) + F(n - 2), for n > 1.

Given `n`, calculate `F(n)`.

**Example 1:**

- Input: n = 2
- Output: 1
- Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

**Example 2:**

- Input: n = 3
- Output: 2
- Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

**Example 3:**

- Input: n = 4
- Output: 3
- Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

**Constraints:**

- 0 <= n <= 30

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0: 0, 1: 1}   # F(0) = 0, F(1) = 1 먼저 저장
        return self.recursion(n, memo)

    def recursion(self, n, memo):
        if n not in memo:
            memo[n] = self.recursion(n-1, memo) + self.recursion(n-2, memo)
        return memo[n]
```
<i class="fa-solid fa-clock"></i> Runtime: **13** ms \| Beats **81.45%**    
<i class="fa-solid fa-memory"></i> Memory: **12.30** MB \| Beats **98.42%**

재귀 호출과 메모이제이션을 이용한 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/fibonacci-number/solutions/6032855/0-ms-runtime-beats-100-user-step-by-step-rnht/" target="_blank">1st</a>

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛) ← 2부터 n까지 n-1번 반복   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)        

재귀 호출 대신 0과 1부터 시작해서 반복적으로 계산하는 방법도 효율적이다.

### <a href="https://leetcode.com/problems/fibonacci-number/solutions/4586217/5-different-approach-full-explained-java-b4lh/" target="_blank">2nd</a>

```python
class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5 ** 0.5                                        # √5 계산
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n  # ϕ^n - ψ^n
        return round(fibN / sqrt5)                              # √5로 나누고 반올림하여 정수 얻기
```
피보나치 수열을 비네의 공식(Binet's Formula)으로 반복문이나 재귀 없이 계산할 수 있다. 다만 n이 매우 클 경우 부동소수점 오차로 인해 결과가 틀릴 수도 있다.

<pre>
ϕ (phi) = (1 + √5) / 2 ≈ 1.618...
ψ (psi) = (1 - √5) / 2 ≈ -0.618...
</pre>

### <a href="https://leetcode.com/problems/fibonacci-number/solutions/4586217/5-different-approach-full-explained-java-b4lh/" target="_blank">3rd</a>

```python
class Solution:
    fib_nums = [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
        6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
        1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
        102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903
    ]

    def fib(self, n):
        return self.fib_nums[n]
```
32비트 부호있는 정수 범위 내에서 피보나치 수열을 저장해 놓고 인덱스로 n번째 항을 바로 조회하는 방식이다.