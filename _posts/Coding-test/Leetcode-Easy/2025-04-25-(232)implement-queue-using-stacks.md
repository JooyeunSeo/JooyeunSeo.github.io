---
excerpt: "'LeetCode-Implement Queue using Stacks' 풀이 정리"
title: "\0232. Implement Queue using Stacks"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Queue
  - Stack
---

## <i class="fa-solid fa-file-lines"></i> Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns true if the queue is empty, false otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

**Example 1:**

- Input   
["MyQueue", "push", "push", "peek", "pop", "empty"]   
[[], [1], [2], [], [], []]
- Output   
[null, null, null, 1, 1, false]
- Explanation   
MyQueue myQueue = new MyQueue();   
myQueue.push(1); // queue is: [1]   
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)   
myQueue.peek(); // return 1   
myQueue.pop(); // return 1, queue is [2]   
myQueue.empty(); // return false

**Constraints:**

- 1 <= x <= 9
- At most 100 calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

**Follow up:** Can you implement the queue such that each operation is <a href="https://en.wikipedia.org/wiki/Amortized_analysis" target="_blank">amortized</a> `O(1)` time complexity? In other words, performing `n` operations will take overall `O(n)` time even if one of those operations may take longer.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class MyQueue(object):

    def __init__(self):
        self.stack_main = []
        self.stack_temp = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while len(self.stack_main) > 0:
            self.stack_temp.append(self.stack_main.pop())
        
        self.stack_temp.append(x)

        while len(self.stack_temp) > 0:
            self.stack_main.append(self.stack_temp.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.stack_main.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack_main[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_main) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.49** MB \| Beats **56.06%**

push를 할 때 순서를 정렬하는 방법으로 구현해봤다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/implement-queue-using-stacks/solutions/6579732/video-simple-solution-by-niits-sqaw/" target="_blank">1st</a>

```python
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # Ensure output stack has the current front
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:  # Transfer elements if output stack is empty
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1): push, empty / amortized 𝑂(1): pop, peek    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛) 

제출했던 답변은 push가 자주 일어날 경우 효율이 좋지 않기 때문에, 이것처럼 각 원소가 input에서 output으로 단 한번만 이동하는 방식이 더 좋은 성능을 낼 수 있다.