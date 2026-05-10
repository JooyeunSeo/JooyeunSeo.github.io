---
excerpt: "'LeetCode: Search in Rotated Sorted Array II' 풀이 정리"
title: "\081. Search in Rotated Sorted Array II"
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

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` if `target` is in `nums`, or `false` if it is not in `nums`.

You must decrease the overall operation steps as much as possible.

**Example 1:**

- Input: nums = [2,5,6,0,0,1,2], target = 0
- Output: true

**Example 2:**

- Input: nums = [2,5,6,0,0,1,2], target = 3
- Output: false

**Constraints:**

- 1 <= nums.length <= 5000
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- `nums` is guaranteed to be rotated at some pivot.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>

**Follow up:** This problem is similar to <a href="https://jooyeunseo.github.io/leetcode-medium/(33)search-in-rotated-sorted-array/" target="_blank">33. Search in Rotated Sorted Array</a>, but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True

            if nums[l] == nums[m] == nums[r]:       # 양쪽에서 한 칸씩 제거
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:                # 왼쪽 정렬
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:                                   # 오른쪽 정렬
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.65** MB \| Beats **32.32%**    

33번 문제와 달리 중복 숫자가 있어서 만약 `[1,0,1,1,1]` 처럼 왼쪽, 가운데, 오른쪽이 모두 같은 숫자일 경우 어느 쪽이 정렬되었는지 판단할 수 없게 된다. 이 조건만 처리하면 나머지 부분은 33번과 동일하게 진행할 수 있다. 다만 배열의 거의 모든 숫자가 중복인 최악의 경우 선형 탐색처럼 될 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/3892127/ex-amazon-explains-a-solution-with-a-vid-lyb1/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[left]:
                left += 1
                continue

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    