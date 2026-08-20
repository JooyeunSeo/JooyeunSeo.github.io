---
excerpt: "'LeetCode: Sum Root to Leaf Numbers' 풀이 정리"
title: "\0129. Sum Root to Leaf Numbers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - Binary Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given the `root` of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)
- Input: root = [1,2,3]
- Output: 25
- Explanation:    
The root-to-leaf path 1->2 represents the number 12.       
The root-to-leaf path 1->3 represents the number 13.     
Therefore, sum = 12 + 13 = 25.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)
- Input: root = [4,9,0,5,1]
- Output: 1026
- Explanation:    
The root-to-leaf path 4->9->5 represents the number 495.     
The root-to-leaf path 4->9->1 represents the number 491.     
The root-to-leaf path 4->0 represents the number 40.      
Therefore, sum = 495 + 491 + 40 = 1026.

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- 0 <= Node.val <= 9
- The depth of the tree will not exceed `10`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return

            path += (str(node.val))

            if not node.left and not node.right:
                path_sums.append(int(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

        path_sums = []
        dfs(root, "")

        return sum(path_sums)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.26** MB \| Beats **71.79%**    

깊이 우선 탐색으로 루트에서 잎 노드까지의 각 경로를 탐색했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/sum-root-to-leaf-numbers/solutions/6965919/beats-100-sum-root-to-leaf-numbers-java-g0j5l/" target="_blank">1st</a>

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path = path * 10 + node.val
            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(ℎ)    

int에서 str, str에서 int 변환없이 푸는 방법이다.