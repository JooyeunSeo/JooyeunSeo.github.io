---
excerpt: "'LeetCode: Middle of the Linked List' 풀이 정리"
title: "\0876. Middle of the Linked List"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Linked List
  - Two Pointers
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `head` of a singly linked list, return *the middle node of the linked list.*

If there are two middle nodes, return **the second middle** node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)
- Input: head = [1,2,3,4,5]
- Output: [3,4,5]
- Explanation: The middle node of the list is node 3.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)
- Input: head = [1,2,3,4,5,6]
- Output: [4,5,6]
- Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

**Constraints:**

- The number of nodes in the list is in the range `[1, 100]`.
- 1 <= Node.val <= 100

**Follow up:** 
**Note:** This question is the same as 번호: <a href="" target="_blank"></a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">hint</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        one_step = head                     # 1노드씩 이동
        two_steps = head                    # 2노드씩 이동

        while two_steps and two_steps.next: # two_steps가 마지막 노드이거나 리스트를 벗어났을 경우 중지
            one_step = one_step.next
            two_steps = two_steps.next.next

        return one_step
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats **84.06%**

한 칸씩 이동하는 포인터와 두 칸씩 이동하는 포인터 두 개를 사용했다. 두 칸씩 이동하는 포인터가 마지막 노드이거나 리스트를 벗어났을 때, 한 칸씩 이동하는 포인터가 리스트의 가운데에 위치하게 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/middle-of-the-linked-list/solutions/2646800/full-beginner-python-explanation-3-metho-4r51/" target="_blank">1st</a>

```python
class Solution(object):
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      runner = head     # runner to find the length of the linked list
      length = 0        # length of list
      while runner:
        length += 1     # add 1 to the length whenever we still have a node
        runner = runner.next
      for i in range(length//2):  # go halfway through the linked list
        head = head.next
      return head                 # return the middle node
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

포인터 두 개를 이용하는 방법이 가장 효율적이지만, 다른 방법도 참고해봤다.