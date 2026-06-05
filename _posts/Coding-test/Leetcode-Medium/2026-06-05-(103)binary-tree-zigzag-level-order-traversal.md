---
excerpt: "'LeetCode: Binary Tree Zigzag Level Order Traversal' 풀이 정리"
title: "\0103. Binary Tree Zigzag Level Order Traversal"
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

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
- Input: root = [3,9,20,null,null,15,7]
- Output: [[3],[20,9],[15,7]]

**Example 2:**

- Input: root = [1]
- Output: [[1]]

**Example 3:**

- Input: root = []
- Output: []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- -100 <= Node.val <= 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        q = deque()
        q.append(root)
        is_reversed = 0

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)

            if is_reversed:
                level.reverse()

            result.append(level)
            is_reversed ^= 1

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.15** MB \| Beats **99.52%**    

is_reversed로 각 level마다 정방향인지 역방향인지 체크하고 result에 넣기 전에 순서를 뒤집었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/6896289/beats-100-using-bfs-and-deque-java-pytho-uc88/" target="_blank">1st</a>

```python
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, dq, reverse = [], deque([root]), False

        while dq:
            level = []
            for _ in range(len(dq)):
                if not reverse:
                    node = dq.popleft()
                    level.append(node.val)
                    if node.left: dq.append(node.left)
                    if node.right: dq.append(node.right)
                else:
                    node = dq.pop()
                    level.append(node.val)
                    if node.right: dq.appendleft(node.right)
                    if node.left: dq.appendleft(node.left)
            res.append(level)
            reverse = not reverse
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑤)    

이 방법은 deque의 양쪽을 모두 사용하기 때문에 자식을 넣는 순서가 달라진다.

### <a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/749036/python-clean-bfs-solution-explained-by-d-eudl/" target="_blank">2nd</a>

```python
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue = deque([root])
        result, direction = [], 1
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result
```