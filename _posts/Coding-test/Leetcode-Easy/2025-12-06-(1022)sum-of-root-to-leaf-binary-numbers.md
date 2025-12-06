---
excerpt: "'LeetCode: Sum of Root To Leaf Binary Numbers' 풀이 정리"
title: "\01022. Sum of Root To Leaf Binary Numbers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Binary Tree
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit.

- For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return *the sum of these numbers.*

The test cases are generated so that the answer fits in a **32-bits** integer.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)
- Input: root = [1,0,1,0,1,0,1]
- Output: 22
- Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

**Example 2:**

- Input: root = [0]
- Output: 0

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `Node.val` is `0` or `1`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Find each path, then transform that path to an integer in base 10.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(0, root)]     # (누적 합계, 현재 노드)

        while stack:
            prev, node = stack.pop()
            curr = (prev * 2) + node.val

            if not node.left and not node.right:  # 잎노드
                result += curr
            
            if node.right:
                stack.append([curr, node.right])
            if node.left:
                stack.append([curr, node.left])              
    
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.99** MB \| Beats **90.01%**    

스택을 이용하여 각 root-to-leaf path를 순회하고 누적 합계를 저장할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/1681682/well-detailed-explaination-java-c-python-mqkc/" target="_blank">1st</a>

```python
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumRootToLeaf(root, res): # here; "res" is "sum"
            if root == None: return 0
            res = (2 * res) + root.val
            if root.left == None and root.right == None: return res
            return sumRootToLeaf(root.left, res) + sumRootToLeaf(root.right, res)
        
        return sumRootToLeaf(root, 0)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)    

재귀 호출로 푸는 방법도 참고했다.