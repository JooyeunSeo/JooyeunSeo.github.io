---
excerpt: "'LeetCode: Swap Nodes in Pairs' 풀이 정리"
title: "\024. Swap Nodes in Pairs"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Linked List
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

**Example 1:**

- Input: head = [1,2,3,4]
- Output: [2,1,4,3]
- Explanation:       
![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

**Example 2:**

- Input: head = []
- Output: []

**Example 3:**

- Input: head = [1]
- Output: [1]

**Example 4:**

- Input: head = [1,2,3]
- Output: [2,1,3]

**Constraints:**

- The number of nodes in the list is in the range `[0, 100]`.
- 0 <= Node.val <= 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy                # 더미 노드에서 시작

        while curr.next and curr.next.next:
            s1 = curr.next          # 다음 노드 주소 참조
            s2 = curr.next.next     # 다음다음 노드 주소 참조
            curr.next = s2          # s2를 현재 노드 뒤에 연결
            s1.next = s2.next       # s2의 다음 노드를 s1도 다음으로 가리키도록 연결
            s2.next = s1            # s2를 s1 앞으로 이동
            curr = curr.next.next
        
        return dummy.next
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.44** MB \| Beats **19.11%**    

뒤쪽 연결을 유지하면서 두 노드의 포인터를 재배치하는 방법으로, 순서가 중요하다.

head = [1,2,3]
{: style="color: blue;"}
<pre>
(d)   (1)  (2)  (3)
curr → s1 → s2 → next
curr → s2 →→→→→→ next 
            s1 ↗︎ 
curr → s2 → s1 → next
(d)   (2)  (1)  (3)
</pre>

return [2,1,3]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/swap-nodes-in-pairs/solutions/171788/python-dummynode-by-yuzhoujr-1ktx/" target="_blank">1st</a>

```python
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

재귀 호출을 통해 뒤쪽 연결을 유지하는 방법이다. `head, head.next = head.next, head`의 경우 오른쪽의 head.next, head 값을 먼저 저장한 후 왼쪽에 할당하기 때문에 가능한 수식이다.