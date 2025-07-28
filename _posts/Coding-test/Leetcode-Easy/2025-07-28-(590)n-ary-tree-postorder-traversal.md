---
excerpt: "'LeetCode: N-ary Tree Postorder Traversal' 풀이 정리"
title: "\0590. N-ary Tree Postorder Traversal"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Tree
  - Stack
  - Depth-First Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of an n-ary tree, return *the postorder traversal of its nodes' values.*

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
- Input: root = [1,null,3,2,4,null,5,6]
- Output: [5,6,3,2,4,1]

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
- Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
- Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

**Constraints:**

- The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
- 0 <= Node.val <= 10<sup>4</sup>
- The height of the n-ary tree is less than or equal to `1000`.

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = []
        result = []

        if root:
            stack.append(root)

        while stack:
            node = stack.pop()        
            result.append(node.val)   # 루트 → 오른쪽 자식 → 왼쪽 자식 순으로 순회

            for c in node.children:   # 왼쪽 → 오른쪽 자식 순으로 스택에 추가(역순x)
                stack.append(c)

        return result[::-1]           # 순회 결과 뒤집기
```
<i class="fa-solid fa-clock"></i> Runtime: **32** ms \| Beats **79.43%**    
<i class="fa-solid fa-memory"></i> Memory: **15.72** MB \| Beats **1.90%**

스택을 이용한 방법으로, 루트 → 오른쪽 자식 → 왼쪽 자식 순서로 순회한 뒤 이를 거꾸로 뒤집으면 후위 순회가 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution(object):
    def postorder(self, root):
        # If the root is None, return an empty list
        if not root:
            return []

        res = []

        # Define the DFS function
        def dfs(root):
            # Recursively call dfs for each child of the current node
            for x in root.children:
                dfs(x)
            # Append the value of the current node to the result list
            res.append(root.val)

        # Start DFS from the root
        dfs(root)

        # Return the result list containing node values in post-order
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)           

후위 순회도 재귀 호출로 하면 더 직관적이고 간단하다.