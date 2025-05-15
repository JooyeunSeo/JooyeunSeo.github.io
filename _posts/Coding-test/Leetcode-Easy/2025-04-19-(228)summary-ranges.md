---
excerpt: "'LeetCode: Summary Ranges' 풀이 정리"
title: "\0228. Summary Ranges"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of nums is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- "a->b" if a != b
- "a" if a == b

**Example 1:**

- Input: nums = [0,1,2,4,5,7]
- Output: ["0->2","4->5","7"]
- Explanation: The ranges are:   
[0,2] --> "0->2"   
[4,5] --> "4->5"   
[7,7] --> "7"

**Example 2:**

- Input: nums = [0,2,3,4,6,8,9]
- Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:   
[0,0] --> "0"   
[2,4] --> "2->4"   
[6,6] --> "6"   
[8,9] --> "8->9"

**Constraints:**

- 0 <= nums.length <= 20
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
- All the values of `nums` are **unique**.
- `nums` is sorted in ascending order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums

        result = []
        chain_start = nums[0]
        chain_end = nums[0]

        for n in nums[1:]:
            if n == chain_end + 1:
                chain_end = n
            else:
                if chain_start == chain_end:
                    result.append(str(chain_start))
                else:
                    result.append("{}->{}".format(chain_start, chain_end))
                chain_start = n
                chain_end = n

        if chain_start == chain_end:
            result.append(str(chain_start))
        else:
            result.append("{}->{}".format(chain_start, chain_end))
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.46** MB \| Beats **52.16%**

두 개의 포인터를 이용하는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/summary-ranges/solutions/6664740/interval-by-zhangjinyuan666666-9o5c/" target="_blank">1st</a>

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Interval
        ret = []
        if not nums: return ret
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:   # should split now
                line = str(start) if start == nums[i-1] else str(start) + "->" + str(nums[i-1])  # one num or more
                ret.append(line)
                start = nums[i]
        line = str(start) if start == nums[-1] else str(start) + "->" + str(nums[-1])  # add the last (n-1) case
        ret.append(line)
        return ret
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)       

하나의 포인터로도 해결할 수 있다.