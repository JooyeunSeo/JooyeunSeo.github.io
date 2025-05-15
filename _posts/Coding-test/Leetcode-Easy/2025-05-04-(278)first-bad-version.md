---
excerpt: "'LeetCode: First Bad Version' 풀이 정리"
title: "\0278. First Bad Version"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Search
---

## <i class="fa-solid fa-file-lines"></i> Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool `isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


**Example 1:**

- Input: n = 5, bad = 4
- Output: 4
- Explanation:   
call isBadVersion(3) -> false   
call isBadVersion(5) -> true   
call isBadVersion(4) -> true   
Then 4 is the first bad version.

**Example 2:**

- Input: n = 1, bad = 1
- Output: 1

**Constraints:**

- 1 <= bad <= n <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            
            if isBadVersion(mid):     # mid가 True면 그 앞부분에 True가 있는지 탐색
                high = mid - 1
            else:                     # mid가 False면 그 뒷부분에 False가 있는지 탐색
                low = mid + 1
        
        return low
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **61.49%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats *77.67%**

1부터 n까지 모두 순회하면 제한시간을 넘는 케이스가 있기 때문에 이진 탐색 방식을 활용해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

while 문의 범위를 수정하면 위의 코드보다 조금 더 빠르게 수행할 수 있다.