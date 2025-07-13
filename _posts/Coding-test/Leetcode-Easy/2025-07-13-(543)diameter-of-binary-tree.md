---
excerpt: "'LeetCode: Diameter of Binary Tree' 풀이 정리"
title: "\0543. Diameter of Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Depth-First Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, return *the length of the **diameter** of the tree.*

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)
- Input: root = [1,2,3,4,5]
- Output: 3
- Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

**Example 2:**

- Input: root = [1,2]
- Output: 1

**Constraints:**

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
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
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0   # 가장 긴 지름

        def dfs(node):
            if not node:
                return 0        # null 노드는 깊이 0
            
            left = dfs(node.left)     # 왼쪽 서브트리 깊이
            right = dfs(node.right)   # 오른쪽 서브트리 깊이

            # 잎노드에서부터 해당 노드를 통과하는 가장 긴 경로 = 왼쪽 깊이 + 오른쪽 깊이
            self.max_diameter = max(self.max_diameter, left + right)

            # 현재 노드의 깊이 반환(자기자신 1 + 왼쪽/오른쪽 중 긴 쪽)
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter
```
<i class="fa-solid fa-clock"></i> Runtime: **7** ms \| Beats **95.07%**    
<i class="fa-solid fa-memory"></i> Memory: **26.26** MB \| Beats **72.15%**

root = [1, 2, 3, 4, 5]
{: style="color: blue;"}
<pre>
    1
   / \
  2   3
 / \
4   5

node    left   right    max_diameter   return(depth)
4       0      0        0               1
5       0      0        0               1
2       1      1        2               2
3       0      0        2               1
1       2      1        3               3
</pre>

max_diameter = 3
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/diameter-of-binary-tree/solutions/6750382/video-using-dfs-step-by-step-algorithm/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            nonlocal res
            res = max(res, l + r)

            return 1 + max(l, r)

        dfs(root)
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)           

파이썬3에서는 self. 대신 **nonlocal**을 사용해서 함수 내부에서도 외부의 값을 사용할 수 있다.