---
excerpt: "'LeetCode: Backspace String Compare' 풀이 정리"
title: "\0844. Backspace String Compare"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
  - Stack
  - Simulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

- Input: s = "ab#c", t = "ad#c"
- Output: true
- Explanation: Both s and t become "ac".

**Example 2:**

- Input: s = "ab##", t = "c#d#"
- Output: true
- Explanation: Both s and t become "".

**Example 3:**

- Input: s = "a#c", t = "b"
- Output: false
- Explanation: s becomes "c" while t becomes "b".

**Constraints:**

- 1 <= s.length, t.length <= 200
- `s` and `t` only contain lowercase letters and `'#'` characters.

**Follow up:** Can you solve it in `O(n)` time and `O(1)` space?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_result = []
        t_result = []

        for ch in s:
            if ch == '#' and s_result:
                s_result.pop()
            elif ch.isalpha():
                s_result.append(ch)
        
        for ch in t:
            if ch == '#' and t_result:
                t_result.pop()
            elif ch.isalpha():
                t_result.append(ch)

        return s_result == t_result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.41** MB \| Beats **51.24%**

스택으로 처리하는 방법이 가장 간단하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/backspace-string-compare/solutions/6280021/video-give-me-10-minutes-how-we-think-ab-fq2w/" target="_blank">1st</a>

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def get_next_valid_char_index(s, end):
            backspace_count = 0
            while end >= 0:
                if s[end] == '#':
                    # find "#"
                    backspace_count += 1
                elif backspace_count > 0:
                    # find an alphabet but skip it because we have backspaces
                    backspace_count -= 1
                else:
                    # if we don't have backspaces and current character is alphabet
                    # it's time to compare two characters from s and t
                    break
                end -= 1
            return end # return current end pointer for the next iteration.

        ps = len(s) - 1
        pt = len(t) - 1

        while ps >= 0 or pt >= 0:
            ps = get_next_valid_char_index(s, ps)
            pt = get_next_valid_char_index(t, pt)

            if ps < 0 and pt < 0:
                # example case s = "ab##" t = "c#d#", case 2                
                return True
            if ps < 0 or pt < 0:
                # example case s = "ab#" t = "c#d#", case 3
                return False
            elif s[ps] != t[pt]:
                # example case s = "a#c" t = "b", case 4
                return False

            ps -= 1
            pt -= 1

        # example case s = "ab#c" t = "ad#c", case 1
        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

포인터를 이용하여 뒤에서부터 역방향으로 비교하면 스택 없이 𝑂(1)의 공간 복잡도로 풀 수 있다.