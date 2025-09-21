---
excerpt: "'LeetCode: Unique Morse Code Words' 풀이 정리"
title: "\0804. Unique Morse Code Words"
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

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

- `'a'` maps to `".-"`,
- `'b'` maps to `"-..."`,
- `'c'` maps to `"-.-."`, and so on.

For convenience, the full table for the `26` letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

- For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the **transformation** of a word.

Return *the number of different **transformations** among all words we have.*

**Example 1:**

- Input: words = ["gin","zen","gig","msg"]
- Output: 2
- Explanation: The transformation of each word is:    
"gin" -> "--...-."    
"zen" -> "--...-."    
"gig" -> "--...--."    
"msg" -> "--...--."    
There are 2 different transformations: "--...-." and "--...--.".

**Example 2:**

- Input: words = ["a"]
- Output: 1

**Constraints:**

- 1 <= words.length <= 100
- 1 <= words[i].length <= 12
- `words[i]` consists of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = []
        codes = {
            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
            "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
            "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
            "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
            "y": "-.--", "z": "--.."
        }

        for word in words:
            t = ""
            for ch in word:
                t += codes[ch]
            if t not in transformations:
                transformations.append(t)
        
        return len(transformations)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.42** MB \| Beats **48.53%**

문제 설명에 있는 모스부호 리스트로 해시 테이블을 만들었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-morse-code-words/solutions/120675/javacpython-easy-and-concise-solution-by-h37f/" target="_blank">1st</a>

```python
    def uniqueMorseRepresentations(self, words):
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛\*𝑚)           

알파벳의 아스키코드값을 이용하면 해시 테이블을 따로 만들지 않아도 모스부호 리스트만으로 풀 수 있다.