---
excerpt: "'LeetCode: Isomorphic Strings' 풀이 정리"
title: "\0205. Isomorphic Strings"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Hash Table
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

- Input: s = "egg", t = "add"
- Output: true
- Explanation: The strings `s` and `t` can be made identical by:
   - Mapping `'e'` to `'a'`.
   - Mapping `'g'` to `'d'`.

**Example 2:**

- Input: s = "foo", t = "bar"
- Output: false
- Explanation: The strings `s` and `t` can not be made identical as `'o'` needs to be mapped to both `'a'` and `'r'`.

**Example 3:**

- Input: s = "paper", t = "title"
- Output: true

**Constraints:**

- 1 <= s.length <= 5 * 10<sup>4</sup>
- t.length == s.length
- `s` and `t` consist of any valid ascii character.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pairing = {}

        for i in range(len(s)):
            if s[i] not in pairing and t[i] not in pairing.values():  # s[i]가 해시테이블에 없고 t[i]가 값으로 추가된 적이 없을 때
                pairing[s[i]] = t[i]                                    # 해시테이블에 쌍 추가
            elif s[i] not in pairing and t[i] in pairing.values():    # s[i]가 해시테이블에 없고 t[i]가 이미 값으로 추가된 적이 있을 때
                return False
            elif s[i] in pairing and pairing[s[i]] != t[i]:           # s[i]가 해시테이블에 있고 t[i]이 해당 키의 값과 다를 때
                return False
        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **7** ms \| Beats **88.82%**    
<i class="fa-solid fa-memory"></i> Memory: **13.55** MB \| Beats **58.55%**

두 문자열 s와 t의 각 문자가 일대일로 매핑되는 동형 구조인지 판단하는 문제다. 해시 테이블을 이용해서 푸는 것이 가장 간단한 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/isomorphic-strings/solutions/5896641/video-keep-pairs-in-hashmap-2-solutions-w4im3/" target="_blank">1st</a>

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            
            if char_index_s[s[i]] != char_index_t[t[i]]:  # s[i]와 t[i]의 처음 등장 위치가 다를 경우
                return False

        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

딕셔너리에 각 문자열의 문자를 키, 해당 문자가 **처음 등장**한 위치(인덱스)를 값으로 저장하는 방법이다.


### <a href="https://leetcode.com/problems/isomorphic-strings/solutions/4960160/beats-100-easiest-code-with-comments-exp-oxmr/" target="_blank">2nd</a>

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexS = [0] * 200 # Stores index of characters in string s
        indexT = [0] * 200 # Stores index of characters in string t
        
        length = len(s) # Get the length of both strings
        
        if length != len(t): # If the lengths of the two strings are different, they can't be isomorphic
            return False
        
        for i in range(length): # Iterate through each character of the strings
            if indexS[ord(s[i])] != indexT[ord(t[i])]: # Check if the index of the current character in string s is different from the index of the corresponding character in string t
                return False # If different, strings are not isomorphic
            
            indexS[ord(s[i])] = i + 1 # updating position of current character
            indexT[ord(t[i])] = i + 1
        
        return True # If the loop completes without returning false, strings are isomorphic
```
문자를 아스키 코드값(정수)으로 변경하여 배열의 인덱스로 사용하는 방법이다. 딕셔너리를 사용하면 더 간단하지만 새로운 방법이어서 참고해봤다.