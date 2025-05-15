---
excerpt: "'LeetCode: Reverse Linked List' 풀이 정리"
title: "\0206. Reverse Linked List"
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

Given the `head` of a singly linked list, reverse the list, and return the *reversed list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

- Input: head = [1,2,3,4,5]
- Output: [5,4,3,2,1]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

- Input: head = [1,2]
- Output: [2,1]

**Example 3:**

- Input: head = []
- Output: []

**Constraints:**

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        value_list = []   # 노드들의 값을 순서대로 저장할 리스트
        current = head    # 노드의 값을 바꾸기 위해 처음부터 다시 순회할 때 쓸 포인터
        result = head     # 완성된 연결 리스트를 리턴할 때 쓸 포인터

        while head:
            value_list.append(head.val)
            head = head.next

        for v in value_list[::-1]:
            current.val = v
            current = current.next

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **16.75%**    
<i class="fa-solid fa-memory"></i> Memory: **14.22** MB \| Beats **87.64%**

연결 리스트를 순회하며 값들을 따로 저장한 후, 다시 연결 리스트를 처음부터 순회하며 값을 바꿔줬다. 많이 느리지만 더 빠르게 할 방법이 생각나지 않아서 일단 풀었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-linked-list/solutions/6072712/video-solution-with-visualization-by-nii-h754/" target="_blank">1st</a>

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None             # head의 반대 방향의 노드(Null에서 시작)

        while head:
            temp = head.next    # head의 원래 방향의 다음 노드를 가리키는 임시 포인터
            head.next = node    # head가 반대 방향의 노드를 가리키도록 변경
            node = head         # 현재 head의 자리로 node 이동
            head = temp         # 현재 temp의 자리로 head 이동
        
        return node
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

head(h) = [1, 2, 3]    
node(n) = None
{: style="color: blue;"}
<pre>
n   h          (○ = Null node)
○   1 → 2 → 3 → ○   
---------------------------------------------
n   h   t                       n   h
○ ← 1   2 → 3 → ○           ○ ← 1   2 → 3 → ○

    n   h   t                       n   h
○ ← 1 ← 2   3 → ○           ○ ← 1 ← 2   3 → ○

        n   h   t                       n   h
○ ← 1 ← 2 ← 3   ○           ○ ← 1 ← 2 ← 3   ○
</pre>

return node(n) = [3, 2, 1]
{: style="color: green;"}

### <a href="https://leetcode.com/problems/reverse-linked-list/solutions/6072712/video-solution-with-visualization-by-nii-h754/" target="_blank">2nd</a>

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:   # base case: 빈 연결리스트이거나 노드가 한 개만 있을 때
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head     # 현재 노드(head)의 다음 노드(head.next)가 현재 노드를 가리키도록 변경
        head.next = None          # 다음 노드(head.next)를 None으로 설정(기존 연결을 끊어서 무한 루프 방지)
        return new_head
```
재귀를 사용한 방법도 참고했다.

head = [1, 2, 3]    
{: style="color: blue;"}
<pre>
호출 단계          head   head.next      올라오는 단계        head   new_head
reverseList(1)    1        2       |   reverseList(2)     2        3
↓                                  |   ↓
reverseList(2)    2        3       |   reverseList(1)     1        3
↓                                  |                           
reverseList(3)    3        ○       |
            (base case, return 3)  |
</pre>

return new_head = [3, 2, 1]
{: style="color: green;"}