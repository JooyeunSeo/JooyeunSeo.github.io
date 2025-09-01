---
excerpt: "'LeetCode: Kth Largest Element in a Stream' 풀이 정리"
title: "\0703. Kth Largest Element in a Stream"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Design
  - Binary Search Tree
  - Heap (Priority Queue)
  - Data Stream
---

## <i class="fa-solid fa-file-lines"></i> Description

You are part of a university admissions office and need to keep track of the `kth` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `k`, maintains a stream of test scores and continuously returns the `k`th highest test score **after** a new score has been submitted. More specifically, we are looking for the `k`th highest score in the sorted list of all scores.

Implement the `KthLargest` class:

- `KthLargest(int k, int[] nums)` Initializes the object with the integer k and the stream of test scores nums.
- `int add(int val)` Adds a new test score `val` to the stream and returns the element representing the k<sup>th</sup> largest element in the pool of test scores so far.

**Example 1:**

- Input:    
["KthLargest", "add", "add", "add", "add", "add"]    
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
- Output: [null, 4, 5, 5, 8, 8]
- Explanation:    
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);    
kthLargest.add(3); // return 4    
kthLargest.add(5); // return 5    
kthLargest.add(10); // return 5    
kthLargest.add(9); // return 8    
kthLargest.add(4); // return 8

**Example 2:**

- Input:    
["KthLargest", "add", "add", "add", "add"]    
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
- Output: [null, 7, 7, 7, 8]
- Explanation:    
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);    
kthLargest.add(2); // return 7    
kthLargest.add(10); // return 7    
kthLargest.add(9); // return 7    
kthLargest.add(9); // return 8

**Constraints:**

- 0 <= nums.length <= 10<sup>4</sup>
- 1 <= k <= nums.length + 1
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- -10<sup>4</sup> <= val <= 10<sup>4</sup>
- At most 10<sup>4</sup> calls will be made to `add`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap_size = k
        self.min_heap = []
        
        for num in nums:
            self.add(num)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        n = len(self.min_heap)

        # 힙 길이가 아직 k보다 작으면 맨 뒤에 새 값 삽입 후 앞으로 이동
        if n < self.heap_size:
            self.min_heap.append(val)
            i = n
            while i > 0:
                parent = (i - 1) // 2   # 부모의 인덱스 계산 공식
                if self.min_heap[i] < self.min_heap[parent]:
                    self.min_heap[i], self.min_heap[parent] = self.min_heap[parent], self.min_heap[i]
                    i = parent
                else:
                    break
        
        # 힙 길이가 이미 k이고 새 값이 최소값(맨 앞)보다 크다면 그 자리에 대입 후 뒤로 이동
        elif val > self.min_heap[0]:                
            self.min_heap[0] = val
            i = 0
            while i < n:
                left = (i * 2) + 1      # 왼쪽자식의 인덱스 계산 공식
                right = (i * 2) + 2     # 오른쪽자식의 인덱스 계산 공식
                min_child = i
                if left < n and self.min_heap[left] < self.min_heap[min_child]:
                    min_child = left
                if right < n and self.min_heap[right] < self.min_heap[min_child]:
                    min_child = right

                if min_child != i:
                    self.min_heap[i], self.min_heap[min_child] = self.min_heap[min_child], self.min_heap[i]
                    i = min_child
                else:
                    break

        return self.min_heap[0] # k번째 큰 값(최소힙의 첫 번째)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

```python
import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.heap_size = k
        self.min_heap = []
        for num in nums:    # 먼저 nums의 원소들을 하나씩 add 함수로 처리
            self.add(num)

    def add(self, val):
        if len(self.min_heap) < self.heap_size:
            heapq.heappush(self.min_heap, val)      # 힙 불변성을 유지하면서 val을 push
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)   # 힙에서 최소값을 pop 및 반환 후 val을 push
        return self.min_heap[0]
```
<i class="fa-solid fa-clock"></i> Runtime: **54** ms \| Beats **73.22%**    
<i class="fa-solid fa-memory"></i> Memory: **18.36** MB \| Beats **17.50%**

일반 리스트로 최소힙을 구현하려고 했는데, 시간이 오래 걸렸다. 파이썬의 경우 내장된 heapq 모듈을 쓰는 것이 가장 빠르고 정석인 방법같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/solutions/148866/python-simple-heapq-solution-beats-100-b-a1r0/" target="_blank">1st</a>

```python
class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)        # 리스트를 선형 시간으로 제자리에서 힙으로 변환
        while len(self.pool) > k:
            heapq.heappop(self.pool)    # 힙 불변성을 유지하면서 최소값을 pop 및 반환

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
```
<i class="fa-solid fa-clock"></i> **time complexity:** Initialization: 𝑂(𝑛log𝑘), add(): 𝑂(log𝑘)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑘) ← heap size          

리스트 nums를 먼저 `heapq.heapify()`를 통해 힙으로 변환하는 방법도 있었다.