---
excerpt: "'LeetCode: License Key Formatting' 풀이 정리"
title: "\0482. License Key Formatting"
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

You are given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. The string is separated into `n + 1` groups by `n` dashes. You are also given an integer `k`.

We want to reformat the string `s` such that each group contains exactly `k` characters, except for the first group, which could be shorter than `k` but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return *the reformatted license key.*

**Example 1:**

- Input: s = "5F3Z-2e-9-w", k = 4
- Output: "5F3Z-2E9W"
- Explanation: The string s has been split into two parts, each part has 4 characters.   
Note that the two extra dashes are not needed and can be removed.

**Example 2:**

- Input: s = "2-5g-3-J", k = 2
- Output: "2-5G-3J"
- Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- `s` consists of English letters, digits, and dashes `'-'`.
- 1 <= k <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []   
        count = k     # 한 파트 안에 들어갈 문자 개수 세기

        for c in s[::-1]:
            if count == 0:
                result.append("-")
                count = k
            
            if c != "-":
                result.append(c.upper())
                count -= 1
            
        if result and result[-1] == "-":  # 빈 리스트가 아니고 마지막이 "-"라면 없애기
            result.pop()
        
        result.reverse()
        return "".join(result)
```
<i class="fa-solid fa-clock"></i> Runtime: **23** ms \| Beats **55.29%**    
<i class="fa-solid fa-memory"></i> Memory: **14.59** MB \| Beats **21.18%**


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/license-key-formatting/solutions/131978/beats-100-python3-submission-by-orphyus-lo03/" target="_blank">1st</a>

```python
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()[::-1]  # s의 대쉬 제거, 대문자 변환, 뒤집기
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

먼저 S를 처리하기 쉽게 가공한 후, K개씩 슬라이스해서 join한 뒤, 다시 뒤집는 방법이다.

### <a href="https://leetcode.com/problems/license-key-formatting/solutions/6655452/conquer-messy-keys-with-one-liner-clean-ywkfx/" target="_blank">2nd</a>

```python
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()
        n = len(s)
        first_group = n % k or k  # 첫 번째 그룹의 길이 계산(n%k가 0이 될 경우 k 사용)
        res = [s[:first_group]]
        for i in range(first_group, n, k):
            res.append(s[i:i + k])
        return '-'.join(res)
```
문자열을 뒤집지 않고 더 효율적으로 풀 수 있다.