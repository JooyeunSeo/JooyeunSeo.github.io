---
excerpt: "'LeetCode: Squares of a Sorted Array' 풀이 정리"
title: "\0977. Squares of a Sorted Array"
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

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order.*

**Example 1:**

- Input: nums = [-4,-1,0,3,10]
- Output: [0,1,9,16,100]
- Explanation: After squaring, the array becomes [16,1,0,9,100].    
After sorting, it becomes [0,1,9,16,100].

**Example 2:**

- Input: nums = [-7,-3,2,3,11]
- Output: [4,9,9,49,121]

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- `nums` is sorted in **non-decreasing** order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:                            # 모든 원소가 0 또는 양수일 경우
            return [num*num for num in nums]
        if nums[-1] <= 0:                           # 모든 원소가 0 또는 음수일 경우
            return [num*num for num in nums[::-1]]

        result = []
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:                               # 둘 중 더 큰 순서대로 리스트에 삽입
            if abs(nums[l]) <= abs(nums[r]):
                result.append(nums[r]*nums[r])
                r -= 1
            else:
                result.append(nums[l]*nums[l])
                l += 1
        
        return result[::-1]                         # 리스트 뒤집기
```
<i class="fa-solid fa-clock"></i> Runtime: **8** ms \| Beats **65.65%**    
<i class="fa-solid fa-memory"></i> Memory: **19.46** MB \| Beats **61.99%**    

sort() 대신 포인터 두 개를 이용하면 𝑂(𝑛) 시간만에 풀 수 있다. 값이 큰 순서대로 리스트에 넣은 뒤 맨 마지막에 거꾸로 뒤집는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/squares-of-a-sorted-array/solutions/6149748/using-two-pointers-by-niits-0c19/" target="_blank">1st</a>

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

len(nums) 만큼의 리스트를 생성하면 뒤에서부터 값을 넣을 수 있기 때문에 뒤집지 않아도 된다.