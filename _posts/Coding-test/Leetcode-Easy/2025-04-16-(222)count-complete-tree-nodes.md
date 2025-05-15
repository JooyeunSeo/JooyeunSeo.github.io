---
excerpt: "'LeetCode: Count Complete Tree Nodes' 풀이 정리"
title: "\0222. Count Complete Tree Nodes"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the root of a **complete** binary tree, return the number of the nodes in the tree.

According to <a href="https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level `h`.

Design an algorithm that runs in less than `O(n)` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

- Input: root = [1,2,3,4,5,6]
- Output: 6

**Example 2:**

- Input: root = []
- Output: 0

**Example 3:**

- Input: root = [1]
- Output: 1

**Constraints:**

- The number of nodes in the tree is in the range [0, 5 * 10<sup>4</sup>].
- 0 <= Node.val <= 5 * 10<sup>4</sup>
- The tree is guaranteed to be **complete**.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        count = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                count += 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return count
```
<i class="fa-solid fa-clock"></i> Runtime: **5** ms \| Beats **64.64%**    
<i class="fa-solid fa-memory"></i> Memory: **28.26** MB \| Beats **64.36%**

모든 노드를 방문하면서 세는 방법보다 완전 이진 트리라는 것을 활용하는 방법이 있기 때문에 다른 답안들에 비해 속도가 느린 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/count-complete-tree-nodes/solutions/62088/my-python-solution-in-olgn-lgn-time-by-4-gsfv/" target="_blank">1st</a>

```python
 class Solution:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0

            leftDepth = self.getDepth(root.left)        # 왼쪽 깊이
            rightDepth = self.getDepth(root.right)      # 오른쪽 깊이

            if leftDepth == rightDepth:   # 왼쪽 서브트리가 포화 이진 트리
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:                         # 오른쪽 서브트리가 포화 이진 트리
                return pow(2, rightDepth) + self.countNodes(root.left)
        
        def getDepth(self, root):     # 해당 서브트리의 깊이를 구하는 함수(완전 이진 트리이므로 왼쪽만 따라가며 계산)
            if not root:
                return 0
            return 1 + self.getDepth(root.left)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂((log𝑛)<sup>2</sup>) ← 깊이를 log𝑛번 측정, 측정할 때마다 log𝑛 깊이만큼 내려감   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(log𝑛)           

왼쪽과 오른쪽 서브트리를 나누어 깊이를 비교하는 방법이다.    
왼쪽 서브트리가 포화 이진 트리라면:   
왼쪽 서브트리의 노드 (2<sup>leftDepth</sup> - 1)개 + 루트 노드 1개 + 오른쪽 서브트리의 노드 개수(재귀 호출)   
오른쪽 서브트리가 포화 이진 트리라면:   
오른쪽 서브트리의 노드 (2<sup>rightDepth</sup> - 1)개 + 루트 노드 1개 + 왼쪽 서브트리의 노드 개수(재귀 호출)

root = [1,2,3,4,5,6]
{: style="color: blue;"}
<pre>
     1
   /   \
  2     3
 / \   /
4   5 6

node 1
leftDepth = 2 (getDepth(2) → 1+getDepth(4) → 1+1+getDepth(None) → 1+1+0)
rightDepth = 2 (getDepth(3) → 1+getDepth(6) → 1+1+getDepth(None) → 1+1+0)
return 2^2 + countNodes(3)

node 3
leftDepth = 1
rightDepth = 0
return 2^0 + countNodes(6)

node 6
leftDepth = 0
rightDepth = 0
return 2^0 + countNodes(None) = 1+0 = 1

4 + (1 + (1 + 0)) = 6
</pre>

return 6
{: style="color: green;"}

### <a href="https://leetcode.com/problems/count-complete-tree-nodes/solutions/2815375/pythoncjavarust-lognlogn-with-proof-bonu-3q67/" target="_blank">2nd</a>

```python
class Solution:
    def countNodes(self, root, l=1, r=1):

        if not root : return 0
        
        left = right = root                           # compute both left and right heights of
        while left  := left.left   : l += 1           # each subtree by going all way down to
        while right := right.right : r += 1           # the left and right (in logN time)

        if l == r : return 2**l - 1                   # if it's a full tree, its size is known
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

<pre>
while left  := left.left   : l += 1
↓
left = left.left
while left:
    l += 1
    left = left.left
</pre>