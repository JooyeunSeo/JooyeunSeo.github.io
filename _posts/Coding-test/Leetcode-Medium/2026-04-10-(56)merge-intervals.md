---
excerpt: "'LeetCode: Merge Intervals' 풀이 정리"
title: "\056. Merge Intervals"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Sorting
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of `intervals` where intervals[i] = [start<sub>i</sub>, end<sub>i</sub>], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Example 1:**

- Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
- Output: [[1,6],[8,10],[15,18]]
- Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

**Example 2:**

- Input: intervals = [[1,4],[4,5]]
- Output: [[1,5]]
- Explanation: Intervals [1,4] and [4,5] are considered overlapping.

**Example 3:**

- Input: intervals = [[4,7],[1,4]]
- Output: [[1,7]]
- Explanation: Intervals [1,4] and [4,7] are considered overlapping.

**Constraints:**

- 1 <= intervals.length <= 10<sup>4</sup>
- intervals[i].length == 2
- 0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()                        # 정렬
        merged = [intervals[0]]                 # 결과 저장

        for pair in intervals[1:]:
            if merged[-1][1] < pair[0]:         # 이전 구간의 끝과 이번 구간의 시작이 겹치는지 확인
                merged.append(pair)
            else:
                merged[-1][1] = max(merged[-1][1], pair[1])

        return merged
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **82.93%**    
<i class="fa-solid fa-memory"></i> Memory: **22.58** MB \| Beats **63.51%**    


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/merge-intervals/solutions/5513226/video-sorting-solution-by-niits-8ea5/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        return merged
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

그냥 sort()로 정렬해도 의도대로 정렬됐지만, 시작점을 기준으로 정렬한다는 것을 확실히 하기 위해 `intervals.sort(key=lambda x: x[0])`으로 키를 사용하는 것이 더 안전한 것 같다.