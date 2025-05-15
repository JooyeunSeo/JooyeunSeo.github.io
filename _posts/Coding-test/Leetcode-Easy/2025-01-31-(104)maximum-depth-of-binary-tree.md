---
excerpt: "'LeetCode: Maximum Depth of Binary Tree' 풀이 정리"
title: "\0104. Maximum Depth of Binary Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Tree
  - DFS
  - Recursion
  - BFS
  - Queue
---

## <i class="fa-solid fa-file-lines"></i> Description

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

- Input: root = [3,9,20,null,null,15,7]
- Output: 3

**Example 2:**

- Input: root = [1,null,2]
- Output: 2

**Constraints:**

- The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
- -100 <= Node.val <= 100

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = 0       # 깊이 초기화

        def count_depth(root, depth): # 매개변수로 depth 전달
            if root is None:          # 노드가 존재하지 않을 경우 현재 저장된 깊이 값 그대로 반환
                return depth
            
            if root:
                depth += 1            # 노드가 존재할 경우 깊이 값에 1 추가
                left_tree = count_depth(root.left, depth)   # 왼쪽 자식 노드에서 재귀 호출
                right_tree = count_depth(root.right, depth) # 오른쪽 자식 노드에서 재귀 호출
                return max(left_tree, right_tree)           # 왼쪽과 오른쪽 중 더 큰 깊이 값 반환

        return count_depth(root, depth)
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **61.36%**    
<i class="fa-solid fa-memory"></i> Memory: **15.33** MB \| Beats **13.68%**

재귀 호출을 하면서 깊이를 계속 카운트하기 위해 변수 depth를 0으로 초기화한 후 count_depth 함수를 생성하여 매개변수로 depth를 전달하는 방식을 사용했다. 또 <mark>.max()</mark> 함수를 사용해서 왼쪽 서브트리와 오른쪽 서브트리 중 더 깊은 쪽을 택하도록 했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/6093733/video-dfs-and-bfs-solution-by-niits-4hmi/" target="_blank">1st</a>

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

깊이 값을 저장하기 위해 따로 변수나 함수를 만들 필요 없이 완성된 답안이어서 좋았다.   
<br>

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:        # 현재 노드가 None이면 깊이 0 반환
            return 0
        
        q = deque()         # 깊이를 저장하는 큐 생성
        q.append(root)      # 큐에 노드 삽입
        depth = 0           # 깊이를 0으로 초기화
        
        while q:            # 큐가 비어있지 않으면 계속 탐색
            depth += 1      # 한 레벨(너비)를 탐색할 때마다 깊이 값에 +1
            
            for _ in range(len(q)):   # 현재 큐에 있는 노드 개수만큼 반복하여 해당 레벨의 모든 노드 처리
                node = q.popleft()      # 큐에서 노드를 꺼내기
                if node.left:             # 왼쪽 자식이 있으면 큐에 추가
                    q.append(node.left)   
                if node.right:            # 오른쪽 자식이 있으면 큐에 추가
                    q.append(node.right)  
        
        return depth        
```
너비 우선 탐색(BFS, Breadth-First Search) 방식으로 접근한 답안도 있어서 참고했다.   
BFS에서는 큐(queue)를 이용하기 때문에 파이썬의 collections 모듈에서 제공하는 <mark>deque</mark>로 큐를 구현한 것을 알 수 있었다.

<div class="notice--info" markdown="1">
💡 **deque(덱, Double-Ended Queue)**

```python
from collections import deque
```

- 양방향에서 삽입/삭제 가능 → `append()`, `appendleft()`, `pop()`, `popleft()`
- 리스트의 `pop()`보다 빠른 연산 가능
- 스택과 큐 모두 구현 가능
</div>

root = [1,2,3,4,5,6]
{: style="color: blue;"}

<pre>
    1
   / \
  2   3
 / \   \
4   5   6

depth = 0                                      →  q = [1]
depth = 1  →  1 out, 2 in, 3 in                →  q = [2, 3]
depth = 2  →  2 out, 4 in, 5 in / 3 out, 6 in  →  q = [4, 5, 6]
depth = 3  →  4 out / 5 out / 6 out            →  q = []
                                                  loop over
</pre>

return 3
{: style="color: green;"}