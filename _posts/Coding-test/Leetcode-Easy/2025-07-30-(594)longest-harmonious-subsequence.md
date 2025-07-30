---
excerpt: "'LeetCode: Longest Harmonious Subsequence' 풀이 정리"
title: "\0594. Longest Harmonious Subsequence"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Sliding Window
  - Sorting
  - Counting
---

## <i class="fa-solid fa-file-lines"></i> Description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is **exactly** `1`.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible **subsequences**.

*[subsequences]: A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

- Input: nums = [1,3,2,2,5,2,3,7]
- Output: 5
- Explanation: The longest harmonious subsequence is `[3,2,2,2,3]`.

**Example 2:**

- Input: nums = [1,2,3,4]
- Output: 2
- Explanation: The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of 2.

**Example 3:**

- Input: nums = [1,1,1,1]
- Output: 0
- Explanation: No harmonic subsequence exists.

**Constraints:**

- 1 <= nums.length <= 2 * 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        max_len = 0
        
        # 각 원소의 빈도수 저장
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # 키(원소)와 값(빈도수) 순회
        for k, f in freq.items():
            if k+1 in freq:
                max_len = max(max_len, (f + freq[k+1]))

        return max_len
```
<i class="fa-solid fa-clock"></i> Runtime: **43** ms \| Beats **77.33%**    
<i class="fa-solid fa-memory"></i> Memory: **14.96** MB \| Beats **5.26%**

딕셔너리를 이용하여 각 원소의 빈도를 센 후, 1과 2 또는 2와 3처럼 인접한 숫자 쌍을 비교했다. 원래 키 값들을 순회하기 위해 `freq.keys()`를 사용했는데, 이 방법은 시간이 너무 오래걸려서 `freq.items()`이 훨씬 좋은 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-harmonious-subsequence/solutions/6900945/cpp-java-python-counting-map-easy-to-understand/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        freq = Counter(nums)
        max_len = 0
        for key in freq:  # 키 순회
            if key + 1 in freq:
                max_len = max(max_len, freq[key] + freq[key + 1])
        return max_len
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

dict의 확장형인 Counter를 사용하면 더 간단하고 빠르게 풀 수 있다.
