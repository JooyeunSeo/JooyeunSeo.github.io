---
excerpt: "'LeetCode: Max Consecutive Ones' 풀이 정리"
title: "\0485. Max Consecutive Ones"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a binary array `nums`, return *the maximum number of consecutive* `1`*'s in the array.*

**Example 1:**

- Input: nums = [1,1,0,1,1,1]
- Output: 3
- Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

**Example 2:**

- Input: nums = [1,0,1,1,0,1]
- Output: 2

**Constraints:**

- 1 <= nums.length <= 10<sup>5</sup>
- nums[i] is either `0` or `1`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        chain = 0
        maxchain = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                chain += 1
                if chain > maxchain:  # 현재 값이 기존 max값보다 클 경우
                    maxchain = chain
            else:
                chain = 0

        return maxchain
```
<i class="fa-solid fa-clock"></i> Runtime: **16** ms \| Beats **79.89%**    
<i class="fa-solid fa-memory"></i> Memory: **16.35** MB \| Beats **6.13%**

값이 0인 인덱스를 찾을 때까지 값이 1인 인덱스를 세는 방법이다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/max-consecutive-ones/solutions/6841744/video-simple-counting-and-sliding-window-vqf9/" target="_blank">1st</a>

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0     # 최대 연속 1의 길이 저장용
        left = 0    # 현재 연속 1의 시작 위치

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1    # 시작 인덱스 이동
            else:
                res = max(res, right - left + 1)
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

슬라이딩 윈도우 방식으로 푸는 방법이다.