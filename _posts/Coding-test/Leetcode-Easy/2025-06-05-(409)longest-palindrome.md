---
excerpt: "'LeetCode: Longest Palindrome' 풀이 정리"
title: "\0409. Longest Palindrome"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Palindrome
  - Hash Table
  - set()
  - Greedy
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest** palindrome that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

*[palindrome]: A palindrome is a string that reads the same forward and backward.

**Example 1:**

- Input: s = "abccccdd"
- Output: 7
- Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

**Example 2:**

- Input: s = "a"
- Output: 1
- Explanation: The longest palindrome that can be built is "a", whose length is 1.

**Constraints:**

- 1 <= s.length <= 2000
- `s` consists of lowercase **and/or** uppercase English letters only.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0    # Longest Palindrome의 길이
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for v in count.values():
            if v % 2 == 0:            # 값이 짝수면 그대로 더하기
                result += v
            else:                     # 값이 홀수면
                if result % 2 == 0:     # result가 아직 짝수일때만 그대로 더하기
                    result += v
                else:                   # result가 이미 홀수이면 -1 해서 더하기
                    result += v - 1
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.41** MB \| Beats **54.61%**

해시 테이블을 사용해서 각 문자의 출현 횟수를 카운트했다. Palindrome이 홀수라면 하나의 문자가 정가운데에 위치하고 나머지는 모두 짝수 개라는 것에 주목해서 작성했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-palindrome/solutions/6642768/unlock-palindrome-frequency-tricks-to-bu-qcml/" target="_blank">1st</a>

```python
class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        r = 0
        for c in s:
            d[c] = d.get(c, 0) + 1
        for v in d.values():
            r += v if v % 2 == 0 else v - 1
        return r + 1 if r < len(s) else r
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

매번 값이 홀수인지 세는 것보다 더 효율적인 것 같아서 참고했다. 일단 짝수 개씩만 더한 후, 결과값이 실제 s보다 작다면 홀수인 값이 있었다는 의미이기 때문에 마지막에 1만 더해주면 된다.

### <a href="https://leetcode.com/problems/longest-palindrome/solutions/5255173/fasterless-memdetailed-approachset-appro-pbyp/" target="_blank">2nd</a>

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize a set to keep track of characters with odd frequencies
        char_set = set()
        # Initialize the length of the longest palindrome
        length = 0
        
        # Iterate over each character in the string
        for char in s:
            # If the character is already in the set, remove it and increase the length by 2
            if char in char_set:
                char_set.remove(char)
                length += 2
            # If the character is not in the set, add it to the set
            else:
                char_set.add(char)
        
        # If there are any characters left in the set, add 1 to the length for the middle character
        if char_set:
            length += 1
        
        # Return the total length of the longest palindrome
        return length
```
반복문을 두 번씩 사용하지 않고 한 번에 해결할 수 있는 방법이다.