---
excerpt: "'LeetCode: Verifying an Alien Dictionary' 풀이 정리"
title: "\0953. Verifying an Alien Dictionary"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.

**Example 1:**

- Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
- Output: true
- Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

**Example 2:**

- Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
- Output: false
- Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

**Example 3:**

- Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
- Output: false
- Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographic_order" target="_blank">More info</a>).

**Constraints:**

- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in `words[i]` and `order` are English lowercase letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            prev_w, curr_w = words[i-1], words[i]

            for j in range(min(len(prev_w), len(curr_w))):
                if prev_w[j] != curr_w[j]:
                    if order_map[prev_w[j]] > order_map[curr_w[j]]:
                        return False  # 정렬이 틀린 경우
                    break             # 정렬이 올바른 경우
            else:   # for 루프가 break 없이 정상 종료된 경우(두 단어의 길이가 다름)
                if len(prev_w) > len(curr_w):
                    return False

        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.73** MB \| Beats **74.01%**    


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/verifying-an-alien-dictionary/solutions/203175/python-straightforward-solution-by-cenka-j29u/" target="_blank">1st</a>

```python
class Solution:
    def isAlienSorted(self, words, order):
        ind = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]:
                    break
                elif ind[s1] > ind[s2]:
                    return False
        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

zip()으로 인접한 두 원소끼리 묶으면 더 짧은 쪽 길이까지만 맞춰서 비교한다.