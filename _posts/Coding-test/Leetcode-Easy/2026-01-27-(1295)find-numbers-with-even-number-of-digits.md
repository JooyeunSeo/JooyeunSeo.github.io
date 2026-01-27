---
excerpt: "'LeetCode: Find Numbers with Even Number of Digits' 풀이 정리"
title: "\01295. Find Numbers with Even Number of Digits"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

**Example 1:**

- Input: nums = [12,345,2,6,7896]
- Output: 2
- Explanation:      
12 contains 2 digits (even number of digits).    
345 contains 3 digits (odd number of digits).     
2 contains 1 digit (odd number of digits).     
6 contains 1 digit (odd number of digits).     
7896 contains 4 digits (even number of digits).     
Therefore only 12 and 7896 contain an even number of digits.

**Example 2:**

- Input: nums = [555,901,482,1771]
- Output: 1 
- Explanation:      
Only 1771 contains an even number of digits.

**Constraints:**

- 1 <= nums.length <= 500
- 1 <= nums[i] <= 10<sup>5</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">How to compute the number of digits of a number ?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Divide the number by 10 again and again to get the number of digits.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            digits = 0

            while n > 0:
                digits += 1
                n //= 10
            
            if digits % 2 == 0:
                result += 1

        return result
```
```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            digits = len(str(n))
            if digits % 2 == 0:
                result += 1

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.36** MB \| Beats **25.90%**    

정수값을 문자열로 변경한 뒤 길이를 재는 방법이 가장 빨랐다. 다만 숫자가 0인 케이스가 있는 경우 에러가 발생한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-numbers-with-even-number-of-digits/solutions/6700412/5-approaches-bit-manipulationmathstringr-qknw/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            digits = int(math.log10(i)) + 1
            if digits % 2 == 0:
                count += 1
        return count
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

밑이 10인 log를 통해 자릿수를 알 수 있다.