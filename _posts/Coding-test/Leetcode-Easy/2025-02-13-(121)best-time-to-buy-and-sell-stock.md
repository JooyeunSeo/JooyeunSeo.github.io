---
excerpt: "'LeetCode-Best Time to Buy and Sell Stock' 풀이 정리"
title: "\0121. Best Time to Buy and Sell Stock"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the i<sup>th</sup> day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the *maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.


**Example 1:**

- Input: prices = [7,1,5,3,6,4]
- Output: 5
- Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.   
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

- Input: prices = [7,6,4,3,1]
- Output: 0
- Explanation: In this case, no transactions are done and the max profit = 0.

**Constraints:**

- 1 <= prices.length <= 10<sup>5</sup>
- 0 <= prices[i] <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy_price = prices[0]     # 최소 구매값(첫 번째 요소부터 시작)
        max_profit = 0                # 최대 이익(0부터 시작)

        for price in prices[1:]:
            min_buy_price = min(min_buy_price, price)
            max_profit = max(max_profit, price - min_buy_price)

        return max_profit
```
<i class="fa-solid fa-clock"></i> Runtime: **130** ms \| Beats **26.47%**    
<i class="fa-solid fa-memory"></i> Memory: **19.20** MB \| Beats **47.74%**

실행 시간이 너무 느려서 다른 방법으로도 접근해봤는데, 기본적으로는 이 방법이 가장 보편적으로 사용되는 것 같다. Kadane's Algorithm을 활용한 방법이라고 하는데, 현 시점에서 가장 낮은 매수 가격과 최대 이익을 갱신하면서 최적화하는 방식이 해당 알고리즘과 비슷하기 때문인 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4868897/most-optimized-kadane-s-algorithm-java-c-python-rust-javascript/" target="_blank">1st</a>

```python
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

제출한 코드와 비슷한데, 매번 min()과 max() 함수를 호출하는 것보다 if문으로 단순 연산하는 이 방법이 훨씬 더 빠른 실행시간을 기록했다.

### <a href="" target="_blank">2nd</a>

```python
class Solution:
    def maxProfit(self,prices):
        left = 0    # Buy
        right = 1   # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
```
두 개의 포인터를 사용한 답안도 참고했다.
