---
excerpt: "'LeetCode: Reverse Vowels of a String' 풀이 정리"
title: "\0345. Reverse Vowels of a String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Example 1:**

- Input: s = "IceCreAm"
- Output: "AceCreIm"
- Explanation:   
The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

- Input: s = "leetcode"
- Output: "leotcede"

**Example 3:**


**Constraints:**

- 1 <= s.length <= 3 * 10<sup>5</sup>
- s consist of **printable ASCII** characters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)              # 문자열을 리스트로 변경
        vowels = set('aeiouAEIOU')    # 대문자, 소문자 모음
        front = 0
        back = len(s) - 1

        while front < back:
            while front < back and s_list[front] not in vowels:
                front += 1
            while front < back and s_list[back] not in vowels:
                back -= 1

            # 둘 다 모음이면 교체
            s_list[front], s_list[back] = s_list[back], s_list[front]
            front += 1
            back -= 1
        
        return ''.join(s_list)
```
<i class="fa-solid fa-clock"></i> Runtime: **12** ms \| Beats **87.27%**    
<i class="fa-solid fa-memory"></i> Memory: **13.55** MB \| Beats **90.79%**

두 글자의 위치를 변경하기 위해 문자열을 리스트로 변경하는 방법이 가장 편한 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-vowels-of-a-string/solutions/5974533/easy-python-solution-beats-95-by-aadit-hpy7/" target="_blank">1st</a>

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 모음만 뽑아서 리스트에 순서대로 저장
        vowels=[i for i in s if i in "aeiouAEIOU"]

        # s의 글자가 모음인 경우 vowels의 뒤에서부터 꺼냄
        result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]  
        return "".join(result)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

투 포인터 방식보다 공간은 더 사용하지만 훨씬 간결한 방법도 있었다.