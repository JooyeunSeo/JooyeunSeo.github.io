---
excerpt: "'LeetCode: Detect Capital' 풀이 정리"
title: "\0520. Detect Capital"
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

We define the usage of capitals in a word to be right when one of the following cases holds:

- All letters in this word are capitals, like `"USA"`.
- All letters in this word are not capitals, like `"leetcode"`.
- Only the first letter in this word is capital, like `"Google"`.

Given a string `word`, return `true` if the usage of capitals in it is right.

**Example 1:**

- Input: word = "USA"
- Output: true

**Example 2:**

- Input: word = "FlaG"
- Output: false

**Constraints:**

- 1 <= word.length <= 100
- word consists of lowercase and uppercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():          # 모두 대문자 또는 모두 소문자
            return True

        if word[0].isupper() and word[1:].islower():  # 첫 번째 문자만 대문자고 나머지는 소문자
            return True
        
        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.49** MB \| Beats **51.59%**

<mark>isupper()</mark> 또는 <mark>islower()</mark> 함수는 문자열의 모든 문자가 대문자 또는 소문자일때만 True를 반환한다.   
첫 번째만 대문자고 나머지는 소문자인 케이스에는 문자열 슬라이싱을 사용했지만, <mark>istitle()</mark>을 사용하면 더 쉽게 해결할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/detect-capital/solutions/99249/python-has-useful-methods-by-stefanpochm-h7ii/" target="_blank">1st</a>

```python
class Solution(object):
    def detectCapitalUse(self, word):
        return word in [word.upper(), word.lower(), word.capitalize()]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

<mark>capitalize()</mark>는 문자열의 첫 번째 문자는 대문자, 나머지는 소문자가 되도록 변경한다.