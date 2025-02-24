---
excerpt: "'LeetCode-Intersection of Two Linked Lists' 풀이 정리"
title: "\0160. Intersection of Two Linked Lists"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Linked List
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the heads of two singly linked-lists `headA` and `headB`, return *the node at which the two lists intersect*. If the two linked lists have no intersection at all, return `null`.

For example, the following two linked lists begin to intersect at node `c1`:

![](https://assets.leetcode.com/uploads/2021/03/05/160_statement.png)

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

**Note** that the linked lists must **retain their original structure** after the function returns.

**Custom Judge:**

The inputs to the **judge** are given as follows (your program is **not** given these inputs):

- `intersectVal` - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
- `listA` - The first linked list.
- `listB` - The second linked list.
- `skipA` - The number of nodes to skip ahead in `listA` (starting from the head) to get to the intersected node.
- `skipB` - The number of nodes to skip ahead in `listB` (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, `headA` and `headB` to your program. If you correctly return the intersected node, then your solution will be **accepted**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png)

- Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
- Output: Intersected at '8'
- Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5].    
From the head of B, it reads as [5,6,1,8,4,5].   
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.   
→ Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png)

- Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
- Output: Intersected at '2'
- Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).   
From the head of A, it reads as [1,9,1,2,4].    
From the head of B, it reads as [3,2,4].    
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

**Example 3:**

![](https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png)

- Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
- Output: No intersection
- Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.   
Explanation: The two lists do not intersect, so return null.

**Constraints:**

- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 1 <= m, n <= 3 * 10<sup>4</sup>
- 1 <= Node.val <= 10<sup>5</sup>
- 0 <= skipA <= m
- 0 <= skipB <= n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

**Follow up:**  Could you write a solution that runs in `O(m + n)` time and use only `O(1)` memory?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA, listB = [], []
        
        while headA:
            listA.append(headA)
            headA = headA.next
        while headB:
            listB.append(headB)
            headB = headB.next
        
        if listA[-1] != listB[-1]:    # 두 리스트의 마지막 노드가 다르다면 교차점 없음
            return listA[-1].next

        i = -1
        nodeA = listA[i]
        nodeB = listB[i]

        while nodeA == nodeB and -i < min(len(listA), len(listB)):
            nodeA = listA[i - 1]
            nodeB = listB[i - 1]
            i -= 1

        if nodeA == nodeB:
            return nodeA
        else:
            return listA[i + 1]       # 마지막으로 같았던 노드
```
<i class="fa-solid fa-clock"></i> Runtime: **123** ms \| Beats **92.52%**    
<i class="fa-solid fa-memory"></i> Memory: **42.49** MB \| Beats **33.60%**

리스트에 두 연결 리스트의 모든 노드를 저장한 후, 뒤에서부터 탐색하며 비교하는 방식을 사용했다. 𝑂(𝑛+𝑚)의 추가 공간이 필요한 단점이 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA   # A 헤드 저장
        listb = headB   # B 헤드 저장

        while lista != listb:
            lista = lista.next if lista else headB  # headA + headB
            listb = listb.next if listb else headA  # headB + headA
        
        return listb
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

`3 + 2`와 `2 + 3`은 모두 5가 되는 것과 비슷한 원리를 이용하여 두 리스트의 길이를 맞추는 방법으로, 두 개의 포인터를 이용해 상수 공간만큼만 추가로 사용할 수 있다는 장점이 있다.

intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
{: style="color: blue;"}

<pre>
                           B→→→→→→→→→→→→
A: 4 → 1 → 8 → 4 → 5 → n → 5 → 6 → 1 → 8 
B: 5 → 6 → 1 → 8 → 4 → 5 → n → 4 → 1 → 8
                               A→→→→→→→→
n = null node                          ↳ intersection
</pre>

Intersected at '8'
{: style="color: green;"}