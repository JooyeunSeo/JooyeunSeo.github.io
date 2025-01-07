---
excerpt: "'LeetCode-Merge Two Sorted Lists' 풀이 정리"
title: "\021. Merge Two Sorted Lists"
header:
  teaser: "/assets/images/defaults/logo-LeetCode-black.png"
categories:
  - Leetcode
tags:
  - Coding Test
  - Easy
  - Python
  - Linked List
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the *head of the merged linked list*.

**Example 1:**

- Input: list1 = \[1,2,4], list2 = \[1,3,4]    
- Output: \[1,1,2,3,4,4]

**Example 2:**

- Input: list1 = \[], list2 = \[]
- Output: \[]

**Example 3:**

- Input: list1 = \[], list2 = \[0]
- Output: \[0]

**Constraints:**

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both `list1` and `list2` are sorted in **non-decreasing** order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()     # 연결 리스트의 시작을 가리키는 헤드 생성(데이터 없음)
        current = head        # 현재 가리키는 노드(연결 리스트 마지막)를 헤드로 초기화
        
        while list1 and list2:            # 두 리스트가 모두 비어있지 않을 때까지 반복
            if list1.val <= list2.val:
                current.next = list1      # list1의 현재 노드를 결과 리스트에 추가
                list1 = list1.next        # 현재 노드의 다음 노드로 이동
            else:
                current.next = list2      # list2의 현재 노드를 결과 리스트에 추가
                list2 = list2.next        # 현재 노드의 다음 노드로 이동

            current = current.next        # 결과 리스트에서 current 포인터를 한 칸 이동
            
        current.next = list1 if list1 else list2  # 한 쪽 리스트가 먼저 끝난 경우 남은 리스트를 전부 연결
        return head.next                          # head를 반환하면 연결 리스트가 전부 반환됨
```
<i class="fa-solid fa-clock"></i> **time complexity:** O(m+n) ← `list1`과 `list2`의 길이     
<i class="fa-solid fa-memory"></i> **space complexity:** O(1)   

연결 리스트를 파이썬으로 구현하는 것이 생소해서 솔루션 게시판의 <a href="https://leetcode.com/problems/merge-two-sorted-lists/solutions/6048156/video-using-dummy-pointer-and-recursion-solution-as-a-bonus/" target="_blank">포스트</a>를 참고했다.

`list1` = 1 → 2 → 4    
`list2` = 1 → 3 → 4
{: style="color: blue;"}

merged sorted list:

|     head →    | 1 → | 1 → | 2 → | 3 → | 4 → | 4 |
|:-------------:|-----|-----|-----|-----|-----|---|
| list1 current | 2   | 2   | 4   | 4   | /   |   |
| list2 current | 1   | 3   | 3   | 4   |     | / |