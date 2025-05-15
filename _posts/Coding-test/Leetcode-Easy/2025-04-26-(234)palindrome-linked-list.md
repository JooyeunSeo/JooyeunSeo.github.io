---
excerpt: "'LeetCode: Palindrome Linked List' 풀이 정리"
title: "\0234. Palindrome Linked List"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Linked List
  - Palindrome
  - Floyd
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `head` of a singly linked list, return `true` *if it is a **palindrome** or* `false` *otherwise*.

*[palindrome]: An integer is a palindrome when it reads the same forward and backward.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)
- Input: head = [1,2,2,1]
- Output: true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)
- Input: head = [1,2]
- Output: false

**Constraints:**

- The number of nodes in the list is in the range [1, 10<sup>5</sup>].
- 0 <= Node.val <= 9

**Follow up:** Could you do it in `O(n)` time and `O(1)` space?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        order = []
        while head:
            order.append(head.val)
            head = head.next
        
        if len(order) % 2 == 0:
            left = order[:(len(order)//2)]
            right = order[(len(order)//2):]
        else:
            left = order[:(len(order)//2 + 1)]
            right = order[(len(order)//2):]

        right.reverse()   # 오른쪽 리스트 뒤집기

        if left == right:
            return True
        else:
            return False
```
<i class="fa-solid fa-clock"></i> Runtime: **125** ms \| Beats **73.06%**    
<i class="fa-solid fa-memory"></i> Memory: **84.23** MB \| Beats **24.55%**

리스트에 저장 후 반으로 나눠서 비교하는 방법을 썼다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/palindrome-linked-list/solutions/1137027/js-python-java-c-easy-floyds-reversal-so-pv1b/" target="_blank">1st</a>

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

플로이드 알고리즘으로 중간 지점을 찾을 수 있다. fast가 끝에 도착하면 slow는 중간에 와 있게 된다. 중간 지점부터 리스트를 역순으로 만든 후, 처음 head와 뒤집힌 중간 이후를 하나씩 비교하면 된다.

<pre>
1 → 2 → 3 → 2 → 1

slow = 1, fast = 1
slow = 2, fast = 3
slow = 3, fast = 1
stop(fast.next == None)

       s
1 → 2  3  2 → 1
1 → 2     2 → 3 → None
1 → 2         1 → 2 → 3 → None

----------------------------
1 → 2 → 3 → 3 → 2 → 1

slow = 1, fast = 1
slow = 2, fast = 3
slow = 3, fast = 2
stop(fast.next == None)

        s
1 → 2 → 3   3 → 2 → 1
1 → 2 → 3       2 → 3 → None
1 → 2 → 3           1 → 2 → 3 → None
</pre>