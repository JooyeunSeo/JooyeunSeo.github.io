---
excerpt: "'LeetCode: Monotonic Array' 풀이 정리"
title: "\0896. Monotonic Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`.    
An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` *if the given array is monotonic, or* `false` *otherwise*.

**Example 1:**

- Input: nums = [1,2,2,3]
- Output: true

**Example 2:**

- Input: nums = [6,5,4,4]
- Output: true

**Example 3:**

- Input: nums = [1,3,2]
- Output: false

**Constraints:**

- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_increasing = None            # 증가하면 True, 감소하면 False

        for i in range(1, len(nums)):
            if is_increasing is None:   # 처음으로 서로 값이 다른 원소가 연속해서 나올 때 체크
                if nums[i-1] < nums[i]: is_increasing = True
                elif nums[i-1] > nums[i]: is_increasing = False
            elif is_increasing:
                if nums[i-1] > nums[i]: return False
            else:
                if nums[i-1] < nums[i]: return False
        
        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **28** ms \| Beats **90.74%**    
<i class="fa-solid fa-memory"></i> Memory: **20.38** MB \| Beats **92.99%**



## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/monotonic-array/solutions/6097952/video-two-flags-python-javascript-java-c-hwgv/" target="_blank">1st</a>

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        is_inc = True
        is_dec = True

        for i in range(1, n):
            if not is_inc and not is_dec:
                return False

            if nums[i] < nums[i-1]:
                is_inc = False
            if nums[i] > nums[i-1]:
                is_dec = False

        return is_inc or is_dec
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

increasing과 decreasing 조건을 동시에 체크하면서 둘 다 False가 될 때 monotonic이 아닌 것으로 판단하는 방법도 깔끔한 것 같다.

### <a href="https://leetcode.com/problems/monotonic-array/solutions/4102847/9744increasing-decreasing1-line-code-by-n8gl9/" target="_blank">2nd</a>

```python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))
```
<mark>all()</mark>을 이용하여 가독성을 높이는 방법도 있다.

### <a href="https://leetcode.com/problems/monotonic-array/solutions/165889/cjavapython-one-pass-on-by-lee215-hd3w/" target="_blank">3rd</a>

```python
class Solution:
    def isMonotonic(self, A):
        return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}
```
**python 2** 버전에서 사용 가능한 <mark>cmp()</mark> 함수는 zip()으로 생성한 인접한 원소 두 개의 쌍을 비교 후 앞의 값이 뒤의 값보다 작다면 `-1`, 같으면 `0`, 크다면 `1`을 반환한다. 결과가 집합 `{1, -1}` 모두를 포함한다면 단조 증가이거나 단조 감소가 아니기 때문에 False가 된다.