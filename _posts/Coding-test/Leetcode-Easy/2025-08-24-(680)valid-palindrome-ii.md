---
excerpt: "'LeetCode: Valid Palindrome II' 풀이 정리"
title: "\0680. Valid Palindrome II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
  - Greedy
  - Palindrome
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, return `true` *if the* `s` *can be palindrome after deleting **at most one** character from it.*

**Example 1:**

- Input: s = "aba"
- Output: true

**Example 2:**

- Input: s = "abca"
- Output: true
- Explanation: You could delete the character 'c'.

**Example 3:**

- Input: s = "abc"
- Output: false

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- `s` consists of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1            # 왼쪽, 오른쪽 포인터

        while l < r:
            if s[l] != s[r]:
                del_l = s[l+1 : r+1]    # 왼쪽 포인터 +1 이동
                del_r = s[l : r]        # 오른쪽 포인터 -1 이동
                return del_l == del_l[::-1] or del_r == del_r[::-1] # 둘 중 하나라도 참이면 됨
            else:
                l += 1
                r -= 1

        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **39** ms \| Beats **90.06%**    
<i class="fa-solid fa-memory"></i> Memory: **12.76** MB \| Beats **40.59%**

양 끝에서 시작해서 서로 일치하지 않을 경우 왼쪽이나 오른쪽을 한 칸 이동해야 하는데, 그 후 나머지 문자열도 회문인지 끝까지 확인해야 한다. 파이썬의 인덱스 슬라이싱으로 편하게 풀 수 있었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-palindrome-ii/solutions/6445414/beats-super-easy-beginners-java-c-c-python-javascript-dart/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

왼쪽 또는 오른쪽 포인터를 한 칸 옮긴 뒤 나머지 문자열을 체크하는 부분을 따로 함수로 만들어도 된다.