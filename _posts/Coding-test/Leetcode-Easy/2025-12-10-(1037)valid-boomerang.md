---
excerpt: "'LeetCode: Valid Boomerang' 풀이 정리"
title: "\01037. Valid Boomerang"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Geometry
  - Weekly Contest
  - Shoelace formula
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array `points` where points[i] = [x<sub>i</sub>, y<sub>i</sub>] represents a point on the **X-Y** plane, return `true` *if these points are a boomerang.*

A **boomerang** is a set of three points that are **all distinct and not in a straight line**.

**Example 1:**

- Input: points = [[1,1],[2,3],[3,2]]
- Output: true

**Example 2:**

- Input: points = [[1,1],[2,2],[3,3]]
- Output: false

**Constraints:**

- points.length == 3
- points[i].length == 2
- 0 <= x<sub>i</sub>, y<sub>i</sub> <= 100

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">3 points form a boomerang if and only if the triangle formed from them has non-zero area.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        area = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) * 0.5
        return area != 0
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.64** MB \| Beats **82.52%**    

세 점으로 만들어진 삼각형의 넓이를 **신발끈 공식**을 이용해서 구했다. 넓이가 0이면 삼각형이 될 수 없는 조건이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-boomerang/solutions/5053709/boomerang-check-detecting-collinearity-i-x1ir/" target="_blank">1st</a>

```python
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[1][1]-points[0][1])*(points[2][0]-points[1][0]) != (points[2][1]-points[1][1])*(points[1][0]-points[0][0])
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

세 점이 모두 일직선상에 있는지만 확인하면 되기 때문에 두 **기울기**를 비교하는 방법을 사용해도 된다.

<pre>
      slope1                slope2
(y2-y1) / (x2-x1)  =  (y3-y2) / (x3-x2)
                   ↓
(y2−y1) * (x3−x2)  =  (y3−y2) * (x2−x1)
</pre>