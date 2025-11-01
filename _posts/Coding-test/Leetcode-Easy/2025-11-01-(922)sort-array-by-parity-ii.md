---
excerpt: "'LeetCode: Sort Array By Parity II' 풀이 정리"
title: "\0922. Sort Array By Parity II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
  - Sorting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half are **even**.

Sort the array so that whenever `nums[i]` is odd, `i` is **odd**, and whenever `nums[i]` is even, `i` is **even**.

Return *any answer array that satisfies this condition.*

**Example 1:**

- Input: nums = [4,2,5,7]
- Output: [4,5,2,7]
- Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

**Example 2:**

- Input: nums = [2,3]
- Output: [2,3]

**Constraints:**

- 2 <= nums.length <= 2 * 10<sup>4</sup>
- nums.length is even.
- Half of the integers in `nums` are even.
- 0 <= nums[i] <= 1000

**Follow up:** Could you solve it in-place?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even, odd = 0, 1

        while even < n-1 and odd < n:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2

        return nums
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **83.23%**    
<i class="fa-solid fa-memory"></i> Memory: **18.84** MB \| Beats **77.60%**

각각 짝수 인덱스, 홀수 인덱스만 이동하는 포인터 두 개를 만들고, 두 인덱스의 모든 원소가 제자리에 있지 않을 경우만 서로 위치를 바꿨다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/sort-array-by-parity-ii/solutions/6966506/two-pointers-by-angielf-kp6y/" target="_blank">1st</a>

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        even_index, odd_index = 0, 1
        
        for num in nums:
            if num % 2 == 0:
                res[even_index] = num
                even_index += 2
            else:
                res[odd_index] = num
                odd_index += 2
        
        return res

```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)

리스트를 새로 생성하기 때문에 포인터를 사용하는 것보다 효율이 떨어지는 방법이다.