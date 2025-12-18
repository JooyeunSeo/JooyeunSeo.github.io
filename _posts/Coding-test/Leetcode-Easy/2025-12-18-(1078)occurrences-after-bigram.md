---
excerpt: "'LeetCode: Occurrences After Bigram' 풀이 정리"
title: "\01078. Occurrences After Bigram"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `first` and `second`, consider occurrences in some text of the form `"first second third"`, where `second` comes immediately after `first`, and `third` comes immediately after `second`.

Return *an array of all the words* `third` *for each occurrence of* `"first second third"`.

**Example 1:**

- Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
- Output: ["girl","student"]

**Example 2:**

- Input: text = "we will we will rock you", first = "we", second = "will"
- Output: ["we","rock"]

**Constraints:**

- 1 <= text.length <= 1000
- `text` consists of lowercase English letters and spaces.
- All the words in `text` are separated by **a single space**.
- 1 <= first.length, second.length <= 10
- `first` and `second` consist of lowercase English letters.
- `text` will not have any leading or trailing spaces.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Split the string into words, then look at adjacent triples of words.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(' ')
        result = []

        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.42** MB \| Beats **99.58%**    


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/occurrences-after-bigram/solutions/308224/javapython-3-split-string-by-rock-5i0a/" target="_blank">1st</a>

```python
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans, words = [], text.split()
        for a, b, c in zip(words, words[1 :], words[2 :]):
            if (a, b) == (first, second):
                ans.append(c)
        return ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

zip()을 사용하는 방법도 있다.