---
excerpt: "'LeetCode: Intersection of Two Arrays II' 풀이 정리"
title: "\0350. Intersection of Two Arrays II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Sorting
  - Array
  - Hash Table
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

**Example 1:**

- Input: nums1 = [1,2,2,1], nums2 = [2,2]
- Output: [2,2]

**Example 2:**

- Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
- Output: [4,9]
- Explanation: [9,4] is also accepted.

**Constraints:**

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

**Follow up:**

- What if the given array is already sorted? How would you optimize your algorithm?
- What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?
- What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_count = {}
        for num in nums1:
            nums1_count[num] = nums1_count.get(num, 0) + 1    # nums1의 원소는 키, 원소의 등장 횟수는 값
        
        result = []
        for num in nums2:
            if num in nums1_count and nums1_count[num] != 0:  # nums2의 원소가 딕셔너리의 키이고 값이 0이 아니면
                result.append(num)
                nums1_count[num] -= 1     # 카운트 1 감소

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.51** MB \| Beats **61.63%**

<a href="https://jooyeunseo.github.io/leetcode-easy/(349)intersection-of-two-arrays/" target="_blank">349. Intersection of Two Arrays</a> 문제와 달리 이번에는 중복된 숫자가 몇 번 등장하는지 카운트해야하기 때문에 이 코드가 유용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/intersection-of-two-arrays-ii/solutions/6635523/master-the-counter-trick-to-find-array-i-rg9c/" target="_blank">1st</a>

```python
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

파이썬 collections 모듈의 <mark>Counter</mark> 클래스를 이용하면 각 요소가 몇 번 등장하는지 횟수를 세서 딕셔너리처럼 저장해주기 때문에 편리하다. 그리고 해당하는 키가 없을 경우에는 0을 반환하기 때문에 `if counts[num] > 0` 같은 조건에서 오류가 나지 않아서 안전하다.