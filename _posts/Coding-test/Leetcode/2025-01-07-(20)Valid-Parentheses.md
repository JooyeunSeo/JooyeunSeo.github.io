---
excerpt: "'LeetCode-Valid Parentheses' 풀이 정리"
title: "\020. Valid Parentheses"
header:
  teaser: "/assets/images/defaults/logo-LeetCode-black.png"
categories:
  - Leetcode
tags:
  - Coding Test
  - Easy
  - Python
  - Stack
  - pop()
  - keys()
  - values()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string s containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

- Input: s = `()`
- Output: true

**Example 2:**

- Input: s = `()[]{}`
- Output: true

**Example 3:**

- Input: s = `(]`
- Output: false

**Example 4:**

- Input: s = `([])`
- Output: true


**Constraints:**

- 1 <= s.length <= 10<sub>4</sub>
- `s` consists of parentheses only `()[]{}`.   


💡 **Hint 1:** <u><span style="color:white">Use a stack of characters.</span></u>

💡 **Hint 2:** <u><span style="color:white">When you encounter an opening bracket, push it to the top of the stack.</span></u>

💡 **Hint 3:** <u><span style="color:white">When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        parentheses = {       # 키는 닫는 괄호, 값은 키에 해당하는 여는 괄호로 서로 매핑
            ')': '(',
            '}': '{',
            ']': '['
        }

        for letter in s:      # s의 문자를 하나씩 확인
            if letter in '([{':
                stack.append(letter)     # 스택에 push
            elif letter in parentheses and self.getTop(stack) == parentheses[letter]:
                stack.pop()              # 스택에서 pop
            else:
                return False

        if len(stack) != 0:   # 스택에 남은 문자가 있는지 체크(여는 괄호가 남아있는 경우 False)
            return False
        else:
            return True
    
    # 스택의 top을 구하는 메서드 정의(인덱스 에러 방지)
    def getTop(self, stack):
        if stack == []:
            return None
        else:
            return stack[-1]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100%**    
<i class="fa-solid fa-memory"></i> Memory: **12.61** MB \| Beats **6.00%**

스택을 이용하는 문제이다.    
여는 괄호가 나올 경우 스택에 넣고, 닫는 괄호이면서 스택의 Top과 매핑되는 경우 스택에서 빼는 방식이다.   
for문 종료 후 마지막에 스택이 비어있을 경우에만 True가 된다.    

스택의 맨 마지막 원소를 구하기 위해 `stack[-1]`을 했는데, 빈 스택일 경우 인덱스 오류가 나서 getTop 메서드를 따로 만들었다. 아마 이 부분이 runtime을 빠르게 하는데 도움이 된 것 같다.

다만 *list*.<mark>pop()</mark> 값 자체가 마지막 원소이기 때문에 굳이 마지막 원소를 따로 구할 필요가 없었다. 또는 if문에서 `stack[-1]` 바로 전에 or 조건으로 `not stack`을 명시했다면 스택이 비어있을 때 `stack[-1]`까지 접근하지 않으므로 오류가 발생하지 않았을 것이다.


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/valid-parentheses/solutions/5139933/video-2-ways-to-solve-this-question-by-n-feft/" target="_blank">1st</a>

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                # 스택이 비어있거나 현재 문자와 짝이 안 맞으면 False
                if not stack or mapping[char] != stack.pop():   
                    return False
        
        return not stack  # 스택이 비어있다면 True 반환
```
<i class="fa-solid fa-clock"></i> **time complexity:** O(n) ← 문자열 s를 한 번 순회    
<i class="fa-solid fa-memory"></i> **space complexity:** O(n) ← 최악의 경우의 스택 크기(모두 여는 괄호)   

- 파이썬 딕셔너리 메소드 <mark>keys()</mark>는 딕셔너리의 키만 모아서 리스트로 반환
- 파이썬 딕셔너리 메소드 <mark>values()</mark>는 딕셔너리의 값만 모아서 리스트로 반환


### <a href="https://leetcode.com/problems/valid-parentheses/solutions/3399077/easy-solutions-in-java-python-and-c-look-zlwg/" target="_blank">2nd</a>

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False # the string is not valid, so return false
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack
```

딕셔너리를 사용하지 않은 코드