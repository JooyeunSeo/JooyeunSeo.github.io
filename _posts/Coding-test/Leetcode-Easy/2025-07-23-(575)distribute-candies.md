---
excerpt: "'LeetCode: Distribute Candies' 풀이 정리"
title: "\0575. Distribute Candies"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
---

## <i class="fa-solid fa-file-lines"></i> Description

Alice has `n` candies, where the i<sup>th</sup> candy is of type `candyType[i]`. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat `n / 2` of the candies she has (`n` is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array `candyType` of length `n`, return *the **maximum** number of different types of candies she can eat if she only eats* `n / 2` *of them.*

**Example 1:**

- Input: candyType = [1,1,2,2,3,3]
- Output: 3
- Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

**Example 2:**

- Input: candyType = [1,1,2,3]
- Output: 2
- Explanation: Alice can only eat 4 / 2 = 2 candies.    
Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

**Example 3:**

- Input: candyType = [6,6,6,6]
- Output: 1
- Explanation: Alice can only eat 4 / 2 = 2 candies.    
Even though she can eat 2 candies, she only has 1 type.

**Constraints:**

- n == candyType.length
- 2 <= n <= 10<sup>4</sup>
- `n` is even.
- -10<sup>5</sup> <= candyType[i] <= 10<sup>5</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">To maximize the number of kinds of candies, we should try to distribute candies such that Alice will gain all kinds.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">What is the upper limit of the number of kinds of candies Alice will gain? Remember candies are to distributed equally.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Which data structure is the most suitable for finding the number of kinds of candies?</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">Will hashset solves the problem? Inserting all candies kind in the hashset and then checking its size with upper limit.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        amount = len(candyType) // 2  # 섭취 가능한 최대 캔디 개수
        kinds = len(set(candyType))   # 캔디 종류 개수

        return min(amount, kinds)   
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **83.33%**    
<i class="fa-solid fa-memory"></i> Memory: **14.16** MB \| Beats **60.56%**

태그는 해시 테이블로 되어있지만 이 문제에서는 단순히 중복 없는 원소 수만 필요하기 때문에 딕셔너리보다 **해시 셋**을 쓰는 것이 더 효율적이다.