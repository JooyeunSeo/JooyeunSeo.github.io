---
excerpt: "'LeetCode: Univalued Binary Tree' 풀이 정리"
title: "\0965. Univalued Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Breadth-First Search
  - Binary Tree
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

A binary tree is **uni-valued** if every node in the tree has the same value.

Given the `root` of a binary tree, return `true` *if the given tree is **uni-valued**, or* `false` *otherwise*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)
- Input: root = [1,1,1,1,1,null,1]
- Output: true

**Example 2:**

- ![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)
- Input: root = [2,2,2,5,2]
- Output: false

**Constraints:**

- The number of nodes in the tree is in the range `[1, 100]`.
- 0 <= Node.val < 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, value):
            if not node:
                return True
            if node.val != value:
                return False
            return dfs(node.left, value) and dfs(node.right, value)
        
        return dfs(root, root.val)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.82** MB \| Beats **37.69%**    

모든 노드의 값은 루트 노드의 값과 동일해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/univalued-binary-tree/solutions/211978/simple-python-solution-explanation-by-mo-kxte/" target="_blank">1st</a>

```python
class Solution:
    def isUnivalTree(self, tree):
        if not tree:
            return True
        
        if tree.right:
            if tree.val != tree.right.val:
                return False
            
        if tree.left:
            if tree.val != tree.left.val:
                return False
        
        return self.isUnivalTree(tree.right) and self.isUnivalTree(tree.left)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)    