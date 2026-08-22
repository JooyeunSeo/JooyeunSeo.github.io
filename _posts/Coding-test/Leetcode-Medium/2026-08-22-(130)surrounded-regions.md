---
excerpt: "'LeetCode: Surrounded Regions' 풀이 정리"
title: "\0130. Surrounded Regions"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Depth-First Search
  - Breadth-First Search
  - Union-Find
  - Matrix
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically.
- **Region**: To form a region **connect every** `'O'` cell.
- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed** by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

**Example 1:**

- Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
- Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
- Explanation:    
![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:**

- Input: board = [["X"]]
- Output: [["X"]]

**Constraints:**

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is `'X'` or `'O'`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # 상하좌우 연결된 'O'를 전부 '#'로 변경하는 함수
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
              return
            board[r][c] = '#'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # 테두리에 연결된 'O'와 그에 연결된 'O'를 '#'로 변경
        for i in range(cols):         # 상단
            if board[0][i] == 'O':
                dfs(0, i)

        for i in range(cols):         # 하단
            if board[rows-1][i] == 'O':
                dfs(rows-1, i)

        for i in range(rows):         # 좌측
            if board[i][0] == 'O':
                dfs(i, 0)

        for i in range(rows):         # 우측
            if board[i][cols-1] == 'O':
                dfs(i, cols-1)

        # 전체 순회
        for r in range(rows):         
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **83.51%**    
<i class="fa-solid fa-memory"></i> Memory: **22.50** MB \| Beats **41.10%**    

DFS 탐색은 테두리에서만 수행하고 전체 순회는 마지막에 한 번만 하는 방식으로 효율을 높이는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/surrounded-regions/solutions/7286083/graph-traversal-dfs-optimised-approach-j-m5qe/" target="_blank">1st</a>

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(i, j):
            # Base case: out of bounds, already visited, or 'X'
            if i < 0 or i >= m or j < 0 or j >= n or vis[i][j] or board[i][j] == 'X':
                return
            
            vis[i][j] = True
            
            # DFS on neighbors
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 1 & 2. DFS from boundary 'O's to mark unflippable regions
        # Left and Right borders
        for i in range(m):
            if board[i][0] == 'O' and not vis[i][0]:
                dfs(i, 0)
            if board[i][n - 1] == 'O' and not vis[i][n - 1]:
                dfs(i, n - 1)
        
        # Top and Bottom borders
        for j in range(n):
            if board[0][j] == 'O' and not vis[0][j]:
                dfs(0, j)
            if board[m - 1][j] == 'O' and not vis[m - 1][j]:
                dfs(m - 1, j)

        # 3. Flip surrounded 'O's
        for i in range(m):
            for j in range(n):
                # If 'O' is not visited, it means it's surrounded
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚\*𝑛)    

이미 방문한 셀을 기록하는 것으로 효율을 더 높였다.