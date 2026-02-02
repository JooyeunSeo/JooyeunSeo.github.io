---
excerpt: "'LeetCode: Convert Integer to the Sum of Two No-Zero Integers' 풀이 정리"
title: "\01317. Convert Integer to the Sum of Two No-Zero Integers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

**No-Zero integer** is a positive integer that **does not contain any** `0` in its decimal representation.

Given an integer `n`, return *a list of two integers* `[a, b]` *where*:

- `a` and `b` are *No-Zero integers*.
- `a + b = n`

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

**Example 1:**

- Input: n = 2
- Output: [1,1]
- Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

**Example 2:**

- Input: n = 11
- Output: [2,9]
- Explanation: Let a = 2 and b = 9.

**Constraints:**

- 2 <= n <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Loop through all elements from 1 to n.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Choose A = i and B = n - i then check if A and B are both No-Zero integers.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.35** MB \| Beats **30.68%**    

최대값이 10<sup>4</sup> 정도이고 여러 답 중 하나만 찾으면 되기 때문에 n에서 1씩 빼는 것을 반복하는 것으로도 충분하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/solutions/7167008/simple-clean-easy-explanation-beats-100-fyujl/" target="_blank">1st</a>

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next([i, n - i] for i in range(1, n) if '0' not in str(i) and '0' not in str(n - i))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

generator를 생성 후 <mark>next()</mark>로 조건에 맞는 첫 번째 값이 나온 순간 반환하는 방법이다.