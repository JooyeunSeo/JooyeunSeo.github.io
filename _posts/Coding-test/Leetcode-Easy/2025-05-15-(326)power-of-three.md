---
excerpt: "'LeetCode: Power of Three' 풀이 정리"
title: "\0326. Power of Three"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Bit Manipulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that n == 3<sup>x</sup>.

**Example 1:**

- Input: n = 27
- Output: true
- Explanation: 27 = 3<sup>3</sup>

**Example 2:**

- Input: n = 0
- Output: false
- Explanation: There is no x where 3<sup>x</sup> = 0.

**Example 3:**

- Input: n = -1
- Output: false
- Explanation: There is no x where 3<sup>x</sup> = (-1).

**Constraints:**

- -2<sup>31</sup> <= n <= 2<sup>31</sup> - 1

**Follow up:** Could you solve it without loops/recursion?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3
            
        return n == 1       # n이 1일 때만 True
```
<i class="fa-solid fa-clock"></i> Runtime: **8** ms \| Beats **79.30%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats **83.48%**

지난 문제 Power of Two의 경우 이진수에서 패턴이 있어서 비트 연산으로 쉽게 풀 수 있는데, 3의 거듭제곱은 패턴이 일정하지 않아서 같은 방법을 쓸 수 없었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/power-of-three/solutions/6053168/0-ms-runtime-beats-100-user-confirm-step-vxgx/" target="_blank">1st</a>

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

재귀 호출이나 반복문 없이 수학적 성질을 이용할 수 있다. 32비트 정수 범위 내에서 가장 큰 3의 거듭제곱 수는 3<sup>19</sup> = **1162261467**인 것을 활용하는 것이다.

### <a href="https://leetcode.com/problems/power-of-three/solutions/77876/a-summary-of-all-solutions-new-method-included-at-15-30pm-jan-8th/" target="_blank">2nd</a>

```java
public boolean isPowerOfThree(int n) {
    return Integer.toString(n, 3).matches("10*");
}
```
3진수에서 3의 거듭제곱 수가 가진 규칙성(모두 1 다음에 0이 여러 개 있는 형태)을 활용한 방법이다. 10진수를 3진수 문자열로 변환한 뒤 정규 표현식을 이용하여 맞는 패턴인지 확인한다.

3<sup>0</sup> =  1 →    1   
3<sup>1</sup> =  3 →   10   
3<sup>2</sup> =  9 →  100   
3<sup>3</sup> = 27 → 1000