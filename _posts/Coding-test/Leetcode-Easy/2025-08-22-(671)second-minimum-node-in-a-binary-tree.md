---
excerpt: "'LeetCode: Second Minimum Node In a Binary Tree' 풀이 정리"
title: "\0671. Second Minimum Node In a Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Depth-First Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

Given such a binary tree, you need to output the **second minimum** value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg)
- Input: root = [2,2,5,null,null,5,7]
- Output: 5
- Explanation: The smallest value is 2, the second smallest value is 5.

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg)
- Input: root = [2,2,2]
- Output: -1
- Explanation: The smallest value is 2, but there isn't any second smallest value.

**Constraints:**

- The number of nodes in the tree is in the range `[1, 25]`.
- 1 <= Node.val <= 2<sup>31</sup> - 1
- `root.val == min(root.left.val, root.right.val)` for each internal node of the tree.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.first_min = root.val
        self.second_min = float('inf')  # 무한대로 큰 값으로 초기화

        def dfs(node):
            if not node:
                return

            # second_min 값 갱신
            if self.first_min < node.val < self.second_min:
                self.second_min = node.val
            # 현재 노드값 = 루트 노드값이면 왼쪽/오른쪽 자식 탐색
            elif node.val == self.first_min:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.second_min if self.second_min < float('inf') else -1
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.42** MB \| Beats **62.76%**

이번 트리는 특수한 조건 때문에 어떤 노드의 값이 루트 노드값보다 크다면 해당 서브트리 아래에서 그보다 더 작은 값은 나올 수 없기 때문에 더 이상 탐색을 하지 않아도 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/solutions/6730243/conquer-second-minimum-in-special-binary-59gg/" target="_blank">1st</a>

```python
class Solution(object):
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if not node:
                return -1
            if node.val > root.val:   # 루트 노트값보다 크다면 값 반환
                return node.val
            
            left = dfs(node.left)     # 왼쪽 노드 값
            right = dfs(node.right)   # 오른쪽 노드 값

            if left == -1:
                return right
            if right == -1:
                return left
            return min(left, right)

        return dfs(root)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)         

따로 속성 지정 없이 리턴값만으로도 풀 수 있다.