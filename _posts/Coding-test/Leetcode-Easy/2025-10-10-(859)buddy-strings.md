---
excerpt: "'LeetCode: Buddy Strings' 풀이 정리"
title: "\0859. Buddy Strings"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Hash Table
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `s` and `goal`, return `true` *if you can swap two letters in* `s` *so the result is equal to* `goal`*, otherwise, return* `false`.

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`.

- For example, swapping at indices `0` and `2` in `"abcd"` results in `"cbad"`.

**Example 1:**

- Input: s = "ab", goal = "ba"
- Output: true
- Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

**Example 2:**

- Input: s = "ab", goal = "ab"
- Output: false
- Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

**Example 3:**

- Input: s = "aa", goal = "aa"
- Output: true
- Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

**Constraints:**

- 1 <= s.length, goal.length <= 2 * 10<sup>4</sup>
- `s` and `goal` consist of lowercase letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
from collections import Counter

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n, m = len(s), len(goal)
        temp_s, temp_g = '', ''
        swap = False
        compare = {}

        if n != m:  return False        # 두 문자열의 길이가 다르면 바로 False

        if s == goal:                   # 같은 문자열이면 2번 이상 등장하는 문자가 있는지 확인
            count = Counter(s)
            return any(v >= 2 for v in count.values())

        for i in range(n):
            if s[i] != goal[i]:
                if swap:    return False
                elif not temp_s:    temp_s, temp_g = s[i], goal[i]
                elif s[i] == temp_g and goal[i] == temp_s:  swap = True
                else:   return False

        if swap:    return True         # 두 문자를 swap해서 똑같은 문자열이 될 경우
        elif temp_s:    return False    # 한 곳만 서로 다른 문자일 경우
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.30** MB \| Beats **73.57%**

collections.Counter을 이용하여 문자의 출현 빈도를 세는 해시 테이블을 빠르게 생성했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/buddy-strings/solutions/141780/easy-understood-by-lee215-u5eq/" target="_blank">1st</a>

```python
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)            

두 문자열이 같은 경우 해시 테이블 대신 <mark>set()</mark>으로도 중복 문자가 있는지 빠르게 확인할 수 있다.     
그리고 서로 다른 곳이 정확히 2개인지 확인하는 방법도 참고했다.
