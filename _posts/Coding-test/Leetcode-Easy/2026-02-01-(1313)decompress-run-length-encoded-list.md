---
excerpt: "'LeetCode: Decompress Run-Length Encoded List' 풀이 정리"
title: "\01313. Decompress Run-Length Encoded List"
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

We are given a list `nums` of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]` (with `i >= 0`).  For each such pair, there are `freq` elements with value `val` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

**Example 1:**

- Input: nums = [1,2,3,4]
- Output: [2,4,4,4]
- Explanation:       
The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].      
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].     
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

**Example 2:**

- Input: nums = [1,1,2,3]
- Output: [1,3,3]

**Constraints:**

- 2 <= nums.length <= 100
- nums.length % 2 == 0
- 1 <= nums[i] <= 100

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Decompress the given array by repeating nums[2*i+1] a number of times equal to nums[2*i].</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for freq, val in zip(nums[0::2], nums[1::2]):
            for _ in range(freq):
                result.append(val)
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.35** MB \| Beats **43.72%**    

<mark>zip()</mark>을 이용하여 [nums[2*i], nums[2*i+1]] 두 쌍을 만들었다. zip()은 인덱스를 초과해도 범위 에러가 발생하지 않기 때문에 range()보다 더 편리해서 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/decompress-run-length-encoded-list/solutions/477055/python-1-line-with-intuition-by-lee215-o4xq/" target="_blank">1st</a>

```python
class Solution:
    def decompressRLElist(self, A):
        return [x for a, b in zip(A[::2], A[1::2]) for x in [b] * a]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    