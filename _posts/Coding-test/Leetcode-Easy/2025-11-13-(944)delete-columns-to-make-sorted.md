---
excerpt: "'LeetCode: Delete Columns to Make Sorted' 풀이 정리"
title: "\0944. Delete Columns to Make Sorted"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

- For example, `strs = ["abc", "bce", "cae"]` can be arranged as follows:
   <pre>
   abc
   bce
   cae
   </pre>

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (**0-indexed**), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return *the number of columns that you will delete*.

**Example 1:**

- Input: strs = ["cba","daf","ghi"]
- Output: 1
- Explanation: The grid looks as follows:   
   <pre>
   cba
   daf
   ghi
   </pre>
   Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

**Example 2:**

- Input: strs = ["a","b"]
- Output: 0
- Explanation: The grid looks as follows:
   <pre>
   a
   b
   </pre>
   Column 0 is the only column and is sorted, so you will not delete any columns.

**Example 3:**

- Input: strs = ["zyx","wvu","tsr"]
- Output: 3
- Explanation: The grid looks as follows:
   <pre>
   zyx   
   wvu   
   tsr   
   </pre>
   All 3 columns are not sorted, so you will delete all 3.

**Constraints:**

- n == strs.length
- 1 <= n <= 100
- 1 <= strs[i].length <= 1000
- strs[i] consists of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        len_list, len_str = len(strs), len(strs[0])
        delete_col = 0

        for j in range(len_str):                # 열
            for i in range(1, len_list):        # 1행부터 시작해서 이전 행과 비교
                if strs[i][j] < strs[i-1][j]:
                    delete_col += 1
                    break
                    
        return delete_col
```
<i class="fa-solid fa-clock"></i> Runtime: **63** ms \| Beats **59.42%**    
<i class="fa-solid fa-memory"></i> Memory: **18.22** MB \| Beats **71.66%**    

각 열을 세로로 읽으면서 사전순대로 정렬되어있는지 확인하면 된다. 0행은 시작부분이기 때문에 이전 값과 비교할 필요가 없어서 1행부터 순회했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/delete-columns-to-make-sorted/solutions/194919/python-count-unsorted-columns-by-lee215-g2hl/" target="_blank">1st</a>

```python
    def minDeletionSize(self, A):
        return sum(list(col) != sorted(col) for col in zip(*A))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛𝑚log𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚)    

```python
    def minDeletionSize(self, A):
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*A))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

`zip(*A)`로 간단하게 열 단위 튜플들을 생성할 수도 있다.