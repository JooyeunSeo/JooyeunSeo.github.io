---
excerpt: "'LeetCode: Implement Stack using Queues' 풀이 정리"
title: "\0225. Implement Stack using Queues"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Stack
  - Queue
  - Design
---

## <i class="fa-solid fa-file-lines"></i> Description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns true if the stack is empty, false otherwise.

**Notes:**

- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

**Example 1:**

- Input   
["MyStack", "push", "push", "top", "pop", "empty"]   
[[], [1], [2], [], [], []]
- Output   
[null, null, null, 2, 2, false]
- Explanation   
MyStack myStack = new MyStack();   
myStack.push(1);   
myStack.push(2);   
myStack.top(); // return 2   
myStack.pop(); // return 2   
myStack.empty(); // return False   

**Constraints:**

- 1 <= x <= 9
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

**Follow up:** Can you implement the stack using only one queue?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()            # 큐 생성

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)            # 가장 위에 값을 추가

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()         # 가장 위의 값을 제거

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]           # 가장 위의 값을 확인만 하기

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0     # 빈 큐일때만 True 반환

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.41** MB \| Beats **56.85%**

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/implement-stack-using-queues/solutions/6251049/video-one-queue-and-two-queue-solution-b-q7eb/" target="_blank">1st</a>

```python
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)                      # 1. 큐의 뒤에 값 추가
        for _ in range(len(self.q) - 1):      # 2. 큐의 앞에서 값을 꺼내서 뒤에 다시 추가하는 것을 (길이-1)번 반복
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()               # pop: 큐의 맨 앞 == 스택의 맨 위(push에서 순서 변경됨)
        
    def top(self) -> int:
        return self.q[0]                      # top: 큐의 맨 앞 == 스택의 맨 위(push에서 순서 변경됨)

    def empty(self) -> bool:
        return len(self.q) == 0               # empty: 큐의 길이가 0이면 비어있는 것
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1): pop, top, empty / 𝑂(𝑛): push    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

큐 1개로 구현하는 방법

### <a href="https://leetcode.com/problems/implement-stack-using-queues/solutions/6251049/video-one-queue-and-two-queue-solution-b-q7eb/" target="_blank">2nd</a>

```python
class MyStack:

    def __init__(self):
        self.q1 = deque()   # 큐1 (메인)
        self.q2 = deque()   # 큐2 (임시)

    def push(self, x: int) -> None:             # push: 큐1에 새 값 추가
        self.q1.append(x)                         

    def pop(self) -> int:                       
        while len(self.q1) > 1:                 # 1. 큐1의 오래된 값부터 하나씩 꺼내서 큐2로 이동
            self.q2.append(self.q1.popleft())

        popped_val = self.q1.popleft()          # 2. 큐1에 마지막 남은 값 꺼내서 저장
        self.q1, self.q2 = self.q2, self.q1     # 3. 큐1과 큐2를 교체

        return popped_val
        
    def top(self) -> int:
        while len(self.q1) > 1:                 # 1. 큐1의 오래된 값부터 하나씩 꺼내서 큐2로 이동
            self.q2.append(self.q1.popleft())

        top_val = self.q1[0]                    # 2. 큐1에 마지막 남은 값 확인만 해서 저장
        self.q2.append(self.q1.popleft())       # 3. 큐1의 마지막 값도 큐2로 이동
        self.q1, self.q2 = self.q2, self.q1     # 4. 큐1과 큐2를 교체

        return top_val

    def empty(self) -> bool:
        return len(self.q1) == 0                # empty: 큐1이 비어있는지 확인
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1): push, empty / 𝑂(𝑛): pop, top    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛) 

큐 2개로 구현하는 방법