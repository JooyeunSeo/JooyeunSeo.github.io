---
excerpt: "'LeetCode: Combination Sum II' 풀이 정리"
title: "\040. Combination Sum II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Backtracking
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Example 1:**

- Input: candidates = [10,1,2,7,6,1,5], target = 8
- Output:            
[           
[1,1,6],           
[1,2,5],           
[1,7],           
[2,6]           
]

**Example 2:**

- Input: candidates = [2,5,2,1,2], target = 5
- Output:            
[           
[1,2,2],           
[5]           
]

**Constraints:**

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, total, comb):
            if total == target:
                res.append(comb.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:  # 중복 숫자 스킵
                    continue
                if total + candidates[i] > target:                  # 그 뒤 조합 스킵
                    break

                comb.append(candidates[i])
                dfs(i + 1, total + candidates[i], comb)
                comb.pop()

        candidates.sort()
        res = []
        dfs(0, 0, [])
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **86.66%**    
<i class="fa-solid fa-memory"></i> Memory: **19.54** MB \| Beats **60.64%**    

<a href="https://jooyeunseo.github.io/leetcode-medium/(39)combination-sum/" target="_blank">39. Combination Sum</a> 문제와 비슷하지만 이번에는 같은 숫자를 재사용할 수 없고 중복된 숫자가 존재한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/combination-sum-ii/solutions/6097940/video-solution-by-niits-0rtj/" target="_blank">1st</a>

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(target, start, comb):
            if target < 0:
                return
            if target == 0:
                res.append(comb)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], i+1, comb+[candidates[i]])

        dfs(target, 0, [])
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(2<sup>𝑛</sup>)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

이 방법은 매번 comb 리스트를 새로 생성하기 때문에 메모리는 더 사용하지만 append와 pop이 필요 없기 때문에 간단하다.