---
excerpt: "'LeetCode: Generate Parentheses' 풀이 정리"
title: "\022. Generate Parentheses"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
  - Dynamic Programming
  - Backtracking
---

## <i class="fa-solid fa-file-lines"></i> Description

Given n pairs of parentheses, write a function to *generate all combinations of well-formed parentheses.*

**Example 1:**

- Input: n = 3
- Output: ["((()))","(()())","(())()","()(())","()()()"]

**Example 2:**

- Input: n = 1
- Output: ["()"]

**Constraints:**

- 1 <= n <= 8

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(comb, open, close):
            if open == close == n:                # 종료 조건
                res.append(comb)
                return
    
            if open < n:                          # '(' 추가 가능
                dfs(comb + "(", open + 1, close)
            if close < open:                      # ')' 추가 가능
                dfs(comb + ")", open, close + 1)
        
        res = []
        dfs("", 0, 0)
        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.46** MB \| Beats **64.25%**    

여는 괄호는 n개까지, 닫는 괄호는 현재까지 사용한 여는 괄호보다 적어야 한다는 규칙을 유지하며 재귀 호출했다.     
이 문제는 여는 괄호를 `+1`, 닫는 괄호를 `-1`로 치환하면 카탈란 수(Catalan number)를 구하는 것으로 볼 수 있다. 카탈란 수는 전체 조합 중에서 중간에 한 번도 깨지지 않는 구조의 개수로, `+1`과 `-1`을 각 n개씩 사용해서 순서대로 더해간다고 생각하면 된다. 이 중 최종 합이 0이고 중간에 한 번도 음수가 되지 않는 순서만 카탈란 수가 되고 조건에 맞지 않으면 바로 탐색을 중단하기 때문에 시간 복잡도는 𝑂(𝐶<sub>𝑛</sub> \* 2𝑛)가 된다.

[![Formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a3798c92c4d4dfc1b40b57b110fd1d91794f8f9)](https://ko.wikipedia.org/wiki/%EC%B9%B4%ED%83%88%EB%9E%91_%EC%88%98)

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/generate-parentheses/solutions/10369/clean-python-dp-solution-by-wz2326-jx4l/" target="_blank">1st</a>

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')                    # 괄호 0쌍(아무것도 없는 상태)
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝐶<sub>𝑛</sub> \* 𝑛)        
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝐶<sub>𝑛</sub> \* 𝑛)     

df[i]에 괄호 i쌍으로 만들 수 있는 모든 문자열을 저장하는 방법으로, 이 코드 역시 카탈란 수를 구하는 방법이다. 다만 모든 중간 결과를 메모리에 유지하기 때문에 실제로는 DFS 방식보다 공간 복잡도가 더 크다.

n = 3
{: style="color: blue;"}
<pre>
   i   j
dp[0]                                     = [""]
dp[1] (0) = ["(" + ""     + ")" + ""    ] = ["()"]
dp[2] (0) = ["(" + ""     + ")" + "()"  ] = ["()()",
      (1) = ["(" + "()"   + ")" + ""    ] =  "(())"]
dp[3] (0) = ["(" + ""     + ")" + "()()"] = ["()()()",
            ["(" + ""     + ")" + "(())"] =  "()(())",
      (1) = ["(" + "()"   + ")" + "()"  ] =  "(())()",
      (2) = ["(" + "()()" + ")" + ""    ] =  "(()())"
            ["(" + "(())" + ")" + ""    ] =  "((()))"]
</pre>

return dp[3] 
{: style="color: green;"}