---
excerpt: "'LeetCode: Binary Tree Level Order Traversal' 풀이 정리"
title: "\0102. Binary Tree Level Order Traversal"
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

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
- Input: root = [3,9,20,null,null,15,7]
- Output: [[3],[9,20],[15,7]]

**Example 2:**

- Input: root = [1]
- Output: [[1]]

**Example 3:**

- Input: root = []
- Output: []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- -1000 <= Node.val <= 1000

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Use a queue to perform BFS.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        q = deque()
        q.append(root)

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

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.93** MB \| Beats **60.85%**    


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/33464/5-6-lines-fast-python-solution-48-ms-by-x7h0p/" target="_blank">1st</a>

```python
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑤)    

큐 없이 리스트만으로 BFS를 구현한 방법이다.