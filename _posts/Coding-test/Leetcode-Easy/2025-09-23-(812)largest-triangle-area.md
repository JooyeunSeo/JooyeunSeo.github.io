---
excerpt: "'LeetCode: Largest Triangle Area' 풀이 정리"
title: "\0812. Largest Triangle Area"
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
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of points on the **X-Y** plane `points` where points[i] = [x<sub>i</sub>, y<sub>i</sub>], return *the area of the largest triangle that can be formed by any three different points*. Answers within 10<sup>-5</sup> of the actual answer will be accepted.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)
- Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
- Output: 2.00000
- Explanation: The five points are shown in the above figure. The red triangle is the largest.

**Example 2:**

- Input: points = [[1,0],[0,0],[0,1]]
- Output: 0.50000

**Constraints:**

- 3 <= points.length <= 50
- -50 <= xi, yi <= 50
- All the given points are `unique`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        max_area = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) * 0.5
                    max_area = max(max_area, area)

        return max_area
```
<i class="fa-solid fa-clock"></i> Runtime: **59** ms \| Beats **46.90%**    
<i class="fa-solid fa-memory"></i> Memory: **12.37** MB \| Beats **84.83%**

브루트포스로 가능한 모든 세 점 조합을 뽑은 후, 각 조합에 아래의 **신발끈 공식(가우스의 면적 공식)**을 적용시켜 삼각형의 넓이를 구했다.

<figure>
  <a href="https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D" target="_blank" title="wikipedia">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/7f438dd4324f336724f124fbf8dc0c0f1b679563" alt="formula" style="display:block; margin:auto;">
  </a>
</figure>

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/largest-triangle-area/solutions/3794039/only-one-line-on-python-by-xxxxkav-dxfe/" target="_blank">1st</a>

```python
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) for [x1,y1], [x2,y2], [x3,y3] in combinations(points, 3))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>3</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

파이썬 내장 라이브러리 <mark>itertools.combinations</mark>로 가능한 모든 3개 조합을 중복없이 뽑을 수 있다.   
여기서는 **벡터 외적 공식**으로 삼각형의 넓이를 구했다.