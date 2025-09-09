---
excerpt: "'LeetCode: Find Pivot Index' 풀이 정리"
title: "\0724. Find Pivot Index"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Prefix Sum
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return *the **leftmost pivot index***. If no such index exists, return `-1`.

**Example 1:**

- Input: nums = [1,7,3,6,5,6]
- Output: 3
- Explanation:    
The pivot index is 3.   
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11   
Right sum = nums[4] + nums[5] = 5 + 6 = 11

**Example 2:**

- Input: nums = [1,2,3]
- Output: -1
- Explanation:    
There is no index that satisfies the conditions in the problem statement.   

**Example 3:**

- Input: nums = [2,1,-1]
- Output: 0
- Explanation:    
The pivot index is 0.   
Left sum = 0 (no elements to the left of index 0)   
Right sum = nums[1] + nums[2] = 1 + -1 = 0

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -1000 <= nums[i] <= 1000

**Note:** This question is the same as 1991: <a href="https://leetcode.com/problems/find-the-middle-index-in-array/" target="_blank">https://leetcode.com/problems/find-the-middle-index-in-array/</a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">For each index i, check if sumLeft[i] equals sumRight[i]. If so, return i. If no such i is found, return -1.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0                         # 피벗 인덱스
        sumLeft = 0               
        sumRight = sum(nums[1:])

        while i < len(nums)-1:
            if sumLeft == sumRight:
                return i
            
            i += 1
            sumLeft += nums[i-1]
            sumRight -= nums[i]

        return i if sumLeft == sumRight else -1
```
<i class="fa-solid fa-clock"></i> Runtime: **7** ms \| Beats **60.74%**    
<i class="fa-solid fa-memory"></i> Memory: **13.34** MB \| Beats **55.26%**

피벗 인덱스는 가장 왼쪽에서부터 시작하고 한 칸씩 옮길 때마다 왼쪽과 오른쪽 누적 합을 갱신하며 비교한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution(object):
    def pivotIndex(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

조금 더 깔끔한 코드를 찾아봤다.