---
excerpt: "'LeetCode: Degree of an Array' 풀이 정리"
title: "\0697. Degree of an Array"
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

Given a non-empty array of non-negative integers `nums`, the **degree** of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of `nums`, that has the same degree as `nums`.

**Example 1:**

- Input: nums = [1,2,2,3,1]
- Output: 2
- Explanation:    
The input array has a degree of 2 because both elements 1 and 2 appear twice.    
Of the subarrays that have the same degree:    
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]    
The shortest length is 2. So return 2.

**Example 2:**

- Input: nums = [1,2,2,3,1,4,2]
- Output: 6
- Explanation:     
The degree is 3 because the element 2 is repeated 3 times.    
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

**Constraints:**

- `nums.length` will be between 1 and 50,000.
- `nums[i]` will be an integer between 0 and 49,999.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Say 5 is the only element that occurs the most number of times - for example, nums = [1, 5, 2, 3, 5, 4, 5, 6]. What is the answer?</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        max_degree = 0              # 가장 큰 degree
        min_length = float('inf')   # 가장 짧은 subarray 길이

        # nums 순회
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = [1, i, i]  # [degree, start, end]
            else:
                map[nums[i]][0] += 1      # degree += 1
                map[nums[i]][2] = i       # end = i
            max_degree = max(map[nums[i]][0], max_degree)

        # 딕셔너리 순회
        for k in map:
            if map[k][0] == max_degree:
                min_length = min((map[k][2] - map[k][1] + 1), min_length)

        return min_length
```
<i class="fa-solid fa-clock"></i> Runtime: **30** ms \| Beats **42.55%**    
<i class="fa-solid fa-memory"></i> Memory: **14.55** MB \| Beats **21.58%**

딕셔너리의 값을 리스트로 설정해서 `등장 횟수, 첫 등장 위치, 마지막 등장 위치`를 모두 저장하는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/degree-of-an-array/solutions/124317/javacpython-one-pass-solution-by-lee215-fzpo/" target="_blank">1st</a>

```python
class Solution(object):
    def findShortestSubArray(self, A):
        first, count, res, degree = {}, {}, 0, 0
        for i, a in enumerate(A):
            first.setdefault(a, i)            # 키(a)가 처음 등장한 인덱스 저장
            count[a] = count.get(a, 0) + 1    # 키(a)의 등장 횟수 카운트
            if count[a] > degree:                 # 지금까지의 최대빈도보다 클 경우
                degree = count[a]                   # 최대빈도 갱신
                res = i - first[a] + 1              # 부분배열의 길이 갱신
            elif count[a] == degree:              # 지금까지의 최대빈도와 같을 경우
                res = min(res, i - first[a] + 1)    # 더 짧은 길이 선택
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

어떤 값이 처음 등장한 인덱스를 저장하는 딕셔너리(first)와 각 값의 등장 횟수를 저장하는 딕셔너리(count) 두 개를 생성하는 방법을 사용하면 for문 한 번으로 해결할 수 있다. 딕셔너리의 <mark>setdefault()</mark> 함수를 사용하면 key가 있을 때는 그 값을 반환하고, 없으면 설정한 값으로 키-값을 저장한다(`if a not in first: first[a] = i`와 같음).