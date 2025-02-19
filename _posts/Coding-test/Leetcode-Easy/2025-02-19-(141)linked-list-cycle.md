---
excerpt: "'LeetCode-Linked List Cycle' 풀이 정리"
title: "\0141. Linked List Cycle"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Linked List
  - Cycle Detection
  - Floyd
  - Two Pointers
  - set()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

- Input: head = [3,2,0,-4], pos = 1
- Output: true
- Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

- Input: head = [1,2], pos = 0
- Output: true
- Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

- Input: head = [1], pos = -1
- Output: false
- Explanation: There is no cycle in the linked list.

**Constraints:**

- The number of the nodes in the list is in the range [0, 10<sup>4</sup>].
- -10<sup>5</sup> <= Node.val <= 10<sup>5</sup>
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `𝑂(1)` (i.e. constant) memory?    

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        one_step = head     # 한 칸씩 이동하는 포인터(slow)
        two_step = head     # 두 칸씩 이동하는 포인터(fast)

        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next

            if one_step == two_step:      # 두 포인터가 동일한 노드를 가리키는 경우 - 사이클 있음
                return True
        return False                      # 끝이 있는 연결 리스트일 경우 - 사이클 없음
```
<i class="fa-solid fa-clock"></i> Runtime: **41** ms \| Beats **33.99%**    
<i class="fa-solid fa-memory"></i> Memory: **19.72** MB \| Beats **19.61%**

`𝑂(1)`의 메모리만 사용하면서 문제를 해결하기 위해서 플로이드의 거북이와 토끼 알고리즘을 참고해야 했다. 이 알고리즘은 속도가 다른 두 개의 포인터를 계속 루프 안에서 반복하다 보면 결국 두 포인터가 같은 노드에서 만나게 된다는 것을 활용한 것이다.   

`head` = [3,2,0,-4], `pos` = 1
{: style="color: blue;"}

<pre>
0  1  2  3  1  2  3 ...  → index
-----------------------
3  2  0 -4  2  0 -4 ...
   s  f                  → s: index = 1, f: index = 2
      s     f            → s: index = 2, f: index = 1
         s        f      → s: index = 3, f: index = 3
</pre>

return True
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/linked-list-cycle/solutions/3999014/9968-two-pointer-hash-table-by-vanamsen-ansm/" target="_blank">1st</a>

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        return False
```
해시 테이블 방법을 사용한 예시로, 방문했던 노드 자체를 저장해놓기 때문에 재방문할 경우 True를 반환하게 된다.   
<mark>set()</mark>은 해시 테이블을 기반으로 동작하는 함수로, 노드의 메모리 주소를 해시 함수에 넣으면 해당 인덱스를 반환하기 때문에 빠른 속도로 연산할 수 있다. 즉 *리스트* 보다 빠르고, 값 없이 키만 저장하기 때문에 *딕셔너리* 보다 효율적이다.   
다만 공간 복잡도가 𝑂(𝑛)이기 때문에 플로이드의 알고리즘보다 비효율적인 방법이다.