---
excerpt: "'LeetCode: Binary Tree Level Order Traversal II' 풀이 정리"
title: "\0107. Binary Tree Level Order Traversal II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Breadth-First Search
  - Binary Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
- Input: root = [3,9,20,null,null,15,7]
- Output: [[15,7],[9,20],[3]]

**Example 2:**

- Input: root = [1]
- Output: [[1]]

**Example 3:**

- Input: root = []
- Output: []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- -1000 <= Node.val <= 1000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            result.append(level)

        return result[::-1]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.44** MB \| Beats **72.06%**    

<a href="https://leetcode.com/problems/binary-tree-level-order-traversal-ii/?envType=problem-list-v2&envId=2s2ff433" target="_blank">102. Binary Tree Level Order Traversal</a>과 동일하고 마지막에 result의 원소 순서만 거꾸로 했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/binary-tree-level-order-traversal-ii/solutions/3293648/superb-breadth-first-search-python3-by-g-11od/" target="_blank">1st</a>

```python
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        list1=[]
        q=deque()
        q.append(root)
        while q:
            level=[]
            for i in range(len(q)):
                poping=q.popleft()
                if poping:
                    level.append(poping.val)
                    q.append(poping.left)
                    q.append(poping.right)
            if level:
                list1.append(level)
        return list1[::-1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑤)    