---
excerpt: "'LeetCode: Prime Arrangements' 풀이 정리"
title: "\01175. Prime Arrangements"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Return the number of permutations of 1 to `n` so that prime numbers are at prime indices (1-indexed.)

*(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)*

Since the answer may be large, return the answer **modulo** `10^9 + 7`.

**Example 1:**

- Input: n = 5
- Output: 12
- Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

**Example 2:**

- Input: n = 100
- Output: 682289015

**Constraints:**

- 1 <= n <= 100

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Solve the problem for prime numbers and composite numbers separately.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Multiply the number of permutations of prime numbers over prime indices with the number of permutations of composite numbers over composite indices.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">The number of permutations equals the factorial.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_nums = 0

        for num in range(1, n+1):
            if self.is_prime(num):
                prime_nums += 1
        
        permutations = math.factorial(prime_nums) * math.factorial(n-prime_nums)
        return permutations % (10**9 + 7)


    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **1** ms \| Beats **27.72%**    
<i class="fa-solid fa-memory"></i> Memory: **17.28** MB \| Beats **96.30%**    

1부터 n까지 숫자 모두를 소수인지 판별하기 때문에 속도가 상대적으로 느리게 나왔다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python

```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂()    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂()    

### <a href="" target="_blank">2nd</a>

```python

```



{: style="color: blue;"}
<pre>

</pre>

{: style="color: green;"}

𝑛
𝑛<sup>2</sup>
log𝑛
𝑚
𝑘
𝑥
ℎ
𝑤
𝑟
𝑐