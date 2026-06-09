---
excerpt: "'LeetCode: Construct Binary Tree from Preorder and Inorder Traversal' 풀이 정리"
title: "\0105. Construct Binary Tree from Preorder and Inorder Traversal"
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

Given two integer arrays `preorder` and `inorder` where `preorder` is the `preorder` traversal of a binary tree and inorder is the `inorder` traversal of the same tree, construct and return the binary tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
- Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
- Output: [3,9,20,null,null,15,7]

**Example 2:**

- Input: preorder = [-1], inorder = [-1]
- Output: [-1]

**Constraints:**

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is **guaranteed** to be the preorder traversal of the tree.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preL, preR, inL, inR):
            if preL > preR:
                return None
            
            root_val = preorder[preL]       # preorder의 첫 원소 -> 현재 서브트리의 루트
            root = TreeNode(root_val)

            idx = inorder_idx[root_val]     # inorder에서 루트 위치
            
            left_size = idx - inL           # 왼쪽 서브트리 노드 수

            root.left = build(preL+1, preL+left_size, inL, idx-1)
            root.right = build(preL+left_size+1, preR, idx+1, inR)

            return root

        inorder_idx = {val: i for i, val in enumerate(inorder)} # inorder 값: 인덱스
        n = len(preorder)
        return build(0, n-1, 0, n-1)
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **60.07%**    
<i class="fa-solid fa-memory"></i> Memory: **21.40** MB \| Beats **48.79%**    

전위 순회로는 어떤 값이 루트인지 알 수 있고, 중위 순회로는 왼쪽 서브트리와 오른쪽 서브트리의 경계를 알 수 있다. 재귀 순서는 `루트 → 왼쪽 → 오른쪽`이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/python-short-recursive-solution-by-oldco-hmzj/" target="_blank">1st</a>

```python
def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛<sup>2</sup>)    

항상 리스트의 맨 앞 원소를 삭제하고 재귀 호출을 할 때마다 슬라이싱을 통해 새 리스트를 생성하기 때문에 최적화된 방법은 아니ㅏ.

### <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/7017307/beats-9589-beginner-friendly-solution-ja-ep33/" target="_blank">2nd</a>

```python
class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def helper(start, end):
            if start > end:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            mid = idx_map[root_val]
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(inorder) - 1)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

preorder의 각 원소는 현재 서브트리의 루트를 의미하고, 재귀 호출로 inorder에서 start~end 범위에 해당하는 서브트리를 생성한다.