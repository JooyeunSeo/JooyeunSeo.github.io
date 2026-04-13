---
excerpt: "'LeetCode: Spiral Matrix II' 풀이 정리"
title: "\059. Spiral Matrix II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Matrix
  - Simulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from 1 to n<sup>2</sup> in spiral order.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)
- Input: n = 3
- Output: [[1,2,3],[8,9,4],[7,6,5]]

**Example 2:**

- Input: n = 1
- Output: [[1]]

**Constraints:**

- 1 <= n <= 20

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, left, bottom, right = 0, 0, n-1, n-1
        number = 1

        while number <= n * n:
            for i in range(left, right+1):          # top행
                matrix[top][i] = number
                number += 1
            top += 1

            if top <= bottom:
                for i in range(top, bottom+1):      # right열
                    matrix[i][right] = number
                    number += 1
                right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):  # bottom행
                    matrix[bottom][i] = number
                    number += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):  # left열
                    matrix[i][left] = number
                    number += 1
                left += 1

        return matrix
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.33** MB \| Beats **55.32%**    

<a href="https://jooyeunseo.github.io/leetcode-medium/(54)spiral-matrix/" target="_blank">54. Spiral Matrix</a> 문제를 응용한 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/spiral-matrix-ii/solutions/6174635/video-explanation-by-niits-xfom/" target="_blank">1st</a>

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    x, y, dx, dy = 0, 0, 1, 0
    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n * n):
        res[y][x] = i + 1

        if not 0 <= x + dx < n or not 0 <= y + dy < n or res[y+dy][x+dx] != 0:
            dx, dy = -dy, dx
        
        x += dx
        y += dy

    return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛<sup>2</sup>)    