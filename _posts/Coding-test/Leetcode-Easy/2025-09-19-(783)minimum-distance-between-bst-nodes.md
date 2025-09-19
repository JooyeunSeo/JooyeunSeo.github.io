---
excerpt: "'LeetCode: Minimum Distance Between BST Nodes' 풀이 정리"
title: "\0783. Minimum Distance Between BST Nodes"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Breadth-First Search
  - Binary Search Tree
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a Binary Search Tree (BST), return *the minimum difference between the values of any two different nodes in the tree.*

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)
- Input: root = [4,2,6,1,3]
- Output: 1

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)
- Input: root = [1,0,48,null,null,12,49]
- Output: 1

**Constraints:**

- The number of nodes in the tree is in the range `[2, 100]`.
- 0 <= Node.val <= 10<sup>5</sup>

**Note:** This question is the same as 530: <a href="https://leetcode.com/problems/minimum-absolute-difference-in-bst/" target="_blank">https://leetcode.com/problems/minimum-absolute-difference-in-bst/</a>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev is not None:
                    self.min_diff = min(self.min_diff, (node.val - self.prev))
                self.prev = node.val
                inorder(node.right)

        inorder(root)
        return self.min_diff
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.45** MB \| Beats **96.41%**

중위 순회로 정렬된 결과에서 앞뒤 노드끼리의 차이를 비교한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/minimum-distance-between-bst-nodes/solutions/114834/cjavapython-inorder-traversal-on-time-re-szqe/" target="_blank">1st</a>

```python
class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)           

이전에 방문한 노드의 값을 저장하는 `pre`의 값을 None이 아니라 음의 무한대로 설정하면 더 간단하게 코드를 짤 수 있다.