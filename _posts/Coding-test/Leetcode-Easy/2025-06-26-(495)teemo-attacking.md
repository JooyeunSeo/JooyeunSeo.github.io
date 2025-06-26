---
excerpt: "'LeetCode: Teemo Attacking' 풀이 정리"
title: "\0495. Teemo Attacking"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Simulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly `duration` seconds. More formally, an attack at second `t` will mean Ashe is poisoned during the **inclusive** time interval `[t, t + duration - 1]`. If Teemo attacks again **before** the poison effect ends, the timer for it is **reset**, and the poison effect will end `duration` seconds after the new attack.

You are given a **non-decreasing** integer array `timeSeries`, where `timeSeries[i]` denotes that Teemo attacks Ashe at second `timeSeries[i]`, and an integer `duration`.

Return *the **total** number of seconds that Ashe is poisoned*.

**Example 1:**

- Input: timeSeries = [1,4], duration = 2
- Output: 4
- Explanation: Teemo's attacks on Ashe go as follows:
   - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
   - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.   
   Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

**Example 2:**

- Input: timeSeries = [1,2], duration = 2
- Output: 3
- Explanation: Teemo's attacks on Ashe go as follows:
   - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
   - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.   
   Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

**Constraints:**

- 1 <= timeSeries.length <= 10<sup>4</sup>
- 0 <= timeSeries[i], duration <= 10<sup>7</sup>
- `timeSeries` is sorted in **non-decreasing** order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n = len(timeSeries)
        total = 0

        for i in range(n):
            if i == n - 1 or timeSeries[i+1] - timeSeries[i] >= duration:
                total += duration
            else:
                total += timeSeries[i+1] - timeSeries[i]

        return total
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **78.93%**    
<i class="fa-solid fa-memory"></i> Memory: **13.16** MB \| Beats **72.19%**

1초부터 timeSeries의 마지막 초까지 1초씩 탐색하면 시간 초과되기 때문에 현재 공격 초와 다음 공격 초의 차이를 계산해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/teemo-attacking/solutions/6664292/on-master-the-overlap-trick-to-track-poi-nhld/" target="_blank">1st</a>

```python
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        res = 0
        n = len(timeSeries)

        for i in range(n - 1):
            d = timeSeries[i + 1] - timeSeries[i]
            res += duration if d > duration else d

        return res + (duration if n else 0)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)          

for문의 범위를 다르게 하는 것으로 더 간단하게 만들 수 있다.

### <a href="https://leetcode.com/problems/teemo-attacking/solutions/97475/python-solution-for-teemo-by-llx9-v774/" target="_blank">2nd</a>

```python
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans
```
모든 공격마다 duration 초 만큼 중독 상태를 유지한다고 가정한 뒤, 중복된 부분만큼 빼는 방법이다.