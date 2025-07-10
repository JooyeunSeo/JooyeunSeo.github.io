---
excerpt: "'LeetCode: Longest Uncommon Subsequence I' 풀이 정리"
title: "\0521. Longest Uncommon Subsequence I"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `a` and `b`, return *the length of the **longest uncommon subsequence** between* `a` *and* `b`. *If no such uncommon subsequence exists, return* `-1`.

An **uncommon subsequence** between two strings is a string that is a **subsequence of exactly one of them**.

*[subsequence]: A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

**Example 1:**

- Input: a = "aba", b = "cdc"
- Output: 3
- Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".   
Note that "cdc" is also a longest uncommon subsequence.

**Example 2:**

- Input: a = "aaa", b = "bbb"
- Output: 3
- Explanation: The longest uncommon subsequences are "aaa" and "bbb".

**Example 3:**

- Input: a = "aaa", b = "aaa"
- Output: -1
- Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.

**Constraints:**

- 1 <= a.length, b.length <= 100
- a and b consist of lower-case English letters.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Think very simple.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">If a == b, the answer is -1.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Otherwise, the answer is the string a or the string b.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        elif len(a) == len(b):
            return len(a)
        else:
            return max(len(a), len(b)) 
```
<i class="fa-solid fa-clock"></i> Runtime: **** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.36** MB \| Beats **80.08%**

'가장 긴' uncommon subsequence를 찾아야 하기 때문에, a, b 둘 중 길이가 더 긴 문자열 자체가 longest uncommon subsequence이 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-uncommon-subsequence-i/solutions/6806779/single-line-code-beats-100-by-shootingst-5q4m/" target="_blank">1st</a>

```python
class Solution(object):
    def findLUSlength(self, a, b):
        return -1 if a==b else max(len(a), len(b))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

파이썬의 경우 한 줄 코드로 작성 가능하다.