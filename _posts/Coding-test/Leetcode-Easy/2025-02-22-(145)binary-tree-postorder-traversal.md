---
excerpt: "'LeetCode-Binary Tree Postorder Traversal' 풀이 정리"
title: "\0145. Binary Tree Postorder Traversal"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Stack
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, return the *postorder traversal of its nodes' values*.

**Example 1:**

- Input: root = [1,null,2,3]
- Output: [3,2,1]
- Explanation:

![](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

**Example 2:**

- Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
- Output: [4,6,7,5,2,9,8,3,1]
- Explanation:

![](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

**Example 3:**

- Input: root = []
- Output: []

**Example 4:**

- Input: root = [1]
- Output: [1]

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

**Follow up:** Recursive solution is trivial, could you do it iteratively?    

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        order = []
        stack = []
        last_visited = None                       # 마지막 방문 노드(부모 노드에서 오른쪽 자식 중복 방문 방지)
        current_node = root                       # 현재 탐색중인 노드

        while current_node or stack:
            if current_node:
                stack.append(current_node)        # 현재 노드를 스택에 추가
                current_node = current_node.left  # 왼쪽 자식 먼저 탐색
            else:
                node = stack[-1]                  # 왼쪽으로 끝까지 갔거나 오른쪽 자식만 있을 경우
                if node.right and last_visited != node.right:
                    current_node = node.right         # 오른쪽 자식 탐색(아직 방문한적 없음)
                else:
                    order.append(node.val)            # 오른쪽 자식을 이미 방문한 경우 부모 노드 방문
                    last_visited = stack.pop()

        return order
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.56** MB \| Beats **17.08%**

후위 순회가 전위 순회나 중위 순회보다 좀 더 까다로웠다. 부모 노드로 거슬러 올라갔을 때, 이미 방문했던 오른쪽 자식을 다시 방문하는 문제를 해결하는데서 시간이 많이 들었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            current = stack.pop()
            result.append(current.val)

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return result[::-1]
```

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack1 = [root]     # 전위 순회(루트 → 왼쪽 → 오른쪽) 비슷하게 탐색
        stack2 = []         # stack1에서 꺼낸 노드를 반대로 쌓음 (왼쪽 → 오른쪽 → 루트)

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            result.append(stack2.pop().val)

        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

스택을 활용한 다양한 예시를 참고했다. 전위 순회 비슷하게 먼저 탐색한 뒤, 후위 순회 순서로 다시 저장하는 방법들이 많이 보였다.

### <a href="" target="_blank">2nd</a>

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root: Optional[TreeNode]) -> List[int]:
            if root:
                preorder(root.left)
                preorder(root.right)
                result.append(root.val)
            return result
        return preorder(root)
```
재귀 호출을 사용한 예시도 참고했다.
