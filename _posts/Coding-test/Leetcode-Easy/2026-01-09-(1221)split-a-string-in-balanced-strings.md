---
excerpt: "'LeetCode: Split a String in Balanced Strings' 풀이 정리"
title: "\01221. Split a String in Balanced Strings"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Greedy
  - Counting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

**Balanced** strings are those that have an equal quantity of `'L'` and `'R'` characters.

Given a **balanced** string `s`, split it into some number of substrings such that:

- Each substring is balanced.

Return *the **maximum** number of balanced strings you can obtain.*

**Example 1:**

- Input: s = "RLRRLLRLRL"
- Output: 4
- Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

**Example 2:**

- Input: s = "RLRRRLLRLL"
- Output: 2
- Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.      
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

**Example 3:**

- Input: s = "LLLLRRRR"
- Output: 1
- Explanation: s can be split into "LLLLRRRR".

**Constraints:**

- 2 <= s.length <= 1000
- s[i] is either 'L' or 'R'.
- s is a balanced string.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Whenever the balance variable reaches zero then we increase the answer by one.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l, count_r, result = 0, 0, 0
        
        for c in s:
            if c == 'L':
                count_l += 1
            else: # 'R'
                count_r += 1

            if count_l == count_r:
                result += 1                 # substring 하나 추가
                count_l, count_r = 0, 0     # 카운트 초기화
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.20** MB \| Beats **7.72%**    

balanced strings을 최대한 많이 만들어야 하기 때문에 l과 r 카운트가 동일해지는 순간 바로 substring이 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/split-a-string-in-balanced-strings/solutions/403836/cjavapython-easy-solution-by-dnuang-ze8u/" target="_blank">1st</a>

```python
def balancedStringSplit(self, s: str) -> int:
    res = cnt = 0         
    for c in s:
        cnt += 1 if c == 'L' else -1            
        if cnt == 0:
            res += 1
    return res  
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    