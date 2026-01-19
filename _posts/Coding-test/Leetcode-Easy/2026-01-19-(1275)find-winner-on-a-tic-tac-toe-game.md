---
excerpt: "'LeetCode: Find Winner on a Tic Tac Toe Game' 풀이 정리"
title: "\01275. Find Winner on a Tic Tac Toe Game"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Matrix
  - Simulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

- Players take turns placing characters into empty squares `' '`.
- The first player `A` always places `'X'` characters, while the second player `B` always places `'O'` characters.
- `'X'` and `'O'` characters are always placed into empty squares, never on filled ones.
- The game ends when there are **three** of the same (non-empty) character filling any row, column, - or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Given a 2D integer array `moves` where moves[i] = [row<sub>i</sub>, col<sub>i</sub>] indicates that the i<sup>th</sup> move will be played on grid[row<sub>i</sub>][col<sub>i</sub>]. return *the winner of the game if it exists* (`A` or `B`). In case the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of **Tic-Tac-Toe**), the grid is initially empty, and `A` will play first.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/22/xo1-grid.jpg)
- Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
- Output: "A"
- Explanation: A wins, they always play first.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/09/22/xo2-grid.jpg)
- Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
- Output: "B"
- Explanation: B wins.

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/09/22/xo3-grid.jpg)
- Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
- Output: "Draw"
- Explanation: The game ends in a draw since there are no moves to make.

**Constraints:**

- 1 <= moves.length <= 9
- moves[i].length == 2
- 0 <= row<sub>i</sub>, col<sub>i</sub> <= 2
- There are no repeated elements on `moves`.
- `moves` follow the rules of tic tac toe.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">It's straightforward to check if A or B won or not, check for each row/column/diag if all the three are the same.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Then if no one wins, the game is a draw iff the board is full, i.e. moves.length = 9 otherwise is pending.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = anti = 0             # 왼쪽->오른쪽 대각선, 반대방향 대각선

        player = 1                  # A = +1, B = -1

        for r, c in moves:
            rows[r] += player
            cols[c] += player
            
            if r == c:              # [0,0] or [1,1] or [2,2]
                diag += player
            if r + c == 2:          # [0,2] or [1,1] or [2,0]
                anti += player

            if 3 in ( abs(rows[r]), abs(cols[c]), abs(diag), abs(anti) ):
                return "A" if player == 1 else "B"

            player *= -1            # 턴 바꾸기

        return "Draw" if len(moves) == 9 else "Pending"     # 승부가 나지 않았을 경우
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.34** MB \| Beats **14.96%**    

한 행(rows[r])이나 열(cols[c]) 또는 2개의 대각선(diag, anti)에 누적된 합이 `3` 또는 `-3`이면 같은 플레이어가 한 줄을 모두 채웠다는 것을 알 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/solutions/441319/javapython-3-check-rows-columns-and-two-n0yqc/" target="_blank">1st</a>

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row, col = [[0] * 3 for _ in range(2)], [[0] * 3 for _ in range(2)]
        d1, d2 = [0] * 2, [0] * 2
        id = 0        # 0=A, 1=B
        for r, c in moves:
            row[id][r] += 1
            col[id][c] += 1
            d1[id] += (r == c)
            d2[id] += (r + c == 2)  
            if 3 in (row[id][r], col[id][c], d1[id], d2[id]):
                return 'AB'[id]
            id ^= 1   # XOR 토글로 플레이어 전환
        return 'Draw' if len(moves) == 9 else 'Pending'
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

id `0` 또는 `1`으로 플레이어를 구분하고 있다. 그리고 `r == c` 또는 `r + c == 2`의 불리언 값을 정수로 사용하여 대각선 누적값에 더하는 것을 볼 수 있다.