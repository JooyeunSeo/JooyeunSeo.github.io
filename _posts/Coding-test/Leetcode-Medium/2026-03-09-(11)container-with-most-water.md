---
excerpt: "'LeetCode: Container With Most Water' 풀이 정리"
title: "\011. Container With Most Water"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
  - Greedy
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i<sup>th</sup> line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store.*

**Notice** that you may not slant the container.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
- Input: height = [1,8,6,2,5,4,8,3,7]
- Output: 49
- Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

- Input: height = [1,1]
- Output: 1

**Constraints:**

- n == height.length
- 2 <= n <= 10<sup>5</sup>
- 0 <= height[i] <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">If you simulate the problem, it will be O(n^2) which is not efficient.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">How can you calculate the amount of water at each step?</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1    # 왼쪽 벽, 오른쪽 벽
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
```
<i class="fa-solid fa-clock"></i> Runtime: **54** ms \| Beats **76.04%**    
<i class="fa-solid fa-memory"></i> Memory: **29.41** MB \| Beats **96.11%**    

물 높이는 더 낮은 쪽 벽이 결정하기 때문에 낮은 벽을 움직여서 더 높은 벽이 있는지 찾으면 된다.