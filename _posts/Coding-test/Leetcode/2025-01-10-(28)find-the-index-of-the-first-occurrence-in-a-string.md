---
excerpt: "'LeetCode-Find the Index of the First Occurrence in a String' 풀이 정리"
title: "\028. Find the Index of the First Occurrence in a String"
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/LeetCode_Logo_black_with_text.svg/458px-LeetCode_Logo_black_with_text.svg.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - find()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

- Input: haystack = "sadbutsad", needle = "sad"
- Output: 0
- Explanation: "sad" occurs at index 0 and 6.    
The first occurrence is at index 0, so we return 0.


**Example 2:**

- Input: haystack = "leetcode", needle = "leeto"
- Output: -1
- Explanation: "leeto" did not occur in "leetcode", so we return -1.

**Constraints:**

- 1 <= haystack.length, needle.length <= 10<sup>4</sup>
- haystack and needle consist of only lowercase English characters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100%**    
<i class="fa-solid fa-memory"></i> Memory: **12.50** MB \| Beats **20.46%**

<mark>.find()</mark> 함수를 사용하면 간단하게 한 줄로 통과할 수 있다.   
(needle이 haystack에 있다면 시작하는 부분의 인덱스를, 없다면 -1를 반환하기 때문)

```python
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100%**    
<i class="fa-solid fa-memory"></i> Memory: **12.56** MB \| Beats **20.46%**

for문과 슬라이싱 기능을 사용한 코드

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/5349528/video-slicing-approach/" target="_blank">1st</a>

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛 \* 𝑚) ← haystack의 길이 n, needle의 길이 m         
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚) ← 슬라이싱 연산으로 needle 길이의 새로운 문자열 생성  

똑같이 슬라이싱을 했지만 haystack이 needle보다 짧을 경우를 미리 필터링한 코드

### <a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/5985413/no-brute-force-boyer-moore-algorithm-official-text-search-research-gif-visualization/" target="_blank">2nd</a>

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # The right-most occurence of letters in needle
        letters = {letter: i for i, letter in enumerate(needle)}

        haystack_length = len(haystack)
        needle_length = len(needle)

        i = 0
        while i <= haystack_length - needle_length:
            # Iterate backwards
            j = needle_length - 1
            while j >= 0 and haystack[i+j] == needle[j]:
                j -= 1

            if j < 0:
                return i
            i += max(1, j - letters.get(haystack[i+j], -1))
        return -1
```
슬라이싱을 이용한 코드는 Brute Force 알고리즘으로, Boyer-Moore 알고리즘을 적용한 코드도 참고해봤다.   
Brute Force 알고리즘의 최악의 시간 복잡도는 𝑂(𝑛 \* 𝑚)이고 평균 𝑛 \* 𝑚 / 2 개의 문자를 체크한다.   
Boyer-Moore 알고리즘의 최악의 시간 복잡도는 𝑂(𝑛 \* 𝑚 + 𝑚)이고 평균 𝑛 / 𝑚 + 𝑚 개의 문자를 체크한다.   

최악의 시간 복잡도는 Brute Force보다 길지만 아주 특별한 케이스가 아니면 거의 일어나지 않고 평균 체크 문자수가 더 적기 때문에 효율적이라고 할 수 있다.

`haystack` = "THISISASIMPLEEXAMPLE"    
`needle`= "EXAMPLE"
{: style="color: blue;"}

<pre>
0123456789.........19 (index)
---------------------------------------------------------------------
THISISASIMPLEEXAMPLE 
EXAMPLE               ← EXAMPLE에 S가 없기 때문에 i=6까지 스킵

THISISASIMPLEEXAMPLE 
       EXAMPLE        ← 공통문자 P가 있고 끝 문자가 다를 땐 P끼리 위치를 맞춰야 한다

THISISASIMPLEEXAMPLE 
      EXAMPLE         ← 뒤에서부터 하나씩 매치한 결과 i=8에서 불일치하므로 스킵 가능

THISISASIMPLEEXAMPLE 
         EXAMPLE      ← 공통문자 X가 있고 끝 문자가 다를 땐 X끼리 위치를 맞춰야 한다

THISISASIMPLEEXAMPLE 
             EXAMPLE  ← 뒤에서부터 하나씩 매치한 결과 모두 매칭됨
</pre>

return i = 13
{: style="color: green;"}