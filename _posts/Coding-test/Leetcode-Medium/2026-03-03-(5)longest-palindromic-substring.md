---
excerpt: "'LeetCode: Longest Palindromic Substring' 풀이 정리"
title: "\05. Longest Palindromic Substring"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
  - Dynamic Programming
  - Palindrome
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, return *the longest palindromic substring* in s.

*[palindromic substring]: A string is palindromic if it reads the same forward and backward.

**Example 1:**

- Input: s = "babad"
- Output: "bab"
- Explanation: "aba" is also a valid answer.

**Example 2:**

- Input: s = "cbbd"
- Output: "bb"

**Constraints:**

- 1 <= s.length <= 1000
- `s` consist of only digits and English letters.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">How can we reuse a previously computed palindrome to compute a larger palindrome?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Complexity based hint:<br>
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        max_palindrome = s[0]
        for i in range(len(s)):
            candidate = search(i, i)        # 가운데 하나(홀수 길이)
            if len(candidate) > len(max_palindrome):
                max_palindrome = candidate

            candidate = search(i, i+1)      # 가운데 두개(짝수 길이)
            if len(candidate) > len(max_palindrome):
                max_palindrome = candidate
        return max_palindrome
```
<i class="fa-solid fa-clock"></i> Runtime: **239** ms \| Beats **79.53%**    
<i class="fa-solid fa-memory"></i> Memory: **19.16** MB \| Beats **91.88%**    

가운데를 기준으로 좌우가 같다는 성질을 이용할 수 있다. 모든 문자에 대해 가운데가 하나일 경우와 두 개일 경우 최대로 확장 가능한 길이를 확인해야 한다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-palindromic-substring/solutions/6141600/video-using-two-pointers-python-javascri-gsz2/" target="_blank">1st</a>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1


        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)
            
            if max_len > end - start:               # 중심 i를 기준으로 왼쪽/오른쪽 이동
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end+1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    