---
excerpt: "'LeetCode: Letter Combinations of a Phone Number' 풀이 정리"
title: "\017. Letter Combinations of a Phone Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Hash Table
  - String
  - Backtracking
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

**Example 1:**

- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Example 2:**

- Input: digits = "2"
- Output: ["a","b","c"]

**Constraints:**

- 1 <= digits.length <= 4
- digits[i] is a digit in the range `['2', '9']`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        table = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        d1 = digits[0]                    # 1번째 숫자
        d2 = digits[1] if n >= 2 else ''  # 2번째 숫자
        d3 = digits[2] if n >= 3 else ''  # 3번째 숫자
        d4 = digits[3] if n == 4 else ''  # 4번째 숫자
        res = []
        
        for l1 in table[d1]:
            if d2:
                for l2 in table[d2]:    
                    if d3:
                        for l3 in table[d3]:
                            if d4:
                                for l4 in table[d4]:
                                    res.append(l1 + l2 + l3 + l4) # 4글자
                            else:
                                res.append(l1 + l2 + l3) # 3글자
                    else:
                        res.append(l1 + l2) # 2글자
            else:
                res.append(l1) # 1글자

        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.34** MB \| Beats **70.28%**    

숫자 4자리까지만 적용 가능해서 확장성은 떨어지는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/6743872/video-simple-solution-by-niits-pny0/" target="_blank">1st</a>

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx, comb):
            if idx == len(digits):                  # 재귀호출 종료 조건
                res.append(comb[:])
                return
            
            for letter in digit_to_letters[digits[idx]]:
                backtrack(idx + 1, comb + letter)   # 재귀호출

        res = []
        backtrack(0, "")                # 첫 번째 숫자에서 시작

        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(3<sup>𝑛</sup>) or 𝑂(4<sup>𝑛</sup>)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

이 코드는 DFS 전략과 재귀 호출을 이용하여 한 경로를 끝까지 탐색한 후, 다시 돌아와서 다른 경로를 탐색하는 순서를 반복한다.

### <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/7343487/cartesian-product-by-sahin_mousli-j9ya/?envType=problem-list-v2&envId=2s2ff433" target="_blank">2nd</a>

```python
from itertools import product

digitmap = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        lls = [digitmap[s] for s in digits]             # lls = ['abc', 'def', 'ghi']
        print(lls)
        return list(''.join(x) for x in product(*lls))  # product('abc', 'def', 'ghi')
```

파이썬에서는 카테시안 곱(Cartesian Product)을 이용하면 간단하게 풀 수 있다. `*`으로 lls를 언패킹하고, product()에서 각 iterable 인자들의 카테시안 곱을 생성한다. 반환되는 튜플을 join()으로 문자열로 변환해 결과 리스트를 만든다.