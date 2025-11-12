---
excerpt: "'LeetCode: Transpose Matrix' 풀이 정리"
title: "\0867. Transpose Matrix"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Matrix
  - Simulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a 2D integer array `matrix`, return *the **transpose** of* `matrix`.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

![](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

**Example 1:**

- Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
- Output: [[1,4,7],[2,5,8],[3,6,9]]

**Example 2:**

- Input: matrix = [[1,2,3],[4,5,6]]
- Output: [[1,4],[2,5],[3,6]]

**Constraints:**

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= m \* n <= 10<sup>5</sup>
- -10<sup>9</sup> <= matrix[i][j] <= 10<sup>9</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">We don't need any special algorithms to do this. You just need to know what the transpose of a matrix looks like. Rows become columns and vice versa!</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                result[c][r] = matrix[r][c]

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.06** MB \| Beats **37.39%**

전치 행렬을 새로 생성한 후, 행과 열의 인덱스를 변경한 위치에 값을 넣어주는 방법이 가장 많이 쓰이는 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/transpose-matrix/solutions/6097971/video-give-me-5-minutes-2-solutions-how-ihrf8/" target="_blank">1st</a>

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        for c in range(len(matrix[0])):
            temp = []

            for r in range(len(matrix)):
                temp.append(matrix[r][c])

            res.append(temp)

        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚\*𝑛)         

미리 모든 위치를 만들어놓지 않고 한 행씩 완성해나가는 방법도 있다.