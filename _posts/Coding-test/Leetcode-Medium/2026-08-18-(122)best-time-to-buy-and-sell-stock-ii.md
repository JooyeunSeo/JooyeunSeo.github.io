---
excerpt: "'LeetCode: Best Time to Buy and Sell Stock II' 풀이 정리"
title: "\0122. Best Time to Buy and Sell Stock II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Dynamic Programming
  - Greedy
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the i<sup>th</sup> day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can sell and buy the stock multiple times on the **same day**, ensuring you never hold more than one share of the stock.

Find and return the **maximum** profit you can achieve.

**Example 1:**

- Input: prices = [7,1,5,3,6,4]
- Output: 7
- Explanation:      
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.    
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.    
Total profit is 4 + 3 = 7.

**Example 2:**

- Input: prices = [1,2,3,4,5]
- Output: 4
- Explanation:     
Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.     
Total profit is 4.

**Example 3:**

- Input: prices = [7,6,4,3,1]
- Output: 0
- Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

**Constraints:**

- 1 <= prices.length <= 3 \* 10<sup>4</sup>
- 0 <= prices[i] <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(len(prices)-1):
            tdy, tmr = prices[i], prices[i+1]
            if tdy < tmr:
                total_profit += tmr - tdy
        
        return total_profit
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **20.36** MB \| Beats **52.69%**    

이 문제의 규칙은 
- 같은 날에 주식을 팔고 나서 다시 구매할 수 있다.
- 거래 횟수의 제한이 없다.
- 미래의 가격을 모두 알고 있다.

이기 때문에 매일 바로 다음날의 가격과 비교하여 이익이 날 때만 결과에 더해주면 한 번의 순회로 최대 이익을 구할 수 있다.


<a href="https://jooyeunseo.github.io/leetcode-easy/(121)best-time-to-buy-and-sell-stock/" target="_blank">121. Best Time to Buy and Sell Stock</a>

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solutions/5816678/video-sell-a-stock-immediately-by-niits-nquk/" target="_blank">1st</a>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    