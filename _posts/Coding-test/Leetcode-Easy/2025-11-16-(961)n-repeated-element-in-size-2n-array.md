---
excerpt: "'LeetCode: N-Repeated Element in Size 2N Array' 풀이 정리"
title: "\0961. N-Repeated Element in Size 2N Array"
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

You are given an integer array nums with the following properties:

- `nums.length == 2 * n`.
- `nums` contains `n + 1` **unique** elements.
- Exactly one element of `nums` is repeated `n` times.

Return *the element that is repeated* `n` *times*.

**Example 1:**

- Input: nums = [1,2,3,3]
- Output: 3

**Example 2:**

- Input: nums = [2,1,2,5,3,2]
- Output: 2

**Example 3:**

- Input: nums = [2,1,2,5,3,2]
- Output: 2

**Constraints:**

- 2 <= n <= 5000
- nums.length == 2 * n
- 0 <= nums[i] <= 10<sup>4</sup>
- `nums` contains `n + 1` **unique** elements and one of them is repeated exactly `n` times.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count= {}
        n = len(nums) // 2
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > 1:
                return num
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **18.85** MB \| Beats **29.19%**    

n번 반복되는 숫자 외에는 모두 1번씩만 등장하기 때문에 카운트한 값이 2가 되는 순간 바로 리턴하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solutions/208398/python-one-liner-beats-100-by-darktianti-r69n/" target="_blank">1st</a>

```python
    def repeatedNTimes(self, A):
        return int((sum(A)-sum(set(A))) // (len(A)//2-1))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

중복으로 인해 추가로 더해진 부분을 구한 뒤, `n - 1`번으로 나누면 반복되는 숫자를 구할 수 있다.

### <a href="https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solutions/6730125/repeated-n-times-by-khakimov_m-smrw/" target="_blank">2nd</a>

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
```
해시 테이블에 카운트하는 것보다 set()을 쓰는 것이 더 간단하다.