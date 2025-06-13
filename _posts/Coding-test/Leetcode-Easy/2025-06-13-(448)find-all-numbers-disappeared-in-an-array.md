---
excerpt: "'LeetCode: Find All Numbers Disappeared in an Array' 풀이 정리"
title: "\0448. Find All Numbers Disappeared in an Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array `nums` of n integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

**Example 1:**

- Input: nums = [4,3,2,7,8,2,3,1]
- Output: [5,6]

**Example 2:**

- Input: nums = [1,1]
- Output: [2]

**Constraints:**

- n == nums.length
- 1 <= n <= 10<sup>5</sup>
- 1 <= nums[i] <= n

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">This is a really easy problem if you decide to use additional memory. For those trying to write an initial solution using additional memory, think <b>counters!</b></span></u>   
💡 **Hint 2:**   
<u><span style="color:#F5F5F5">However, the trick really is to not use any additional space than what is already available to use. Sometimes, multiple passes over the input array help find the solution. However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.</span></u>   
💡 **Hint 3:**   
<u><span style="color:#F5F5F5">The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements in the array. Can we use this information and modify the array in-place somehow to find what we need?</span></u>   

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -abs(nums[idx])
        
        return [i + 1 for i, n in enumerate(nums) if n > 0]
```
<i class="fa-solid fa-clock"></i> Runtime: **47** ms \| Beats **35.71%**    
<i class="fa-solid fa-memory"></i> Memory: **26.64** MB \| Beats **99.15%**

순서대로 정렬했을 경우 각 원소가 원래 있어야 할 인덱스의 값을 음수로 바꾸는 방법으로 이미 존재하는 숫자를 마킹할 수 있다. 중복된 값일 경우 이미 음수로 마킹되어있지만 절대값을 구하기 때문에 다시 +로 되돌아가지 않는다. 

nums = [4,3,2,7,8,2,3,1]
{: style="color: blue;"}
<pre>
 n   idx     0  1  2  3  4  5  6  7
 4   3     [ 4, 3, 2,-7, 8, 2, 3, 1]
 3   2     [ 4, 3,-2,-7, 8, 2, 3, 1]
 2   1     [ 4,-3,-2,-7, 8, 2, 3, 1]
-7   6     [ 4,-3,-2,-7, 8, 2,-3, 1]
 8   7     [ 4,-3,-2,-7, 8, 2,-3,-1]
 2   1     
-3   2
-1   0     [-4,-3,-2,-7, 8, 2,-3,-1]

↓
nums[4] > 0  →  4 + 1
nums[5] > 0  →  5 + 1
</pre>

return [5,6]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/6648801/unlock-in-place-swapping-to-detect-missi-c65p/" target="_blank">1st</a>

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        return [i + 1 for i in range(n) if nums[i] != i + 1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

값을 스왑하면서 제자리에 정렬하는 방법이다.

nums = [4,3,2,7,8,2,3,1]
{: style="color: blue;"}
<pre>
                       0 1 2 3 4 5 6 7
nums[0] ↔︎  nums[3]  = [7,3,2,4,8,2,3,1]
nums[0] ↔︎  nums[6]  = [3,3,2,4,8,2,7,1]
nums[0] ↔︎  nums[1]  = [3,2,3,4,8,2,7,1]  
nums[0] ↔︎  nums[2]  = (3 == 3)

nums[1] == nums[1]
nums[2] == nums[2]
nums[3] == nums[3]

nums[4] ↔︎  nums[7]  = [3,2,3,4,1,2,7,8]
nums[4] ↔︎  nums[0]  = [1,2,3,4,3,2,7,8]
nums[4] ↔︎  nums[2]  = (3 == 3)

nums[5] ↔︎  nums[1]  = (2 == 2)
nums[6] == nums[6]
nums[7] == nums[7]

↓
nums[4] != 4 + 1  →  [5]
nums[5] != 5 + 1  →  [5,6]
</pre>

return [5,6]
{: style="color: green;"}

### <a href="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/6837974/even-faster-c-python-o-n-time-o-1-space-using-linked-list-dfs-no-abs-or-1/" target="_blank">2nd</a>

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            curr = i            # 현재 위치 인덱스
            valToPlace = 0      # 놓아야 할 값 (0으로 초기화 = 빈 공간)

            while nums[curr] != curr + 1:   # 현재 값이 올바른 위치에 있지 않은 경우 반복
                if nums[curr] == 0:
                    nums[curr] = valToPlace # 현재 자리가 비어 있으면, 놓아야 할 값을 배치
                    break
                
                # 현재 값 저장, 그 자리에 valToPlace 넣기 (처음엔 0)
                valToPlace, nums[curr] = nums[curr], valToPlace
                curr = valToPlace - 1

        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[k] = i + 1   # 누락된 숫자를 nums[k]에 저장 (배열 앞쪽 재사용)
                k += 1
        del nums[k:]              # 남은 부분 삭제
        return nums
```
잘못된 값이 있는 인덱스의 값을 0으로 만들고 해당 값은 제자리를 찾을 때까지 이동시키는 방법이다.
