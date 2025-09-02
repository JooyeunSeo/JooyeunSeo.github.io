---
excerpt: "'LeetCode: Binary Search' 풀이 정리"
title: "\0704. Binary Search"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

- Input: nums = [-1,0,3,5,9,12], target = 9
- Output: 4
- Explanation: 9 exists in nums and its index is 4

**Example 2:**

- Input: nums = [-1,0,3,5,9,12], target = 2
- Output: -1
- Explanation: 2 does not exist in nums so return -1

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> < nums[i], target < 10<sup>4</sup>
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.26** MB \| Beats **93.13%**

이미 오름차순으로 정렬되어 있기 때문에 이진 탐색 알고리즘으로 𝑂(log𝑛)의 시간 만에 빠르게 찾을 수 있다.