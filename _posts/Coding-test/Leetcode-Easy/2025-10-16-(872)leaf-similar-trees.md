---
excerpt: "'LeetCode: Leaf-Similar Trees' 풀이 정리"
title: "\0872. Leaf-Similar Trees"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Binary Tree
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence**.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered *leaf-similar* if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)
- Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)
- Input: root1 = [1,2,3], root2 = [1,3,2]
- Output: false

**Constraints:**

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def find_leaf(node, leaf_values):
            if not node.left and not node.right:    # 잎노드이면 리스트에 값 추가
                leaf_values.append(node.val)
            
            if node.left:
                find_leaf(node.left, leaf_values)
            if node.right:
                find_leaf(node.right, leaf_values)
        
        root1_leaf = []
        root2_leaf = []

        find_leaf(root1, root1_leaf)
        find_leaf(root2, root2_leaf)

        return root1_leaf == root2_leaf
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.57** MB \| Beats **69.57%**

DFS로 잎 노드들을 왼쪽에서 오른쪽 순서로 수집한 뒤, 두 리스트를 비교했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/leaf-similar-trees/solutions/4531517/9939easy-solutionwith-explanation-by-mra-sevc/" target="_blank">1st</a>

```python
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaf_values(root, leaf_values):
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ1+ℎ2)           

재귀 종료 조건을 `if not node: return`으로 명시하는 것이 더 깔끔한 것 같다.

### <a href="https://leetcode.com/problems/leaf-similar-trees/solutions/152329/cjavapython-oh-space-by-lee215-dvco/" target="_blank">2nd</a>

```python
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i    # == yield from dfs(node.left)
            for i in dfs(node.right): yield i   # == yield from dfs(node.right)
        return all(a == b for a, b in itertools.izip_longest(dfs(root1), dfs(root2)))
```
**제너레이터**를 사용하면 잎 노드를 만날 때마다 값을 하나씩 내놓기 때문에 리스트를 만들지 않아도 된다는 장점이 있다.    
itertools 모듈의 <mark>izip_longest()</mark>는 dfs(root1)과 dfs(root2)를 순서대로 실행하여 각각에서 잎의 값 하나씩을 가져온 후, 두 값을 묶어주는 함수다. <mark>zip()</mark>과 비슷하지만 차이점은 두 시퀀스 길이가 다를 경우 짧은 쪽을 None으로 채워서 끝까지 비교할 수 있도록 해준다는 것이다.