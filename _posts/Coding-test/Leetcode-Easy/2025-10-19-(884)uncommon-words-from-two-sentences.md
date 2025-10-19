---
excerpt: "'LeetCode: Uncommon Words from Two Sentences' 풀이 정리"
title: "\0884. Uncommon Words from Two Sentences"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Hash Table
  - String
  - Counting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

A word is **uncommon** if it appears exactly once in one of the sentences, and **does not appear** in the other sentence.

Given two **sentences** `s1` and `s2`, return *a list of all the **uncommon words***. You may return the answer in **any order**.

**Example 1:**

- Input: s1 = "this apple is sweet", s2 = "this apple is sour"
- Output: ["sweet","sour"]
- Explanation: The word "sweet" appears only in s1, while the word "sour" appears only in s2.

**Example 2:**

- Input: s1 = "apple apple", s2 = "banana"
- Output: ["banana"]

**Constraints:**

- 1 <= s1.length, s2.length <= 200
- s1 and s2 consist of lowercase English letters and spaces.
- s1 and s2 do not have leading or trailing spaces.
- All the words in s1 and s2 are separated by a single space.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        counting = {}
        result = []

        for word in s1.split():
            counting[word] = counting.get(word, 0) + 1
        
        for word in s2.split():
            counting[word] = counting.get(word, 0) + 1

        for k, v in counting.items():
            if v == 1: result.append(k)

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.59** MB \| Beats **15.36%**

s1과 s2의 모든 단어를 합쳐 카운팅하면 한 번만 등장하는 단어가 uncommon words가 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/uncommon-words-from-two-sentences/solutions/158967/cjavapython-easy-solution-with-explanati-6viz/" target="_blank">1st</a>

```python
class Solution(object):
    def uncommonFromSentences(self, A, B):
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚+𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚+𝑛)           

collections 모듈로 단어 등장 빈도를 카운팅하는 딕셔너리를 빠르게 생성할 수 있다.