---
excerpt: "'LeetCode: Rectangle Overlap' 풀이 정리"
title: "\0836. Rectangle Overlap"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Geometry
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is **positive**. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true` *if they overlap, otherwise return* `false`.

**Example 1:**

- Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
- Output: true

**Example 2:**

- Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
- Output: false

**Example 3:**

- Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
- Output: false

**Constraints:**

- rec1.length == 4
- rec2.length == 4
- -10<sup>9</sup> <= rec1[i], rec2[i] <= 10<sup>9</sup>
- `rec1` and `rec2` represent a valid rectangle with a non-zero area.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 겹치지 않는 조건: rec2가 rec1보다 완전히 오른쪽or왼쪽or위쪽or아래쪽에 있는 경우
        if rec2[0] >= rec1[2] or rec2[2] <= rec1[0] or rec2[1] >= rec1[3] or rec2[3] <= rec1[1]:
            return False
        # 넷 중 어느 한 쪽이라도 겹친다면 True
        else:
            return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats **79.60%**

두 사각형이 겹치지 않는 조건을 먼저 파악했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/rectangle-overlap/solutions/235202/elegant-python-solution-beat-100-by-infi-mh8e/" target="_blank">1st</a>

```python
class Solution:
    def isRectangleOverlap(self, rec1: 'List[int]', rec2: 'List[int]') -> 'bool':
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        bottom = max(rec1[1], rec2[1])
        up = min(rec1[3], rec2[3])
        
        if left < right and up > bottom:
            return True
        else:
            return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

두 사각형의 교집합 영역을 계산해서 양수일 경우 겹쳤다고 판단할 수 있다.