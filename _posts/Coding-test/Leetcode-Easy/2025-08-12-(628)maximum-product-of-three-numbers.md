---
excerpt: "'LeetCode: Maximum Product of Three Numbers' 풀이 정리"
title: "\0628. Maximum Product of Three Numbers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Sorting
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums`, *find three numbers whose product is maximum and return the maximum product.*

**Example 1:**

- Input: nums = [1,2,3]
- Output: 6

**Example 2:**

- Input: nums = [1,2,3,4]
- Output: 24

**Example 3:**

- Input: nums = [-1,-2,-3]
- Output: -6

**Constraints:**

- 3 <= nums.length <= 10<sup>4</sup>
- -1000 <= nums[i] <= 1000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = min(nums)    # 최대값 3개를 최소값으로 초기화
        min1 = min2 = max(nums)           # 최소값 2개를 최대값으로 초기화

        for n in nums:
            # 최소값 갱신
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n

            # 최대값 갱신
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        
        # 최대값 3개의 곱 또는 최소값 2개와 최대값 1개의 곱 중 큰 값 선택
        return max((max1*max2*max3), (max1*min1*min2))
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **99.91%**    
<i class="fa-solid fa-memory"></i> Memory: **13.27** MB \| Beats **59.49%**

sort()를 사용하면 너무 느려서 한 번의 순회로 끝내는 방법이 가장 효율적이다. 최대값 3개가 모두 양수 또는 모두 음수일 경우 그대로 3개의 값을 곱하면 된다. 하지만 최소값 2개가 음수이고 최대값 1개가 양수인 경우 두 번째, 세 번째 최대값의 곱과 최소값 2개의 곱 중 어느 쪽이 더 큰지 비교해야 한다.

nums = [-8,-7,-2,10,20]
{: style="color: blue;"}
<pre>
nums   min1  min2  max1  max2  max3
       20    20    -8    -8    -8
-8     -8    20    -8    -8    -8
-7     -8    -7    -7    -8    -8
-2     -8    -7    -2    -7    -8
10     -8    -7    10    -2    -7
20     -8    -7    20    10    -2

-8 * -7 * 20 = 1120
-2 * 10 * 20 = -400
</pre>

return 1120
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximum-product-of-three-numbers/solutions/3309876/easiest-two-lines-of-code-python3/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)          

위의 방법에 비해 비효율적이지만 간단한 방법이다.