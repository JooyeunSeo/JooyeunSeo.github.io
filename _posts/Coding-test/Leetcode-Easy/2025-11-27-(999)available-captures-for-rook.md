---
excerpt: "'LeetCode: Available Captures for Rook' 풀이 정리"
title: "\0999. Available Captures for Rook"
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

You are given an `8 x 8` **matrix** representing a chessboard. There is **exactly one** white rook represented by `'R'`, some number of white bishops `'B'`, and some number of black pawns `'p'`. Empty squares are represented by `'.'`.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is **attacking** a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the **number of pawns** the white rook is **attacking**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG)
- Input:      
   <pre>
   board = [[".",".",".",".",".",".",".","."],    
            [".",".",".","p",".",".",".","."],    
            [".",".",".","R",".",".",".","p"],    
            [".",".",".",".",".",".",".","."],    
            [".",".",".",".",".",".",".","."],    
            [".",".",".","p",".",".",".","."],    
            [".",".",".",".",".",".",".","."],    
            [".",".",".",".",".",".",".","."]]
   </pre>
- Output: 3
- Explanation: In this example, the rook is attacking all the pawns.

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG)
- Input:     
   <pre>
   board = [[".",".",".",".",".",".",".","."],
            [".","p","p","p","p","p",".","."],
            [".","p","p","B","p","p",".","."],
            [".","p","B","R","B","p",".","."],
            [".","p","p","B","p","p",".","."],
            [".","p","p","p","p","p",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
   </pre>
- Output: 0
- Explanation: The bishops are blocking the rook from attacking any of the pawns.

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG)
- Input:    
   <pre>
   board = [[".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            ["p","p",".","R",".","p","B","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","B",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
   </pre>
- Output: 3
- Explanation: The rook is attacking the pawns at positions b5, d6, and f5.

**Constraints:**

- board.length == 8
- board[i].length == 8
- `board[i][j]` is either `'R'`, `'.'`, `'B'`, or `'p'`
- There is exactly one cell with `board[i][j] == 'R'`


## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        attacks = 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r_pos = (i, j)
                    break
        
        u, d, l, r = r_pos[0], r_pos[0], r_pos[1], r_pos[1]
        
        while u > 0:
            if board[u-1][r_pos[1]] == 'B':
                break
            if board[u-1][r_pos[1]] == 'p':
                attacks += 1
                break
            u -= 1
        
        while d < 7:
            if board[d+1][r_pos[1]] == 'B':
                break
            if board[d+1][r_pos[1]] == 'p':
                attacks += 1
                break
            d += 1
        
        while l > 0:
            if board[r_pos[0]][l-1] == 'B':
                break
            if board[r_pos[0]][l-1] == 'p':
                attacks += 1
                break
            l -= 1
        
        while r < 7:
            if board[r_pos[0]][r+1] == 'B':
                break
            if board[r_pos[0]][r+1] == 'p':
                attacks += 1
                break
            r += 1
        
        return attacks
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.77** MB \| Beats **61.19%**    

먼저 룩을 찾은 뒤, 룩의 위치를 중심으로 4방향을 조회했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/available-captures-for-rook/solutions/242932/javacpython-straight-forward-solution-by-mevg/" target="_blank">1st</a>

```python
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j
        res = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + i, y0 + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p': res += 1
                if board[x][y] != '.': break
                x, y = x + i, y + j
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

forloop 하나에서 4방향 모두를 처리하는 방법을 참고했다.