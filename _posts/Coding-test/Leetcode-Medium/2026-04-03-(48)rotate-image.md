---
excerpt: "'LeetCode: Rotate Image' 풀이 정리"
title: "\048. Rotate Image"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Matrix
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a>, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
- Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
- Output: [[7,4,1],[8,5,2],[9,6,3]]

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
- Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
- Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

**Constraints:**

- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        row, col = 0, n-1
        
        for i in range(n // 2):                 # 레이어
            for j in range(i, (n - 1 - i)):     # 레이어에서 4방향 이동
                temp = matrix[i][j]                                     # 상단 값 저장
                matrix[i][j] = matrix[n - 1 - j][i]                     # ↱
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]     # ↖
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]     # ↵
                matrix[j][n - 1 - i] = temp                             # ↴
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.32** MB \| Beats **46.38%**    

레이어별(i)로 순회하면서 각 위치(j)의 4개 좌표(상하좌우)를 회전시켰다. 좌표 4개를 돌리는 부분은 상단 가장 왼쪽 값을 임시로 저장 후, 시계 반대 방향으로 이동하면서 값을 왼쪽으로 밀어넣는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/rotate-image/solutions/7484792/clean-simple-beats-easy-to-understand-ef-alpj/" target="_blank">1st</a>

```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for k in range(row):
            matrix[k].reverse()
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1) 

행렬을 먼저 대각선 기준으로 뒤집어서 행을 열로 바꾼 뒤, 각 행(가로)을 거꾸로 뒤집으면 90도로 시계 방향 회전한 결과와 같게 된다.

### <a href="https://leetcode.com/problems/rotate-image/solutions/6146973/vertical-reversal-transpose-by-niits-81gh/" target="_blank">2nd</a>

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            for col in range(edge_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row+1, edge_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix
```
여기서는 먼저 각 열(세로)을 거꾸로 뒤집은 후 대각선으로 뒤집는 순서를 사용했다.
