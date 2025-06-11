---
excerpt: "'LeetCode: Range Sum Query - Immutable' 풀이 정리"
title: "\0303. Range Sum Query - Immutable"
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

Given an integer array `nums`, handle multiple queries of the following type:

Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- NumArray(int[] nums) Initializes the object with the integer array `nums`.
- int sumRange(int left, int right) Returns the **sum** of the elements of `nums` between indices left and right **inclusive** (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

**Example 1:**

- Input:     
["NumArray", "sumRange", "sumRange", "sumRange"]    
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
- Output:   
[null, 1, -1, -3]   
- Explanation:   
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);   
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1   
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1   
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3   

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>
- 0 <= left <= right < nums.length
- At most 10<sup>4</sup> calls will be made to `sumRange`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [nums[0]]         # nums의 첫 번째 원소 먼저 저장
        for i in range(1, len(nums)):   # nums의 두 번째 원소부터 prefix의 마지막 값과 더해서 새로 저장
            self.prefix.append(self.prefix[-1] + nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **16.39** MB \| Beats **13.66%**

매번 left부터 right까지의 합을 일일이 반복문으로 계산하는 Brute force 방법은 시간이 너무 오래 걸린다. 초기화할 때 **누적 합(Prefix Sum)**을 배열에 저장해 둔 뒤, sumRange(left, right)를 호출할 때마다 사용하는 것이 더 효율적이다.

nums = [-2, 0, 3, -5, 2, -1]
{: style="color: blue;"}
<pre>
nums   = [-2,  0,  3, -5,  2, -1]
prefix = [-2, -2,  1, -4, -2, -3]

[0,2] → prefix[1] = 1
[2,5] → prefix[5] - prefix[2-1] = (-3) - (-2) = -1
</pre>

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/range-sum-query-immutable/solutions/6175062/elegant-python3-solution-with-explanatio-k7p1/" target="_blank">1st</a>

```python
class NumArray:
    def __init__(self, nums: List[int]):
        # Initialize the prefix_sum array with a 0 at the start
        self.prefix_sum = [0]
        
        # Precompute the prefix sums
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of elements from left to right using the prefix_sum array
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
```
<i class="fa-solid fa-clock"></i> **time complexity:** Initialization: 𝑂(𝑛), sumRange: 𝑂(1)  
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)         
좀 더 짧게 코드를 작성하는 방법