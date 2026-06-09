---
excerpt: "'LeetCode: Construct Binary Tree from Inorder and Postorder Traversal' 풀이 정리"
title: "\0106. Construct Binary Tree from Inorder and Postorder Traversal"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Divide and Conquer
  - Binary Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two integer arrays `inorder` and `postorder` where inorder is the `inorder` traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
- Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
- Output: [3,9,20,null,null,15,7]

**Example 2:**

- Input: inorder = [-1], postorder = [-1]
- Output: [-1]

**Constraints:**

- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- `inorder` and `postorder` consist of **unique** values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.
- `postorder` is **guaranteed** to be the postorder traversal of the tree.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.idx = len(inorder) - 1

        def build(start, end):
            if start > end:
                return None

            root_val = postorder[self.idx]
            self.idx -= 1

            root = TreeNode(root_val)
            mid = inorder_idx[root_val]

            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)
            return root

        return build(0, len(inorder) - 1)
```
<i class="fa-solid fa-clock"></i> Runtime: **2** ms \| Beats **77.06%**    
<i class="fa-solid fa-memory"></i> Memory: **21.01** MB \| Beats **74.48%**    

<a href="https://jooyeunseo.github.io/leetcode-medium/(105)construct-binary-tree-from-preorder-and-inorder-traversal/" target="_blank">105. Construct Binary Tree from Preorder and Inorder Traversal</a>에서는 전위 순회이기 때문에 preorder[0]이 최상단 루트였다. 하지만 이번에는 `왼쪽 → 오른쪽 → 루트`으로 가는 후위 순회로, postorder[-1]이 최상단 루트가 된다. 또 뒤집어서 읽기 때문에 재귀 순서도 `루트 → 오른쪽 → 왼쪽`으로 변경해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/3302159/easy-solutions-in-java-python-and-c-look-71ia/" target="_blank">1st</a>

```python
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Base case
        if not inorder:
            return None
        
        # The last element of postorder list is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the position of the root in the inorder list
        inorder_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)         
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛<sup>2</sup>)   

루트 값을 결정하는 인덱스가 postorder의 맨 뒤에서부터 시작되기 때문에 pop()으로 간단히 할 수 있지만, `inorder.index(root.val)` 부분에서 시간을 낭비하기 때문에 해시 테이블로 `값: 인덱스` 정보를 저장하는 쪽이 훨씬 효율적이다.