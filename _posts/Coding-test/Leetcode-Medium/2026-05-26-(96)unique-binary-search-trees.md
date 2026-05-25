---
excerpt: "'LeetCode: Unique Binary Search Trees' 풀이 정리"
title: "\096. Unique Binary Search Trees"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Math
  - Dynamic Programming
  - Binary Search Tree
  - Catalan number
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `n`, return the number of structurally unique **BST**'s (binary search trees) which has exactly `n` nodes of unique values from `1` to `n`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)
- Input: n = 3
- Output: 5

**Example 2:**

- Input: n = 1
- Output: 1

**Constraints:**

- 1 <= n <= 19

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)                      # 노드 n개로 만들 수 있는 BST 개수 저장

        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            total = 0

            for root in range(1, nodes + 1):    # 루트 선택
                left = root - 1                 # 왼쪽 노드 수
                right = nodes - root            # 오른쪽 노드 수
                total += dp[left] * dp[right]   # 조합 수 계산

            dp[nodes] = total

        return dp[n]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.12** MB \| Beats **87.84%**    

실제로 트리를 만들어야 하는 <a href="https://jooyeunseo.github.io/leetcode-medium/(95)unique-binary-search-trees-ii/" target="_blank">95. Unique Binary Search Trees II</a>와 달리 노드 개수에 따라 만들 수 있는 BST 개수만 세면 되기 때문에 더 간단하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-binary-search-trees/solutions/1565543/cpython-5-easy-solutions-w-explanation-o-ohmi/" target="_blank">1st</a>

```python
class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1
        return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

`@cache`는 내부적으로 `memo = {}`와 같은 딕셔너리를 자동 생성 후 한 번 계산한 numTrees(n)의 결과를 저장한다. 