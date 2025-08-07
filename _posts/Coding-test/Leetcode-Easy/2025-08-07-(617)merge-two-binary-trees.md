---
excerpt: "'LeetCode: Merge Two Binary Trees' 풀이 정리"
title: "\0617. Merge Two Binary Trees"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Recursion
  - Depth-First Search
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given two binary trees `root1` and `root2`.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return *the merged tree.*

**Note:** The merging process must start from the root nodes of both trees.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/05/merge.jpg)
- Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
- Output: [3,4,5,5,4,null,7]

**Example 2:**

- Input: root1 = [1], root2 = [1,2]
- Output: [2,2]

**Constraints:**

- The number of nodes in both trees is in the range `[0, 2000]`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 한 쪽 노드만 존재하면 다른 쪽 노드 반환(양쪽 다 빈 노드면 None 반환됨)
        if not root1:
            return root2
        if not root2:
            return root1
        
        # 두 노드 모두 존재하는 경우 값을 더해서 root1 노드 갱신
        root1.val += root2.val
        
        # 왼쪽 자식 병합
        root1.left = self.mergeTrees(root1.left, root2.left)
        # 오른쪽 자식 병합
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1
```
<i class="fa-solid fa-clock"></i> Runtime: **2** ms \| Beats **75.54%**    
<i class="fa-solid fa-memory"></i> Memory: **13.16** MB \| Beats **65.76%**

전위 순회 순서로 DFS를 했다. 새로운 트리를 만들 필요 없이 root1 트리에 병합한 후 해당 트리를 반환했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/merge-two-binary-trees/solutions/7015914/beats-10000-2-tricks-new-tree-creation-i-8cgc/" target="_blank">1st</a>

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        mergedNode = TreeNode(root1.val + root2.val)
        mergedNode.left = self.mergeTrees(root1.left, root2.left)
        mergedNode.right = self.mergeTrees(root1.right, root2.right)
        return mergedNode
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

기존 트리에 병합하지 않고 새 트리를 만드는 방법도 참고했다.