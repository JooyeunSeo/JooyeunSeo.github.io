---
excerpt: "'LeetCode: Can Place Flowers' 풀이 정리"
title: "\0605. Can Place Flowers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Greedy
---

## <i class="fa-solid fa-file-lines"></i> Description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` *if* `n` *new flowers can be planted in the* `flowerbed` *without violating the no-adjacent-flowers rule and* `false` *otherwise.*

**Example 1:**

- Input: flowerbed = [1,0,0,0,1], n = 1
- Output: true

**Example 2:**

- Input: flowerbed = [1,0,0,0,1], n = 2
- Output: false

**Constraints:**

- 1 <= flowerbed.length <= 2 * 10<sup>4</sup>
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.
- 0 <= n <= flowerbed.length

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        plots = len(flowerbed)

        for i in range(plots):
            if n == 0:
                break

            if flowerbed[i] == 0 and \
               (i == 0 or flowerbed[i-1] == 0) and \
               (i == plots-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1

        return n == 0
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **97.29%**    
<i class="fa-solid fa-memory"></i> Memory: **12.96** MB \| Beats **73.88%**

밭의 왼쪽, 오른쪽을 조건문으로 처리하고 n이 0이 되는 순간 반복문을 조기 종료하도록 했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/can-place-flowers/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

왼쪽, 오른쪽을 변수로 만들어서 가독성을 향상시킬 수 있다.

### <a href="https://leetcode.com/problems/can-place-flowers/solutions/5839959/simple-solution-with-explanation/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">2nd</a>

```python
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        i = 0
        while i < length and n > 0:
            if flowerbed[i] == 1:
                i += 2  # Skip next spot since a flower is planted at i
            elif i == length - 1 or flowerbed[i + 1] == 0:
                # Plant a flower if it's the last spot or the next spot is empty
                n -= 1
                i += 2  # Move two steps forward since we just planted
            else:
                i += 3  # Skip to the next possible empty spot
        return n <= 0  # If all flowers are planted, return True
```
가독성은 조금 낮지만 꽃을 심을 수 없는 자리는 스킵하기 때문에 위의 코드들보다 효율적이다.