---
excerpt: "'LeetCode: Maximum Subarray' 풀이 정리"
title: "\053. Maximum Subarray"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Divide and Conquer
  - Dynamic Programming
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

*[subarray]: A subarray is a contiguous non-empty sequence of elements within an array.

**Example 1:**

- Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
- Output: 6
- Explanation: The subarray [4,-1,2,1] has the largest sum 6.

**Example 2:**

- Input: nums = [1]
- Output: 1
- Explanation: The subarray [1] has the largest sum 1.

**Example 3:**

- Input: nums = [5,4,-1,7,8]
- Output: 23
- Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

**Constraints:**

- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0              # 현재까지 누적값
        max_sum = float('-inf')   # 최대 누적값

        for n in nums:
            curr_sum = max(n, (curr_sum + n)) # 이전까지의 합을 계속 잇거나 여기서 새로 시작
            max_sum = max(curr_sum, max_sum)

        return max_sum
```
<i class="fa-solid fa-clock"></i> Runtime: **35** ms \| Beats **62.61%**    
<i class="fa-solid fa-memory"></i> Memory: **31.24** MB \| Beats **96.33%**    

배열을 한 번만 순회하기 때문에 𝑂(𝑛) 시간 안에 풀 수 있는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximum-subarray/solutions/6075383/video-simple-solution-by-niits-uigt/" target="_blank">1st</a>

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

이전까지의 합이 음수이면 현재 숫자에 붙일 경우 무조건 더 작은 숫자가 되기 때문에 새로 시작할 수 있다.

### <a href="https://leetcode.com/problems/maximum-subarray/solutions/1595195/cpython-7-simple-solutions-w-explanation-kb6j/" target="_blank">2nd</a>

```python
from math import inf

class Solution:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])

            # 왼쪽, 오른쪽, 가운데 걸치는 범위 중 최대값 찾기
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

분할 정복을 사용한 방법으로, 최대 subarray은 왼쪽 절반, 오른쪽 절반 또는 중앙을 가로지르는 범위 3개 중 하나에 포함되어 있다는 것이 포인트이다.