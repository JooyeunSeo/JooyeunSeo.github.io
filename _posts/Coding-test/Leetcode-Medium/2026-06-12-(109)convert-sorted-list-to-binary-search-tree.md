---
excerpt: "'LeetCode: Convert Sorted List to Binary Search Tree' 풀이 정리"
title: "\0109. Convert Sorted List to Binary Search Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Linked List
  - Divide and Conquer
  - Binary Search Tree
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `head` of a singly linked list where elements are sorted in **ascending order**, convert it to a height-balanced binary search tree.

*[height-balanced]: A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)
- Input: head = [-10,-3,0,5,9]
- Output: [0,-3,9,-10,null,5]
- Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

**Example 2:**

- Input: head = []
- Output: []

**Constraints:**

- The number of nodes in head is in the range [0, 2 * 10<sup>4</sup>].
- -10<sup>5</sup> <= Node.val <= 10<sup>5</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = build(left, mid-1)
            root.right = build(mid+1 , right)

            return root
        
        return build(0, len(nums)-1)
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **98.53%**    
<i class="fa-solid fa-memory"></i> Memory: **24.07** MB \| Beats **29.79%**    

연결 리스트를 먼저 순회해서 배열로 변환했다. 이미 오름차순으로 정렬된 배열이기 때문에 쉽게 BST로 변환할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solutions/8314650/python-fast-slow-pointers-divide-conquer-lcfe/" target="_blank">1st</a>

```python
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow = head
        slow_prev = slow    # used to break the connection for the root.left
        fast = head
        
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if slow_prev:
            slow_prev.next = None
        
        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
    
        return root
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(log𝑛)    

연결 리스트를 배열로 저장하고 싶지 않을 때 사용할 수 있는 방법이다. 다만 중간 노드를 찾기 위해 매번 slow/fast pointer로 순회하기 때문에 앞의 방법보다 시간 복잡도가 더 올라간다.