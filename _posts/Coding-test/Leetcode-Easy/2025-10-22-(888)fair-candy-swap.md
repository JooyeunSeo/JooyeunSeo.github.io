---
excerpt: "'LeetCode: Fair Candy Swap' 풀이 정리"
title: "\0888. Fair Candy Swap"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Binary Search
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Alice and Bob have a different total number of candies. You are given two integer arrays `aliceSizes` and `bobSizes` where `aliceSizes[i]` is the number of candies of the i<sup>th</sup> box of candy that Alice has and `bobSizes[j]` is the number of candies of the j<sup>th</sup> box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return *an integer array* `answer` *where* `answer[0]` *is the number of candies in the box that Alice must exchange, and* `answer[1]` *is the number of candies in the box that Bob must exchange*. If there are multiple answers, you may **return any** one of them. It is guaranteed that at least one answer exists.

**Example 1:**

- Input: aliceSizes = [1,1], bobSizes = [2,2]
- Output: [1,2]

**Example 2:**

- Input: aliceSizes = [1,2], bobSizes = [2,3]
- Output: [1,2]

**Example 3:**

- Input: aliceSizes = [2], bobSizes = [1,3]
- Output: [2,3]

**Constraints:**

- 1 <= aliceSizes.length, bobSizes.length <= 10<sup>4</sup>
- 1 <= aliceSizes[i], bobSizes[j] <= 105<sup>5</sup
- Alice and Bob have a different total number of candies.
- There will be at least one valid answer for the given input.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sum_alice, sum_bob = sum(aliceSizes), sum(bobSizes) # 각자 가진 사탕의 총합
        delta = (sum_alice - sum_bob) // 2                  # alice와 bob의 합 차이의 절반(보정량)
        alice_set, bob_set = set(aliceSizes), set(bobSizes)

        for alice_exchange in alice_set:                    # alice_exchange: alice가 교환할 사탕 개수
            bob_exchange = alice_exchange - delta           # bob_exchange: bob이 교환할 사탕 개수
            if bob_exchange in bob_set:
                return [alice_exchange, bob_exchange]
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **93.36%**    
<i class="fa-solid fa-memory"></i> Memory: **14.52** MB \| Beats **22.82%**

서로 교환해야 할 사탕의 개수만 필요하기 때문에 각자 가진 사탕의 총합을 구한 후, 리스트를 <mark>set()</mark>으로 변경해서 효율을 높였다. 항상 답을 보장하는 문제이기 때문에 첫 번째로 조건에 맞는 쌍이 나왔을 때 바로 리턴하도록 했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/fair-candy-swap/solutions/6202408/easy-binary-search-with-explanation-pyth-ar7x/" target="_blank">1st</a>

```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Calculate the total candy size for Alice and Bob
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        
        # Calculate the difference between their totals
        diff = (bob_total - alice_total) // 2
        
        # Sort Bob's candy sizes for binary search
        bobSizes.sort()
        
        # Helper function for binary search
        def binary_search(target):
            left, right = 0, len(bobSizes) - 1
            while left <= right:
                mid = (left + right) // 2
                if bobSizes[mid] == target:
                    return True
                elif bobSizes[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        # Check for each candy size in Alice's list
        for candy in aliceSizes:
            if binary_search(candy + diff):
                return [candy, candy + diff]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂((𝑛+𝑚)log𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

Sorting과 Binary Search를 사용해도 된다. set을 이용한 방법보다 느리지만 문제 topics에 있는 태그이기 때문에 참고했다.