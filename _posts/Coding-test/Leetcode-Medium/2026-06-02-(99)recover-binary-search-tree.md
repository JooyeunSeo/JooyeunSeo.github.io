---
excerpt: "'LeetCode: Recover Binary Search Tree' 풀이 정리"
title: "\099. Recover Binary Search Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Binary Search Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given the root of a binary search tree (BST), where the values of **exactly** two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)
- Input: root = [1,3,null,null,2]
- Output: [3,1,null,null,2]
- Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)
- Input: root = [3,1,4,null,null,2]
- Output: [2,1,4,null,null,3]
- Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

**Constraints:**

- The number of nodes in the tree is in the range `[2, 1000]`.
- -2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1

**Follow up:** A solution using `O(n)` space is pretty straight-forward. Could you devise a constant `O(1)` space solution?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)                          # 왼쪽

            if self.prev and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev
                self.second = node
            self.prev = node

            inorder(node.right)                         # 오른쪽

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **20.44** MB \| Beats **24.09%**    

BST를 중위 순회하면 노드의 값이 오름차순 정렬된다는 것을 이용할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/recover-binary-search-tree/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        curr, prev, a, b = root, None, None, None        
        while curr:
            if not curr.left:   
                # find the node that is violating the ordering 
                if prev and curr.val < prev.val:					
                    if not a: # find the first node to swap
                        a = prev
                    b = curr                   
                prev = curr
                curr = curr.right                
            else:
                temp = curr.left
                while temp.right and temp.right is not curr:    # 왼쪽 서브트리의 가장 오른쪽 노드 찾기
                    temp = temp.right
                if temp.right is curr:
                    temp.right = None 
                    if prev and curr.val < prev.val:
                        if not a:
                            a = prev
                        b = curr   
                    prev = curr
                    curr = curr.right
                else:
                    temp.right = curr                           # 트리 포인터 임시 변경
                    curr = curr.left

        # swap bide values
        a.val,b.val = b.val, a.val
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

공간 복잡도를 𝑂(1)로 유지하면서 순회할 수 있는 **Morris Traversal**을 사용한 방법이다.

root = [4, 2, null, 1, 3]
{: style="color: blue;"}
<pre>             
    4 (curr)                   4 (curr)
   /                          /
  2 (temp)                   2
 / \                        / \
1   3 (temp.right)         1   3 (temp)
                                \
                                 4 (curr) 임시연결
</pre>