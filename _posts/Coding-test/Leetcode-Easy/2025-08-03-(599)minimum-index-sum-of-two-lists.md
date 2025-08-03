---
excerpt: "'LeetCode: Minimum Index Sum of Two Lists' 풀이 정리"
title: "\0599. Minimum Index Sum of Two Lists"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two arrays of strings `list1` and `list2`, find the **common strings with the least index sum.**

A **common string** is a string that appeared in both `list1` and `list2`.

A **common string with the least index sum** is a common string such that if it appeared at `list1[i]` and `list2[j]` then `i + j` should be the minimum value among all the other **common strings.**

Return *all the **common strings with the least index sum.*** Return the answer in **any order.**

**Example 1:**

- Input:    
list1 = ["Shogun","Tapioca Express","Burger King","KFC"],     
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
- Output: ["Shogun"]
- Explanation: The only common string is "Shogun".

**Example 2:**

- Input:z list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
- Output: ["Shogun"]
- Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

**Example 3:**

- Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
- Output: ["sad","happy"]
- Explanation: There are three common strings:    
"happy" with index sum = (0 + 1) = 1.    
"sad" with index sum = (1 + 0) = 1.    
"good" with index sum = (2 + 2) = 4.    
The strings with the least index sum are "sad" and "happy".

**Constraints:**

- 1 <= list1.length, list2.length <= 1000
- 1 <= list1[i].length, list2[i].length <= 30
- `list1[i]` and `list2[i]` consist of spaces `' '` and English letters.
- All the strings of `list1` are **unique**.
- All the strings of `list2` are **unique**.
- There is at least a common string between `list1` and `list2`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_idx_sum = len(list1) + len(list2) - 2
        result = []

        intersection = set(list1) & set(list2)
        
        for resto in intersection:
            idx_sum = list1.index(resto) + list2.index(resto)
            if idx_sum == min_idx_sum:
                result.append(resto)
            elif idx_sum < min_idx_sum:
                min_idx_sum = idx_sum
                result = [resto]
                
        return result
```
두 리스트를 set()으로 바꾼 뒤 교집합을 구하는 방법을 사용해봤는데 인덱스를 호출하는 부분 때문에 공통된 단어가 많을수록 느려지는 단점이 있었다.

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        hashmap = {}
        min_idx_sum = len(list1) + len(list2) - 2   # 최대값으로 초기화
        result = []

        # list1의 원소값과 인덱스를 딕셔너리에 저장
        for i, val in enumerate(list1):
            hashmap[val] = i

        # list2의 원소값이 이미 딕셔너리에 있는지 확인
        for j, val in enumerate(list2):
            if val in hashmap:
                idx_sum = hashmap[val] + j
                
                # 두 인덱스를 더한 값이 최소값을 갱신하는지 확인
                if idx_sum < min_idx_sum:
                    min_idx_sum = idx_sum
                    result = [val]
                elif idx_sum == min_idx_sum:
                    result.append(val)
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **1** ms \| Beats **96.97%**    
<i class="fa-solid fa-memory"></i> Memory: **12.57** MB \| Beats **90.02%**

첫 번째 리스트를 먼저 순회하며 해시 테이블에 저장하고, 그 다음 두 번째 리스트를 순회하며 해시 테이블에 같은 키가 있는지 확인했다. 해당 문제에서는 이 방법이 가장 효율적인 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/minimum-index-sum-of-two-lists/solutions/6723641/conquer-common-restaurant-index-match-with-hashmap-beginner-friendly-clean/" target="_blank">1st</a>

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in index_map:
                index_sum = j + index_map[word]
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [word]
                elif index_sum == min_sum:
                    result.append(word)

        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑘) ← 공통 단어의 개수          

약간 디테일이 다른 코드도 참고해봤다.