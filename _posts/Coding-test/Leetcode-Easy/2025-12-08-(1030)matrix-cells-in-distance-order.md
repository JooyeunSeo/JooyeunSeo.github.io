---
excerpt: "'LeetCode: Matrix Cells in Distance Order' 풀이 정리"
title: "\01030. Matrix Cells in Distance Order"
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
  - Sorting
  - Matrix
  - Weekly Contest
  - Manhattan distance
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given four integers `row`, `cols`, `rCenter`, and `cCenter`. There is a `rows x cols` matrix and you are on the cell with the coordinates `(rCenter, cCenter)`.

*Return the coordinates of all cells in the matrix, sorted by their **distance** from* `(rCenter, cCenter)` *from the smallest distance to the largest distance*. You may return the answer in **any order** that satisfies this condition.

The **distance** between two cells `(r1, c1)` and `(r2, c2)` is `|r1 - r2| + |c1 - c2|`.

**Example 1:**

- Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
- Output: [[0,0],[0,1]]
- Explanation: The distances from (0, 0) to other cells are: [0,1]

**Example 2:**

- Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
- Output: [[0,1],[0,0],[1,1],[1,0]]
- Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]      
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

**Example 3:**

- Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
- Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
- Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]       
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

**Constraints:**

- 1 <= rows, cols <= 100
- 0 <= rCenter < rows
- 0 <= cCenter < cols

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        max_dist = rows + cols - 2                  # 최대 거리
        buckets = [[] for _ in range(max_dist+1)]   # 버킷 생성
        result = []

        for r in range(rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                buckets[dist].append([r, c])

        for b in buckets:
            result.extend(b)
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **98.67%**    
<i class="fa-solid fa-memory"></i> Memory: **19.52** MB \| Beats **39.25%**    

각 거리별로 **버킷**에 담은 뒤, 마지막에 합치는 방법을 사용하여 sort 정렬없이 풀었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/matrix-cells-in-distance-order/solutions/278746/python-straightforward-dfs-bfs-by-cenkay-8gfx/" target="_blank">1st</a>

```python
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        bfs = [[r0, c0]]      # 현재 레벨(거리)의 셀들
        res = []              
        seen = {(r0, c0)}     # 방문한 셀 체크
        
        while bfs:
            res += bfs        # 현재 레벨의 모든 셀 추가(거리 순서대로 채워짐)
            new = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1): # 상하좌우로 거리 +1
                    if 0 <= x < R and 0 <= y < C and (x, y) not in seen:    # 미방문한 유효 좌표만 추가
                        seen.add((x, y))
                        new.append([x, y])
            bfs = new
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑟\*𝑐)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑟\*𝑐)     

**맨해튼 거리** 순서대로 셀을 방문하는 **BFS** 코드이다. 맨해튼 거리는 두 점 사이를 수평(x축)과 수직(y축)으로만 이동하는 거리의 합으로, 시작점에서부터 마름모 모양으로 확장되는 순서를 따르게 된다. 때문에 정렬하거나 거리 계산을 할 필요가 없어서 sort 방식보다 빠르게 풀 수 있다.

### <a href="https://leetcode.com/problems/matrix-cells-in-distance-order/solutions/278786/python-1-line-sorting-based-solution-by-euv35/" target="_blank">2nd</a>

```python
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - r0) + abs(pj - c0)

        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑟\*𝑐log(𝑟\*𝑐))    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑟\*𝑐)    

거리 계산 함수를 key로 사용하여 sort하는 방법도 있다.