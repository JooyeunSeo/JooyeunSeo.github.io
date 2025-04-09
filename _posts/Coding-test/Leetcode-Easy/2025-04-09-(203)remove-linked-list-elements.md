---
excerpt: "'LeetCode-Remove Linked List Elements' 풀이 정리"
title: "\0203. Remove Linked List Elements"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Linked List
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

- Input: head = [1,2,6,3,4,5,6], val = 6
- Output: [1,2,3,4,5]

**Example 2:**

- Input: head = [], val = 1
- Output: []

**Example 3:**

- Input: head = [7,7,7,7], val = 7
- Output: []

**Constraints:**

- The number of nodes in the list is in the range [0, 10<sup>4</sup>].
- 1 <= Node.val <= 50
- 0 <= val <= 50

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:                      # 빈 리스트일 경우 바로 반환
            return head

        while head and head.val == val:   # 값이 val이 아닌 첫 번째 노드 정하기
            head = head.next

        result = head                     # 첫 번째 노드를 result로 저장

        while head and head.next:
            if head.next.val == val:          # 현재 노드의 다음 노드값이 val과 같다면
                head.next = head.next.next      # 다음 노드는 한 칸 건너뛴 노드가 됨
            else:
                head = head.next

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.36** MB \| Beats **54.35%**


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-linked-list-elements/solutions/6124597/video-dummy-pointer-by-niits-x6o1/" target="_blank">1st</a>

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        dummy = ans

        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        
        return ans.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

현재 노드의 값이 val일 경우 노드를 스킵할 수 없어서 코드가 길어졌었는데, 맨 앞에 더미 노드를 붙여서 시작하면 훨씬 간단하게 해결할 수 있었다.

### <a href="https://leetcode.com/problems/remove-linked-list-elements/solutions/6628425/master-the-smartest-way-to-delete-nodes-0yado/" target="_blank">2nd</a>

```python
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
```
더미 노드를 생성한 후 head와 연결하는 방법이 위의 솔루션과 조금 달라서 참고했다.