---
excerpt: "'LeetCode: Valid Sudoku' 풀이 정리"
title: "\036. Valid Sudoku"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Matrix
---

## <i class="fa-solid fa-file-lines"></i> Description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules:**

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1:**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
- Input: board =       
    <pre>
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    </pre>
- Output: true

**Example 2:**

- Input: board =       
    <pre>
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    </pre>
- Output: false
- Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

**Constraints:**

- board.length == 9
- board[i].length == 9
- `board[i][j]` is a digit `1-9` or `'.'`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]        # 각 행
        cols = [set() for _ in range(9)]        # 각 열
        boxes = [set() for _ in range(9)]       # 각 3x3 박스
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue

                b = ((r // 3) * 3) + (c // 3)   # 3x3 박스 인덱스 계산

                if (val in rows[r]) or (val in cols[c]) or (val in boxes[b]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)
        
        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.32** MB \| Beats **62.67%**    

해시셋으로 각 행, 열, 3x3 서브 박스들에 중복이 있는지 체크하는 방법이다. 서브 박스들은 또 하나의 3x3 grid처럼 인덱스를 매길 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)       
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)     

한 셀에 대한 행, 열, 서브 박스 정보를 모두 res에 넣은 뒤 마지막에 해시셋으로 변경해서 중복이 있는지 확인하는 방법이다. 서로의 튜플 구조를 다르게 만들었기 때문에 모두 하나의 배열에 넣어도 충돌하지 않는 아이디어가 좋았다.