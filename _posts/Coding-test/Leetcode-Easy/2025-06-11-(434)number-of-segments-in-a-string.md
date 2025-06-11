---
excerpt: "'LeetCode: Number of Segments in a String' 풀이 정리"
title: "\0434. Number of Segments in a String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, return *the number of segments in the string.*

A **segment** is defined to be a contiguous sequence of **non-space characters**.

**Example 1:**

- Input: s = "Hello, my name is John"
- Output: 5
- Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

**Example 2:**

- Input: s = "Hello"
- Output: 1

**Constraints:**

- 0 <= s.length <= 300
- `s` consists of lowercase and uppercase English letters, digits, or one of the following characters `"!@#$%^&*()_+-=',.:"`.
- The only space character in `s` is `' '`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
```
<mark>split()</mark>으로 공백을 기준으로 하여 문자열을 분할한 뒤, 반환된 리스트의 길이를 구하면 한 줄 코드로 구현할 수 있다.

```python
class Solution(object):
    def countSegments(self, s):
        count = 0       # 세그먼트 개수 카운트
        is_seg = False  # 세그먼트인지 확인(False로 초기화)

        for ch in s:
            if ch != " " and is_seg == False:   # 세그먼트의 시작일 경우에 해당
                count += 1
                is_seg = True
            elif ch == " ":
                is_seg = False

        return count
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.50** MB \| Beats **6.33%**

내장 함수 없이 Brute force로 해결하는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/number-of-segments-in-a-string/solutions/6648809/master-word-boundary-detection-to-count-t6lis/" target="_blank">1st</a>

```python
class Solution(object):
    def countSegments(self, s):
        c = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                c += 1
        return c
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)      

다양한 반복문 조건을 참고해봤다.