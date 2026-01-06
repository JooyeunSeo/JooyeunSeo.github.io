---
excerpt: "'LeetCode: Unique Number of Occurrences' 풀이 정리"
title: "\01207. Unique Number of Occurrences"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `arr`, return `true` *if the number of occurrences of each value in the array is **unique** or* `false` *otherwise*.

**Example 1:**

- Input: arr = [1,2,2,1,1,3]
- Output: true
- Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

**Example 2:**

- Input: arr = [1,2]
- Output: false

**Example 3:**

- Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
- Output: true

**Constraints:**

- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Find the number of occurrences of each element in the array using a hash map.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Iterate through the hash map and check if there is a repeated value.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        occurrences = []                        # 등장 횟수 기록

        for n in arr:                           # 해시맵 생성
            counter[n] = counter.get(n, 0) + 1

        for v in counter.values():
            if v not in occurrences:
                occurrences.append(v)
            else:
                return False

        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.45** MB \| Beats **15.00%**    

해시 테이블을 이용하는 간단한 문제다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-number-of-occurrences/solutions/4577893/beats-100-users-cjavapythonjavascript-2-g7425/" target="_blank">1st</a>

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return len(freq) == len(set(freq.values()))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    