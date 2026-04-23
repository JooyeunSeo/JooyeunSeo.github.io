---
excerpt: "'LeetCode: Minimum Path Sum' 풀이 정리"
title: "\064. Minimum Path Sum"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Dynamic Programming
  - Matrix
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)
- Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
- Output: 7
- Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

**Example 2:**

- Input: grid = [[1,2,3],[4,5,6]]
- Output: 12

**Constraints:**

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:             # grid[0][0]에서 시작
                    dp[j] = grid[i][j]
                elif i == 0:                      # 0행에서는 왼쪽에서 오는 값만 사용
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:                      # 0열에서는 위쪽에서 오는 값만 사용
                    dp[j] += grid[i][j]
                else:                             # min(위쪽에서 오는 값, 왼쪽에서 오는 값) 사용
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]
```
<i class="fa-solid fa-clock"></i> Runtime: **9** ms \| Beats **95.78%**    
<i class="fa-solid fa-memory"></i> Memory: **20.45** MB \| Beats **90.65%**    

1차원 배열 하나로 누적 합을 관리하는 DP 방법을 사용했다. 매 칸마다 위쪽에서 오는 방향과 왼쪽에서 오는 방향 중 비용이 더 적은 쪽을 선택해서 누적해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/minimum-path-sum/solutions/3345656/pythonjava-csimple-solutioneasy-to-under-occy/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

grid를 DP 배열로 재활용했기 때문에 추가 공간이 거의 안 드는 방법이다.