---
excerpt: "'LeetCode: Unique Paths' 풀이 정리"
title: "\062. Unique Paths"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Math
  - Dynamic Programming
  - Combinatorics
---

## <i class="fa-solid fa-file-lines"></i> Description

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10<sup>9</sup>.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
- Input: m = 3, n = 7
- Output: 28

**Example 2:**

- Input: m = 3, n = 2
- Output: 3
- Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
   1. Right -> Down -> Down
   2. Down -> Down -> Right
   3. Down -> Right -> Down

**Constraints:**

- 1 <= m, n <= 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d, r = (m - 1), (n - 1)     # 아래쪽 이동 횟수, 오른쪽 이동 횟수
        steps = d + r               # 총 이동 수
        c = math.factorial(steps) // (math.factorial(steps - d) * math.factorial(d))
        return c
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.55** MB \| Beats **16.79%**    

모든 경로는 오른쪽 이동과 아래쪽 이동을 섞은 순서열과 같기 때문에 조합으로 풀 수 있다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/e9ca19980bff5f199d7a37eb0d882a6dcfa0862c)

m = 3 (d = 2)        
n = 2 (r = 1)
{: style="color: blue;"}
<pre>
3! / 2!(3 - 2)! = 3

d  d  _
d  _  d
_  d  d
</pre>

return 3
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-paths/solutions/7581882/video-calculating-up-left-by-niits-awyh/" target="_blank">1st</a>

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        aboveRow = [1] * n            # 첫 번째 행은 경우의 수 전부 1

        for _ in range(m - 1):        
            currentRow = [1] * n      # 다음 행 계산 (첫 번째 열도 항상 1)
            for i in range(1, n):
                currentRow[i] = currentRow[i-1] + aboveRow[i] # 왼쪽에서 오는 경우 + 위에서 오는 경우
            aboveRow = currentRow
        
        return aboveRow[-1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂()    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂()    

Dynamic Programming으로 푸는 방법으로, 어떤 칸까지 오는 경우의 수는 `위에서 오는 경우 + 왼쪽에서 오는 경우`인 것을 이용했다.

m = 3            
n = 3
{: style="color: blue;"}
<pre>
aboveRow    = [1, 1, 1]

currentRow  = [1, _, _]
i=1 → 1 + 1 =     2
i=2 → 2 + 1 =        3

aboveRow    = [1, 2, 3]

currentRow  = [1, _, _]
i=1 → 1 + 2 =     3
i=2 → 3 + 3 =        6

aboveRow    = [1, 3, 6]
</pre>

return 6
{: style="color: green;"}