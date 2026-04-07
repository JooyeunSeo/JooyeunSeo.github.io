---
excerpt: "'LeetCode: Spiral Matrix' 풀이 정리"
title: "\054. Spiral Matrix"
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

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

**Constraints:**

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column. Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, left, bottom, right = 0, 0, m-1, n-1
        res = []

        while left <= right and top <= bottom:
            for i in range(left, right+1):          # top행
                res.append(matrix[top][i])
            top += 1

            if top <= bottom:                       # right열
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1

            if top <= bottom:                       # bottom행
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:                       # left열
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.30** MB \| Beats **82.65%**    

한 줄을 완성한 다음 해당 행이나 열을 한 칸 안으로 옮기고 방향을 바꾸는 식으로 계속 반복했다. if문으로 중복 순회를 막는 것이 중요했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/spiral-matrix/solutions/5513240/video-explanation-by-niits-1mqh/" target="_blank">1st</a>

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx    # 방향 벡터를 90도 회전
            
            x += dx
            y += dy
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚\*𝑛)    

이미 방문한 곳은 `'.'`으로 바꾸고 방향 벡터를 이용하여 이동하는 방법이다.

<pre>
(dx,dy)	   (-dy,dx)
( 1, 0)	→   ( 0, 1) ↓
( 0, 1)	↓   (-1, 0) ←
(-1, 0)	←   (0, -1) ↑ 
(0, -1)	↑   ( 1, 0) →
</pre>

### <a href="https://leetcode.com/problems/spiral-matrix/solutions/20571/1-liner-in-python-ruby-by-stefanpochmann-rqep/?envType=problem-list-v2&envId=2s2ff433" target="_blank">2nd</a>

```python
class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛<sup>2</sup>)    

맨 위 행을 떼고, 나머지를 반시계 방향으로 90도 회전해서 재귀 호출하는 방법이다. `[*zip(*matrix)]`(또는 `list(zip(*matrix))`)는 matrix를 한 행씩 풀어서 zip()으로 묶는 동작으로, 열 단위로 재구성된 결과가 된다. 전치(transpose)된 행렬을 거꾸로 뒤집으면 원래 matrix를 반시계 방향으로 90도 회전한 것과 같다.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
{: style="color: blue;"}
<pre>
[1,2,3]           [6,9]
[4,5,6]  [4,5,6]  [5,8]  [5,8]  [8,7]         [4]
[7,8,9]  [7,8,9]  [4,7]  [4,7]  [5,4]  [5,4]  [5]  [5]

[         1,2,3,          6,9,          8,7,        4, 5]
</pre>

return [1,2,3,6,9,8,7,4,5]
{: style="color: green;"}