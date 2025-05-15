---
excerpt: "'LeetCode: Remove Duplicates from Sorted List' 풀이 정리"
title: "\083. Remove Duplicates from Sorted List"
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

Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return the *linked list* ***sorted*** *as well*.


**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)

- Input: head = [1,1,2]
- Output: [1,2]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)

- Input: head = [1,1,2,3,3]
- Output: [1,2,3]

**Constraints:**

- The number of nodes in the list is in the range `[0, 300]`.
- -100 <= Node.val <= 100
- The list is guaranteed to be **sorted** in ascending order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(-101)          # 더미 노드 초기값을 문제에서 설정한 범위의 밖으로 설정
        cur = ans                     # 결과 리스트에 사용되는 포인터를 ans로 초기화

        while head:                   # 입력 리스트 head 순회
            if head.val != cur.val:
                cur.next = head       # head를 결과 리스트에 연결
                cur = cur.next        # cur을 새로 추가된 노드로 이동

            head = head.next          # head에서 다음 노드로 이동

        cur.next = None               # head의 마지막 노드 이후 연결 제거
        return ans.next               # 더미 노드 이후의 리스트를 반환
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.50** MB \| Beats **13.71%**

ListNode() 함수로 연결 리스트를 생성하면 초기값이 자동으로 0으로 설정되어서 `0 → 0 → 0` 과 같은 head일 경우 아무 것도 출력되지 않았다.
그래서 -101로 더미 노드의 초기값을 설정해서 처음 시작은 무조건 중복되지 않도록 했는데, 깔끔한 알고리즘은 아닌 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/solutions/5810798/video-explain-important-points-by-niits-maxm/" target="_blank">1st</a>

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head                            # head를 변경해도 계속 리스트 시작 부분을 추적하기 위함

        while head and head.next:             # head와 head.next가 None이 아닐 때까지 반복
            if head.val == head.next.val:     # head에서 현재 가리키는 노드와 그 다음 노드가   
                head.next = head.next.next      # 같으면 그 다음 노드를 스킵하고 그 다음 다음의 노드를 포인트
            else:
                head = head.next                # 같지 않으면 그 다음 노드를 포인트 
        
        return res                            # 변경된 연결 리스트의 헤드를 가리키는 res 반환
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)            

`head` = 1 → 1 → 2 → 3 → 3   
{: style="color: blue;"}

<pre>
1 → 1 → 2 → 2 → 3   head.val(= 1) == head.next(= 1)  ⇒ remove 1
h
r

1 → 2 → 2 → 3       head.val(= 1) != head.next(= 2)  ⇒ move h  
h
r

1 → 2 → 2 → 3       head.val(= 2) == head.next(= 2)  ⇒ remove 2
r   h

1 → 2 → 3           head.val(= 2) != head.next(= 3)  ⇒ move h  
r   h

1 → 2 → 3           return res(= 1 → 2 → 3)
r       h
</pre>

`res` = 1 → 2 → 3
{: style="color: green;"}


### <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/solutions/6108743/0-ms-runtime-beats-100-user-code-idea-al-4hk9/" target="_blank">2nd</a>

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate
            else:
                current = current.next  # Move to the next node
        
        return head
```

위의 예시 답안과 달리 두 개의 포인터를 따로 두지 않았다.
하지만 리스트를 변경하는 것은 current고 head가 리스트 시작점을 나타내는 포인터인 것은 변함없기 때문에 head를 반환해도 올바른 결과가 나온다.