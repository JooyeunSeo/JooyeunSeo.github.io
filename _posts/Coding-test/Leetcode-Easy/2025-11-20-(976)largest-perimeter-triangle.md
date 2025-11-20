---
excerpt: "'LeetCode: Largest Perimeter Triangle' 풀이 정리"
title: "\0976. Largest Perimeter Triangle"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Greedy
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums`, return *the largest perimeter of a triangle with a non-zero area, formed from three of these lengths*. If it is impossible to form any triangle of a non-zero area, return `0`.

**Example 1:**

- Input: nums = [2,1,2]
- Output: 5
- Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

**Example 2:**

- Input: nums = [1,2,1,10]
- Output: 0
- Explanation:    
You cannot use the side lengths 1, 1, and 2 to form a triangle.    
You cannot use the side lengths 1, 1, and 10 to form a triangle.    
You cannot use the side lengths 1, 2, and 10 to form a triangle.    
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

**Constraints:**

- 3 <= nums.length <= 10<sup>4</sup>
- 1 <= nums[i] <= 10<sup>6</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()                 # 오름차순 정렬
        n = len(nums)
        a, b, c = n-3, n-2, n-1     # nums[a] <= nums[b] <= nums[c]

        while a >= 0:
            if (nums[a] == nums[b] == nums[c]) or (nums[a] + nums[b] > nums[c]):
                return nums[a] + nums[b] + nums[c]
            else:
                a -= 1
                b -= 1
                c -= 1

        return 0
```
<i class="fa-solid fa-clock"></i> Runtime: **10** ms \| Beats **86.88%**    
<i class="fa-solid fa-memory"></i> Memory: **18.72** MB \| Beats **45.77%**    

가장 긴 둘레를 구해야 하기 때문에 sort()로 정렬하고 뒤에서부터 시작했다. 세 변의 길이가 같거나, 가장 긴 변의 길이가 나머지 두 변의 합보다 짧으면 삼각형을 만들 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/largest-perimeter-triangle/solutions/7229559/sort-then-greedy-checkbeats-100-by-anwen-kyrl/" target="_blank">1st</a>

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
       nums.sort(reverse=True)
       return next((x+y+z for x,y,z in zip(nums, nums[1:], nums[2:]) if x<y+z), 0)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

<mark>next()</mark>는 처음으로 조건에 만족하는 값 `x+y+z`를 반환한다.