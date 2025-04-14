---
excerpt: "'LeetCode-Contains Duplicate' 풀이 정리"
title: "\0217. Contains Duplicate"
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

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

- Input: nums = [1,2,3,1]
- Output: true
- Explanation: The element 1 occurs at the indices 0 and 3.

**Example 2:**

- Input: nums = [1,2,3,4]
- Output: false
- Explanation: All elements are distinct.

**Example 3:**

- Input: nums = [1,1,1,3,3,4,3,2,4,2]
- Output: true

**Constraints:**

- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) < len(nums):    # set(nums)의 길이가 nums의 길이보다 작으면 중복이 있다는 뜻
            return True
        else:
            return False
```

```python
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **25.87** MB \| Beats **67.27%**

<mark>set()</mark>을 이용해서 빠르게 해결 가능했다. 다만 두 번째 코드로 했을 때 훨씬 빠른 런타임을 기록했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-methods-c-java-python-beginner-friendl-zozw/" target="_blank">1st</a>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

위와 같이 set()을 이용했지만, 여기서는 nums의 숫자를 저장하는 용도로 사용했다. 참고로 같은 구조의 코드를 set()이 아니라 list를 이용해서 제출했었는데, nums가 엄청나게 긴 케이스에서 시간초과 때문에 통과하지 못했다. 그러나 set()은 해시 테이블 기반이어서 리스트보다 빠르게 검색할 수 있기 때문에 시간복잡도를 크게 단축할 수 있다.

### <a href="https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-methods-c-java-python-beginner-friendl-zozw/" target="_blank">2nd</a>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1) ← 제자리 정렬 

<mark>sort()</mark>로 숫자를 정렬한 후, 인접한 값끼리 비교하는 방법을 사용할 수도 있다.