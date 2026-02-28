---
excerpt: "'LeetCode: Add Two Numbers' 풀이 정리"
title: "\02. Add Two Numbers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Principal
  - Linked List
  - Math
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)
- Input: l1 = [2,4,3], l2 = [5,6,4]
- Output: [7,0,8]
- Explanation: 342 + 465 = 807.

**Example 2:**

- Input: l1 = [0], l2 = [0]
- Output: [0]

**Example 3:**

- Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
- Output: [8,9,9,9,0,0,0,1]

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)     # 결과 연결리스트 노드 생성(더미 노드로 시작)
        curr = dummy            # 현재 노드 위치
        carry = 0               # 올림수

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)    # 다음 노드 생성
            curr = curr.next                    # 다음 노드로 이동

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.42** MB \| Beats **39.11%**    

새 연결 리스트를 만들어서 더한 값을 저장하는 방법을 사용했다. 연결 리스트는 head를 유지해야 하기 때문에 더미 노드로 시작점을 고정했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/add-two-numbers/solutions/5184763/video-simple-addition-algorithm-python-j-hgno/" target="_blank">1st</a>

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(max(𝑚,𝑛))    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(max(𝑚,𝑛))    