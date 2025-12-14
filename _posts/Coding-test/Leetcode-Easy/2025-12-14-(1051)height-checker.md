---
excerpt: "'LeetCode: Height Checker' 풀이 정리"
title: "\01051. Height Checker"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Sorting
  - Counting Sort
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the i<sup>th</sup> student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the i<sup>th</sup> student in line **(0-indexed)**.

Return *the **number of indices** where* `heights[i] != expected[i]`.

**Example 1:**

- Input: heights = [1,1,4,2,1,3]
- Output: 3
- Explanation:        
<span style="color:#F5F5F5">_</span>heights : [1,1,<u>4</u>,2,<u>1</u>,<u>3</u>]        
expected: [1,1,<u>1</u>,2,<u>3</u>,<u>4</u>]        
Indices 2, 4, and 5 do not match.

**Example 2:**

- Input: heights = [5,1,2,3,4]
- Output: 5
- Explanation:        
<span style="color:#F5F5F5">_</span>heights : [<u>5</u>,<u>1</u>,<u>2</u>,<u>3</u>,<u>4</u>]         
expected: [<u>1</u>,<u>2</u>,<u>3</u>,<u>4</u>,<u>5</u>]        
All indices do not match.

**Example 3:**

- Input: heights = [1,2,3,4,5]
- Output: 0
- Explanation:        
<span style="color:#F5F5F5">_</span>heights : [1,2,3,4,5]        
expected: [1,2,3,4,5]        
All indices match.

**Constraints:**

- 1 <= heights.length <= 100
- 1 <= heights[i] <= 100

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Build the correct order of heights by sorting another array, then compare the two arrays.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        countdown = len(heights)
        expected = sorted(heights)

        for i in range(len(heights)):
            if heights[i] == expected[i]:
                countdown -= 1
        
        return countdown
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.64** MB \| Beats **78.49%**    

sorted()로 정렬된 리스트를 하나 더 만든 후 두 리스트를 비교하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/height-checker/solutions/5286562/easy-java-python3-c-solution-2-ms-_-by-s-np8o/" target="_blank">1st</a>

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

조금 더 파이썬스러운 코드도 참고했다.