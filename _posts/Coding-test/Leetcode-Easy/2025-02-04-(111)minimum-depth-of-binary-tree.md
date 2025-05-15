---
excerpt: "'LeetCode: Minimum Depth of Binary Tree' 풀이 정리"
title: "\0111. Minimum Depth of Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - DFS
  - Recursion
  - BFS
  - Queue
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

- Input: root = [3,9,20,null,null,15,7]
- Output: 2

**Example 2:**

- Input: root = [2,null,3,null,4,null,5,null,6]
- Output: 5

**Constraints:**

- The number of nodes in the tree is in the range [0, 10<sup>5</sup>].
- -1000 <= Node.val <= 1000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:                              # 빈 트리일 경우 깊이는 0
            return 0
        
        def leaf_depth(root, depth):
            if not root.left and not root.right:  # 서브트리가 없는 잎 노드에 도달
                return depth
            
            left_depth = None if not root.left else leaf_depth(root.left, depth + 1)
            right_depth = None if not root.right else leaf_depth(root.right, depth + 1)

            if left_depth is None:                # 왼쪽 서브트리가 없으면 오른쪽 서브트리의 깊이 반환
                return right_depth
            elif right_depth is None:             # 오른쪽 서브트리가 없으면 왼쪽 서브트리의 깊이 반환
                return left_depth
            
            return min(left_depth, right_depth)   # 두 서브트리의 깊이 중 더 얕은 쪽의 값을 반환

        return leaf_depth(root, 1)
```
<i class="fa-solid fa-clock"></i> Runtime: **162** ms \| Beats **48.46%**    
<i class="fa-solid fa-memory"></i> Memory: **96.76** MB \| Beats **6.10%**

`.min()`으로 두 서브트리의 깊이 중 더 작은 값을 반환하도록 했는데, 자식 노드가 없는 쪽의 경로는 깊이 계산에서 포함하지 않아야 하는 부분이 어려웠다. 처음에는 <mark>float('inf')</mark>으로 양의 무한대값을 넣어서 최소값이 되지 않도록 만들었는데, 이 방법은 시간이 너무 오래걸렸다. 그래서 대신 `None`을 넣고 값이 None이면 최소값 계산에서 빼는 것으로 조금 단축했다.   
재귀 호출이 아닌 다른 방법으로 푼 답안들에 비해 많이 느리지만, 이진 트리 문제는 재귀 호출을 연습하는 것에 좀 더 의의를 두기로 했다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize the queue with the root node and its depth
        queue = [(root, 1)]
        
        while queue:
            # Dequeue the first node and its depth
            node, depth = queue.pop(0)
            
            # If the node is a leaf, return its depth
            if not node.left and not node.right:
                return depth
            
            # Enqueue the left and right children if they exist
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑤)           

큐를 사용하여 너비 우선 탐색을 한 예시다. 너비를 우선으로 탐색할 경우 가장 먼저 만난 잎 노드가 최소 깊이이기 때문에 아주 빠르게 해결할 수 있다.

### <a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/solutions/2429057/very-easy-100-fully-explained-c-java-pyt-uiik/" target="_blank">2nd</a>

```python
class Solution:
   def minDepth(self, root: Optional[TreeNode]) -> int:
       if not root: return 0
       l, r = self.minDepth(root.left), self.minDepth(root.right)
       if not root.left or not root.right:
           return 1 + max(l, r)
       return min(l, r) + 1
```
링크된 솔루션 게시판의 코멘트에서 가져온 답안이다. 한 쪽 자식이 없는 경우 그 자식의 깊이를 포함하지 않기 위해 반대로 `.max()`를 사용했다. 이렇게 하면 간단하게 해결할 수 있었다는 것을 알게 됐다.