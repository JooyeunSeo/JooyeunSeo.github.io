---
excerpt: "'LeetCode: Construct the Rectangle' 풀이 정리"
title: "\0492. Construct the Rectangle"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
---

## <i class="fa-solid fa-file-lines"></i> Description

A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.
2. The width `W` should not be larger than the length `L`, which means `L >= W`.
3. The difference between length `L` and width `W` should be as small as possible.
Return *an array `[L, W]` where `L` and `W` are the length and width of the web page you designed in sequence.*

**Example 1:**

- Input: area = 4
- Output: [2,2]
- Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].    
But according to requirement 2, [1,4] is illegal;    
according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

**Example 2:**

- Input: area = 37
- Output: [37,1]

**Example 3:**

- Input: area = 122122
- Output: [427,286]

**Constraints:**

- 1 <= area <= 10<sup>7</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">The W is always less than or equal to the square root of the area, so we start searching at sqrt(area) till we find the result.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l = area    # 초기 길이 값
        w = 1       # 초기 너비 값
        combinations = []

        while l >= w:             # 길이가 너비보다 크거나 같은 경우만
            if l * w == area:     
                combinations.append((l, w))
            w += 1          # 너비를 1 증가
            l = area // w   # 해당 너비에 가능한 최대 길이

        return combinations[-1] # 마지막에 들어간 조합 반환 (e.g. [(1,4), (2,2)])
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.50** MB \| Beats **65.38%**

`l - w`의 값을 최소화하는 조합을 찾기 위해 너비 값 w를 1씩 늘리는 것으로 고정하는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/construct-the-rectangle/solutions/6851877/simple-python-solution-beats-100-by-user-ie69/" target="_blank">1st</a>

```python
from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w = int(sqrt(area))
        while area % w:         # area가 w로 나누어떨어질 때까지
            w -= 1                # w를 줄이며 약수 찾기
        return [area//w, w]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(√𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

l과 w가 `√area`에 가까울 때 둘의 차이가 가장 작아진다는 것을 활용한 방법이다.

### <a href="https://leetcode.com/problems/construct-the-rectangle/solutions/899176/python-a-simple-for-loop-by-blue_sky5-wu4n/" target="_blank">2nd</a>

```python
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for l in range(int(area**0.5), 0, -1):            
            if area % l == 0: 
                return [area // l, l]
```
w의 범위를 for문으로 명시하는 방식으로 푼 답안이다. 변수 이름이 l이지만 의미상 너비에 해당하기 때문에 w로 이름을 바꾸는 것이 더 명확한 것 같다.