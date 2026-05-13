---
excerpt: "'LeetCode: Remove Duplicates from Sorted List II' 풀이 정리"
title: "\082. Remove Duplicates from Sorted List II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Linked List
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list **sorted** as well.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)
- Input: head = [1,2,3,3,4,4,5]
- Output: [1,2,5]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)
- Input: head = [1,1,1,2,3]
- Output: [2,3]

**Constraints:**

- The number of nodes in the list is in the range `[0, 300]`.
- -100 <= Node.val <= 100
- The list is guaranteed to be **sorted** in ascending order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                dup = head.val                  # 중복 숫자 기억
                while head and head.val == dup: # 중복 숫자 전부 스킵
                    head = head.next
                prev.next = head                # 연결 이어붙이기
            else:
                prev = head
                head = head.next

        return dummy.next
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.31** MB \| Beats **33.17%**    

<a href="https://jooyeunseo.github.io/leetcode-easy/(83)remove-duplicates-from-sorted-list/" target="_blank">83. Remove Duplicates from Sorted List</a> 문제와 달리 중복값 자체를 전부 제거해야 해서 조금 더 까다로워졌다. dummy 노드가 거의 필수로 사용되며, 이전 정상 노드(prev)를 유지하는 것이 중요하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solutions/6801800/beats-100-easiest-explanation-for-beginn-6noz/" target="_blank">1st</a>

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next  # Skip all duplicates
            else:
                prev = prev.next  # Move to next distinct node
            cur = cur.next

        return dummy.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

중복 숫자를 굳이 기억하지 않아도 된다.