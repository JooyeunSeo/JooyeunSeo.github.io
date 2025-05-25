---
excerpt: "'LeetCode: Valid Perfect Square' 풀이 정리"
title: "\0367. Valid Perfect Square"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Search
  - Bitwise
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a positive integer num, return `true` *if `num` is a perfect square or* `false` *otherwise*.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

**Example 1:**

- Input: num = 16
- Output: true
- Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

**Example 2:**

- Input: num = 14
- Output: false
- Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

**Constraints:**

- 1 <= num <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        result = num
        while result * result > num:
            result = (result + (num // result)) // 2    # 갱신식
        
        return result * result == num   # result를 거듭제곱한 값이 정확히 num이면 True
```

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2   

            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.40** MB \| Beats **51.51%**

첫 번째 코드는 **Newton-Raphson(뉴턴-랩슨)** 방식으로, 갱신식을 반복하며 거듭제곱 시 num 또는 num에 가장 근접해지는 자연수를 찾는다.   
두 번째 코드는 **이진 탐색** 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-perfect-square/solutions/130010/python-4-methods-with-time-testing-by-ge-h86q/" target="_blank">1st</a>

```python
class Solution(object):
    def isPerfectSquare(self, num):
        i = 1   # 1부터 시작해서 2씩 더해지는 변수(1, 3, 5...)
        while (num>0):
            num -= i
            i += 2       
        return num == 0
```
하나 이상의 연속된 홀수의 합(1, 1+3, 1+3+5...)인 수는 완전 제곱수라는 것을 활용한 방법이다.       

### <a href="" target="_blank">2nd</a>

```python
class Solution(object):
    def isPerfectSquare(self, num):
      root = 0          # num의 제곱근을 추정해가는 값
      bit = 1 << 15     # 가장 큰 자리 비트(2^15 = 32768)부터 하나씩 내려가는 역할
       
       while bit > 0 :
           root |= bit              # OR 연산으로 비트를 더해봤을 때
           if root > num // root:     # root가 너무 커진다면 
               root ^= bit              # XOR 연산으로 더했던 비트를 다시 되돌림    
           bit >>= 1                  # 다음 작은 자리수 비트로 내려감
       return root * root == num
```
비트 연산을 사용하여 빠르고 가볍게 구할 수 있다.

num = 16   
root = 0   
bit = 32768
{: style="color: blue;"}

| Step | bit (2ⁿ) | `root |= bit` | `root > num // root` | `^= bit` 여부 | 최종 root |
|------|----------|----------------|----------------------|------------|----------|
| 1 | 32768 | 32768 | 32768 > 0 → True | 비트 끔 | 0 |
| 2 | 16384 | 16384 | 16384 > 0 → True | 비트 끔 | 0 |
| 3 | 8192 | 8192 | 8192 > 0 → True | 비트 끔 | 0 |
| ... | ... | ... | ... | ... | ... |
| 12 | 8 | 8 | 8 > 2 → True | 비트 끔 | 0 |
| 13 | 4 | 4 | 4 > 4 → False | 유지 | 4 |
| 14 | 2 | 6 (4 \| 2) | 6 > 2 → True | 비트 끔 | 4 |
| 15 | 1 | 5 | 5 > 3 → True | 비트 끔 | 4 |
| 끝 | - | | | | 4 |

4 * 4 == 16
{: style="color: green;"}