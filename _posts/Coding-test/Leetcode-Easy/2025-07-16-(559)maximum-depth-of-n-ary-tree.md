---
excerpt: "'LeetCode: Maximum Depth of N-ary Tree' 풀이 정리"
title: "\0559. Maximum Depth of N-ary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Tree
  - Depth-First Search
  - Breadth-First Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)
- Input: root = [1,null,3,2,4,null,5,6]
- Output: 3

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)
- Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
- Output: 5

**Constraints:**

- The total number of nodes is in the range [0, 10<sup>4</sup>].
- The depth of the n-ary tree is less than or equal to `1000`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        q.append(child)

        return depth
```
<i class="fa-solid fa-clock"></i> Runtime: **32** ms \| Beats **58.66%**    
<i class="fa-solid fa-memory"></i> Memory: **15.62** MB \| Beats **10.03%**

BFS 방식을 사용해서 깊이를 계산했다. `node.children`가 복수 개일 경우 리스트 형식이기 때문에 for문으로 하나씩 추가했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximum-depth-of-n-ary-tree/solutions/330666/3-python-solutions-recursion-bfs-dfs-by-29p76/" target="_blank">1st</a>

```python
class Solution(object):
    def maxDepth(self, root):
        queue = []
        if root: queue.append((root, 1))    # 빈 트리가 아니라면 (루트 노트, 깊이)를 포함
        depth = 0
        for (node, level) in queue:
            depth = level
            queue += [(child, level+1) for child in node.children]
        return depth
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑤)           

큐를 이용한 방법 중 더 간단하게 짠 코드를 참고했다. deque()를 사용하지 않고 구현했다.

### <a href="https://leetcode.com/problems/maximum-depth-of-n-ary-tree/solutions/330666/3-python-solutions-recursion-bfs-dfs-by-29p76/" target="_blank">2nd</a>

```python
class Solution(object):
    def maxDepth(self, root):
        stack = []
        if root: stack.append((root, 1))
        depth = 0
        while stack:
            (node, d) = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((child, d+1))
        return depth
```
이 문제에서는 스택을 이용한 DFS가 BFS보다 더 효율적이었다. 노드들의 깊이 중 가장 큰 값을 저장하면 된다.

### <a href="" target="_blank">3rd</a>

```python
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0

        # 현재 루트의 깊이 1 + 각 자식의 깊이 중 최대값(자식이 없는 경우는 0 반환)
        return 1 + max(map(self.maxDepth, root.children or [None]))
```
재귀 호출을 사용한 두 줄짜리 코드다. 자식이 없는 노드의 경우 `root.children or [None]` 부분은 `False or [None]`이 되기 때문에 자동으로 or 뒤의 값을 선택하게 되고 `0`을 반환하게 된다.
<mark>map()</mark>은 두 번째 인자로 iterable를 요구하기 때문에 None을 리스트로 만들어줘야 한다.