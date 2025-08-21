---
excerpt: "'LeetCode: Image Smoother' 풀이 정리"
title: "\0661. Image Smoother"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Matrix
---

## <i class="fa-solid fa-file-lines"></i> Description

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

![](https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg)

Given an `m x n` integer matrix `img` representing the grayscale of an image, return *the image after applying the smoother on each cell of it.*

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg)
- Input: img = [[1,1,1],[1,0,1],[1,1,1]]
- Output: [[0,0,0],[0,0,0],[0,0,0]]
- Explanation:    
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0   
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0   
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg)
- Input: img = [[100,200,100],[200,50,200],[100,200,100]]
- Output: [[137,141,137],[141,138,141],[137,141,137]]
- Explanation:    
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137   
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141   
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

**Constraints:**

- m == img.length
- n == img[i].length
- 1 <= m, n <= 200
- 0 <= img[i][j] <= 255

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        dirctions = [                       # 현재 가리키는 셀(0,0) 및 주변 셀의 이동 방향
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        rows, cols = len(img), len(img[0])  # 행렬 크기
        new_img = []                        # 새 행렬

        for i in range(rows):               # 행 기준으로 한 줄씩 새로 생성
            new_row = []
                                
            for j in range(cols):           # 현재 가리키는 셀과 주변 셀의 값 평균
                total = 0                       # 값의 합
                amount = 0                      # 값이 있는 셀 개수

                for dr, dc in dirctions:        
                    nr = i + dr                     # 새 행 인덱스
                    nc = j + dc                     # 새 열 인덱스
                    # 새 행/열 인덱스가 모두 유효한 경우에만 평균 계산에 값 넣기
                    if (0 <= nr < rows) and (0 <= nc < cols):
                        total += img[nr][nc]
                        amount += 1
                new_row.append(int(total / amount)) # 구한 평균을 new_row에 넣기

            new_img.append(new_row)                 # 한 행 완성

        return new_img
```
<i class="fa-solid fa-clock"></i> Runtime: **219** ms \| Beats **71.43%**    
<i class="fa-solid fa-memory"></i> Memory: **13.39** MB \| Beats **93.14%**

좌표의 변화를 `(행 변화량, 열 변화량)`으로 표현한 방향 벡터를 리스트에 넣어서 반복하면 깔끔하게 주변 이웃을 탐색할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/image-smoother/solutions/4423391/video-give-me-10-minutes-how-we-think-ab-y3wd/" target="_blank">1st</a>

```python
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the image matrix
        rows, cols = len(img), len(img[0])
        
        # Define a helper function to calculate the average value for a pixel
        def average_value(r, c):
            total, count = 0, 0

            # Define the boundaries for the neighboring pixels
            top = max(0, r - 1)
            bottom = min(rows, r + 2)
            left = max(0, c - 1)
            right = min(cols, c + 2)

            # Iterate over the neighboring pixels and calculate the sum and count
            for row in range(top, bottom):
                for col in range(left, right):
                    total += img[row][col]
                    count += 1

            # Calculate and return the average value for the pixel
            return total // count

        # Apply the average function to each pixel in the image matrix
        return [[average_value(r, c) for c in range(cols)] for r in range(rows)]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(rows\*cols)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(rows\*cols)            

<mark>max()</mark>와 <mark>min()</mark>을 이용하여 유효한 범위 내에서만 평균을 계산하는 효율적인 방법이 있었다.

### <a href="https://leetcode.com/problems/image-smoother/solutions/4423344/beats-100-explained-with-video-cjavapyth-qsg0/" target="_blank">2nd</a>

```python
class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = self.smoothen(img, i, j)

        return res

    def smoothen(self, img, x, y):
        m, n = len(img), len(img[0])
        _sum, count = 0, 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n:
                    _sum += img[nx][ny]
                    count += 1

        return _sum // count
```
유효한 범위를 제한하는 또 다른 방법도 참고해봤다. 이번 문제처럼 코드가 복잡한 경우에는 이렇게 따로 함수를 만드는 것이 더 깔끔한 것 같다.