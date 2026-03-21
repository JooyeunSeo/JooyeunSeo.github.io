---
excerpt: "'LeetCode: Next Permutation' 풀이 정리"
title: "\031. Next Permutation"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: [`1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, *find the next permutation of* `nums`.

The replacement must be **<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>** and use only constant extra memory.

**Example 1:**

- Input: nums = [1,2,3]
- Output: [1,3,2]

**Example 2:**

- Input: nums = [3,2,1]
- Output: [1,2,3]

**Example 3:**

- Input: nums = [1,1,5]
- Output: [1,5,1]

**Constraints:**

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = len(nums) - 2   
        while p >= 0 and nums[p] >= nums[p+1]:  # 오른쪽에서 처음으로 증가하는 지점 찾기
            p -= 1
        
        if p < 0:                               # 다시 순열 처음으로 리셋
            nums.reverse()
            return

        q = len(nums) - 1
        while nums[q] <= nums[p]:               # 피벗 뒤에서 피벗과 스왑할 자리 찾기
            q -= 1

        nums[p], nums[q] = nums[q], nums[p]     # 스왑
        nums[p+1:] = reversed(nums[p+1:])       # 피벗 뒤 반대로 재정렬(내림차순 -> 오름차순)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.36** MB \| Beats **55.56%**    

사전 순 정렬에서 그 다음 순서를 찾는 문제로, 현재 순열보다 큰 순열 중에서 가장 작은 순열을 찾아야 한다. 오른쪽에서 처음으로 증가하는 지점을 찾아 그 값을 조금 더 큰 값으로 바꾸고, 뒤쪽을 최소(오름차순)로 만들면 된다.

nums = [1,2,3]
{: style="color: blue;"}
<pre>    
 1  (2) [3] →  1   3  [2]
[1]  3  (2) → [2]  3   1  → [2]  1   3  
 2  [1] (3) →  2  [3]  1 
[2] (3)  1  → [3]  2   1  → [3]  1   2 
 3  [1] (2) →  3  [2]  1 
 3   2   1  →  1   2   3
</pre>

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/next-permutation/solutions/14054/python-solution-with-comments-by-oldcodi-m2mi/" target="_blank">1st</a>

```python
class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

두 위치를 변경 후 뒤쪽을 reverse()하는 대신 포인터 두 개로 직접 뒤집는 방법이다.