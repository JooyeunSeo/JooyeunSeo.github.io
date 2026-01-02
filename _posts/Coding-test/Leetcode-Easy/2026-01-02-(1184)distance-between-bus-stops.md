---
excerpt: "'LeetCode: Distance Between Bus Stops' 풀이 정리"
title: "\01184. Distance Between Bus Stops"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

A bus has n stops numbered from `0` to `n - 1` that form a circle. We know the distance between all pairs of neighboring stops where `distance[i]` is the distance between the stops number `i` and `(i + 1) % n`.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given `start` and `destination` stops.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1.jpg)
- Input: distance = [1,2,3,4], start = 0, destination = 1
- Output: 1
- Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-1.jpg)
- Input: distance = [1,2,3,4], start = 0, destination = 2
- Output: 3
- Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-2.jpg)
- Input: distance = [1,2,3,4], start = 0, destination = 3
- Output: 4
- Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

**Constraints:**

- 1 <= n <= 1<sup>04</sup>
- distance.length == n
- 0 <= start, destination < n
- 0 <= distance[i] <= 1<sup>04</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Find the distance between the two stops if the bus moved in clockwise or counterclockwise directions.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        total = sum(distance)
        cw= sum(distance[ min(start, destination) : max(start, destination) ])
        ccw = total - cw

        return min(cw, ccw)
```
<i class="fa-solid fa-clock"></i> Runtime: **39** ms \| Beats **97.70%**    
<i class="fa-solid fa-memory"></i> Memory: **18.04** MB \| Beats **96.42%**    

시계방향(시작역 값이 도착역보다 작을 때)과 시계 반대방향의 거리 합은 모든 거리의 합과 같다는 것을 이용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        total = sum(distance)
        return min(clockwise, total - clockwise)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

start가 destination보다 작거나 같도록 미리 설정하면 min()이나 max()를 사용하지 않아도 된다.