---
excerpt: "'LeetCode: Two Sum IV - Input is a BST' 풀이 정리"
title: "\0653. Two Sum IV - Input is a BST"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Search Tree
  - Depth-First Search
  - Hash Table
  - Stack
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary search tree and an integer `k`, return `true` *if there exist two elements in the BST such that their sum is equal to* `k`*, or* `false` *otherwise.*

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
- Input: root = [5,3,6,2,4,null,7], k = 9
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
- Input: root = [5,3,6,2,4,null,7], k = 28
- Output: false

**Constraints:**

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
- root is guaranteed to be a valid binary search tree.
- -10<sup>5</sup> <= k <= 10<sup>5</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        values = set()
        is_founded = [False]    # 합이 k인 두 노드의 존재 여부
        
        def inorder(node):
            if not node or is_founded[0]:
                return

            # 왼쪽 자식
            inorder(node.left)
            # 루트
            if (k - node.val) in values:
                is_founded[0] = True
            else:
                values.add(node.val)
            # 오른쪽
            inorder(node.right)

        inorder(root)
        return is_founded[0]
```
<i class="fa-solid fa-clock"></i> Runtime: **9** ms \| Beats **63.21%**    
<i class="fa-solid fa-memory"></i> Memory: **18.81** MB \| Beats **29.93%**

노드를 순회하며 값을 저장해야 하는데, list는 너무 느려서 set을 사용해야 했다. 그리고 BST이기 때문에 중위 순회를 했는데, 사실 이 방법으로는 순회 순서가 별로 중요하지 않았다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/7020487/beats-96-33-easiest-explanation-and-code-java-python-c-javascript/" target="_blank">1st</a>

```python
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

합이 `k`인 노드 두 개의 존재 여부를 따로 저장하지 않고, F/T로 리턴하는 편이 더 깔끔한 것 같다.

### <a href="https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/1420711/cjavapython-3-solutions-hashset-stack-py-xi1n/" target="_blank">2nd</a>

```python
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):     # 왼쪽 끝까지 내려가며 스택에 push(내림차순)
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):    # 오른쪽 끝까지 내려가며 스택에 push(오름차순)
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):           # inorder 순서대로 다음 작은 값을 반환
            node = st.pop()             # 왼쪽 스택에서 pop
            pushLeft(st, node.right)    # 오른쪽 서브트리가 있다면 왼쪽 끝까지 push
            return node.val

        def nextRight(st):          # 역 inorder 순서대로 다음 큰 값 반환
            node = st.pop()             # 오른쪽 스택에서 pop
            pushRight(st, node.left)    # 왼쪽 서브트리가 있다면 오른쪽 끝까지 push
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)  # 최소값, 최대값으로 초기화

        while left < right:
            if left + right == k: return True

            if left + right < k:            # 합이 작으면 left를 다음 큰 값으로 이동
                left = nextLeft(stLeft)
            else:                           # 합이 크면 right를 다음 작은 값으로 이동
                right = nextRight(stRight)
        
        return False
```
BST의 특성과 two pointers를 잘 활용한 방법이 있어서 참고했다.

root = [5,3,6,2,4,null,7]   
k = 9
{: style="color: blue;"}
<pre>
    5
   / \
  3   6
 / \    \
2   4    7

left, right stacks
stLeft  = [5, 3, 2]
stRight = [5, 6, 7]

left, right pointers
left  = nextLeft(stLeft)   → pop 2, pushLeft(node.right=None) → 2
                             ㄴ stLeft  = [5, 3]
right = nextRight(stRight) → pop 7, pushRight(node.left=None) → 7
                             ㄴ stRight = [5, 6]

left + right = 2 + 7 = 9
</pre>

return True
{: style="color: green;"}