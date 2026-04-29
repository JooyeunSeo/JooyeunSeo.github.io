---
excerpt: "'LeetCode: Set Matrix Zeroes' 풀이 정리"
title: "\073. Set Matrix Zeroes"
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

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
- Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
- Output: [[1,0,1],[0,0,0],[1,0,1]]

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
- Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
- Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

**Constraints:**

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2<sup>31</sup> <= matrix[i][j] <= 2<sup>31</sup> - 1


**Follow up:**

- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with O(1) space.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False

        for i in range(m):
            for j in range(n):
                if i == 0 and matrix[0][j] == 0 and not first_row_zero: # 첫 행에 0 포함 여부 체크
                    first_row_zero = True
                if j == 0 and matrix[i][0] == 0 and not first_col_zero: # 첫 열에 0 포함 여부 체크
                    first_col_zero = True
                if i > 0 and j > 0 and matrix[i][j] == 0:               # (1,1)부터 첫 행과 열에 마킹
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):                                           # 마킹 체크하며 내부 채우기 
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:                                              # 첫 행 처리
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:                                              # 첫 열 처리
            for i in range(m):
                matrix[i][0] = 0

        return matrix
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **88.81%**    
<i class="fa-solid fa-memory"></i> Memory: **20.23** MB \| Beats **56.82%**    

𝑂(1)의 공간만 사용해서 풀기 위해서 첫 행과 첫 열에 0 포함 여부를 마킹할 수 있다. 다만 처음부터 첫 열이나 첫 행에 0이 있을 경우 내부에 있는 0을 마킹한 것과 구분이 되지 않기 때문에 두 부분을 나눠서 봐야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/set-matrix-zeroes/solutions/657430/python-solution-w-approach-explanation-r-vh4j/" target="_blank">1st</a>

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
        
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    