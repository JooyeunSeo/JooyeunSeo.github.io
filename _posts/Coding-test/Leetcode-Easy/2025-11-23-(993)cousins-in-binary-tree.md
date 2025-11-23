---
excerpt: "'LeetCode: Cousins in Binary Tree' 풀이 정리"
title: "\0993. Cousins in Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Breadth-First Search
  - Binary Tree
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree with unique values and the values of two different nodes of the tree `x` and `y`, return `true` *if the nodes corresponding to the values* `x` *and* `y` *in the tree are **cousins**, or* `false` *otherwise*.

Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth `0`, and children of each depth `k` node are at the depth `k + 1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)
- Input: root = [1,2,3,4], x = 4, y = 3
- Output: false

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)
- Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
- Output: true

**Example 3:**

![](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)
- Input: root = [1,2,3,null,4], x = 2, y = 3
- Output: false

**Constraints:**

- The number of nodes in the tree is in the range `[2, 100]`.
- 1 <= Node.val <= 100
- Each node has a **unique** value.
- `x != y`
- `x` and `y` are exist in the tree.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])

        while q:
            found_x = found_y = False

            # 동일 레벨에 대해 탐색
            for _ in range(len(q)):             
                node = q.popleft()

                if node.val == x: found_x = True
                if node.val == y: found_y = True

                # 형제 노드인지 set으로 체크
                if node.left and node.right:
                    if {node.left.val, node.right.val} == {x, y}:
                        return False

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            
            if found_x and found_y: # 같은 레벨에서 둘 다 존재 → 사촌
                return True
            if found_x or found_y:  # 같은 레벨에서 하나만 존재 → 사촌 아님
                return False

        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.93** MB \| Beats **28.09%**    

두 노드가 같은 레벨에 있는지 찾아야 하기 때문에 DFS보다 BFS가 더 적합한 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/cousins-in-binary-tree/solutions/654172/python-straight-forward-bfs-and-dfs-solu-nxgg/" target="_blank">1st</a>

```python
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		# store (parent, depth) tuple
        res = []
		
		# bfs
        queue = deque([(root, None, 0)])        
        while queue:
			# minor optimization to stop early if both targets found
            if len(res) == 2:
                break
            node, parent, depth = queue.popleft()
            # if target found
            if node.val == x or node.val == y:
                res.append((parent, depth))
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

		# unpack two nodes
        node_x, node_y = res
		
		# compare and decide whether two nodes are cousins		
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
```
```python
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		# store (parent, depth) tuple
		res = [] 
        
		# dfs
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((parent, depth))
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        dfs(root, None, 0)

		# unpack two nodes found
        node_x, node_y = res  
		
		# compare and decide whether two nodes are cousins
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ) / 𝑂(𝑤)     

x, y 노드의 `(parent, depth)` 정보를 저장해서 비교하는 로직을 BFS, DFS에 둘 다 적용할 수 있다.