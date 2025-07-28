---
excerpt: "'LeetCode: N-ary Tree Preorder Traversal' 풀이 정리"
title: "\0589. N-ary Tree Preorder Traversal"
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

Given the `root` of an n-ary tree, return *the preorder traversal of its nodes' values.*

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
- Input: root = [1,null,3,2,4,null,5,6]
- Output: [1,3,5,6,2,4]

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
- Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
- Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

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
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
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
            result.append(node.val)       # 전위순회: 루트 먼저 추가
            for c in node.children[::-1]: # 자식 노드들을 역순으로 스택에 추가
                stack.append(c)
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **27** ms \| Beats **96.17%**    
<i class="fa-solid fa-memory"></i> Memory: **15.55** MB \| Beats **48.67%**

스택으로 N-ary 트리를 전위 순회했다. 루트 노드 값을 출력 후 자식 노드들을 역순으로 추가해야 왼쪽 자식부터 순회할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/n-ary-tree-preorder-traversal/solutions/786364/python-iterative-recursive-explanation/" target="_blank">1st</a>

```python
class Solution(object):
    def preorder(self, root):
        output =[]
        
        # perform dfs on the root and get the output stack
        self.dfs(root, output)
        
        # return the output of all the nodes.
        return output
    
    def dfs(self, root, output):
        # If root is none return
        if root is None:
            return
        
        # for preorder we first add the root val
        output.append(root.val)
        
        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, output)
       
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)           

전위 순회는 재귀 호출을 사용하면 더 간단하고 직관적으로 구현할 수 있다. 