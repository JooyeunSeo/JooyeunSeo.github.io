---
excerpt: "'LeetCode: Unique Paths II' 풀이 정리"
title: "\063. Unique Paths II"
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

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10<sup>9</sup>.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)
- Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
- Output: 2
- Explanation: There is one obstacle in the middle of the 3x3 grid above.     
There are two ways to reach the bottom-right corner:
   1. Right -> Right -> Down -> Down
   2. Down -> Down -> Right -> Right

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)
- Input: obstacleGrid = [[0,1],[0,0]]
- Output: 1

**Constraints:**

- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is `0` or `1`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Use dynamic programming since, from each cell, you can move to the right or down.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">assume dp[i][j] is the number of unique paths to reach (i, j). dp[i][j] = dp[i][j -1] + dp[i - 1][j]. Be careful when you encounter an obstacle. set its value in dp to 0.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]        # 위에서 내려온 값 + 왼쪽 값

        return dp[-1]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.26** MB \| Beats **91.65%**    

1차원 배열 하나로 위에서 내려온 값과 왼쪽의 값을 더해서 누적할 수 있다.

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
{: style="color: blue;"}
<pre>
i   obstacleGrid   dp
                   [1, 0, 0]
0   [0, 0, 0]      [1, 1, 1]
1   [0, 1, 0]      [1, 0, 1]
2   [0, 0, 0]      [1, 1, 2]
</pre>

return 2
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-paths-ii/solutions/7430274/easy-python-code-with-full-dry-run-examp-1zoa/" target="_blank">1st</a>

```python
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # If start or end is blocked
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        # Initialize start
        grid[0][0] = 1

        # Initialize first row
        for i in range(1, n):
            if grid[0][i] == 0 and grid[0][i - 1] == 1:
                grid[0][i] = 1
            else:
                grid[0][i] = 0

        # Initialize first column
        for j in range(1, m):
            if grid[j][0] == 0 and grid[j - 1][0] == 1:
                grid[j][0] = 1
            else:
                grid[j][0] = 0

        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    