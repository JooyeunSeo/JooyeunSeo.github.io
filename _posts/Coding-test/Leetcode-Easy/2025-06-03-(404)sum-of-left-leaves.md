---
excerpt: "'LeetCode: Sum of Left Leaves' 풀이 정리"
title: "\0404. Sum of Left Leaves"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Recursion
  - Depth-First Search
  - Breadth-First Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, return the sum of all left leaves.

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg)

- Input: root = [3,9,20,null,null,15,7]
- Output: 24
- Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

**Example 2:**

- Input: root = [1]
- Output: 0

**Constraints:**

- The number of nodes in the tree is in the range [1, 1000].
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def find_left_leaf(node):
            # left leaves 합
            total = 0

            # 왼쪽 자식이 left leaf라면 total에 더하고 더 깊이 안 들어감
            if node.left:
                if not node.left.left and not node.left.right:
                    total += node.left.val
                else:
                    total += find_left_leaf(node.left)
            # 오른쪽 자식 재귀 호출
            if node.right:
                total += find_left_leaf(node.right)
            return total

        return find_left_leaf(root)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.24** MB \| Beats **11.24%**

재귀 호출을 이용했다. 현재 노드에 왼쪽 자식이 존재하고, 그 왼쪽 자식이 잎일 때만 왼쪽 자식 노드의 값을 total에 더하고 나머지 경우에는 아무것도 안 더하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/sum-of-left-leaves/solutions/6641945/master-tree-traversal-to-sum-left-leaves-n1sq/" target="_blank">1st</a>

```python
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:    # 현재 노드가 leaf인 경우
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)  # 재귀 호출
        
        return dfs(root, False)         # 루트는 왼쪽 자식이 아니므로 False로 시작

```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ) ← height

left leaf의 여부(현재 노드가 부모 기준으로 왼쪽 자식인지)를 bool 값으로 추적하는 **깊이 우선 탐색** 방법이다. 왼쪽 자식으로 재귀 호출할 때는 True 값을 넘겨주고, 오른쪽으로 갈때는 False 값을 준다.

### <a href="" target="_blank">2nd</a>

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, False)])  # (node, is_left)
        total_sum = 0
        
        while queue:
            node, is_left = queue.popleft()
            
            if is_left and not node.left and not node.right:
                total_sum += node.val
            
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        
        return total_sum
```
위와 같이 bool 값을 이용했으나 **너비 우선 탐색**을 사용하여 재귀 호출 없이 해결하는 방법이다. 큐에서 꺼낸 노드가 왼쪽 자식이면서(is_left가 True) 잎이면 합산하고, 왼쪽/오른쪽 자식이 있다면 큐에 추가함과 동시에 is_left를 업데이트한다.