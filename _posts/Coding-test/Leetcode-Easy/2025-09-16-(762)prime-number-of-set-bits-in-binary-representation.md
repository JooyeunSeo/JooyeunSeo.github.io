---
excerpt: "'LeetCode: Prime Number of Set Bits in Binary Representation' 풀이 정리"
title: "\0762. Prime Number of Set Bits in Binary Representation"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Bit Manipulation
  - Weekly Contest
  - Brian Kernighan
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two integers `left` and `right`, return *the **count** of numbers in the **inclusive** range* `[left, right]` *having a **prime number of set bits** in their binary representation.*

Recall that the **number of set bits** an integer has is the number of `1`'s present when written in binary.

- For example, `21` written in binary is `10101`, which has `3` set bits.

**Example 1:**

- Input: left = 6, right = 10
- Output: 4
- Explanation:     
6  -> 110 (2 set bits, 2 is prime)     
7  -> 111 (3 set bits, 3 is prime)     
8  -> 1000 (1 set bit, 1 is not prime)     
9  -> 1001 (2 set bits, 2 is prime)     
10 -> 1010 (2 set bits, 2 is prime)     
4 numbers have a prime number of set bits.

**Example 2:**

- Input: left = 10, right = 15
- Output: 5
- Explanation:     
10 -> 1010 (2 set bits, 2 is prime)     
11 -> 1011 (3 set bits, 3 is prime)     
12 -> 1100 (2 set bits, 2 is prime)     
13 -> 1101 (3 set bits, 3 is prime)     
14 -> 1110 (3 set bits, 3 is prime)     
15 -> 1111 (4 set bits, 4 is not prime)     
5 numbers have a prime number of set bits.

**Constraints:**

- 1 <= left <= right <= 10<sup>6</sup>
- 0 <= right - left <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_nums = [2, 3, 5, 7, 11, 13, 17, 19]
        result = 0

        for num in range(left, right+1):
            count_bit = bin(num).count("1")
            
            if count_bit in prime_nums:
                result += 1
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **131** ms \| Beats **51.56%**    
<i class="fa-solid fa-memory"></i> Memory: **12.61** MB \| Beats **74.22%**

left 또는 right의 최대값 10<sup>6</sup>은 이진수로 `11110100001001000000`이기 때문에 범위 내에서 가능한 1의 최대 개수는 19개(`01111111111111111111`)다. 1부터 19까지 숫자들 중 소수는 2, 3, 5, 7, 11, 13, 17, 19이다.   
`&` 연산자로 비트를 하나씩 밀면서 1의 개수를 세는 방법은 시간이 너무 오래 걸려서 <mark>bin()</mark>과 <mark>count()</mark>로 빠르게 셌다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solutions/7105983/super-ez-sol-for-absolute-beginner-by-ng-e9jo/" target="_blank">1st</a>

```python
def count_one(n):
    ans = 0
    while n:
        n &= n-1
        ans += 1
    return ans

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        total = 0
        for i in range(left, right+1):
            new = count_one(i)
            if new in prime:
                total += 1
        return total
```
<i class="fa-solid fa-clock"></i> **time complexity:**     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

1비트의 개수를 세는 방법
1. `n & 1 == 1`으로 최하위 비트가 1인지 확인한 후 `n >>= 1`으로 다음 비트를 검사하기
2. Brian Kernighan 알고리즘(`n &= n - 1`)

### <a href="https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solutions/113232/665772-by-stefanpochmann-sli1/" target="_blank">2nd</a>

```python
def countPrimeSetBits(self, L, R):
    return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))
```
소수의 집합(2, 3, 5, 7, 11, 13, 17, 19)을 비트마스크로 저장하는 방법이다.
<pre>
index:  19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
bits :   1  0  1  0  0  0  1  0  1  0  0  0  1  0  1  0  1  1  0  0
</pre>

bits를 2진수로 놓고 이를 10진수로 변경하면 `665772`이 되기 때문에 이 숫자가 쓰였다.   
각 숫자의 1비트 개수 k만큼 비트마스크를 오른쪽으로 시프트한 후 `& 1`으로 맨 끝 비트를 확인해서 `1`이면 소수임을 알 수 있다.