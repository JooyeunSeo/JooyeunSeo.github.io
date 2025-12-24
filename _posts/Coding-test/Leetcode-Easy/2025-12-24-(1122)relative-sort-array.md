---
excerpt: "'LeetCode: Relative Sort Array' 풀이 정리"
title: "\01122. Relative Sort Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Sorting
  - Counting Sort
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two arrays `arr1` and `arr2`, the elements of arr2 are distinct, and all elements in `arr2` are also in `arr1`.

Sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `rr2.` Elements that do not appear in `arr2` should be placed at the end of `arr1` in **ascending** order.

**Example 1:**

- Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
- Output: [2,2,2,1,4,3,3,9,6,7,19]

**Example 2:**

- Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
- Output: [22,28,8,6,17,44]

**Constraints:**

- 1 <= arr1.length, arr2.length <= 1000
- 0 <= arr1[i], arr2[i] <= 1000
- All the elements of `arr2` are **distinct**.
- Each arr2[i] is in arr1.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Using a hashmap, we can map the values of arr2 to their position in arr2.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">After, we can use a custom sorting function.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_idx = {n: i for i, n in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (arr2_idx.get(x, 1001), x))
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.54** MB \| Beats **94.80%**    

arr2의 원소를 키로 하고 인덱스를 값으로 하는 해시맵을 생성 후, lambda로 정의한 key 함수를 이용하여 arr1을 재정렬했다. 첫 번째 정렬 기준은 arr2_idx의 값 i로, x값이 키로 존재할 경우 그대로 값을 가져오고 키가 없을 경우 최대값보다 큰 `1001`을 가져오는 것으로 처리했다. 값 1001을 가진 모든 원소들은 두 번째 정렬 기준에 따라 맨 뒤에 오름차순으로 들어오게 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/relative-sort-array/solutions/334585/python-straight-forward-1-line-and-2-lin-skrv/" target="_blank">1st</a>

```python
class Solution:
    def relativeSortArray(self, A, B):
            k = {b: i for i, b in enumerate(B)}
            return sorted(A, key=lambda a: k.get(a, 1000 + a))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛) ← n: len(arr1)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛+𝑚) ← m: len(arr2)   

arr1의 원소가 arr2의 키가 아닐 경우, `원소 + 1000`을 값으로 가져오는 것으로 변경하면 정렬 조건을 하나만 작성해도 된다.