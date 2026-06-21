---
excerpt: "'LeetCode: Populating Next Right Pointers in Each Node II' 풀이 정리"
title: "\0117. Populating Next Right Pointers in Each Node II"
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

Given a binary tree

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

![](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)
- Input: root = [1,2,3,4,5,null,7]
- Output: [1,#,2,3,#,4,5,7,#]
- Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

**Example 2:**

- Input: root = []
- Output: []

**Constraints:**

- The number of nodes in the tree is in the range `[0, 6000]`.
- -100 <= Node.val <= 100

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
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        dummy = Node(0)
        child_tail = dummy          # 다음 레벨의 연결 마지막

        while curr:
            head = curr             # 현재 레벨 연결 상태

            while head:
                if head.left:
                    child_tail.next = head.left
                    child_tail = child_tail.next

                if head.right:
                    child_tail.next = head.right
                    child_tail = child_tail.next

                head = head.next

            curr = dummy.next       # 다음 레벨 시작 노드
            dummy.next = None       # 다음 레벨에 재사용하기 위해 연결 끊음
            child_tail = dummy      

        return root
```
<i class="fa-solid fa-clock"></i> Runtime: **45** ms \| Beats **89.42%**    
<i class="fa-solid fa-memory"></i> Memory: **20.40** MB \| Beats **25.66%**    

<a href="https://jooyeunseo.github.io/leetcode-medium/(116)populating-next-right-pointers-in-each-node/" target="_blank">116. Populating Next Right Pointers in Each Node</a> 문제와 달리 자식이 한 쪽만 있거나 아예 없는 경우도 고려해야 한다. 여기서는 매 레벨마다 가짜 헤드 노드 dummy를 이용하여 연결하기 때문에 중간에 자식이 없는 노드가 끼어있어도 연결할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/solutions/37824/ac-python-o1-space-solution-12-lines-and-xu4d/" target="_blank">1st</a>

```python
class Solution:
    def connect(self, node):
        tail = dummy = TreeLinkNode(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

### <a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/solutions/961868/python-on-solution-explained-by-dbabiche-k8kw/" target="_blank">2nd</a>

```python
class Solution:
    def connect(self, root):
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
               
        return root
```