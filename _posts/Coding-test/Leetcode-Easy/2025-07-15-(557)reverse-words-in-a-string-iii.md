---
excerpt: "'LeetCode: Reverse Words in a String III' 풀이 정리"
title: "\0557. Reverse Words in a String III"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

- Input: s = "Let's take LeetCode contest"
- Output: "s'teL ekat edoCteeL tsetnoc"

**Example 2:**

- Input: s = "Mr Ding"
- Output: "rM gniD"

**Constraints:**

- 1 <= s.length <= 5 * 10<sup>4</sup>
- `s` contains printable **ASCII** characters.
- `s` does not contain any leading or trailing spaces.
- There is **at least one** word in `s`.
- All the words in `s` are separated by a single space.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")                # 공백으로 단어 분할 → 리스트
        reversed_words = ["".join(reversed(word)) for word in words]    # 각 단어 뒤집기
        return " ".join(reversed_words)     # 다시 공백으로 연결 → 문자열
```
<i class="fa-solid fa-clock"></i> Runtime: **11** ms \| Beats **33.31%**    
<i class="fa-solid fa-memory"></i> Memory: **12.95** MB \| Beats **63.11%**

<mark>split()</mark> 함수로 공백을 기준으로 문자열을 나눈 후, 리스트 컴프리헨션으로 각 단어를 뒤집은 버전의 리스트를 다시 만들었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-words-in-a-string-iii/solutions/6685920/master-word-reversal-inside-sentences-wi-n78i/" target="_blank">1st</a>

```python
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s.split())
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

한 줄짜리 코드로 만들 수 있다.