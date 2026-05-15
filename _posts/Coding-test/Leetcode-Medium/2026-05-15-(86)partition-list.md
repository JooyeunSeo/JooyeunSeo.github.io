---
excerpt: "'LeetCode: Partition List' 풀이 정리"
title: "\086. Partition List"
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

Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

You should **preserve** the original relative order of the nodes in each of the two partitions.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)
- Input: head = [1,4,3,2,5,2], x = 3
- Output: [1,2,2,4,3,5]

**Example 2:**

- Input: head = [2,1], x = 2
- Output: [1,2]

**Constraints:**

- The number of nodes in the list is in the range `[0, 200]`.
- -100 <= Node.val <= 100
- -200 <= x <= 200

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small = small_dummy
        large = large_dummy

        while head:
            temp = head.next            # 다음 노드를 임시저장
            head.next = None            # 현재 노드-다음 노드 연결 끊기

            if head.val < x:            # 현재 노드 이동
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next

            head = temp                 # 임시저장했던 다음 노드로 이동

        small.next = large_dummy.next   # small-large 연결

        return small_dummy.next
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.46** MB \| Beats **7.58%**    

x값 기준으로 small, large 리스트를 따로 분리한 후 현재 노드를 하나씩 떼어서 둘 중 하나에 붙이는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/partition-list/solutions/6750680/video-solution-by-niits-yzyp/" target="_blank">1st</a>

```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        slist, blist = ListNode(), ListNode()
        small, big = slist, blist # dummy lists

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next

        small.next = blist.next
        big.next = None # prevent linked list circle

        return slist.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    