---
excerpt: "'LeetCode: Flatten Binary Tree to Linked List' 풀이 정리"
title: "\0114. Flatten Binary Tree to Linked List"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Linked List
  - Stack
  - Depth-First Search
  - Binary Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR" target="_blank">pre-order traversal</a> of the binary tree.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)
- Input: root = [1,2,5,3,4,null,6]
- Output: [1,null,2,null,3,null,4,null,5,null,6]

**Example 2:**

- Input: root = []
- Output: []

**Example 3:**

- Input: root = [0]
- Output: [0]

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- -100 <= Node.val <= 100

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        rights = []                         # 오른쪽 서브트리 루트 저장

        while root:
            if root.right:                  # 오른쪽 자식 있을 때
                rights.append(root.right)

            if root.left:                   # 왼쪽 자식 있을 때
                next_node = root.left
                root.right = next_node
                root.left = None
                root = next_node
            elif rights:
                root.right = rights.pop()
                root = root.right
            else:
                break
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.60** MB \| Beats **43.29%**    

오른쪽 서브트리 루트만 스택에 저장하고 더 이상 왼쪽 서브트리가 없을 때 꺼내서 연결하는 방법을 사용했다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/1207642/js-python-java-c-simple-o1-space-recursi-b73z/" target="_blank">1st</a>

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                runner = curr.left
                while runner.right: runner = runner.right
                runner.right, curr.right, curr.left = curr.right, curr.left, None
            curr = curr.right
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

스택이나 재귀 없이 Morris Traversal과 비슷하게 푸는 방법이다.

root = [1,2,5,3,4,null,6]
{: style="color: blue;"}
<pre>
    1 (curr)                    1
   / \                         / \
  2   5     →     2      →    n   2
 / \   \         / \             / \
3   4   6       3   4           3   4 
                     \               \
                      5               5
                       \               \
                        6               6

1               1
 \               \
  2 (curr)        2
 / \       →       \
3   4               3
     \               \
      5               4
       \               \
        6               5
                         \
                          6
</pre>

root = [1,null,2,null,3,null,4,null,5,null,6]
{: style="color: green;"}

### <a href="https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/2340445/python-intuitive-explained-o1-space-igno-og6j/" target="_blank">2nd</a>

```python
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if not root: return 
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root        
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)   

원래 전위 순회 `root -> left -> right`를 뒤집어서 `right -> left -> root`로 돌면서 연결 리스트를 뒤에서부터 조립하는 방법이다. 