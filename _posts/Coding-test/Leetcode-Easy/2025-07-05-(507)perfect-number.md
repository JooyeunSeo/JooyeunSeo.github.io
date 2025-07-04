---
excerpt: "'LeetCode: Perfect Number' 풀이 정리"
title: "\0507. Perfect Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
---

## <i class="fa-solid fa-file-lines"></i> Description

A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank">**perfect number**</a> is a **positive integer** that is equal to the sum of its positive divisors, excluding the number itself. A **divisor** of an integer `x` is an integer that can divide `x` evenly.

Given an integer `n`, return `true` *if* `n` *is a perfect number, otherwise return* `false`.

**Example 1:**

- Input: num = 28
- Output: true
- Explanation: 28 = 1 + 2 + 4 + 7 + 14   
1, 2, 4, 7, and 14 are all divisors of 28.

**Example 2:**

- Input: num = 7
- Output: false

**Constraints:**

- 1 <= num <= 10<sup>8</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:        # num이 1일 경우 제외
            return False
        
        total = 1           # 1은 항상 약수이기 때문에 포함

        for i in range(2, (int(num**0.5)+1)):   # 약수 i는 √num 까지만 확인
            if num % i == 0:
                total += i
                if i != num // i:               # 중복된 약수(e.g. 4*4=16)는 한 번만 적용
                    total += num // i

        return total == num
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **87.16%**    
<i class="fa-solid fa-memory"></i> Memory: **12.77** MB \| Beats **23.85%**

완전수는 자기 자신을 제외한 양의 약수를 모두 더한 값이므로, 약수를 찾을 때마다 그 쌍을 더해가며 계산한다.

num = 36
{: style="color: blue;"}
<pre>
total   i    new total
1       2     1 + (2+18) = 21
21      3    21 + (3+12) = 36
36      4    36 + (4+9)  = 49
        5
49      6    49 + (6)    = 55
</pre>

return False
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/perfect-number/solutions/6664352/beginner-friendly-master-the-divisor-tri-pbv7/" target="_blank">1st</a>

```python
class Solution(object):
    def checkPerfectNumber(self, num):
        if num < 2: return False
        s = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num // i
            i += 1
        return s == num
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(√𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

int(num**0.5) 수식 없이 푸는 방법이다.

### <a href="https://leetcode.com/problems/perfect-number/solutions/3326058/one-line-of-code-python-two-approaches-b-xn09/" target="_blank">2nd</a>

```python
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]
```
10<sup>8</sup> 까지의 숫자 중에서 오직 5개의 완전수만 존재하기 때문에 그 값을 알 경우 사용할 수 있는 방법이다.