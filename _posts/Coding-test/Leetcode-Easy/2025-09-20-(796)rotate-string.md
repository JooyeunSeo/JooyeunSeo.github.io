---
excerpt: "'LeetCode: Rotate String' 풀이 정리"
title: "\0796. Rotate String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - String Matching
  - Weekly Contest
  - Boyer–Moore
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of **shifts** on* `s`.

A `shift` on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

**Example 1:**

- Input: s = "abcde", goal = "cdeab"
- Output: true

**Example 2:**

- Input: s = "abcde", goal = "abced"
- Output: false

**Constraints:**

- 1 <= s.length, goal.length <= 100
- `s` and `goal` consist of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        slicing = 0
        while slicing < len(s)-1:
            shift = s[slicing+1:] + s[:slicing+1]
            if shift == goal: return True
            slicing += 1

        return True if s == goal else False
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.56** MB \| Beats **8.92%**

각 회전마다 새 문자열을 만들어야 하기 때문에 비효율적인 방법이지만, 문제의 입력 크기가 크지 않아서 빠른 시간 내에 통과됐던 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/rotate-string/solutions/7197304/easy-solution-by-nitin_joshi77-j0qs/" target="_blank">1st</a>

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal) and goal in (s + s):
            return True
        else:
            return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

문자열 s를 회전시킨 결과는 항상 **s+s** 안에 부문 문자열로 포함되기 때문에 `goal in (s + s)`로 쉽게 확인할 수 있다. 파이썬에서는 이를 단순히 한 글자씩 전부 비교하는 것이 아니라 내부적으로 <mark>Boyer–Moore–Horspool</mark>을 기반으로 한 알고리즘을 사용하기 떄문에 최악의 경우 𝑂(𝑛<sup>2</sup>), 평균적으로 𝑂(𝑛)에 가깝게 동작한다.

s = "abcde", goal = "cdeab"    
{: style="color: blue;"}
<pre>
s+s    abcdeabcde   abcdeabcde   abcdeabcde
goal   cdeab         cdeab         cdeab 
           ↑             ↑             ↑
          e≠b           a≠b           b=b, a=a, e=e, d=d, c=c
</pre>

return True
{: style="color: green;"}