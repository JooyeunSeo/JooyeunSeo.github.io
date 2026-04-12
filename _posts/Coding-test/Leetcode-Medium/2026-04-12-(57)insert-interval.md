---
excerpt: "'LeetCode: Insert Interval' 풀이 정리"
title: "\057. Insert Interval"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an array of non-overlapping intervals intervals where intervals[i] = [start<sub>i</sub>, end<sub>i</sub>] represent the start and the end of the i<sup>th</sup> interval and `intervals` is sorted in ascending order by start<sub>i</sub>. You are also given an `interval newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by start<sub>i</sub>, and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

**Example 1:**

- Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
- Output: [[1,5],[6,9]]

**Example 2:**

- Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
- Output: [[1,2],[3,10],[12,16]]
- Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

**Constraints:**

- 0 <= intervals.length <= 10<sup>4</sup>
- intervals[i].length == 2
- 0 <= starti <= endi <= 10<sup>5</sup>
- `intervals` is sorted by start<sub>i</sub> in **ascending** order.
- newInterval.length == 2
- 0 <= start <= end <= 10<sup>5</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Intervals Array is sorted. Can you use Binary Search to find the correct position to insert the new Interval?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Can you try merging the overlapping intervals while inserting the new interval?</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">This can be done by comparing the end of the last interval with the start of the new interval and vice versa.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for pair in intervals:
            if pair[1] < newInterval[0]:                        # 현재 구간이 newInterval보다 작음
                res.append(pair)
            elif newInterval[1] < pair[0]:                      # 현재 구간이 newInterval보다 큼
                res.append(newInterval)                             # newInterval 추가
                newInterval = pair                                  # newInterval 갱신
            else:                                               # 겹치면 newInterval을 현재 구간으로 교체
                newInterval[0] = min(newInterval[0], pair[0])
                newInterval[1] = max(newInterval[1], pair[1])

        res.append(newInterval)                                 # 마지막으로 newInterval 추가

        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **21.24** MB \| Beats **92.24%**       

처음부터 순회하면서 newInterval과 겹치는 구간은 흡수하면서 키워가다가 더 이상 겹치지 않는 시점에 결과에 넣는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/insert-interval/solutions/4885946/beat-9722-full-explanation-with-pictures-b9ch/" target="_blank">1st</a>

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

위와 같은 과정이지만 세 구간으로 나눠서 보다 가독성이 좋은 방법이다.