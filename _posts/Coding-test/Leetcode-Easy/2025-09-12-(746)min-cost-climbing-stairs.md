---
excerpt: "'LeetCode: Min Cost Climbing Stairs' 풀이 정리"
title: "\0746. Min Cost Climbing Stairs"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Dynamic Programming
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `cost` where `cost[i]` is the cost of i<sup>th</sup> step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index `1`.

*Return the minimum cost to reach the top of the floor.*

**Example 1:**

- Input: cost = [10,<u>15</u>,20]
- Output: 15
- Explanation: You will start at index 1.
   - Pay 15 and climb two steps to reach the top.    
   The total cost is 15.

**Example 2:**

- Input: cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
- Output: 6
- Explanation: You will start at index 0.
   - Pay 1 and climb two steps to reach index 2.
   - Pay 1 and climb two steps to reach index 4.
   - Pay 1 and climb two steps to reach index 6.
   - Pay 1 and climb one step to reach index 7.
   - Pay 1 and climb two steps to reach index 9.
   - Pay 1 and climb one step to reach the top.     
   The total cost is 6.

**Constraints:**

- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Assuming we have n staircase labeled from 0 to n - 1 and assuming the top is n, then dp[n] = 0, marking that if you are at the top, the cost is 0.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Now, looping from n - 1 to 0, the dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]). The answer will be the minimum of dp[0] and dp[1]</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        prev2, prev1 = cost[0], cost[1]   # 2계단 뒤, 1계단 뒤

        for i in range(2, n):             # 3번째 계단부터 시작
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr
        
        return min(prev1, prev2)    # 마지막 cost[-1], cost[-2] 중 선택
```
<i class="fa-solid fa-clock"></i> Runtime: **1** ms \| Beats **83.11%**    
<i class="fa-solid fa-memory"></i> Memory: **12.47** MB \| Beats **85.11%**

점화식과 변수 2개만을 이용하는 최적화된 방법이다. 현재 계단에 이르기 위해 2계단 뒤에서 2칸 올라오거나 1계단 뒤에서 1칸 올라오는 방법 중 더 최소 비용이 드는 쪽을 선택해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/min-cost-climbing-stairs/solutions/657490/python-solution-from-a-beginner-some-eas-qrz3/" target="_blank">1st</a>

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
		    if not cost:
            return 0

        dp = [0] * len(cost)
		    dp[0] = cost[0]
		
        if len(cost) >= 2:
            dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

i번째 계단에 도달하는 최소 비용을 dp 배열에 저장할 수도 있다.

### <a href="" target="_blank">2nd</a>

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # top [10,15,20,0]
        
        for i in range(len(cost)-4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])
```
뒤에서부터 앞으로 가는 방법으로, 원본 cost 배열을 바로 수정하기 때문에 공간 낭비를 줄일 수 있다.