---
excerpt: "'LeetCode: Number of Equivalent Domino Pairs' 풀이 정리"
title: "\01128. Number of Equivalent Domino Pairs"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Counting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`) - that is, one domino can be rotated to be equal to another domino.

Return *the number of pairs* `(i, j)` *for which* `0 <= i < j < dominoes.length`*, and* `dominoes[i]` *is **equivalent to*** `dominoes[j]`.

**Example 1:**

- Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
- Output: 1

**Example 2:**

- Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
- Output: 3

**Constraints:**

- 1 <= dominoes.length <= 4 * 1<sup>04</sup>
- dominoes[i].length == 2
- 1 <= dominoes[i][j] <= 9

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">You can keep track of what you've seen using a hashmap.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashmap = {}
        result = 0

        for d in dominoes:
            key = tuple(sorted(d))                  # 정렬하여 통일 후 타입 변경
            hashmap[key] = hashmap.get(key, 0) + 1

        for count in hashmap.values():
            if count > 1:
                result += count * (count - 1) // 2  # 조합 C(n, 2)
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **98.02%**    
<i class="fa-solid fa-memory"></i> Memory: **23.98** MB \| Beats **91.35%**    

`sorted()`로 각 도미노의 방향을 통일해서 저장했다. 또 값을 변경 불가능한 immutable 타입만 딕셔너리의 키로 사용 가능하기 때문에 리스트를 튜플로 변경했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/number-of-equivalent-domino-pairs/solutions/6712147/on2-on-log-n-on-hashmap-cpythonjava-by-l-osnz/" target="_blank">1st</a>

```python
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        mpp = [0] * 100
        count = 0
        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            count += mpp[key]
            mpp[key] += 1
        return count
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

정렬이나 딕셔너리 없이 고정된 크기를 가진 리스트를 사용하는 최적화된 버전이다.