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

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

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

## <i class="fa-solid fa-flask"></i> Other Solutions

### 1st

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:               # 둘 중 빈 리스트가 있을 경우 재귀 호출 종료
            return list2
        if not list2:
            return list1
            
        if list1.val < list2.val:   # 재귀: 각 리스트의 현재 노드를 비교
            # list1의 현재 노드가 더 작으면, list1을 결과에 포함
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2의 현재 노드가 더 작으면, list2를 결과에 포함
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

재귀 호출을 이용한 방법으로, 위의 함수보다 실행 시간은 더 오래걸렸다.

`list1` = 1 → 2 → 4    
`list2` = 1 → 3 → 4
{: style="color: blue;"}
<br>

**재귀 호출 순서**

1. mergeTwoLists(`1 → 2 → 4`, `1 → 3 → 4`)
   - **list1.val (1)** vs list2.val (1) ⇒ list1 선택
   - list1.next = mergeTwoLists(`2 → 4`, `1 → 3 → 4`) 호출
2. mergeTwoLists(`2 → 4`, `1 → 3 → 4`)
   - list1.val (2) vs **list2.val (1)** ⇒ list2 선택
   - list2.next = mergeTwoLists(`2 → 4`, `3 → 4`) 호출
3. mergeTwoLists(`2 → 4`, `3 → 4`)
   - **list1.val (2)** vs list2.val (3) ⇒ list1 선택
   - list1.next = mergeTwoLists(`4`, `3 → 4`) 호출
4. mergeTwoLists(`4`, `3 → 4`)
   - list1.val (4) vs **list2.val (3)** ⇒ list2 선택
   - list2.next = mergeTwoLists(`4`, `4`) 호출
5. mergeTwoLists(`4`, `4`)
   - **list1.val (4)** vs list2.val (4) ⇒ list1 선택
   - list1.next = mergeTwoLists(`None`, `4`) 호출
6. mergeTwoLists(`None`, `4`)
   - list1이 `None`이므로, **list2**를 return `4 → None`
   
<br>

**반환 과정(역순 호출)**

1. mergeTwoLists(`None`, `4`) ⇒ return `4 → None` (반환된 값을 이전 호출에서 list1.next에 연결)
2. mergeTwoLists(`4`, `4`) ⇒ return `4 → 4 → None`
3. mergeTwoLists(`4`, `3 → 4`) ⇒ return `3 → 4 → 4 → None`
4. mergeTwoLists(`2 → 4`, `3 → 4`) ⇒ return `2 → 3 → 4 → 4 → None`
5. mergeTwoLists(`2 → 4`, `1 → 3 → 4`) ⇒ return `1 → 2 → 3 → 4 → 4 → None`
6. mergeTwoLists(`1 → 2 → 4`, `1 → 3 → 4`) ⇒ return `1 → 1 → 2 → 3 → 4 → 4 → None`