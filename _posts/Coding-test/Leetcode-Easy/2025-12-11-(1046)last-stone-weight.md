---
excerpt: "'LeetCode: Last Stone Weight' 풀이 정리"
title: "\01046. Last Stone Weight"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Heap (Priority Queue)
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an array of integers `stones` where `stones[i]` is the weight of the i<sub>th</sub> stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return *the weight of the last remaining stone*. If there are no stones left, return `0`.

**Example 1:**

- Input: stones = [2,7,4,1,8,1]
- Output: 1
- Explanation:       
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,      
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,      
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,      
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

**Example 2:**

- Input: stones = [1]
- Output: 1

**Constraints:**

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Simulate the process. We can do it with a heap, or by sorting some list of stones every time we take a turn.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        # 값에 -를 붙여서 최소힙으로 변경
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            # # 가장 무거운 돌 두 개를 꺼내서 부호 되돌리기
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            # 두 돌의 차이가 남는 경우만 다시 힙에 push
            if y > x:
                heapq.heappush(heap, -(y - x))

        # 남은 돌이 있으면 부호를 되돌려서 반환    
        return -heap[0] if heap else 0
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.86** MB \| Beats **30.70%**    

매번 정렬하는 것은 비효율적이기 때문에 힙을 사용했다. 파이썬에서는 최소힙만 지원하기 때문에 값의 부호를 변경해서 최대힙처럼 만드는 방법을 사용해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/last-stone-weight/solutions/294956/javacpython-priority-queue-by-lee215-p4p3/" target="_blank">1st</a>

```python
class Solution:
    def lastStoneWeight(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

먼저 리스트 원소들의 부호를 반대로 변경한 뒤, heapq 모듈의 `heapify()`를 이용하여 최소힙으로 만드는 방법도 있다.

```python
class Solution:
    def lastStoneWeight(self, A):
        A.sort()
        while len(A) > 1:
            bisect.insort(A, A.pop() - A.pop())
        return A[0]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

정렬로만 푸는 방법은 효율이 낮다. 참고로 <mark>bisect</mark>는 정렬된 리스트에서 값을 빠르게 찾거나 삽입할 위치를 알 수 있는 라이브러리이다.