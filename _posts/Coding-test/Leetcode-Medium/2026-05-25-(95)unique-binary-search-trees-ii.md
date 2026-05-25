---
excerpt: "'LeetCode: Unique Binary Search Trees II' 풀이 정리"
title: "\095. Unique Binary Search Trees II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Dynamic Programming
  - Backtracking
  - Binary Search Tree
  - Binary Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `n`, return all the structurally unique **BST**'s (binary search trees), which has exactly `n` nodes of unique values from `1` to `n`. Return the answer in **any order.**

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)
- Input: n = 3
- Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

**Example 2:**

- Input: n = 1
- Output: [[1]]

**Constraints:**

- 1 <= n <= 8

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start, end):
            if start > end:                             # 만들 수 있는 숫자가 없으면 빈 트리 반환
                return [None]

            trees = []

            for root_val in range(start, end + 1):      # root 후보 선택
                left_trees = build(start, root_val - 1) # 가능한 모든 왼쪽 서브트리
                right_trees = build(root_val + 1, end)  # 가능한 모든 오른쪽 서브트리

                for left in left_trees:                 # 왼쪽 × 오른쪽 모든 조합 연결
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right

                        trees.append(root)

            return trees

        return build(1, n)
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **57.32%**    
<i class="fa-solid fa-memory"></i> Memory: **20.38** MB \| Beats **51.79%**    

각 root마다 가능한 왼쪽 트리들과 오른쪽 트리들을 전부 조합해서 새로운 트리를 만드는 구조다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-binary-search-trees-ii/solutions/6116084/video-3-important-points-by-niits-auvc/" target="_blank">1st</a>

```python
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        memo = {}

        def generate_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            
            trees = []
            if start > end:
                trees.append(None)
                return trees
            
            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1)
                right_trees = generate_trees(root_val + 1, end)
            
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)
            
            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑪<sub>𝑛</sub>) ← Catalan number   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑪<sub>𝑛</sub>)    

같은 범위의 BST들을 매번 새로 생성하기 때문에 메모이제이션으로 중복 재귀를 제거하면 성능을 더 올릴 수 있다.