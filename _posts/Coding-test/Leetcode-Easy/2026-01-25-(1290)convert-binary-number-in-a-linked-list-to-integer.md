---
excerpt: "'LeetCode: Convert Binary Number in a Linked List to Integer' 풀이 정리"
title: "\01290. Convert Binary Number in a Linked List to Integer"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Linked List
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either `0` or `1`. The linked list holds the binary representation of a number.

Return *the decimal value* of the number in the linked list.

The **most significant bit** is at the head of the linked list.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/12/05/graph-1.png)
- Input: head = [1,0,1]
- Output: 5
- Explanation: (101) in base 2 = (5) in base 10

**Example 2:**

- Input: head = [0]
- Output: 0

**Constraints:**

- The Linked List is not empty.
- Number of nodes will not exceed `30`.
- Each node's value is either `0` or `1`.

**Follow up:** 
**Note:** This question is the same as <a href="" target="_blank">번호.제목</a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        
        while head:
            result <<= 1        # 비트를 왼쪽으로 밀어서 마지막 자리 확보
            result |= head.val  # 마지막 자리에 현재 값 넣기
            head = head.next

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.35** MB \| Beats **14.40%**    

리스트를 순회하며 발견한 값을 문자열로 저장해도 되지만, 비트를 누적시키는 방법을 사용하면 O(1) 메모리만 사용하여 풀 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solutions/455239/python-simple-20ms-by-rohin7-4cqe/" target="_blank">1st</a>

```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

비트 연산 대신 사칙연산으로 계산해도 같은 결과가 나온다.