---
excerpt: "'LeetCode: Replace Elements with Greatest Element on Right Side' 풀이 정리"
title: "\01299. Replace Elements with Greatest Element on Right Side"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Biweekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

After doing so, return the array.

**Example 1:**

- Input: arr = [17,18,5,4,6,1]
- Output: [18,6,6,6,1,-1]
- Explanation:        
   - index 0 --> the greatest element to the right of index 0 is index 1 (18).       
   - index 1 --> the greatest element to the right of index 1 is index 4 (6).       
   - index 2 --> the greatest element to the right of index 2 is index 4 (6).       
   - index 3 --> the greatest element to the right of index 3 is index 4 (6).       
   - index 4 --> the greatest element to the right of index 4 is index 5 (1).       
   - index 5 --> there are no elements to the right of index 5, so we put -1.

**Example 2:**

- Input: arr = [400]
- Output: [-1]
- Explanation: There are no elements to the right of index 0.

**Constraints:**

- 1 <= arr.length <= 10<sup>4</sup>
- 1 <= arr[i] <= 10<sup>5</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Loop through the array starting from the end.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Keep the maximum value seen so far.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_val = -1

        for i in range(n-1, -1, -1):
            arr[i], max_val = max_val, max(max_val, arr[i])
        
        return arr
```
<i class="fa-solid fa-clock"></i> Runtime: **20** ms \| Beats **72.69%**    
<i class="fa-solid fa-memory"></i> Memory: **20.50** MB \| Beats **28.28%**    

뒤에서부터 순회하는 방법이 가장 간단하다. 맨 마지막 원소는 무조건 -1이 되기 때문에 max_val도 -1로 시작했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/solutions/6120871/simple-python-solution-easy-100-by-ogjdu-b1qw/" target="_blank">1st</a>

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = Max
            if temp > Max: Max = temp 
        return arr
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    