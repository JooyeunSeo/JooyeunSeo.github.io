---
excerpt: "'LeetCode: Interleaving String' 풀이 정리"
title: "\097. Interleaving String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
  - Dynamic Programming
---

## <i class="fa-solid fa-file-lines"></i> Description

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub>
- t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub>
- \|n - m\| <= 1
- The **interleaving** is s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ... or t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...

**Note:** `a + b` is the concatenation of strings `a` and `b`.

*[substrings]: A substring is a contiguous non-empty sequence of characters within a string.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)
- Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
- Output: true
- Explanation: One way to obtain s3 is:       
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".       
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".       
Since s3 can be obtained by interleaving s1 and s2, we return true.

**Example 2:**

- Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
- Output: false
- Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

**Example 3:**

- Input: s1 = "", s2 = "", s3 = ""
- Output: true

**Constraints:**

- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- `s1`, `s2`, and `s3` consist of lowercase English letters.

**Follow up:** Could you solve it using only O(s2.length) additional memory space?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)      
        dp[0] = True

        # 첫 번째 행 초기화(s2만 사용하는 경우)
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            # 첫 번째 열 업데이트(s1만 사용하는 경우)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            # 해당 행 나머지 칸 채우기
            for j in range(1, len(s2) + 1):
                use_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]       # s1에서 문자 가져오는 경우
                use_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]   # s2에서 문자 가져오는 경우
                dp[j] = use_s1 or use_s2

        return dp[-1]
```
<i class="fa-solid fa-clock"></i> Runtime: **48** ms \| Beats **74.22%**    
<i class="fa-solid fa-memory"></i> Memory: **19.24** MB \| Beats **91.16%**    

s1 앞 i개와 s2 앞 j개로 s3 앞 i+j개를 만들 수 있는지 확인하기 위해 2차원 DP(dp[i][j])를 사용할 수 있다. Follow up 조건을 충족하려면 현재 행만 저장하는 1차원 DP(dp[j])로 공간을 최적화해야 한다.

s1 = "aabcc"      
s2 = "dbbca"      
s3 = "aadbbcbcac"
{: style="color: blue;"}
<pre>
    ""  d   b   b   c   a
""  T   F   F   F   F   F  ← only s2
a   T   F   F   F   F   F
a   T   T   T   T   T   F
b   F   T   T   F   T   F
c   F   F   T   T   T   T
c   F   F   F   T   F   T
    ↑
    only s1
</pre>

return True
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/interleaving-string/solutions/3956393/9978-2-approaches-dp-recursion-by-vanams-alwn/" target="_blank">1st</a>

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[m][n]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛\*𝑚)    

2차원 DP