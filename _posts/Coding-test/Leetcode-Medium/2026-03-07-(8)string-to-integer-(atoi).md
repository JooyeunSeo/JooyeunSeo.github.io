---
excerpt: "'LeetCode: String to Integer (atoi)' 풀이 정리"
title: "\08. String to Integer (atoi)"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

- **Whitespace:** Ignore any leading whitespace (`" "`).
- **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
- **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
- **Rounding**: If the integer is out of the 32-bit signed integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then round the integer to remain in the range. Specifically, integers less than -2<sup>31</sup> should be rounded to -2<sup>31</sup>, and integers greater than 2<sup>31</sup> - 1 should be rounded to 2<sup>31</sup> - 1.

Return the integer as the final result.

**Example 1:**

- Input: s = "42"
- Output: 42
- Explanation:     
    The underlined characters are what is read in and the caret is the current reader position.      
    <pre>
    Step 1: "42" (no characters read because there is no leading whitespace)
             ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "42" ("42" is read in)
               ^
    </pre> 

**Example 2:**

- Input: s = " -042"
- Output: -42
- Explanation:      
    <pre>
    Step 1: "   -042" (leading whitespace is read and ignored)
                ^
    Step 2: "   -042" ('-' is read, so the result should be negative)
                 ^
    Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
                   ^
    </pre>

**Example 3:**

- Input: s = "1337c0d3"
- Output: 1337
- Explanation:      
    <pre>
    Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
             ^
    Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a     non-digit)
                 ^
    </pre>

**Example 4:**

- Input: s = "0-1"
- Output: 0
- Explanation:      
    <pre>
    Step 1: "0-1" (no characters read because there is no leading whitespace)
             ^
    Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
              ^ 
    </pre>

**Example 5:**

- Input: s = "words and 987"
- Output: 0
- Explanation:      
Reading stops at the first non-digit character 'w'.

**Constraints:**

- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < len(s) and s[i] == ' ':   # 1. 시작 공백 처리
            i += 1
        
        if i == n:                          # (빈 문자열이거나 모두 공백일 경우 0)
            return 0

        sign = -1 if s[i] == '-' else 1     # 2. 부호 처리
        if s[i] in "+-":
            i += 1

        result = ""
        while i < n and s[i].isdigit():     # 3. 정수 읽기 
            result += s[i]
            i += 1
        
        if not result:                      # (변환된 정수 없으면 0)
            return 0
        
        num = sign * int(result)
        if num < -2**31:                    # 4. 반올림
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.35** MB \| Beats **77.85%**    

주의해야 할 edge case로 `"     "`, `"+"`, `".1"` 등이 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/string-to-integer-atoi/solutions/6924378/video-on-time-and-o1-space-by-niits-8h92/" target="_blank">1st</a>

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if we've reached the end
        if i == n:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # Step 3: Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        # Step 4: Apply sign and return
        return res * sign
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

문자열 생성없이 숫자를 직접 누적하는 방식이 더 공간을 절약할 수 있다. 한편 c에서는 오버플로가 발생하면 터지기 때문에 `res = res * 10 + digit` 하기 전에 미리 체크해야 한다.