---
excerpt: "'LeetCode: Smallest Range I' 풀이 정리"
title: "\0908. Smallest Range I"
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

You are given an integer array `nums` and an integer `k`.

In one operation, you can choose any index `i` where `0 <= i < nums.length` and change `nums[i]` to `nums[i] + x` where `x` is an integer from the range `[-k, k]`. You can apply this operation **at most once** for each index `i`.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

Return *the minimum **score** of* `nums` *after applying the mentioned operation at most once for each index in it*.

**Example 1:**

- Input: nums = [1], k = 0
- Output: 0
- Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

**Example 2:**

- Input: nums = [0,10], k = 2
- Output: 6
- Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

**Example 3:**

- Input: nums = [1,3,6], k = 3
- Output: 0
- Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- 0 <= nums[i] <= 10<sup>4</sup>
- 0 <= k <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_num, max_num = min(nums), max(nums)
        new_min, new_max = min_num + k, max_num - k

        return max(0, new_max - new_min)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.15** MB \| Beats **90.76%**

score는 nums의 최댓값과 최솟값의 차이이고, 이를 가능한 한 작게 만들어야 한다. 두 값에 k를 빼거나 더해서 이동할 수 있는 최대치만큼 이동 후, 새로 만든 최댓값과 최솟값이 겹친다면 차이를 0으로 만들 수 있다는 의미가 된다. 그렇지 않다면 두 값의 차이만 반환하면 된다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/smallest-range-i/description/" target="_blank">1st</a>

```python
class Solution:
        return max(0, max(A) - min(A) - 2 * K)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

공식을 사용하여 간단하게 한 방법이다.