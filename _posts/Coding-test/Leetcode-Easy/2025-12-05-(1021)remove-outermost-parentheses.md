---
excerpt: "'LeetCode: Remove Outermost Parentheses' 풀이 정리"
title: "\01021. Remove Outermost Parentheses"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Stack
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: s = P<sub>1</sub> + P<sub>2</sub> + ... + P<sub>k</sub>, where P<sub>i</sub> are primitive valid parentheses strings.

Return `s` *after removing the outermost parentheses of every primitive string in the primitive decomposition of* `s`.

**Example 1:**

- Input: s = "(()())(())"
- Output: "()()()"
- Explanation:      
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".     
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".     

**Example 2:**

- Input: s = "(()())(())(()(()))"
- Output: "()()()()(())"
- Explanation:      
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".     
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

**Example 3:**

- Input: s = "()()"
- Output: ""
- Explanation:      
The input string is "()()", with primitive decomposition "()" + "()".     
After removing outer parentheses of each part, this is "" + "" = "".

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- `s[i]` is either `'('` or `')'`.
- `s` is a valid parentheses string.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Can you find the primitive decomposition? The number of ( and ) characters must be equal.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = ""

        for ch in s:
            if ch == '(':
                if depth > 0:
                    result += ch
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result += ch
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **18.00** MB \| Beats **39.36%**    

스택을 직접 만들지는 않았지만 깊이로 스택처럼 관리했다. 기본적으로는 `'('`를 만나면 깊이에 +1, `')'`를 만나면 -1을 한 뒤 출력하고, 예외로 깊이가 0일때 들어온 `'('`과 -1을 한 뒤 깊이가 0이 되는 `')'`는 가장 바깥 괄호이기 때문에 출력하지 않는다.

s = "(()())(())"
{: style="color: blue;"}
<pre>
ch    depth    print
(     0 → 1    x
(     1 → 2    o
)     2 → 1    o
(     1 → 2    o    
)     2 → 1    o
)     1 → 0    x
(     0 → 1    x
(     1 → 2    o
)     2 → 1    o
)     1 → 0    x
</pre>

return "()()()"
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-outermost-parentheses/solutions/270022/javacpython-count-opened-parenthesis-by-p45ye/" target="_blank">1st</a>

```python
class Solution:
    def removeOuterParentheses(self, S):
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        
        return "".join(res)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

좀 더 간단하게 만든 코드도 참고했다.