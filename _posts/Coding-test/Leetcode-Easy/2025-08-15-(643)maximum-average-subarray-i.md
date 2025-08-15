---
excerpt: "'LeetCode: Maximum Average Subarray I' 풀이 정리"
title: "\0643. Maximum Average Subarray I"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Sliding Window
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than 10<sup>-5</sup> will be accepted.

**Example 1:**

- Input: nums = [1,12,-5,-6,50,3], k = 4
- Output: 12.75000
- Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

**Example 2:**

- Input: nums = [5], k = 1
- Output: 5.00000

**Constraints:**

- n == nums.length
- 1 <= k <= n <= 10<sup>5</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        subarrys = len(nums) - k + 1    # 가능한 subarrys 개수
        max_sum = float('-inf')         # 최소값으로 초기화
        
        for i in range(subarrys):
            if i == 0:
                curr_sum = sum(nums[:k])                      # 최초 슬라이스
            else:
                prev_sum = curr_sum                           # 기존 슬라이스
                curr_sum = prev_sum - nums[i-1] + nums[i+k-1] # 기존값에서 -1칸 앞 값 + 1칸 뒤 값
                
            max_sum = max(curr_sum, max_sum)                  # 최대값 갱신
        
        return max_sum / float(k)
```
<i class="fa-solid fa-clock"></i> Runtime: **79** ms \| Beats **62.75%**    
<i class="fa-solid fa-memory"></i> Memory: **19.16** MB \| Beats **42.94%**

매번 슬라이스마다 원소의 합을 새로 구하면 너무 오래걸리기 때문에 이전 슬라이스의 값을 활용하는 방법을 사용했다.

nums = [1,12,-5,-6,50,3], k = 4
{: style="color: blue;"}
<pre>
subarrys = 3
max_sum = -Infinity

nums   1,  12,  -5,  -6,  50,   3
---------------------------------
i=0    1 + 12 + -5 + -6            =  2 (=max_sum)
i=1   -1            (2) + 50       = 51 (=max_sum)
i=2       -12            (51) + 3  = 42

51 / 4 = 12.75
</pre>

return 12.75
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximum-average-subarray-i/solutions/7078217/sliding-window-by-nghiemngocduc07-v39n/" target="_blank">1st</a>

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currsum = sum(nums[:k])
        maxval = currsum / k
        for i in range(k, len(nums)):
            currsum -= nums[i-k]
            currsum += nums[i]
            if currsum / k > maxval:
                maxval = currsum/k

        return maxval
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)          

이 방법처럼 맨 처음 슬라이스를 먼저 계산 후 그 다음부터 반복문으로 계산하는 것이 더 깔끔한 것 같다.