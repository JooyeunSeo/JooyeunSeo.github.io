---
excerpt: "'LeetCode: Self Dividing Numbers' 풀이 정리"
title: "\0728. Self Dividing Numbers"
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

A **self-dividing number** is a number that is divisible by every digit it contains.

- For example, `128` is **a self-dividing number** because `128 % 1 == 0`, `128 % 2 == 0`, and `128 % 8 == 0`.

A **self-dividing number** is not allowed to contain the digit zero.

Given two integers `left` and `right`, *return a list of all the **self-dividing numbers** in the range* `[left, right]` (both **inclusive**).

**Example 1:**

- Input: left = 1, right = 22
- Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

**Example 2:**

- Input: left = 47, right = 85
- Output: [48,55,66,77]

**Constraints:**

- 1 <= left <= right <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), then checking that each digit is nonzero and divides the original number.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right+1):
            is_dividing = True
            
            for ch in str(num):             # 각 숫자를 문자열로 변환 후 한 문자씩 확인
                if int(ch) == 0 or num % int(ch) != 0:
                    is_dividing = False
                    break

            if is_dividing:
                result.append(num)

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **31** ms \| Beats **23.19%**    
<i class="fa-solid fa-memory"></i> Memory: **12.56** MB \| Beats **74.87%**

힌트처럼 각 숫자를 문자열로 바꾸는 방법은 시간이 오래 걸리는 단점이 있었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/self-dividing-numbers/solutions/7041682/simple-iterative-solution-java-python-cl-3p05/" target="_blank">1st</a>

```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left, right + 1):
            n = i
            flag = True
            while n > 0:
                rem = n % 10
                if rem == 0 or i % rem != 0:
                    flag = False
                    break
                n //= 10
            if flag:
                ans.append(i)
        return ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛*𝑑) ← d: number of digits in each number   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

각 숫자를 문자열로 변환하는 것보다 10씩 나누면서 모든 자리를 확인하면 더 빠르다.

### <a href="https://leetcode.com/problems/self-dividing-numbers/solutions/162578/one-line-python-learn-some-python-tricks-fqy6/" target="_blank">2nd</a>

```python
return [x for x in range(left, right+1) if all([int(i) != 0 and x % int(i)==0 for i in str(x)])]
```

```python
return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]
```
파이썬의 경우 위의 두 방법 모두 한 줄로 작성 가능하다.