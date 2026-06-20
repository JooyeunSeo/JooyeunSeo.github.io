---
excerpt: "'LeetCode: Populating Next Right Pointers in Each Node' 풀이 정리"
title: "\0116. Populating Next Right Pointers in Each Node"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Linked List
  - Depth-First Search
  - Breadth-First Search
  - Binary Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

<pre>
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)
- Input: root = [1,2,3,4,5,6,7]
- Output: [1,#,2,3,#,4,5,6,7,#]
- Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

**Example 2:**

- Input: root = []
- Output: []

**Constraints:**

- The number of nodes in the tree is in the range [0, 2<sup>12</sup> - 1].
- -1000 <= Node.val <= 1000

**Follow up:** 

- You may only use constant extra space.
- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_start = root                          # 레벨 시작(가장 왼쪽 노드)
        
        while level_start and level_start.left:
            head = level_start                      # 연결 리스트 시작

            while head:
                head.left.next = head.right         # 같은 부모의 자식끼리 연결
                if head.next:                       # 다른 부모의 자식끼리 연결
                    head.right.next = head.next.left
                head = head.next
            
            level_start = level_start.left

        return root
```
<i class="fa-solid fa-clock"></i> Runtime: **48** ms \| Beats **95.70%**    
<i class="fa-solid fa-memory"></i> Memory: **20.68** MB \| Beats **48.31%**    

현재 레벨의 가장 왼쪽 노드를 가리키는 level_start 포인터와 현재 레벨을 연결 리스트처럼 가로로 순회하는 head 포인터를 사용해서 자식들의 next를 연결했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def connect(self, root):
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1) → 재귀 스택 제외   

재귀 호출로 구현한 코드이다.