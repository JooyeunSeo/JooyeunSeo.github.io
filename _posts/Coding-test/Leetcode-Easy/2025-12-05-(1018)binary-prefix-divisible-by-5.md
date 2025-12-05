---
excerpt: "'LeetCode: Binary Prefix Divisible By 5' 풀이 정리"
title: "\01018. Binary Prefix Divisible By 5"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Bit Manipulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).

- For example, if `nums = [1,0,1]`, then x<sub>0</sub> = 1, x<sub>1</sub> = 2, and x<sub>2</sub> = 5.

Return *an array of booleans* `answer` *where* `answer[i]` *is* `true` *if* x<sub>i</sub> *is divisible by* `5`.

**Example 1:**

- Input: nums = [0,1,1]
- Output: [true,false,false]
- Explanation:    
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.    
Only the first number is divisible by 5, so answer[0] is true.

**Example 2:**

- Input: nums = [1,1,1]
- Output: [false,false,false]

**Constraints:**

- 1 <= nums.length <= 10<sup>5</sup>
- `nums[i]` is either `0` or `1`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">If X is the first i digits of the array as a binary number, then 2X + A[i] is the first i+1 digits.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        remainder = 0
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            result.append(remainder == 0)
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **81.68%**    
<i class="fa-solid fa-memory"></i> Memory: **19.30** MB \| Beats **25.06%**    

모든 숫자들을 직접 십진수로 계산하면 시간 초과되는 문제이기 때문에 힌트에서 나온 대로 이전 값에 2를 곱한 뒤 마지막에 더해진 비트 0 또는 1을 더하는 방법을 사용했다. 또 숫자가 5로 나누어지는지만 알면 되기 때문에 나머지값만 추적했다.

nums = [0,1,1]
{: style="color: blue;"}
<pre>
bit    remainder              new
0      0  → (0 * 2 + 0) % 5 →  0     true
1      0  → (0 * 2 + 1) % 5 →  1     false
1      1  → (1 * 2 + 1) % 5 →  3     false
</pre>

return [true,false,false]
{: style="color: green;"}


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/binary-prefix-divisible-by-5/solutions/7370402/binary-prefix-to-decimal-modular-arithme-6a7q/" target="_blank">1st</a>

```python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        for i in range(len(nums)):
            val = ((val << 1) + nums[i]) % 5
            nums[i] = val == 0
        return nums
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

이전 값에 2를 곱하는 대신 오른쪽으로 1비트 밀어도 된다.