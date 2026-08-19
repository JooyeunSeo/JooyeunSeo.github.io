---
excerpt: "'LeetCode: Longest Consecutive Sequence' 풀이 정리"
title: "\0128. Longest Consecutive Sequence"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Union-Find
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

- Input: nums = [100,4,200,1,3,2]
- Output: 4
- Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

**Example 2:**

- Input: nums = [100,4,200,1,3,2]
- Output: 4
- Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

**Example 3:**

- Input: nums = [1,0,1,2]
- Output: 3

**Constraints:**

- 0 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)                        # 해시셋으로 변경
        max_len = 0

        for n in nums_set:
            if n-1 not in nums_set:                 # 해당 숫자가 연속 수열의 처음인지 확인
                curr_len = 1
                while n+1 in nums_set:
                    curr_len += 1
                    n += 1
                max_len = max(curr_len, max_len)

        return max_len
```
<i class="fa-solid fa-clock"></i> Runtime: **39** ms \| Beats **94.78%**    
<i class="fa-solid fa-memory"></i> Memory: **36.63** MB \| Beats **37.05%**    

𝑂(𝑛)의 시간 내에 해결하려면 해시셋을 사용해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-consecutive-sequence/solutions/8468692/easy-approach-using-hash-set-by-shehryar-5bqp/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            if n - 1 not in numset:
                length = 1
                while n + length in numset:
                    length += 1
                longest = max(longest, length)
        return longest
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    