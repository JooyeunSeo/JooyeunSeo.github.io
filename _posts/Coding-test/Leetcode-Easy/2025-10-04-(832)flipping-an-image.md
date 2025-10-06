---
excerpt: "'LeetCode: Flipping an Image' 풀이 정리"
title: "\0832. Flipping an Image"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
  - Bit Manipulation
  - Matrix
  - Simulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an `n x n` binary matrix `image`, flip the image **horizontally**, then invert it, and return **the resulting image.**

To flip an image horizontally means that each row of the image is reversed.

- For example, flipping `[1,1,0]` horizontally results in `[0,1,1]`.

To invert an image means that each 0 is replaced by `1`, and each `1` is replaced by `0`.

- For example, inverting `[0,1,1]` results in `[1,0,0]`.

**Example 1:**

- Input: image = [[1,1,0],[1,0,1],[0,0,0]]
- Output: [[1,0,0],[0,1,0],[1,1,1]]
- Explanation:     
First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].     
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]      

**Example 2:**

- Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
- Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
- Explanation:      
First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].     
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

**Constraints:**

- n == image.length
- n == image[i].length
- 1 <= n <= 20
- `images[i][j]` is either `0` or `1`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        for row in image:
            new_row = []

            for bit in row[::-1]:           # 거꾸로 순회
                new_row.append(bit ^ 1)     # 0^1=1, 1^1=0
            
            result.append(new_row)

        return result
                
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.49** MB \| Beats **53.63%**

**XOR**을 이용하여 비트를 반전시켰다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/flipping-an-image/solutions/130590/javacpython-reverse-and-toggle-by-lee215-ee9e/" target="_blank">1st</a>

```python
    def flipAndInvertImage(self, A):
        return [[1 ^ i for i in reversed(row)] for row in A]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛<sup>2</sup>)           

<mark>reversed()</mark> 함수로 순서를 바꿀 수도 있다.

### <a href="https://leetcode.com/problems/flipping-an-image/solutions/6759015/master-row-flip-invert-in-a-2d-binary-im-wcen/" target="_blank">2nd</a>

```python
class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            i, j = 0, len(row) - 1
            while i <= j:
                if i == j:
                    row[i] ^= 1
                else:
                    row[i], row[j] = row[j] ^ 1, row[i] ^ 1
                i += 1
                j -= 1
        return image
```
각 row마다 맨 앞과 뒤에서 시작하는 두 개의 포인터를 사용하는 방법도 있다. row의 절반까지만 탐색하면 되고, 원본 리스트를 수정하기 때문에 더 효율적이다.