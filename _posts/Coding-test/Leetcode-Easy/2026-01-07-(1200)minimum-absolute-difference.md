---
excerpt: "'LeetCode: Minimum Absolute Difference' 풀이 정리"
title: "\01200. Minimum Absolute Difference"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

- `a, b` are from `arr`
- `a < b`
- `b - a` equals to the minimum absolute difference of any two elements in `arr`

**Example 1:**

- Input: arr = [4,2,1,3]
- Output: [[1,2],[2,3],[3,4]]
- Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

**Example 2:**

- Input: arr = [1,3,6,10,15]
- Output: [[1,3]]

**Example 3:**

- Input: arr = [3,8,-10,23,19,-4,-14,27]
- Output: [[-14,-10],[19,23],[23,27]]

**Constraints:**

- 2 <= arr.length <= 1<sup>05</sup>
- -106 <= arr[i] <= 1<sup>06</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Find the minimum absolute difference between two elements in the array.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">The minimum absolute difference must be a difference between two consecutive elements in the sorted array.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result = []

        for a, b in zip(arr, arr[1:]):
            min_diff = min(min_diff, (b - a))

        for a, b in zip(arr, arr[1:]):
            if b - a == min_diff:
                result.append([a, b])
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **50** ms \| Beats **66.07%**    
<i class="fa-solid fa-memory"></i> Memory: **31.41** MB \| Beats **12.42%**    


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/minimum-absolute-difference/solutions/901118/python-3-on-log-n-time-and-on-space-usin-mysp/" target="_blank">1st</a>

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = math.inf
        dic = collections.defaultdict(list)
        arr.sort()                               #O(n log n) time
        
        for i in range(len(arr)-1):              #O(n) time
          diff = arr[i+1] - arr[i]
          dic[diff].append([arr[i], arr[i+1]])   #O(n) space if all the pairs have the same minimum difference
          minDiff = min(minDiff, diff)
        return dic[minDiff]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

연속한 두 원소의 차이를 키로 하는 딕셔너리를 이용할 수도 있다. collections의 **defaultdict**는 키가 없을 때 KeyError가 나지 않고 자동으로 빈 리스트를 만들어주기 때문에 편리하다.