---
excerpt: "'LeetCode: Number of Recent Calls' 풀이 정리"
title: "\0933. Number of Recent Calls"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Design
  - Queue
  - Data Stream
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

**Example 1:**

- Input    
["RecentCounter", "ping", "ping", "ping", "ping"]    
[[], [1], [100], [3001], [3002]]
- Output    
[null, 1, 2, 3, 3]
- Explanation    
RecentCounter recentCounter = new RecentCounter();    
recentCounter.ping(1);     // requests = [<u>1</u>], range is [-2999,1], return 1    
recentCounter.ping(100);   // requests = [<u>1</u>, <u>100</u>], range is [-2900,100], return 2    
recentCounter.ping(3001);  // requests = [<u>1</u>, <u>100</u>, <u>3001</u>], range is [1,3001], return 3    
recentCounter.ping(3002);  // requests = [1, <u>100</u>, <u>3001</u>, <u>3002</u>], range is [2,3002], return 3    

**Constraints:**

- 1 <= t <= 10<sup>9</sup>
- Each test case will call `ping` with **strictly increasing** values of `t`.
- At most 10<sup>4</sup> calls will be made to `ping`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t-3000:
            self.requests.popleft()
        return len(self.requests)
            
            
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```
<i class="fa-solid fa-clock"></i> Runtime: **22** ms \| Beats **95.31%**    
<i class="fa-solid fa-memory"></i> Memory: **23.13** MB \| Beats **41.34%**

ping에 매개변수로 들어오는 값이 점점 높아지는 조건이기 때문에 현재 범위의 최소값보다 작은 request는 제외해야 효율이 높아진다. 리스트로도 구현할 수 있지만 더 빠른 연산을 위해 collections 모듈의 <mark>deque()</mark>를 이용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/number-of-recent-calls/solutions/4534372/python-solution-beats-9999-os-solutions-wftw8/" target="_blank">1st</a>

```python
class RecentCounter:

    def __init__(self):
        self.counter =0
        self.queue =deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.counter+=1

        while self.queue[0] < t-3000:
            self.queue.popleft()
            self.counter-=1

        return self.counter
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1) ← per operation   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

ping()을 호출할 때마다 큐의 길이를 세는 것보다 더 효율적인 방법인 것 같다.