---
excerpt: "'LeetCode: Third Maximum Number' 풀이 정리"
title: "\0414. Third Maximum Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - set()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number.*

**Example 1:**

- Input: nums = [3,2,1]
- Output: 1
- Explanation:   
The first distinct maximum is 3.   
The second distinct maximum is 2.   
The third distinct maximum is 1.

**Example 2:**

- Input: nums = [1,2]
- Output: 2
- Explanation:   
The first distinct maximum is 2.   
The second distinct maximum is 1.   
The third distinct maximum does not exist, so the maximum (2) is returned instead.

**Example 3:**

- Input: nums = [2,2,3,1]
- Output: 1
- Explanation:   
The first distinct maximum is 3.   
The second distinct maximum is 2 (both 2's are counted together since they have the same value).   
The third distinct maximum is 1.

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1

**Follow up:** Can you find an `O(n)` solution?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)   # 내림차순으로 정렬        

        maxpoint = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[maxpoint]:
                maxpoint = i
                count += 1
                if count == 3:
                    return nums[maxpoint]
        
        return nums[maxpoint - 1]   # count가 3이 되기 전에 nums
```
<mark>sort()</mark>를 이용해서 정렬하면 쉽게 해결할 수 있지만, 시간 복잡도가 𝑂(𝑛log𝑛)이 되기 때문에 Follow up에서 제시한 조건에는 맞출 수 없는 방법이다.

```python
class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))  # first distinct maximum
            nums.remove(max(nums))  # second distinct maximum
            return max(nums)        # third distinct maximum
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.32** MB \| Beats **15.31%**

<mark>set()</mark>을 이용하면 max(nums)를 최대 3번까지만 반복하기 때문에 시간 복잡도를 𝑂(𝑛)으로 맞출 수 있다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/third-maximum-number/solutions/6646298/master-top-3-tracking-to-find-the-third-5d054/" target="_blank">1st</a>

```python
class Solution(object):
    def thirdMax(self, nums):
        first = second = third = None
        
        for num in nums:
            if num == first or num == second or num == third: # 중복된 값은 건너뜀
                continue  
            
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num
        
        return third if third is not None else first          # third가 없으면 최대값 반환
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

정렬 없이 3개의 변수를 사용하여 값을 추적할 수 있다. 속도도 빠르고 메모리도 아낄 수 있는 정석적인 방법이다.