---
excerpt: "'LeetCode: Remove All Adjacent Duplicates In String' 풀이 정리"
title: "\01047. Remove All Adjacent Duplicates In String"
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

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make **duplicate removals** on `s` until we no longer can.

Return *the final string after all such duplicate removals have been made*. It can be proven that the answer is **unique**.

**Example 1:**

- Input: s = "abbaca"
- Output: "ca"
- Explanation:        
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

**Example 2:**

- Input: s = "azxxzy"
- Output: "ay"

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- s consists of lowercase English letters.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Use a stack to process everything greedily.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if (not stack) or (stack[-1] != ch):
                stack.append(ch)
            else:                                 # (stack) and (stack[-1] == ch)
                stack.pop()

        return ''.join(stack)
```
<i class="fa-solid fa-clock"></i> Runtime: **17** ms \| Beats **88.89%**    
<i class="fa-solid fa-memory"></i> Memory: **18.72** MB \| Beats **55.16%**    

스택으로 쉽게 풀 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/solutions/294893/javacpython-two-pointers-and-stack-solut-5gfa/" target="_blank">1st</a>

```python
    def removeDuplicates(self, S):
        return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, S)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    