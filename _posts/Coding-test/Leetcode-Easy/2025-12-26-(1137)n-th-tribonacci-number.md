---
excerpt: "'LeetCode: N-th Tribonacci Number' 풀이 정리"
title: "\01137. N-th Tribonacci Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Dynamic Programming
  - Memoization
  - Weekly Contest
  - Tribonacci Numbers
---

## <i class="fa-solid fa-file-lines"></i> Description

The Tribonacci sequence T<sub>n</sub> is defined as follows: 

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n >= 0.

Given `n`, return the value of T<sub>n</sub>.

**Example 1:**

- Input: n = 4
- Output: 4
- Explanation:     
T_3 = 0 + 1 + 1 = 2     
T_4 = 1 + 1 + 2 = 4      

**Example 2:**

- Input: n = 25
- Output: 1389537

**Constraints:**

- 0 <= n <= 37
- The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2<sup>31</sup> - 1.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0] * 38
        memo[0], memo[1], memo[2] = 0, 1, 1

        for i in range(3, n+1):
              memo[i] = memo[i-3] + memo[i-2] + memo[i-1]

        return memo[n]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.12** MB \| Beats **98.26%**    

앞 숫자들의 계산 결과를 리스트에 저장했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/n-th-tribonacci-number/solutions/345236/javacpython-easy-and-concise-by-lee215-m6f6/" target="_blank">1st</a>

```python
class Solution:
    def tribonacci(self, n):
        dp = [0, 1, 1]
        for i in xrange(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

이전 값 3개만 저장하면 되기 때문에 메모이제이션 없이 공간을 최적화하는 것도 좋은 방법이다.