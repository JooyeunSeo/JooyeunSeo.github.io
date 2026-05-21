---
excerpt: "'LeetCode: Reverse Linked List II' 풀이 정리"
title: "\092. Reverse Linked List II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Linked List
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
- Input: head = [1,2,3,4,5], left = 2, right = 4
- Output: [1,4,3,2,5]

**Example 2:**

- Input: head = [5], left = 1, right = 1
- Output: [5]

**Constraints:**

- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

**Follow up:** Could you do it in one pass?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        i = 1

        while curr:
            if i == left:                       # reverse 시작 위치 도착
                before_left = prev                  # reverse 구간 직전 노드
                reversed_tail = curr                # reverse 후 꼬리가 될 노드(원래 left 위치)
                reversed_prev = None                # reverse용 이전 노드

                while left <= i <= right:           # reverse 구간
                    temp = curr.next                  # 다음 노드 저장
                    curr.next = reversed_prev         # 방향 반전
                    reversed_prev = curr              # 포인터들 이동
                    curr = temp
                    i += 1

                before_left.next = reversed_prev    # reverse된 새 head 연결
                reversed_tail.next = curr           # reverse된 tail과 나머지 연결

                return dummy.next                   # reverse 구간 뒤집은 후 바로 반환 가능

            else:                               # 일반 순회
                prev = curr
                curr = curr.next
                i += 1

        return dummy.next
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.28** MB \| Beats **91.53%**    

<a href="https://jooyeunseo.github.io/leetcode-easy/(206)reverse-linked-list/" target="_blank">206. Reverse Linked List</a> 문제에서 업그레이드 되어 중간 일부분만 뒤집어야 한다. 문제에서 제대로 설명이 안 되어있지만, 인덱스가 1부터 시작하고 left와 right는 인덱스 위치를 의미한다는 것을 알아야 한다.

head = [1,2,3,4,5]     
left = 2    
right = 4
{: style="color: blue;"}
<pre>
1  → [2  →  3  →  4] →  5      
bl    rt

N     2  →  3  →  4        |  N  ←  2     3  →  4
rp    c     t                       rp    c

N  ←  2     3  →  4        |  N  ←  2  ←  3     4   
      rp    c     t                       rp    c
 
N  ←  2  ←  3     4  →  5  |  N  ←  2  ←  3  ←  4     5
            rp    c     t                       rp    c

1  → [4  →  3  →  2] →  5
bl    rp          rt    c
</pre>

return [1,4,3,2,5]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-linked-list-ii/solutions/4011862/9240-two-pointers-stack-recursion-by-van-sz5v/" target="_blank">1st</a>

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):       # left 전까지 이동
            prev = prev.next

        cur = prev.next                 # reverse 구간 시작
        for _ in range(right - left):   # reverse 구간 뒤집기
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

여기서는 cur 다음 노드를 떼어서 reverse 구간 맨 앞으로 이동하는 방법으로 구간을 뒤집는다.

head = [1,2,3,4,5]     
left = 2    
right = 4
{: style="color: blue;"}
<pre>
d  →  1  → [2  →  3  →  4] →  5    |    d  →  1  → [3  →  2  →  4] →  5 
      p     c     t                           p     t     c

d  →  1  → [3  →  2  →  4] →  5    |    d  →  1  → [4  →  3  →  2] →  5
      p           c     t                     p     t           c

      1  → [4  →  3  →  2] →  5
</pre>