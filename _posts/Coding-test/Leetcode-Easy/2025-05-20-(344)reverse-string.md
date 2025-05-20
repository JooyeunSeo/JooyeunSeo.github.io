---
excerpt: "'LeetCode: Reverse String' 풀이 정리"
title: "\0344. Reverse String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> with `O(1)` extra memory.

**Example 1:**

- Input: s = ["h","e","l","l","o"]
- Output: ["o","l","l","e","h"]

**Example 2:**

- Input: s = ["H","a","n","n","a","h"]
- Output: ["h","a","n","n","a","H"]

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- s[i] is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">The entire logic for reversing a string is based on using the opposite directional two-pointer approach!</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        front = 0
        back = len(s) - 1

        while front < back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.86** MB \| Beats **66.81%**


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-string/solutions/6696029/reverse-string-3-methods-beats-100-java-08ab7/" target="_blank">1st</a>

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

내장 함수로 간단하게 구현 가능하다.