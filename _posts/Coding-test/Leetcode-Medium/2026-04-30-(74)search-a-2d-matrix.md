---
excerpt: "'LeetCode: Search a 2D Matrix' 풀이 정리"
title: "\074. Search a 2D Matrix"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
  - Matrix
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
- Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)
- Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
- Output: false

**Constraints:**

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target:
                l = m + 1
            else:
                r = m - 1

        row = r
        if row < 0 or row > len(matrix)-1:
            return False

        l, r = 0, len(matrix[0]) - 1        
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.54** MB \| Beats **40.83%**    

먼저 각 행의 첫 번째 숫자를 기준으로 이진 탐색해서 target이 속할 수 있는 행을 찾아낸다. 그 후 해당 행 안에서 다시 이진 탐색해서 target이 있는지 체크한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/search-a-2d-matrix/solutions/6750177/video-simple-solution-by-niits-xp0d/" target="_blank">1st</a>

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // cols, mid % cols
            guess = matrix[row][col]

            if guess == target:
                return True
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log(𝑚\*𝑛)) = 𝑂(log𝑚 + log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

2차원 배열을 1차원으로 펼쳐서(flatten) 이진 탐색하는 방법으로, 더 깔끔하고 자주 사용되는 방법이다.