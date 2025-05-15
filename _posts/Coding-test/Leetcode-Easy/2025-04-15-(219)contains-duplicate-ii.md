---
excerpt: "'LeetCode: Contains Duplicate II' 풀이 정리"
title: "\0219. Contains Duplicate II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - set()
  - Sliding Window
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums` and an integer `k`, return `true` *if there are **two distinct** indices* `i` *and* `j` *in the array such that* `nums[i] == nums[j]` *and* `abs(i - j) <= k`.

**Example 1:**

- Input: nums = [1,2,3,1], k = 3
- Output: true

**Example 2:**

- Input: nums = [1,0,1,1], k = 1
- Output: true

**Example 3:**

- Input: nums = [1,2,3,1,2,3], k = 2
- Output: false

**Constraints:**

- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- 0 <= k <= 10<sup>5</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_idx = {}

        for i in range(len(nums)):
            if nums[i] in nums_idx and abs(nums_idx[nums[i]] - i) <= k:
                return True
            else:
                nums_idx[nums[i]] = i
        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **32** ms \| Beats **47.23%**    
<i class="fa-solid fa-memory"></i> Memory: **24.72** MB \| Beats **18.62%**

설명이 조금 헷갈리는 문제였는데, 조건 `nums[i] == nums[j]`와 `abs(i - j) <= k`에 모두 부합하는 인덱스 `i`와 `j`가 한 쌍이라도 있을 경우 True를 반환해야 한다는 뜻이었다. 그렇기 때문에 이미 딕셔너리에 저장된 키가 nums[i]이고 이와 비교할 현재 원소의 값이 nums[j]일 때, abs(i - j)가 k보다 크다면 바로 False를 반환하는 것이 아니라 키의 값인 i를 j로 업데이트해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/contains-duplicate-ii/solutions/6012642/video-2-solutions-hashmap-set-by-niits-tmg9/" target="_blank">1st</a>

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        
        return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)  

같은 방법이지만 <mark>enumerate()</mark>를 쓰는 것이 더 깔끔해서 좋은 것 같다.

### <a href="https://leetcode.com/problems/contains-duplicate-ii/solutions/6012642/video-2-solutions-hashmap-set-by-niits-tmg9/" target="_blank">2nd</a>

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()    # 최근 k개의 원소들을 저장

        for i, val in enumerate(nums):  
            if i > k:           # 현재 인덱스가 k보다 크면 슬라이딩 윈도우를 벗어낫다는 의미(윈도우 크기가 k+1)
                seen.remove(nums[i - k - 1])    # 슬라이딩 윈도우에서 가장 오래된 값 제거

            if val in seen:
                return True

            seen.add(val)

        return False
```
<mark>set()</mark>으로 **Sliding Window**처럼 최근 k개만 추적하는 방법이다. 

nums = [2,0,3,2,3,4]    
k = 2
{: style="color: blue;"}
<pre>
i   val    seen
-----------------------
0    2     {2}            add val
1    0     {2, 0}         add val
2    3     {2, 0, 3}      add val
3    2        {0, 3, 2}   remove nums[0], add val
4    3           {3, 2}   remove nums[1], return True (val in seen)
</pre>

return True
{: style="color: green;"}