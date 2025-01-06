---
excerpt: "'LeetCode-Roman to Integer' 풀이 정리"
title: "\013. Roman to Integer"
header:
  teaser: "/assets/images/defaults/logo-LeetCode-black.png"
categories:
  - Leetcode
tags:
  - Coding Test
  - Easy
  - Python
  - zip()
---

## <i class="fa-solid fa-file-lines"></i> Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

|Symbol |  Value|
|------:|------:|
|I      |      1|
|V      |      5|
|X      |     10|
|L      |     50|
|C      |    100|
|D      |    500|
|M      |   1000|

For example, `2` is written as `II` in Roman numeral, just two ones added together.   
`12` is written as `XII`, which is simply `X + II`.   
The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

+ `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
+ `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
+ `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

- Input: s = "III"
- Output: 3
- Explanation: III = 3.

**Example 2:**

- Input: s = "LVIII"
- Output: 58
- Explanation: L = 50, V= 5, III = 3.

**Example 3:**

- Input: s = "MCMXCIV"
- Output: 1994
- Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

**Constraints:**

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].   

💡 **Hint 1:** <u><span style="color:white">Problem is simpler to solve by working the string from back to front and using a map.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        hashmap['I'] = 1    # 딕셔너리에 각 문자열을 키값으로 값 저장
        hashmap['V'] = 5
        hashmap['X'] = 10
        hashmap['L'] = 50
        hashmap['C'] = 100
        hashmap['D'] = 500
        hashmap['M'] = 1000

        reversed_c = ''     # 문자열 c를 거꾸로 세면서 보관하는 변수
        output = 0          # 출력값을 0으로 초기화

        for c in s[::-1]:
            if reversed_c == '':
                output += hashmap[c]
            elif c == 'I' and reversed_c[-1] == 'V':
                output -= 1
            elif c == 'I' and reversed_c[-1] == 'X':
                output -= 1
            elif c == 'X' and reversed_c[-1] == 'L':
                output -= 10
            elif c == 'X' and reversed_c[-1] == 'C':
                output -= 10
            elif c == 'C' and reversed_c[-1] == 'D':
                output -= 100
            elif c == 'C' and reversed_c[-1] == 'M':
                output -= 100
            else:
                output += hashmap[c]
            reversed_c += c
        return output
```
<i class="fa-solid fa-clock"></i> Runtime: **12** ms \| Beats **40.02%**    
<i class="fa-solid fa-memory"></i> Memory: **12.52** MB \| Beats **14.91%**

문자열의 맨 뒤 문자부터 하나씩 변수 reversed_c에 보관하고,    
`I`, `X`, `C`가 나올 때 reversed_c의 맨 마지막 원소를 확인하여 어떤 값을 output에 넣을지 결정했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/roman-to-integer/solutions/5848685/video-looping-two-characters-at-a-time-b-squ4/" target="_blank">1st</a>

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        return res + roman[s[-1]]   # 마지막 남은 1개의 문자는 그대로 더하기
```
<i class="fa-solid fa-clock"></i> **time complexity:** O(n) ← 입력 문자열 `s`의 길이         
<i class="fa-solid fa-memory"></i> **space complexity:** O(1) ← `s`와 상관없이 딕셔너리의 크기는 동일       

`s` =  "XIV"    
`res` = 0    
{: style="color: blue;"}

문자를 앞에서부터 2개씩 묶어가며 계산하는 방식   
두 문자 중 앞의 문자가 더 크면 앞의 문자를 합계에 더하고, 뒤의 문자가 더 크면 앞의 문자를 합계에서 뺀다. 

| loop | characters | result | res |
|------|------------|--------|-----|
| 1    | **X** > I  | +10    | 10  |
| 2    | **I** < V  | -1     | 9   |
| 3    | **V**      | +5     |     |

return `res` + roman[s[-1]]    
∴ return 9 + 5

∴ return 14
{: style="color: green;"}

### <a href="https://leetcode.com/problems/roman-to-integer/solutions/264743/clean-python-beats-9978-by-hgrsd-axkt/" target="_blank">2nd</a>

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0

        # Chaining 방식으로 문자열 변경 e.g. 먼저 s의 IV를 IIII로 변경 후, 그 값에 IX가 있을 경우 VIIII로 변경
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
```

특수한 규칙을 변환 처리하여 계산을 단순화한 코드