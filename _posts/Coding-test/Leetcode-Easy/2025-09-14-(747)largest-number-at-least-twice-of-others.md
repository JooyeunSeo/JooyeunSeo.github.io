---
excerpt: "'LeetCode: Largest Number At Least Twice of Others' 풀이 정리"
title: "\0747. Largest Number At Least Twice of Others"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `nums` where the largest integer is **unique**.

Determine whether the largest element in the array is **at least twice** as much as every other number in the array. If it is, *return the **index** of the largest element, or return* `-1` *otherwise*.

**Example 1:**

- Input: nums = [3,6,1,0]
- Output: 1
- Explanation: 6 is the largest integer.   
For every other number in the array x, 6 is at least twice as big as x.   
The index of value 6 is 1, so we return 1.

**Example 2:**

- Input: nums = [1,2,3,4]
- Output: -1
- Explanation: 4 is less than twice the value of 3, so we return -1.

**Constraints:**

- 2 <= nums.length <= 50
- 0 <= nums[i] <= 100
- The largest element in `nums` is unique.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`. Scan through the array again. If we find some `x != m` with `m < 2*x`, we should return `-1`. Otherwise, we should return `maxIndex`.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0                       # 최대값 초기화

        for i in range(len(nums)):  
            if nums[i] > m:
                m = nums[i]         # 최대값
                maxIndex = i        # 최대값 인덱스

        for n in nums:
            if n != m and m < n*2:
                return -1
        
        return maxIndex
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.48** MB \| Beats **51.79%**

첫 번째 루프에서 최대값과 최대값의 인덱스를 찾고, 두 번째 루프에서 모든 원소가 조건에 맞는지 체크한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/largest-number-at-least-twice-of-others/solutions/2383331/python-elegant-short-on-time-one-pass-o1-oowr/" target="_blank">1st</a>

```python
def dominantIndex(self, nums: List[int]) -> int:
  	first_max = second_max = -1
    max_ind = 0

	  for i, num in enumerate(nums):
	  	if num >= first_max:
	  		first_max, second_max = num, first_max
	  		max_ind = i
	  	elif num > second_max:
	  		second_max = num

	  if first_max < 2*second_max:
	  	max_ind = -1

	  return max_ind
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

두 번째로 큰 값의 두 배가 첫 번째로 큰 값보다 크지 않다면 다른 모든 원소들에도 똑같이 적용되기 때문에 한 번의 루프만으로도 해결할 수 있다.