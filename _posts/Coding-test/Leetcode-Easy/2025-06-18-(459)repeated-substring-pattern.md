---
excerpt: "'LeetCode: Repeated Substring Pattern' 풀이 정리"
title: "\0459. Repeated Substring Pattern"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - String Matching
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

**Example 1:**

- Input: s = "abab"
- Output: true
- Explanation: It is the substring "ab" twice.

**Example 2:**

- Input: s = "aba"
- Output: false

**Example 3:**

- Input: s = "abcabcabcabc"
- Output: true
- Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

**Constraints:**

- 1 <= s.length <= 10<sup>4</sup>
- `s` consists of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)    # s의 길이
        
        for i in range(1, (s_len // 2 + 1)):  # substring의 가능한 길이 범위
            if s_len % i == 0:
                sub = s[:i]
                if sub * (s_len // i) == s:
                    return True
        
        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **11** ms \| Beats **41.28%**    
<i class="fa-solid fa-memory"></i> Memory: **12.63** MB \| Beats **47.68%**

substring의 반복으로 s가 완성된다면 substring의 길이의 배수는 s의 길이와 동일하다는 것을 이용했다. substring의 최소 길이는 1, 최대 길이는 s 길이의 절반까지 허용된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/repeated-substring-pattern/solutions/6756608/video-2-solutions-by-niits-2tz4/" target="_blank">1st</a>

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

s가 어떤 substring으로 반복된 문자열이라면, s를 두 번 이어붙인 문자열에서 처음과 끝 문자를 제외한 부분에 s가 반드시 등장한다는 원리를 이용한 답안이다.

s = "abacababacab"   
{: style="color: blue;"}
<pre>
s+s         = "abacababacababacababacab"   
(s+s)[1:-1] =  "bacababacababacababaca"
                     abacababacab
</pre>