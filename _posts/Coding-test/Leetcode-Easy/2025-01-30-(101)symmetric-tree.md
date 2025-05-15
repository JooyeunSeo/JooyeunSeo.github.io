---
excerpt: "'LeetCode: Symmetric Tree' 풀이 정리"
title: "\0101. Symmetric Tree"
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
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, check *whether it is a mirror of itself* (i.e., symmetric around its center).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

- Input: root = [1,2,2,3,4,4,3]
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

- Input: root = [1,2,2,null,3,null,3]
- Output: false

**Constraints:**

- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

**Follow up:** Could you solve it both recursively and iteratively?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def compare(l_tree, r_tree):        # 왼쪽 서브트리와 오른쪽 서브트리 비교
            if not l_tree and not r_tree:   # 둘 다 None이면 대칭
                return True         
            if not l_tree or not r_tree:    # 한 쪽만 None이면 대칭 x
                return False  
            if l_tree.val != r_tree.val:    # 두 값이 다르면 대칭 x
                return False  
            
            # 왼쪽 서브트리의 왼쪽과 오른쪽 서브트리의 오른쪽 비교 and 왼쪽 서브트리의 오른쪽과 오른쪽 서브트리의 왼쪽 비교
            return compare(l_tree.left, r_tree.right) and compare(l_tree.right, r_tree.left)

        return compare(root.left, root.right)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.77** MB \| Beats **15.01%**

처음에는 트리를 왼쪽과 오른쪽으로 절반 나눈 뒤, 왼쪽 서브트리는 루트 → 왼쪽 자식 → 오른쪽 자식 순으로 순회하고, 오른쪽 서브트리는 루트 → 오른쪽 자식 → 왼쪽 자식 순으로 순회해서 두 순서가 동일한지 비교하는 방법을 사용했다.   
그러나 단순히 순회 순서를 비교하는 것은 트리의 모양이 달라도 우연의 일치로 결과가 같아질 가능성이 있어서 적합하지 않았다. 때문에 재귀 방식으로 직접 좌우 노드를 각각 비교하는 방법으로 바꿨다.

root = [1,2,2,3,4,4,3]
{: style="color: blue;"}

<pre>
    1
   / \
  2   2
 / \ / \
3  4 4  3

1.    compare(root.left, root.right)
    → compare(2, 2)
    → compare(2.left, 2.right) and compare(2.right, 2.left)
    → compare(3, 3) and compare(4, 4)

2-1.  compare(3, 3)
    → compare(3.left, 3.right) and compare(3.right, 3.left)
    → compare(None, None) and compare(None, None)
    → True

2-2.  compare(4, 4)
    → compare(4.left, 4.right) and compare(4.right, 4.left)
    → compare(None, None) and compare(None, None)
    → True
</pre>

compare(2, 2) = `True` and `True`   
return `True`
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/symmetric-tree/solutions/6104800/video-going-to-left-side-and-right-side-at-the-same-time/" target="_blank">1st</a>

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_mirror(n1, n2): # n1:left, n2:right
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False
            
            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
        
        return is_mirror(root.left, root.right)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)     