---
excerpt: "'LeetCode: Multiply Strings' 풀이 정리"
title: "\043. Multiply Strings"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Math
  - String
  - Simulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

**Example 1:**

- Input: num1 = "2", num2 = "3"
- Output: "6"

**Example 2:**

- Input: num1 = "123", num2 = "456"
- Output: "56088"

**Constraints:**

- 1 <= num1.length, num2.length <= 200
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        result = [0] * (n + m)                      # 최대 길이로 결과 배열 생성

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                curr_digit = i + j + 1              # 현재 자리
                next_digit = i + j                  # 다음 자리    

                mul = int(num1[i]) * int(num2[j])
                total = mul + result[curr_digit]

                result[next_digit] += total // 10   # 올림수
                result[curr_digit] = total % 10     # 현재 자리에 남는 수
        
        result = ''.join(map(str, result)).lstrip('0')
        
        return result if result else '0'
```
<i class="fa-solid fa-clock"></i> Runtime: **35** ms \| Beats **50.36%**    
<i class="fa-solid fa-memory"></i> Memory: **19.28** MB \| Beats **81.43%**    

nums1 = "123"      
nums2 = "45"      
{: style="color: blue;"}
<pre>
      1     2     3
            4     5
---------------------
   (1)+5 (1)+10   15    [0 0 6 1 5]
4  (1)+8    12          [0 4 9 2 0]
                        "0 5 5 3 5"   
</pre>

return "5535"
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/multiply-strings/solutions/17746/python-easy-to-understand-solution-by-ol-s7jq/?envType=problem-list-v2&envId=2s2ff433" target="_blank">1st</a>

```python
class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
                carry = (res[i+j+1]+tmp) // 10
                res[i+j+1] = (res[i+j+1]+tmp) % 10
            res[i] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛+𝑚)    

int() 대신 ord()를 사용하면 조금 더 빠르게 할 수 있다.