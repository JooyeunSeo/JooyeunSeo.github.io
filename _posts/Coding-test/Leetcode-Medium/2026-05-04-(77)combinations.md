---
excerpt: "'LeetCode: Combinations' 풀이 정리"
title: "\077. Combinations"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Backtracking
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two integers `n` and `k`, return all possible combinations of k numbers chosen from the range `[1, n]`.

You may return the answer in **any order.**

**Example 1:**

- Input: n = 4, k = 2
- Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
- Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

**Example 2:**

- Input: n = 1, k = 1
- Output: [[1]]
- Explanation: There is 1 choose 1 = 1 total combination.

**Constraints:**

- 1 <= n <= 20
- 1 <= k <= n

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, comb):
            if len(comb) == k:
                result.append(comb[:])
                return
            
            for i in range(start, n - (k - len(comb)) + 2):
                dfs(i+1, comb + [i])

        result = []
        dfs(1, [])
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **83** ms \| Beats **85.76%**    
<i class="fa-solid fa-memory"></i> Memory: **61.31** MB \| Beats **53.51%**    

핵심은 항상 오름차순으로만 생성해서 이미 [1,2]가 생성된 시점에 [2,1]이 중복 생성되지 않도록 방지하고, 불가능한 조합(e.g. comb 시작부터 마지막 숫자 n 등장)을 계속 탐색하지 않도록 i 범위를 조절하는 것에 있다.

n = 4      
k = 2
{: style="color: blue;"}
<pre>
[]
 ├─ 1 → [1]
 ⎪       ├─ 2 → [1,2]
 ⎪       ├─ 3 → [1,3]
 ⎪       └─ 4 → [1,4]
 ├─ 2 → [2]
 ⎪       ├─ 3 → [2,3]
 ⎪       └─ 4 → [2,4]
 └─ 3 → [3]
         └─ 4 → [3,4]
   (4 → 시도x)
</pre>

return [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/combinations/solutions/5418489/video-simple-backtracking-solution-by-ni-ug0h/" target="_blank">1st</a>

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑘)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑘)    

가지치기 없이 완전 탐색하는 백트래킹이다.