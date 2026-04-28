---
excerpt: "'LeetCode: Edit Distance' 풀이 정리"
title: "\072. Edit Distance"
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

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

**Example 1:**

- Input: word1 = "horse", word2 = "ros"
- Output: 3
- Explanation:      
horse -> rorse (replace 'h' with 'r')      
rorse -> rose (remove 'r')      
rose -> ros (remove 'e')

**Example 2:**

- Input: word1 = "intention", word2 = "execution"
- Output: 5
- Explanation:      
intention -> inention (remove 't')       
inention -> enention (replace 'i' with 'e')       
enention -> exention (replace 'n' with 'x')       
exention -> exection (replace 'n' with 'c')       
exection -> execution (insert 'u')

**Constraints:**

- 0 <= word1.length, word2.length <= 500
- `word1` and `word2` consist of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # 1. dp 배열 생성
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 2. 초기값 세팅
        for i in range(m + 1):
            dp[i][0] = i                            # 전부 삭제
        
        for j in range(n + 1):
            dp[0][j] = j                            # 전부 삽입
        
        # 3. dp 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:    # 같은 문자면 그대로
                    dp[i][j] = dp[i - 1][j - 1]
                else:                               # 다르면 3가지 중 최소
                    dp[i][j] = min(
                        dp[i][j - 1],               # insert
                        dp[i - 1][j],               # delete
                        dp[i - 1][j - 1]            # replace
                    ) + 1                           # + 1
        
        return dp[m][n]
```
<i class="fa-solid fa-clock"></i> Runtime: **49** ms \| Beats **55.43%**    
<i class="fa-solid fa-memory"></i> Memory: **22.74** MB \| Beats **49.52%**    

2차원 DP가 필요한 문제로, dp[i][j]는 word1의 i번째 문자까지를 word2의 j번째 문자까지로 만드는 데 필요한 최소 작업 횟수를 뜻한다.

- 초기값 설정 (한 쪽이 빈 문자열이면 다른 문자열의 길이만큼 문자를 모두 삽입하거나 삭제)
   - `dp[i][0] = i`: word2가 빈 문자열이면 word1의 i개 모두 삭제
   - `dp[0][j] = j`: word1이 빈 문자열이면 word2를 만들기 위해 j개를 모두 삽입
- 점화식
   - 두 문자가 같으면(word1[i-1] == word2[j-1]): 이전 단계의 최소 비용 그대로 가져옴      
   (`dp[i][j] == dp[i-1][j-1]`)
   - 두 문자가 다르면(word1[i-1] != word2[j-1]): 세 가지 연산 중 최소 비용 + 작업 횟수 1
      - 삽입: dp[i][j-1] + 1
      - 삭제: dp[i-1][j] + 1
      - 교체: dp[i-1][j-1] + 1
  

word1 = "horse"      
word2 = "ros"
{: style="color: blue;"}
<pre>
    Base Case dp[i][0] = i
    ↓
   "" r o s
"" [0 1 2 3] ← Base Case dp[0][j] = j
h  [1 1 2 3]
o  [2 2 1 2]
r  [3 2 2 2]
s  [4 3 3 2]
e  [5 4 4 3]

(1,1) = "h" → "r"  insert  → dp[1][0] = 1
                   delete  → dp[0][1] = 1
                   replace → dp[0][0] = 0
                           min(1,1,0) = 1
(1,2) = "h" → "ro"                    = 2
(1,3) = "h" → "ros"                   = 3
(2,1) = "ho" → "r"                    = 1+1 = 2
(2,2) = "ho" → "ro"                   = 1
(2,3) = "ho" → "ros"                  = 1+1 = 2
...
</pre>

{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/edit-distance/solutions/7017810/video-edit-distance-explained-insert-del-ankj/" target="_blank">1st</a>

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == 0:
                return j
            if j == 0:
                return i

            if word1[i - 1] == word2[j - 1]:
                res = dp(i - 1, j - 1)
            else:
                res = 1 + min(
                    dp(i - 1, j),      # Delete
                    dp(i, j - 1),      # Insert
                    dp(i - 1, j - 1)   # Replace
                )

            cache[(i, j)] = res
            return res

        return dp(len(word1), len(word2))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚\*𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚\*𝑛)    