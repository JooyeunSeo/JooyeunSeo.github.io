---
excerpt: "'LeetCode: Count and Say' 풀이 정리"
title: "\038. Count and Say"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

- `countAndSay(1) = "1"`
- `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.

<a href="https://en.wikipedia.org/wiki/Run-length_encoding" target="_blank">Run-length encoding</a> (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string `"3322251"` we replace `"33"` with `"23"`, replace `"222"` with `"32"`, replace `"5"` with `"15"` and replace `"1"` with `"11"`. Thus the compressed string becomes `"23321511"`.

Given a positive integer `n`, return *the* n<sup>th</sup> *element of the **count-and-say** sequence.*

**Example 1:**

- Input: n = 4
- Output: "1211"
- Explanation:                 
countAndSay(1) = "1"                 
countAndSay(2) = RLE of "1" = "11"                 
countAndSay(3) = RLE of "11" = "21"                 
countAndSay(4) = RLE of "21" = "1211"

**Example 2:**

- Input: n = 1
- Output: "1"
- Explanation:                 
This is the base case.

**Constraints:**

- 1 <= n <= 30

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Create a helper function that maps an integer to pairs of its digits and their frequencies. For example, if you call this function with "223314444411", then it maps it to an array of pairs [[2,2], [3,2], [1,1], [4,5], [1, 2]].</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Create another helper function that takes the array of pairs and creates a new integer. For example, if you call this function with [[2,2], [3,2], [1,1], [4,5], [1, 2]], it should create "22"+"23"+"11"+"54"+"21" = "2223115421".</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Now, with the two helper functions, you can start with "1" and call the two functions alternatively n-1 times. The answer is the last integer you will obtain.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        rle = "1"                       # n=1에서 시작
        
        for _ in range(n - 1):          # 2~n번 반복
            prev, count = rle[0], 0       # 이전 숫자, 같은 숫자 누적 카운트
            new_rle = []
            
            for c in rle:                 # 현재 rle 순환
                if c == prev:
                    count += 1
                else:
                    new_rle.append(str(count))  # count, prev 순으로 저장
                    new_rle.append(prev)
                    prev, count = c, 1
            new_rle.append(str(count))
            new_rle.append(prev)
            
            rle = "".join(new_rle)
        
        return rle
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **98.49%**    
<i class="fa-solid fa-memory"></i> Memory: **19.34** MB \| Beats **61.37%**    

문자열을 계속 누적하는 것보다 리스트에 변환된 문자열을 쌓고 마지막에 join으로 합치는 방법으로 시간 복잡도를 개선했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/count-and-say/solutions/6662478/beats-basic-for-loop-super-easy-beginner-wdsj/" target="_blank">1st</a>

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = self.describe(result)
        return result

    def describe(self, s: str) -> str:
        result = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(f"{count}{s[i - 1]}")
                count = 1

        result.append(f"{count}{s[-1]}")
        return "".join(result)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(2<sup>𝑛</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(2<sup>𝑛</sup>)    

### <a href="https://leetcode.com/problems/count-and-say/solutions/15999/4-5-lines-python-solutions-by-stefanpoch-uiwf/" target="_blank">2nd</a>

```python
from itertools import groupby

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + digit for digit, group in groupby(s)
            )
    return s
```
파이썬의 groupby를 이용하여 연속된 같은 숫자를 빠르게 묶을 수 있다.

n = 4
{: style="color: blue;"}
<pre>
n   s      digit   group
1  "1"    → ('1', ['1'])     → str(len(group)) = "1" → "1"+"1" = "11"
2  "11"   → ('1', ['1','1']) → str(len(group)) = "2" → "2"+"1" = "21"
3  "21"   → ('2', ['2'])     → str(len(group)) = "1" → "1"+"2" = "12"
          → ('1', ['1'])     → str(len(group)) = "1" → "1"+"1" = "11"
4  "1211"
</pre>

return "1211"
{: style="color: green;"}