---
excerpt: "'LeetCode: Rank Transform of an Array' 풀이 정리"
title: "\01331. Rank Transform of an Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Sorting
  - Biweekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.

**Example 1:**

- Input: arr = [40,10,20,30]
- Output: [4,1,2,3]
- Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

**Example 2:**

- Input: arr = [100,100,100]
- Output: [1,1,1]
- Explanation: Same elements share the same rank.

**Example 3:**

- Input: arr = [37,12,28,9,100,56,80,5,12]
- Output: [5,3,4,2,8,6,7,1,3]

**Constraints:**

- 0 <= arr.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= arr[i] <= 10<sup>9</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Use a temporary array to copy the array and sort it.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">The rank of each element is the number of unique elements smaller than it in the sorted array plus one.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {}
        temp = sorted(set(arr))

        for i, num in enumerate(temp):
            table[num] = i + 1

        return [table[num] for num in arr]
```
<i class="fa-solid fa-clock"></i> Runtime: **31** ms \| Beats **92.38%**    
<i class="fa-solid fa-memory"></i> Memory: **37.79** MB \| Beats **37.75%**    

set()으로 중복된 원소를 없앤 후 sorted()로 정렬된 리스트를 만들었다. 임시 리스트에서 각 원소의 `index + 1`이 rank가 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/rank-transform-of-an-array/solutions/489753/javacpython-hashmap-by-lee215-2kqv/" target="_blank">1st</a>

```python
class Solution:
    def arrayRankTransform(self, A):
        rank = {}
        for a in sorted(A):
            rank.setdefault(a, len(rank) + 1)
        return list(map(rank.get, A))   # [rank[x] for x in A]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

딕셔너리의 <mark>setdefault(key, value)</mark>는 키가 없을 때만 값을 저장할 수 있다. 값(rank)은 `현재까지 저장된 키 개수 + 1`이다.