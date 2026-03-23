---
excerpt: "'LeetCode: Find First and Last Position of Element in Sorted Array' 풀이 정리"
title: "\034. Find First and Last Position of Element in Sorted Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

- Input: nums = [5,7,7,8,8,10], target = 8
- Output: [3,4]

**Example 2:**

- Input: nums = [5,7,7,8,8,10], target = 6
- Output: [-1,-1]

**Example 3:**

- Input: nums = [], target = 0
- Output: [-1,-1]

**Constraints:**

- 0 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- nums is a non-decreasing array.
- -10<sup>9</sup> <= target <= 10<sup>9</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:               # 왼쪽 시작점 찾기
            m = (l + r) // 2
            if nums[m] >= target:
                r = m - 1           # 답 후보 포함해서 왼쪽 탐색
            else:
                l = m + 1           # 답 후보 아닌 절반 제외
        start = l

        if start == len(nums) or nums[start] != target: # nums가 비었거나 target이 없는 경우
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l <= r:               # 오른쪽 시작점 찾기
            m = (l + r) // 2
            if nums[m] <= target:   # 답 후보 포함해서 오른쪽 탐색
                l = m + 1
            else:
                r = m - 1           # 답 후보 아닌 절반 제외
        end = r

        return [start, end]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **20.46** MB \| Beats **96.32%**    

이진 탐색으로 왼쪽 시작과 오른쪽 끝을 각각 탐색하는 방법이다. 𝑂(log𝑛) 시간 안에 풀어야 하기 때문에 target이 존재하지 않는 경우도 이진 탐색 결과만을 이용해서 판단해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/6753678/video-binary-search-solution-by-niits-jewi/" target="_blank">1st</a>

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    