---
excerpt: "'LeetCode: Decrypt String from Alphabet to Integer Mapping' 풀이 정리"
title: "\01309. Decrypt String from Alphabet to Integer Mapping"
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

You are given a string `s` formed by digits and `'#'`. We want to map `s` to English lowercase characters as follows:

- Characters (`'a'` to `'i'`) are represented by (`'1'` to `'9'`) respectively.
- Characters (`'j'` to `'z'`) are represented by (`'10#'` to `'26#'`) respectively.

Return *the string formed after mapping.*

The test cases are generated so that a unique mapping will always exist.

**Example 1:**

- Input: s = "10#11#12"
- Output: "jkab"
- Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

**Example 2:**

- Input: s = "1326#"
- Output: "acz"

**Constraints:**

- 1 <= s.length <= 1000
- `s` consists of digits and the `'#'` letter.
- `s` will be a valid string such that mapping is always possible.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Scan from right to left, in each step of the scanning check whether there is a trailing "#" 2 indexes away.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1        # 거꾸로 순회
        result = []

        while i >= 0:
            if s[i] == '#':
                mapping = chr(int(s[i-2 : i]) + 96)
                result.append(mapping)
                i -= 3
            else:
                mapping = chr(int(s[i]) + 96)
                result.append(mapping)
                i -= 1
        
        return ''.join(reversed(result))
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.22** MB \| Beats **29.59%**    

a의 아스키코드 값이 97인 것을 이용해서 해시 테이블 없이 작성했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/solutions/470867/python-1-line-regex-by-lee215-fjej/" target="_blank">1st</a>

```python
import re

class Solution:
    def freqAlphabets(self, s):
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

정규식 `\d\d#`은 '숫자 2개 + #'의 조합이고 `\d`는 숫자 1개를 의미한다. 두 자리 숫자# 이거나 한 자리 숫자를 <mark>findall</mark>으로 모두 찾을 수 있다. 정규식의 장점은 식의 왼쪽부터, 그리고 가능한 한 긴 패턴을 먼저 소비하기 때문에 OR에서 앞의 `\d\d#`의 성립 여부를 `\d`보다 먼저 체크한다는 것이다.