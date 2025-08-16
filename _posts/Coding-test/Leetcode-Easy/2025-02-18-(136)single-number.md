---
excerpt: "'LeetCode: Single Number' 풀이 정리"
title: "\0136. Single Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Bit Manipulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a **non-empty array** of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

- Input: nums = [2,2,1]
- Output: 1

**Example 2:**

- Input: nums = [4,1,2,1,2]
- Output: 4

**Example 3:**

- Input: nums = [1]
- Output: 1

**Constraints:**

- 1 <= nums.length <= 3 * 10<sup>4</sup>
- -3 * 10<sup>4</sup> <= nums[i] <= 3 * 10<sup>4</sup>
- Each element in the array appears twice except for one element which appears only once.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Think about the XOR (^) operator's property.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        nums.sort()     # 오름차순 정렬
        
        while p < len(nums) - 1:
            if nums[p] == nums[p + 1]:  # 해당 원소가 다음 원소와 같으면 2칸 넘어가기
                p += 2
            else:
                return nums[p]
        return nums[p]                  # 가장 마지막 원소가 정답일 경우(nums의 길이가 1인 경우 포함)
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **30.88%**    
<i class="fa-solid fa-memory"></i> Memory: **13.94** MB \| Beats **74.99%**

정렬을 할 때 Timsort 알고리즘을 이용하여 𝑂(𝑛log𝑛)의 시간이 걸리기 때문에, 문제에서 요구하는 𝑂(𝑛)의 시간 복잡도는 충족하지 못했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/single-number/solutions/6026000/0-ms-runtime-beats-100-user-step-by-step-nnmr/" target="_blank">1st</a>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0              # 0으로 초기화
        for num in nums:
            result ^= num       # result = result ^ num
        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

XOR 연산(^)의 성질을 이용한 답안으로, 문제에서 요구하는 모든 조건을 만족했다. 같은 숫자끼리는 결국 0이 되기 때문에 단 하나만 있는 숫자가 결과가 된다. XOR 연산끼리는 순서를 바꿔도 같은 결과가 나온다는 것이 중요했던 것 같다.

<div class="notice--info" markdown="1">
💡 <a href="https://jooyeunseo.github.io/cheatsheet/digital-logic-gate/" target="_blank">XOR 연산</a>의 성질

- 같은 숫자끼리 XOR 연산: 0
- 0과 어떤 숫자를 XOR 연산: 그 숫자 자신   
- XOR 연산은 순서를 바꿔도 같은 결과

`nums` = [4,1,2,1,2], `result` = 0
{: style="color: blue;"}

<pre>
result
     0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2
   = 0 ^ 4 ^ 1 ^ 1 ^ 2 ^ 2
   = 0 ^ 4 ^   0   ^   0  
   = 0 ^ 4 ^ 0
   = 4
</pre>

return 4
{: style="color: green;"}
</div>

### <a href="https://leetcode.com/problems/single-number/solutions/3171261/solution-by-deleted_user-um8h/" target="_blank">2nd</a>

```python
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, nums, 0)
```
<mark>functools.reduce()</mark> 함수는 첫 번째 요소와 두 번째 요소를 <mark>lambda</mark> 함수에 적용하고, 그 결과를 세 번째 요소에 다시 적용하는 방식으로 요소들을 누적해가며 값을 하나로 줄인다.