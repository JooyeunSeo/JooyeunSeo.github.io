---
excerpt: "'LeetCode: Count Binary Substrings' 풀이 정리"
title: "\0696. Count Binary Substrings"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a binary string `s`, return the number of non-empty substrings that have the same number of `0`'s and `1`'s, and all the `0`'s and all the `1`'s in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

**Example 1:**

- Input: s = "00110011"
- Output: 6
- Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".   
Notice that some of these substrings repeat and are counted the number of times they occur.   
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

**Example 2:**

- Input: s = "10101"
- Output: 4
- Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- s[i] is either `'0'` or `'1'`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev, curr = 0, 1           # 전 그룹, 현 그룹(s[0]에서 시작)의 길이
        count = 0
        
        for i in range(1, len(s)):  # 두 번째 원소부터 시작
            if s[i] == s[i-1]:          # 이전 원소와 같은 값이면 현 그룹 길이 +1
                curr += 1
            else:                       # 이전 원소와 다른 값이면 갱신
                count += min(prev, curr)
                prev, curr = curr, 1
        
        count += min(prev, curr)
        return count
```
<i class="fa-solid fa-clock"></i> Runtime: **77** ms \| Beats **95.83%**    
<i class="fa-solid fa-memory"></i> Memory: **14.60** MB \| Beats **21.13%**

연속된 같은 숫자 그룹 두 개의 시작점을 포인터로 지정하여 세는 방식도 사용해봤는데 너무 느렸다. 시간과 공간을 절약하려면 직전 그룹 `prev`와 현재 그룹 `curr`의 크기만 유지하는 방법으로 최적화할 수 있다.

s = "00110011"
{: style="color: blue;"}
<pre>
i    0 0 1 1 0 0 1 1     count
0    c                   
1      c               
2    p p c               min(0, 2) → +0
3    p p c c 
4        p p c           min(2, 2) → +2
5        p p c c
6            p p c       min(2, 2) → +2
7            p p c c    
                         min(2, 2) → +2
                                     ---
                                      6
</pre>

return 6 
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/count-binary-substrings/solutions/108625/javacpython-easy-and-concise-with-explan-li94/" target="_blank">1st</a>

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

파이썬을 이용해서 짧게 압축한 코드도 참고했다.

1. "01" 또는 "10"이 나오면 그 사이에 공백을 삽입하고 그 공백을 기준으로 나눈다.
2. 생성된 리스트의 모든 원소를 해당 문자열의 길이로 변환한다.
3. 리스트에서 인접한 그룹 쌍을 `zip(s, s[1:])`으로 묶는다.
4. 각 그룹 쌍에서 생성 가능한 substring 개수를 구한다.
5. substring 개수의 총합을 구한다.