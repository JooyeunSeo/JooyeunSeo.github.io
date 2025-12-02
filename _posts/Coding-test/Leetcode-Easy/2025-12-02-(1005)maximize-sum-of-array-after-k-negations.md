---
excerpt: "'LeetCode: Maximize Sum Of Array After K Negations' 풀이 정리"
title: "\01005. Maximize Sum Of Array After K Negations"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Greedy
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums` and an integer `k`, modify the array in the following way:

- choose an index `i` and replace `nums[i]` with `-nums[i]`.

You should apply this process exactly `k` times. You may choose the same index `i` multiple times.

Return *the largest possible sum of the array after modifying it in this way.*

**Example 1:**

- Input: nums = [4,2,3], k = 1
- Output: 5
- Explanation: Choose index 1 and nums becomes [4,-2,3].

**Example 2:**

- Input: nums = [3,-1,0,2], k = 3
- Output: 6
- Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

**Example 3:**

- Input: nums = [2,-3,-1,5,-4], k = 2
- Output: 13
- Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -100 <= nums[i] <= 100
- 1 <= k <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # k가 유효할 동안 음수 -> 양수
        i = 0
        nums.sort()
        while i < len(nums) and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1

        # 모든 음수를 짝수로 변환 후 남은 k가 짝수면 그대로, 홀수면 최솟값을 1번 뒤집기
        nums.sort()
        if k % 2 == 1:
            nums[0] = -nums[0]

        return sum(nums)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **18.15** MB \| Beats **18.00%**    

두 번 sort하는 방법이 가장 간단하고 안전한 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/solutions/252254/javacpython-sort-by-lee215-cr0w/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution:
    def largestSumAfterKNegations(self, A, K):
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

모든 음수를 가능한 만큼 양수로 변환 뒤, 추가 정렬 없이 `min()`으로 최솟값을 찾아도 된다. `(K - i) % 2`가 1이라면 `sum(A) - 2 * min(A)`이 되고, 이는 min(A)을 직접 뒤집은 후 전체 합을 구하는 것과 같은 결과다.