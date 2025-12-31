---
excerpt: "'LeetCode: Find Words That Can Be Formed by Characters' 풀이 정리"
title: "\01160. Find Words That Can Be Formed by Characters"
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
  - Counting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from `chars` (each character can only be used once for **each** word in `words`).

Return *the sum of lengths of all good strings in words.*

**Example 1:**

- Input: words = ["cat","bt","hat","tree"], chars = "atach"
- Output: 6
- Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

**Example 2:**

- Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
- Output: 10
- Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

**Constraints:**

- 1 <= words.length <= 1000
- 1 <= words[i].length, chars.length <= 100
- `words[i]` and `chars` consist of lowercase English letters.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Solve the problem for each string in words independently.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Now try to think in frequency of letters.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Count how many times each character occurs in string chars.</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">To form a string using characters from chars, the frequency of each character in chars must be greater than or equal the frequency of that character in the string to be formed.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = collections.Counter(chars)
        result = 0

        for word in words:
            word_cnt = collections.Counter(word)
            is_formed = True

            for k, v in word_cnt.items():
                if v > char_cnt[k]:
                    is_formed = False
                    break
            
            if is_formed:
                result += len(word)

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **65** ms \| Beats **69.97%**    
<i class="fa-solid fa-memory"></i> Memory: **17.85** MB \| Beats **89.75%**    

collections 모듈의 Counter로 각 문자의 빈도수를 세는 해시테이블을 생성했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/solutions/6563826/video-give-me-5-minutes-how-we-think-abo-r2gp/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = {}

        for c in chars:
            ch[c] = 1 + ch.get(c, 0)

        res = 0
        for word in words:
            copy = ch.copy()

            for c in word:
                if c in copy and copy[c] != 0:
                    copy[c] -= 1
                else:
                    res -= len(word)                    
                    break
            
            res += len(word)
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+/*𝑚𝑘)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)      

chars의 각 문자 출현 빈도를 카운트한 딕셔너리를 매 단어마다 복사하는 방법이 사용됐다.

### <a href="https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/solutions/4352039/beats-100-cjavapythonjs-counting-charact-686p/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">2nd</a>

```python
class Solution(object):
    def countCharacters(self, words, chars):
        counts = [0] * 26

        # Step 1: Initialize Character Counts Array
        for ch in chars:
            counts[ord(ch) - ord('a')] += 1

        result = 0

        # Step 3: Check Words
        for word in words:
            if self.canForm(word, counts):
                # Step 4: Calculate Lengths
                result += len(word)

        return result

    def canForm(self, word, counts):
        c = [0] * 26

        # Step 2: Update Counts Array
        for ch in word:
            x = ord(ch) - ord('a')
            c[x] += 1
            if c[x] > counts[x]:
                return False

        return True
```
딕셔너리 대신 길이 26짜리 배열을 사용하는 방법이다.