---
excerpt: "'LeetCode: Remove Nth Node From End of List' 풀이 정리"
title: "\019. Remove Nth Node From End of List"
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

Given the `head` of a linked list, remove the n<sup>th</sup> node from the end of the list and return its head.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
- Input: head = [1,2,3,4,5], n = 2
- Output: [1,2,3,5]

**Example 2:**

- Input: head = [1], n = 1
- Output: []

**Example 3:**

- Input: head = [1,2], n = 1
- Output: [1]

**Constraints:**

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

**Follow up:** Could you do this in one pass?

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Maintain two pointers and update one with a delay of n steps.
</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        save = head
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next

        if not fast:            # 노드가 1개인 경우
            return head.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return save
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.28** MB \| Beats **85.01%**    

fast를 먼저 n칸 보내고 slow와 같이 움직이는 구조로 한 번의 순회만에 풀 수 있다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/7262169/remove-nth-node-from-end-of-list-by-prag-kxg5/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second= dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

head를 따로 저장하는 것보다 맨 앞에 더미 노드를 생성하는 방법이 훨씬 더 깔끔해서 좋았다.