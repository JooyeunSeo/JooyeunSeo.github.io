---
excerpt: "'LeetCode: Longest Continuous Increasing Subsequence' 풀이 정리"
title: "\0674. Longest Continuous Increasing Subsequence"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an unsorted array of integers `nums`, *return the length of the longest **continuous increasing subsequence** (i.e. subarray)*. The subsequence must be **strictly** increasing.

A **continuous increasing subsequence** is defined by two indices `l` and `r` (`l < r`) such that it is `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` and for each `l <= i < r`, `nums[i] < nums[i + 1]`.

**Example 1:**

- Input: nums = [1,3,5,4,7]
- Output: 3
- Explanation:    
The longest continuous increasing subsequence is [1,3,5] with length 3.    
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element 4.

**Example 2:**

- Input: nums = [2,2,2,2,2]
- Output: 1
- Explanation:    
The longest continuous increasing subsequence is [2] with length 1.    
Note that it must be strictly increasing.

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 1       # subsequence 길이
        max_len = 1     # 가장 긴 subsequence

        for i in range(1, n):
            if nums[i] - nums[i-1] <= 0:
                max_len = max(count, max_len)
                count = 1
            else:
                count += 1
        
        return max(count, max_len)
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **68.31%**    
<i class="fa-solid fa-memory"></i> Memory: **13.32** MB \| Beats **60.24%**

반복문 종료 후 리스트의 마지막 원소까지 신경써서 처리해줘야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-continuous-increasing-subsequence/solutions/6935243/sliding-window-streak-lcis-in-on-time-by-in4r/" target="_blank">1st</a>

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        left, right = 0, 1
        max_len = 1

        while right < len(nums):
            if nums[right] > nums[right - 1]:
                max_len = max(max_len, right - left + 1)
            else:
                left = right
            right += 1
        return max_len
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

while문으로도 풀 수 있다.