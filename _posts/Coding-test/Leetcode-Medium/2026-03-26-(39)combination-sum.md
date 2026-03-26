---
excerpt: "'LeetCode: Combination Sum' 풀이 정리"
title: "\039. Combination Sum"
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

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

*[frequency]: The frequency of an element x is the number of times it occurs in the array.

**Example 1:**

- Input: candidates = [2,3,6,7], target = 7
- Output: [[2,2,3],[7]]
- Explanation:     
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.      
7 is a candidate, and 7 = 7.      
These are the only two combinations.     

**Example 2:**

- Input: candidates = [2,3,5], target = 8
- Output: [[2,2,2,2],[2,3,3],[3,5]]

**Example 3:**

- Input: candidates = [2], target = 1
- Output: []

**Constraints:**

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of `candidates` are **distinct**.
- 1 <= target <= 40

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, total, comb):
            if total == target:
                res.append(comb.copy())
                return

            for i in range(start, len(candidates)):
                if total + candidates[i] > target:      # 그 뒤 조합 스킵
                    break
                comb.append(candidates[i])              
                dfs(i, total + candidates[i], comb)     # 현재 숫자 선택 후 다시 재귀호출
                comb.pop()                              # 원래 조합으로 복귀

        candidates.sort()
        res = []
        dfs(0, 0, [])

        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **95.20%**    
<i class="fa-solid fa-memory"></i> Memory: **19.74** MB \| Beats **25.28%**    

현재 상태를 저장했다가 다시 되돌아오는 과정이 필요하기 때문에 백트래킹이 적합한 문제다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/combination-sum/solutions/16510/python-dfs-solution-by-oldcodingfarmer-lmie/" target="_blank">1st</a>

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>(𝑡/𝑚𝑖𝑛)</sup>) ←  candidates's min        
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑡/𝑚𝑖𝑛)      

total을 따로 저장하지 않고 target에서 값을 깎는 방법으로 풀 수도 있다.