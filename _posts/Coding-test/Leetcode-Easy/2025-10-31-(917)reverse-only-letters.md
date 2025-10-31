---
excerpt: "'LeetCode: Reverse Only Letters' 풀이 정리"
title: "\0917. Reverse Only Letters"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, reverse the string according to the following rules:

- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.

Return `s` *after reversing it.*

**Example 1:**

- Input: s = "ab-cd"
- Output: "dc-ba"

**Example 2:**

- Input: s = "a-bC-dEf-ghIj"
- Output: "j-Ih-gfE-dCba"

**Example 3:**

- Input: s = "Test1ng-Leet=code-Q!"
- Output: "Qedo1ct-eeLg=ntse-T!"

**Constraints:**

- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range `[33, 122]`.
- s does not contain `'\"'` or `'\\'`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        front, back = 0, len(s)-1

        while front < back:
            if not s[front].isalpha():
                front += 1
            elif not s[back].isalpha():
                back -= 1
            else:
                s[front], s[back] = s[back], s[front]
                front += 1
                back -= 1

        return ''.join(s)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.73** MB \| Beats **49.06%**

두 개의 포인터가 모두 알파벳을 가리킬 때만 서로 위치를 교환하는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-only-letters/solutions/7232206/reverse-only-letters-beats-100-by-rafa_f-hfut/" target="_blank">1st</a>

```python
class Solution(object):
    def reverseOnlyLetters(self, s):

        ls = []
        cont = -1
        s = list(s)

        for i in range(0, len(s)):
            if s[i] in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
                ls.append(s[i])


        for i in range(0, len(s)):
            if s[i] in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
                s[i] = ls[cont]
                cont -= 1

        return "".join(s)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

포인터 두 개로 한 번 순회하는 코드보다 비효율적이지만 두 번 반복하는 방법도 있다.