---
excerpt: "'LeetCode: Palindrome Partitioning' 풀이 정리"
title: "\0131. Palindrome Partitioning"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
  - Dynamic Programming
  - Backtracking
  - palindrome
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

*[substring]: A substring is a contiguous non-empty sequence of characters within a string.
*[palindrome]: A substring is a contiguous non-empty sequence of characters within a string.

**Example 1:**

- Input: s = "aab"
- Output: [["a","a","b"],["aa","b"]]

**Example 2:**

- Input: s = "a"
- Output: [["a"]]

**Constraints:**

- 1 <= s.length <= 16
- `s` contains only lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l, r):                # 문자열이 palindrome인지 확인
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtracking(start):                # 문자열의 시작 인덱스부터 시작해 가능한 모든 위치에서 잘라서 확인
            if start == len(s):                     # path 완성
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):       
                    path.append(s[start:end+1])     # 문자열 추가
                    backtracking(end+1)             # 다음 재귀호출
                    path.pop()                      # 마지막으로 추가한 문자열 제거

        result = []
        path = []
        backtracking(0)

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **39** ms \| Beats **78.80%**    
<i class="fa-solid fa-memory"></i> Memory: **34.25** MB \| Beats **32.86%**    

백트래킹과 분할이 결합된 유형의 문제이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/palindrome-partitioning/solutions/5191375/fasterless-mem2-methodsdetailed-approach-iycz/" target="_blank">1st</a>

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*2<sup>𝑛</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    