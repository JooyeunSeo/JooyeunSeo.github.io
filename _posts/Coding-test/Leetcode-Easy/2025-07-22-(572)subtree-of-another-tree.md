---
excerpt: "'LeetCode: Subtree of Another Tree' 풀이 정리"
title: "\0572. Subtree of Another Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Depth-First Search
  - String Matching
  - Binary Tree
  - Hash Function
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)
- Input: root = [3,4,5,1,2], subRoot = [4,1,2]
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
- Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
- Output: false

**Constraints:**

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- -10<sup>4</sup> <= root.val <= 10<sup>4</sup>
- -10<sup>4</sup> <= subRoot.val <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Which approach is better here- recursive or iterative?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">If recursive approach is better, can you write recursive function with its parameters?</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Two trees <b>s</b> and <b>t</b> are said to be identical if their root values are same and their left and right subtrees are identical. Can you write this in form of recursive formulae?</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">Recursive formulae can be: isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isIdentical(t1, t2):
            if not t1 and not t2:   # 둘 다 None이면 같음
                return True
            if not t1 or not t2:    # 둘 중 하나만 None이면 다름
                return False
            return t1.val == t2.val and \   
                   isIdentical(t1.left, t2.left) and \
                   isIdentical(t1.right, t2.right)

        # 큰 트리의 현재 노드가 None이면 비교 불가
        if not root:
            return False

        # 큰 트리의 현재 노드와 작은 트리의 루트 값이 같다면 전체 구조 비교
        if isIdentical(root, subRoot):
            return True

        # 구조가 달랐다면 큰 트리의 왼쪽 or 오른쪽 서브트리 중 일치하는 것이 있는지 다시 확인
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```
<i class="fa-solid fa-clock"></i> Runtime: **69** ms \| Beats **86.11%**    
<i class="fa-solid fa-memory"></i> Memory: **14.00** MB \| Beats **9.92%**

`isSubtree`로 메인 트리를 순회하면서 두 노드가 동일한 트리인지 확인하는 `isIdentical`을 반복해서 검사하는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/subtree-of-another-tree/solutions/6723566/master-subtree-detection-with-tree-seria-fvta/" target="_blank">1st</a>

```python
class Solution(object):
    def isSubtree(self, root, subRoot):
        def ser(n):
            if not n:
                return ',#'
            return ',' + str(n.val) + ser(n.left) + ser(n.right)

        return ser(subRoot) in ser(root)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛*𝑚) ← 각 트리의 노드 수   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛+𝑚)           

두 트리를 **직렬화(serialize)**해서 문자열로 표현한 뒤, `subRoot`가 `root` 안에 포함되는지 확인하는 방법이다. 각 노드끼리는 `,`로 구분하고 만약 노드가 None일 경우 값 대신 `#`으로 대체해서 트리 구조를 유지했다.

root = [3,4,5,1,2]    
subRoot = [4,1,2]
{: style="color: blue;"}
<pre>
  root          
    3           
   / \       subRoot
  4   5         4   
 / \           / \
1   2         1   2

ser(root)    = ,3,4,1,#,#,2,#,#,5,#,#
ser(subRoot) =   ,4,1,#,#,2,#,#
</pre>

return True
{: style="color: green;"}