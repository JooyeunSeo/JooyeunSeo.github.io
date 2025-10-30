---
excerpt: "'LeetCode: X of a Kind in a Deck of Cards' 풀이 정리"
title: "\0914. X of a Kind in a Deck of Cards"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Math
  - Counting
  - Number Theory
  - Weekly Contest
  - Euclidean
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `deck` where `deck[i]` represents the number written on the i<sup>th</sup> card.

Partition the cards into **one or more groups** such that:

- Each group has **exactly** `x` cards where `x > 1`, and
- All the cards in one group have the same integer written on them.

Return `true` *if such partition is possible, or* `false` *otherwise.*

**Example 1:**

- Input: deck = [1,2,3,4,4,3,2,1]
- Output: true
- Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

**Example 2:**

- Input: deck = [1,1,1,2,2,2,3,3]
- Output: false
- Explanation: No possible partition.

**Constraints:**

- 1 <= deck.length <= 10<sup>4</sup>
- 0 <= deck[i] < 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}

        for card in deck:
            count[card] = count.get(card, 0) + 1
        
        values = [v for v in count.values()]        # 각 카드 개수
        g = 0                                       # 현재까지 최대공약수

        for v in values:
            g = math.gcd(g, v)

        return g > 1
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **75.33%**    
<i class="fa-solid fa-memory"></i> Memory: **18.09** MB \| Beats **79.84%**

딕셔너리에 각 카드마다 개수를 세서 저장한 후, 파이썬 3.5부터 사용 가능한 <mark>math.gcd()</mark> 모듈로 최대공약수(GCD)를 구했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solutions/175845/cjavapython-greatest-common-divisor-by-l-ibi5/" target="_blank">1st</a>

```python
class Solution:
    def hasGroupsSizeX(self, deck):
        # a%b가 0이면 b가 최대공약수, 0이 아니면 a=b, b=a%b 로 바꾸고 반복
        def gcd(a, b):
            while b: a, b = b, a % b  
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)  

GCD를 구하는 모듈 없이 **유클리드 호제법(Euclidean algorithm)**으로 직접 구현하는 방법도 참고했다. 또 <mark>functools.reduce()</mark> 모듈로 count의 원소에 함수를 차례로 적용시켰다.