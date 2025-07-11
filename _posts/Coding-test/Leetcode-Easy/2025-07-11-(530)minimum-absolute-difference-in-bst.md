---
excerpt: "'LeetCode: Minimum Absolute Difference in BST' 풀이 정리"
title: "\0530. Minimum Absolute Difference in BST"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Search Tree
  - Depth-First Search
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a Binary Search Tree (BST), *return the minimum absolute difference between the values of any two different nodes in the tree*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)
- Input: root = [4,2,6,1,3]
- Output: 1

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)
- Input: root = [1,0,48,null,null,12,49]
- Output: 1

**Constraints:**

- The number of nodes in the tree is in the range [2, 10<sup>4</sup>].
- 0 <= Node.val <= 10<sup>5</sup>

**Note:** This question is the same as 783: <a href="https://leetcode.com/problems/minimum-distance-between-bst-nodes/" target="_blank">https://leetcode.com/problems/minimum-distance-between-bst-nodes/</a>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        prev = None         # 이전 순서 노드값(None으로 초기화)
        diff = 10**5 - 0    # 노드 값의 차(범위 내 '최대값 - 최소값' 으로 초기화)
        stack = []

        while root or stack:
            while root:
                stack.append(root)      # 현재 노드 스택에 추가
                root = root.left        # 왼쪽 자식으로 이동
            
            root = stack.pop()          # 스택에서 pop
            if prev is not None:
                diff = min(diff, (root.val - prev))     # pop한 노드값 - 이전 순서 노드값
            prev = root.val             # pop한 노드값이 prev값이 됨
            root = root.right           # 오른쪽 자식으로 이동

        return diff
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **96.65%**    
<i class="fa-solid fa-memory"></i> Memory: **16.63** MB \| Beats **39.96%**

**BST**에서는 **중위 순회(inorder traversal)**를 하면 노드의 값들이 오름차순으로 정렬되는 순서로 방문하게 된다는 것을 이용할 수 있다. prev 값을 None으로 초기화했는데, 주의해야 했던 점은 root 노드가 `0`으로 시작하고 왼쪽 자식이 없는 경우였다. 이 경우 prev값이 `0`이 되는데, 그 다음 pop 이후 `if prev:` 조건에서 `0`도 False로 간주되어서 넘어가버리는 문제가 있었다. `if prev is not None:`으로 확실하게 명시하면 해결할 수 있다.

root = [236,104,701,null,227,null,911]
{: style="color: blue;"}
<pre>
   236
  /   \
104   701
  \     \   
  227   911

                   104   pop   227   pop
stack   -    236   236   236   236   236   pop   701   pop   911   pop
-----------------------------------------------------------------------
root   236   104    n    104    n    227   236    n    701    n    911
                          ↓           ↓     ↓           ↓           ↓
                         227          n    701         911          n

order  104 → 227 → 236 → 701 → 911
diff      23     9    465   210
               (min)  
</pre>

return 9
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/minimum-absolute-difference-in-bst/solutions/6672758/master-bst-in-order-traversal-to-find-mi-k5gd/" target="_blank">1st</a>

```python
class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = None
        self.ans = float('inf')   # 초기값을 무한대로 설정

        def dfs(node):
            if node:
                dfs(node.left)      # 왼쪽 자식 재귀
                if self.prev is not None:
                    self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)     # 오른쪽 자식 재귀

        dfs(root)
        return self.ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ) ← 트리 높이          

이전 노드의 값을 저장하는 변수와 최소 차이를 저장하는 변수를 클래스의 멤버로 선언하고, 재귀 호출을 사용했다.

### <a href="https://leetcode.com/problems/minimum-absolute-difference-in-bst/solutions/338515/python-recursive-by-leetcoder289-i01n/" target="_blank">2nd</a>

```python
class Solution(object):
    def getMinimumDifference(self, root):
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))
```
재귀 호출의 다른 형태도 참고했다. 여기서는 이전 노드의 값을 None이 아니라 가장 작은 값으로 초기화했기 때문에 코드가 조금 더 간단하다.