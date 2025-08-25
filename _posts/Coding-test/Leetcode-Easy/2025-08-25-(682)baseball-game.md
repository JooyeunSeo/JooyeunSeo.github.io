---
excerpt: "'LeetCode: Baseball Game' 풀이 정리"
title: "\0682. Baseball Game"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Stack
  - Simulation
---

## <i class="fa-solid fa-file-lines"></i> Description

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the i<sup>th</sup> operation you must apply to the record and is one of the following:

- An integer `x`.   
Record a new score of `x`.
- `'+'`.   
Record a new score that is the sum of the previous two scores.
- `'D'`.   
Record a new score that is the double of the previous score.
- `'C'`.   
Invalidate the previous score, removing it from the record.

Return *the sum of all the scores on the record after applying all the operations.*

The test cases are generated such that the answer and all intermediate calculations fit in a **32-bit** integer and that all operations are valid.

**Example 1:**

- Input: ops = ["5","2","C","D","+"]
- Output: 30
- Explanation:    
"5" - Add 5 to the record, record is now [5].    
"2" - Add 2 to the record, record is now [5, 2].    
"C" - Invalidate and remove the previous score, record is now [5].    
"D" - Add 2 \* 5 = 10 to the record, record is now [5, 10].    
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].    
The total sum is 5 + 10 + 15 = 30.

**Example 2:**

- Input: ops = ["5","-2","4","C","D","9","+","+"]
- Output: 27
- Explanation:    
"5" - Add 5 to the record, record is now [5].    
"-2" - Add -2 to the record, record is now [5, -2].    
"4" - Add 4 to the record, record is now [5, -2, 4].    
"C" - Invalidate and remove the previous score, record is now [5, -2].    
"D" - Add 2 \* -2 = -4 to the record, record is now [5, -2, -4].    
"9" - Add 9 to the record, record is now [5, -2, -4, 9].    
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].    
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].    
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

**Example 3:**

- Input: ops = ["1","C"]
- Output: 0
- Explanation:    
"1" - Add 1 to the record, record is now [1].   
"C" - Invalidate and remove the previous score, record is now [].    
Since the record is empty, the total sum is 0.

**Constraints:**

- 1 <= operations.length <= 1000
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range [-3 \* 10<sup>4</sup>, 3 \* 10<sup>4</sup>].
- For operation `"+"`, there will always be at least two previous scores on the record.
- For operations `"C"` and `"D"`, there will always be at least one previous score on the record.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.56** MB \| Beats **41.90%**

`+`나 `C`, `D`를 정수형으로 변환하면 오류가 나기 때문에 앞에서 모두 필터링한 후 숫자일 경우를 else문으로 넣었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/baseball-game/solutions/6979760/python-on-time-and-space-complexity-base-rdl0/" target="_blank">1st</a>

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            try:
                res.append(int(operations[i]))
            except ValueError:
                if operations[i] == "+":
                    res.append(res[-2] + res[-1])
                elif operations[i] == "D":
                    res.append(res[-1] * 2)
                elif operations[i] == "C":
                    res.pop()  # pop is way quicker here than del
        return sum(res)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

먼저 try에서 정수형으로 변환을 시도한 후, ValueError가 발생할 경우 except 처리하는 방법도 있었다.