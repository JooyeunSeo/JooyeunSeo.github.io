---
excerpt: "'LeetCode: Permutations' 풀이 정리"
title: "\046. Permutations"
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

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

*[permutation]: A permutation is a rearrangement of all the elements of an array.

**Example 1:**

- Input: nums = [1,2,3]
- Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

**Example 2:**

- Input: nums = [0,1]
- Output: [[0,1],[1,0]]

**Example 3:**

- Input: nums = [1]
- Output: [[1]]

**Constraints:**

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of `nums` are **unique**.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path) == len(nums):          # 종료조건
                result.append(path.copy())
                return

            for num in nums:
                if num not in path:
                    path.append(num)            # num 추가
                    dfs(path)                   # 재귀 호출
                    path.pop()                  # num 제거

        result = []
        dfs([])

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.57** MB \| Beats **49.57%**    

현재까지 방문했던 숫자를 path에 저장하고, for문으로 매번 모든 선택지를 순회하며 path에 포함되어 있는지 확인하는 방법이다.

nums = [1, 2, 3]
{: style="color: blue;"}
<pre>
nums           path
├─ 1           [1]
│  ├─ 2
│  │  └─ 3   → [1,2,3]
│  └─ 3
│     └─ 2   → [1,3,2]
│  
├─ 2           [2] (1 out)
│  ├─ 1
│  │  └─ 3   → [2,1,3]
│  └─ 3
│     └─ 1   → [2,3,1]
│  
└─ 3           [3] (2 out)
   ├─ 1
   │  └─ 2   → [3,1,2]
   └─ 2
      └─ 1   → [3,2,1]
</pre>

return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/permutations/solutions/6914844/most-optimal-approach-swapping-beats-100-638l/" target="_blank">1st</a>

```python
class Solution:
    def permute(self, nums):
        res = []
        
        def perms(i):                       # 현재 채울 자리 i
            if i == len(nums):
                res.append(nums[:])
                return
            for j in range(i, len(nums)):   # i와 swap할 j 후보
                nums[i], nums[j] = nums[j], nums[i]   # swap  
                perms(i + 1)                          # 다음 자리 채우기
                nums[i], nums[j] = nums[j], nums[i]   # nums 복구

        perms(0)
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑛!)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

nums 내에서 자리(i)를 기준으로 값을 바꿨다가 재귀가 끝나면 다시 되돌리는 방법으로, 따로 path를 만들지 않기 때문에 공간을 더 절약할 수 있다.

nums = [1, 2, 3]
{: style="color: blue;"}
<pre>
 nums   i j    swap
[1,2,3] 0↔︎0 → [1,2,3] → perms(1)
  [1,2,3] 1↔︎1 → [1,2,3] → perms(2)
    [1,2,3] 2↔︎2 → [1,2,3] → perms(3) → append
    (복구) 2↔︎2 → [1,2,3]
  (복구) 1↔︎1 → [1,2,3]

  [1,2,3] 1↔︎2 → [1,3,2] → perms(2)
    [1,3,2] 2↔︎2 → [1,3,2] → perms(3) → append
    (복구) 2↔︎2 → [1,3,2]
  (복구) 1↔︎2 → [1,2,3]
(복구) 0↔︎0 → [1,2,3]

[1,2,3] 0↔︎1 → [2,1,3] → perms(1)
  [2,1,3] 1↔︎1 → [2,1,3] → perms(2)
    [2,1,3] 2↔︎2 → [2,1,3] → perms(3) → append 
    (복구) 2↔︎2 → [2,1,3]
  (복구) 1↔︎1 → [2,1,3]

  [2,1,3] 1↔︎2 → [2,3,1] → perms(2)
    [2,3,1] 2↔︎2 → [2,3,1] → perms(3) → append
    (복구) 2↔︎2 → [2,3,1]
  (복구) 1↔︎2 → [2,1,3]
(복구) 0↔︎1 → [1,2,3]

[1,2,3] 0↔︎2 → [3,2,1] → perms(1)
  [3,2,1] 1↔︎1 → [3,2,1] → perms(2)
    [3,2,1] 2↔︎2 → [3,2,1] → perms(3) → append
    (복구) 2↔︎2 → [3,2,1]
  (복구) 1↔︎1 → [3,2,1]

  [3,2,1] 1↔︎2 → [3,1,2] → perms(2)
    [3,1,2] 2↔︎2 → [3,1,2] → perms(3) → append
    (복구) 2↔︎2 → [3,1,2]
  (복구) 1↔︎2 → [3,2,1]
(복구) 0↔︎2 → [1,2,3]
</pre>

return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
{: style="color: green;"}