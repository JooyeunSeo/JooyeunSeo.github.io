---
excerpt: "'LeetCode: Sort Array By Parity' 풀이 정리"
title: "\0905. Sort Array By Parity"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return ***any array** that satisfies this condition.*

**Example 1:**

- Input: nums = [3,1,2,4]
- Output: [2,4,3,1]
- Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

**Example 2:**

- Input: nums = [0]
- Output: [0]

**Constraints:**

- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        front, end = 0, (len(nums)-1)
        
        while front <= end:
            if nums[front] % 2 == 0:  # 해당 원소가 짝수이면 front를 뒤로 이동
                front += 1
            else:                     # 해당 원소가 홀수이면 서로 자리를 바꾼 후 end를 앞으로 이동
                nums[front], nums[end] = nums[end], nums[front]
                end -= 1

        return nums
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.09* MB \| Beats **61.39%**

맨 앞과 맨 뒤에서 시작하는 포인터 두 개로 nums 리스트 안에서 두 원소 위치를 바꾸는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/sort-array-by-parity/solutions/6280114/video-how-we-think-about-a-solution-one-0ks18/" target="_blank">1st</a>

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        return nums
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)       

for문을 사용하는 방법도 있다.