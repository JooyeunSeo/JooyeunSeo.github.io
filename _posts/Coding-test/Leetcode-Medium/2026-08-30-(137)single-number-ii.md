---
excerpt: "'LeetCode: Single Number II' 풀이 정리"
title: "\0137. Single Number II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Bit Manipulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

- Input: nums = [2,2,3,2]
- Output: 3

**Example 2:**

- Input: nums = [0,1,0,1,0,1,99]
- Output: 99

**Constraints:**

- 1 <= nums.length <= 3 * 10<sup>4</sup>
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
- Each element in nums appears exactly **three times** except for one element which appears **once**.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = 0, 0

        for n in nums:
            once = (once ^ n) & ~twice
            twice = (twice ^ n) & ~once

        return once
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **70.65%**    
<i class="fa-solid fa-memory"></i> Memory: **20.73** MB \| Beats **36.66%**    

nums = [5, 5, 5, 3]
{: style="color: blue;"}
<pre>
          once          twice
          0000          0000
          ------------------
0101(5)   0101 ←1st     0000 /
0101(5)   0000 /        0101 ←2nd
0101(5)   0000 /3rd     0000 /3rd   (3번째 등장하면 둘 다 0으로 초기화)
0011(3)   0011 ←1st     0000    
</pre>

return 3
{: style="color: green;"}

<a href="https://jooyeunseo.github.io/leetcode-easy/(136)single-number/" target="_blank">136. Single Number I</a>

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/single-number-ii/solutions/7554077/simple-bitwise-logic-on-time-o1-space-be-7nbp/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    ones = 0
    twos = 0
    for num in nums:
      ones ^= (num & ~twos)
      twos ^= (num & ~ones)

    return ones
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

### <a href="https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-l7m9l/?envType=problem-list-v2&envId=2s2ff433" target="_blank">2nd</a>

```python
class Solution:
    def singleNumber(self, nums):
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Convert the number to two's complement representation to handle large test case
                if num < 0:
                    num = num & (2**32-1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            ans |= bit_sum << i

        # Convert the result back to two's complement representation if it's negative to handle large test case
        if ans >= 2**31:
            ans -= 2**32

        return ans
```

각 비트 자릿수(0~31번째)의 합을 3으로 나눈 나머지를 구해서 단 한 번만 등장하는 수의 비트를 복원하는 방법이다. 파이썬의 경우 음수를 따로 처리해야 한다.