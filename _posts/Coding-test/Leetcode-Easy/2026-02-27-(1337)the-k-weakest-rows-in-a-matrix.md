---
excerpt: "'LeetCode: The K Weakest Rows in a Matrix' 풀이 정리"
title: "\01337. The K Weakest Rows in a Matrix"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
  - Sorting
  - Heap (Priority Queue)
  - Matrix
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an `m x n` binary matrix `mat` of `1`'s (representing soldiers) and `0`'s (representing civilians). The soldiers are positioned **in front** of the civilians. That is, all the `1`'s will appear to the **left** of all the `0`'s in each row.

A row `i` is **weaker** than a row `j` if one of the following is true:

- The number of soldiers in row `i` is less than the number of soldiers in row `j`.
- Both rows have the same number of soldiers and `i < j`.

Return *the indices of the* `k` ***weakest*** *rows in the matrix ordered from weakest to strongest.*

**Example 1:**

- Input:      
mat = [       
`[1,1,0,0,0]`,     
`[1,1,1,1,0]`,     
`[1,0,0,0,0]`,     
`[1,1,0,0,0]`,     
`[1,1,1,1,1]`       
],     
k = 3
- Output: [2,0,3]
- Explanation: The number of soldiers in each row is:       
Row 0: 2        
Row 1: 4        
Row 2: 1        
Row 3: 2        
Row 4: 5        
The rows ordered from weakest to strongest are [2,0,3,1,4].

**Example 2:**

- Input:       
mat = [      
`[1,0,0,0]`,    
`[1,1,1,1]`,    
`[1,0,0,0]`,    
`[1,0,0,0]`    
],     
k = 2
- Output: [0,2]
- Explanation: The number of soldiers in each row is:      
Row 0: 1      
Row 1: 4      
Row 2: 1      
Row 3: 1      
The rows ordered from weakest to strongest are [0,2,3,1].

**Constraints:**

- m == mat.length
- n == mat[i].length
- 2 <= n, m <= 100
- 1 <= k <= m
- matrix[i][j] is either `0` or `1`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Sort the matrix row indexes by the number of soldiers and then row indexes.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order = []
        result = []

        for i, row in enumerate(mat):     # (군인 수, 인덱스)
            soldiers = row.count(1)
            order.append((soldiers, i))

        order.sort()                      # 정렬
        
        for i in range(k):                # 인덱스 k개
            result.append(order[i][1])

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.82** MB \| Beats **31.61%**    

파이썬에서 튜플 비교는 앞자리부터 우선 비교하고, 같으면 다음 자리를 비교하는 방식이기 때문에 편리하게 정렬할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solutions/1201679/c-python3-no-heap-no-bs-simple-sort-9920-phhq/" target="_blank">1st</a>

```python
class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		m = len(mat)
		rows = sorted(range(m), key=lambda i: (mat[i], i))
		del rows[k:]
		return rows
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚𝑛 + 𝑚log𝑚 + 𝑘)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚)    

파이썬에서는 리스트도 튜플처럼 사전식 비교가 되기 때문에 `[1,1,0,0,0] < [1,1,1,0,0]`과 같이 비교할 수 있다. 이 문제에서는 1이 앞쪽에 몰려있는 형태이기 때문에 `mat[i]`만으로도 1의 개수 순서대로 정렬할 수 있다.

### <a href="https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solutions/4057683/9841-sorting-min-heap-binary-search-by-v-mzlp/" target="_blank">2nd</a>

```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            strength = sum(row)
            heapq.heappush(heap, (-strength, -i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [-i for _, i in sorted(heap, reverse=True)]
```
최소힙을 사용한 방법이다.