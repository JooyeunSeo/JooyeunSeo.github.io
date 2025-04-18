---
excerpt: "'LeetCode-Invert Binary Tree' 풀이 정리"
title: "\0226. Invert Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

- Input: root = [4,2,7,1,3,6,9]
- Output: [4,7,2,9,6,3,1]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

- Input: root = [2,1,3]
- Output: [2,3,1]

**Example 3:**

- Input: root = []
- Output: []

**Constraints:**

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left   # 왼쪽, 오른쪽 자식 노드를 스왑

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
```

```python
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats **93.21%**

큐를 사용한 방법과 재귀 호출 방법 두 가지로 풀어봤다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/invert-binary-tree/solutions/5513149/video-swap-left-child-and-right-child-by-pc7i/" target="_blank">1st</a>

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

temp를 사용해서 두 노드를 스왑하는 방법을 사용했는데, 사실 파이썬에서는 동시에 할당이 가능하다.