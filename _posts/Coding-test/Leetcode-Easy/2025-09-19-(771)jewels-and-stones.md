---
excerpt: "'LeetCode: Jewels and Stones' 풀이 정리"
title: "\0771. Jewels and Stones"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Hash Table
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.


**Example 1:**

- Input: jewels = "aA", stones = "aAAbbbb"
- Output: 3

**Example 2:**

- Input: jewels = "z", stones = "ZZ"
- Output: 0

**Constraints:**

- 1 <= jewels.length, stones.length <= 50
- `jewels` and `stones` consist of only English letters.
- All the characters of jewels are **unique**.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">For each stone, check if it is a jewel.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.36** MB \| Beats **80.20%**

jewels 문자열에서 바로 해당 stone이 있는지 찾는 방식으로 카운트했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/jewels-and-stones/solutions/6743190/master-set-lookup-to-count-jewels-in-sto-8exv/" target="_blank">1st</a>

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels_set = set(jewels)
        return sum(s in jewels_set for s in stones)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

문자열에서 문자를 검색하는 것보다 **해시셋**을 조회하는 것이 훨씬 빠르기 때문에 입력 크기를 고려해서 해시셋을 쓰는 것이 더 좋다.