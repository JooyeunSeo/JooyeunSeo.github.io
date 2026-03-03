---
excerpt: "'LeetCode: Longest Substring Without Repeating Characters' 풀이 정리"
title: "\03. Longest Substring Without Repeating Characters"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Staff
  - Hash Table
  - String
  - Sliding Window
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, find the length of the **longest** substring without duplicate characters.

*[substring]: A substring is a contiguous non-empty sequence of characters within a string.

**Example 1:**

- Input: s = "abcabcbb"
- Output: 3
- Explanation: The answer is "abc", with the length of 3.       
Note that "bca" and "cab" are also correct answers.

**Example 2:**

- Input: s = "bbbbb"
- Output: 1
- Explanation: The answer is "b", with the length of 1.

**Example 3:**

- Input: s = "pwwkew"
- Output: 3
- Explanation: The answer is "wke", with the length of 3.       
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

- 0 <= s.length <= 5 * 10<sup>4</sup>
- `s` consists of English letters, digits, symbols and spaces.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, (right - left + 1))
        
        return max_len
```
<i class="fa-solid fa-clock"></i> Runtime: **11** ms \| Beats **78.99%**    
<i class="fa-solid fa-memory"></i> Memory: **19.09** MB \| Beats **91.14%**    

중복이 없다면 오른쪽 포인터를 이동시키고, 중복이 나올 때는 왼쪽 포인터를 이동시키는 방법이다. 문제에서 사용되는 문자의 최대 개수는 정해져 있기 때문에 set()을 사용할 경우 공간 복잡도가 𝑂(1)이 되는 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/5111376/video-3-ways-to-solve-this-question-slid-uupi/" target="_blank">1st</a>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = 0
        count = {}

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
        
            max_length = max(max_length, right - left + 1)

        return max_length
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

set() 대신 해시 테이블을 사용한 방법도 있다.