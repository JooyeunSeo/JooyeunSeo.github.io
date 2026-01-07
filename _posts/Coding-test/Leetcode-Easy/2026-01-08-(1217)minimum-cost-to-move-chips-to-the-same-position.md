---
excerpt: "'LeetCode: Minimum Cost to Move Chips to The Same Position' 풀이 정리"
title: "\01217. Minimum Cost to Move Chips to The Same Position"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Greedy
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

We have `n` chips, where the position of the i<sup>th</sup> chip is `position[i]`.

We need to move all the chips to **the same position**. In one step, we can change the position of the i<sup>th</sup> chip from `position[i]` to:

- `position[i] + 2` or `position[i] - 2` with `cost = 0`.
- `position[i] + 1` or `position[i] - 1` with `cost = 1`.

Return *the minimum cost* needed to move all the chips to the same position.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg)
- Input: position = [1,2,3]
- Output: 1
- Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg)
- Input: position = [2,2,2,3,3]
- Output: 2
- Explanation:      
We can move the two chips at position 3 to position 2.     
Each move has cost = 1. The total cost = 2.

**Example 3:**

- Input: position = [1,1000000000]
- Output: 1

**Constraints:**

- 1 <= position.length <= 100
- 1 <= position[i] <= 10<sup>9</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">The first move keeps the parity of the element as it is.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">The second move changes the parity of the element.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Since the first move is free, if all the numbers have the same parity, the answer would be zero.</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">Find the minimum cost to make all the numbers have the same parity.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_nums, odd_nums = 0, 0

        for n in position:
            if n % 2 == 0:
                even_nums += 1
            else:
                odd_nums += 1
        
        return min(even_nums, odd_nums)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.28** MB \| Beats **21.46%**    

짝수 간격으로는 얼마든지 0 코스트로 이동할 수 있고 패리티를 바꾸는 순간에만 비용이 들기 때문에 짝수와 홀수 중 개수가 더 많은 쪽으로 이동하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/solutions/398342/python-simple-oddeven-approach-with-expl-tsb0/" target="_blank">1st</a>

```python
def minCostToMoveChips(self, chips: List[int]) -> int:
	odds = sum(x % 2 for x in chips)
	return min(odds, len(chips) - odds)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    