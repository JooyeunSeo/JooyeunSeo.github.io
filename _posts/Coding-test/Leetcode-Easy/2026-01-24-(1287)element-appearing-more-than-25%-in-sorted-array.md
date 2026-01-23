---
excerpt: "'LeetCode: Element Appearing More Than 25% In Sorted Array' 풀이 정리"
title: "\01287. Element Appearing More Than 25% In Sorted Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Biweekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array **sorted** in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

**Example 1:**

- Input: arr = [1,2,2,6,6,6,6,7,10]
- Output: 6

**Example 2:**

- Input: arr = [1,1]
- Output: 1

**Constraints:**

- 1 <= arr.length <= 10<sup>4</sup>
- 0 <= arr[i] <= 10<sup>5</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%]</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">The answer should be in one of the ends of the intervals.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">In order to check which is element is the answer we can count the frequency with binarySearch.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]  # 25%, 50%, 75% 구간

        for c in candidates:
            if arr.count(c) > n // 4:
                return c
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **20.51** MB \| Beats **25.03%**    

25% 이상의 빈도를 가진 숫자는 무조건 25%, 50%, 75% 세 구간 중 하나에 포함된다는 것을 이용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/solutions/6101183/video-give-me-5-minutes-2-solutions-how-4pqs6/" target="_blank">1st</a>

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def binary_search(target, is_first):
            left, right = 0, len(arr) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    result = mid
                    if is_first:
                        right = mid - 1   # 왼쪽 시작 부분 찾기
                    else:
                        left = mid + 1    # 오른쪽 끝 부분 찾기
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result
        
        n = len(arr)
        quarter = n // 4

        # Handle the case where quarter is zero
        if quarter == 0:
            return arr[0] if n > 0 else None

        # Check every possible candidate element
        for i in range(quarter, n, quarter):
            # Use binary search to find the first and last occurrence of the candidate element
            left_occurrence = binary_search(arr[i], True)
            right_occurrence = binary_search(arr[i], False)

            # Check if the frequency is greater than 25%
            if right_occurrence - left_occurrence + 1 > quarter:
                return arr[i]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

이 문제의 가장 최적화된 방법은 이진 탐색을 사용하는 것이다. 