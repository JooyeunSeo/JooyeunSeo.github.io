---
excerpt: "'LeetCode: Validate Binary Search Tree' 풀이 정리"
title: "\098. Validate Binary Search Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Binary Search Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
- The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

*[subtree]: A subtree of treeName is a tree consisting of a node in treeName and all of its descendants.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
- Input: root = [2,1,3]
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)
- Input: root = [5,1,4,null,null,3,6]
- Output: false
- Explanation: The root node's value is 5 but its right child's value is 4.

**Constraints:**

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
- -2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, -float('inf'), float('inf'))
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **20.84** MB \| Beats **74.49%**    

부모 노드뿐만 아니라 조상 노드에서부터 정해진 범위를 만족해야 하기 때문에 허용 범위(min, max) 값을 넘겨주는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/validate-binary-search-tree/solutions/974147/pythonjsjavagoc-on-by-dfs-and-rule-w-vis-150l/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # Use maximal system integer to represent infinity
        INF = sys.maxsize
        
        def helper(node, lower, upper):
            
            if not node:
                # empty node or empty tree
                return True
            
            if lower < node.val < upper:
                # check if all tree nodes follow BST rule
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            
            else:
                # early reject when we find violation
                return False
            
        # ----------------------------------
        
        return helper( node=root, lower=-INF, upper=INF )
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)     