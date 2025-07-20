---
excerpt: "'LeetCode: Reshape the Matrix' 풀이 정리"
title: "\0566. Reshape the Matrix"
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
---

## <i class="fa-solid fa-file-lines"></i> Description

In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new one with a different size `r x c` keeping its original data.

You are given an `m x n` matrix `mat` and two integers `r` and `c` representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the `reshape` operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg)
- Input: mat = [[1,2],[3,4]], r = 1, c = 4
- Output: [[1,2,3,4]]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg)
- Input: mat = [[1,2],[3,4]], r = 2, c = 4
- Output: [[1,2],[3,4]]

**Constraints:**

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- -1000 <= mat[i][j] <= 1000
- 1 <= r, c <= 300

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index. Now, how will you convert 1-d index into 2-d indices?</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Try to use division and modulus to convert 1-d index into 2-d indices.</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">M[i] => M[i/n][i%n] Will it result in right mapping? Take some example and check this formula.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:      # 두 행렬의 원소 개수가 다르면 mat 그대로 반환
            return mat
        
        # 1차원 행렬로 변환
        d1 = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                d1[n*i + j] = mat[i][j]
        
        # 2차원 행렬로 재변환
        d2 = []
        for row_idx in range(r):
            d2.append(d1[row_idx*c : (row_idx+1)*c])

        return d2
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.81** MB \| Beats **92.40%**

행렬을 1차원으로 변환 후 새로운 행과 열에 맞춰 재배열하는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reshape-the-matrix/solutions/1317225/python-one-pass-clean-concise-by-hiepit-dp9y/" target="_blank">1st</a>

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n: return mat  # Invalid size -> return original matrix
        ans = [[0] * c for _ in range(r)]
        for i in range(m * n):
            ans[i // c][i % c] = mat[i // n][i % n]
        return ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚*𝑛)           

mat를 1차원 행렬로 변환했다가 다시 2차원으로 변환하는 과정을 한 번으로 압축하는 방법이다. 리스트 컴프리헨션을 통해 새 배열의 구조를 미리 만드는 부분을 참고했다.