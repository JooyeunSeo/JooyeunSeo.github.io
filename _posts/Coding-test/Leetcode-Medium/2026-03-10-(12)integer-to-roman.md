---
excerpt: "'LeetCode: Integer to Roman' 풀이 정리"
title: "\012. Integer to Roman"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Hash Table
  - Math
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
|:------:|:-----:|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the **subtractive form** representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`) and 900 (`CM`).
- Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the **subtractive form**.

Given an integer, convert it to a Roman numeral.

**Example 1:**

- Input: num = 3749
- Output: "MMMDCCXLIX"
- Explanation:       
    <pre>
    3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
     700 = DCC as 500 (D) + 100 (C) + 100 (C)
      40 = XL as 10 (X) less of 50 (L)
       9 = IX as 1 (I) less of 10 (X)
    </pre>       
    Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

**Example 2:**

- Input: num = 58
- Output: "LVIII"
- Explanation:        
    <pre>
    50 = L
     8 = VIII
    </pre>

**Example 3:**

- Input: num = 1994
- Output: "MCMXCIV"
- Explanation:        
    <pre>
    1000 = M
     900 = CM
      90 = XC
       4 = IV
    </pre>

**Constraints:**

- 1 <= num <= 3999

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        vals = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        for val, rom in vals:
            while num >= val:
                num -= val
                res.append(rom)

        return "".join(res)
```
<i class="fa-solid fa-clock"></i> Runtime: **1** ms \| Beats **85.85%**    
<i class="fa-solid fa-memory"></i> Memory: **19.18** MB \| Beats **97.90%**    

큰 값부터 빼면서 로마자를 붙이는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/integer-to-roman/solutions/6034491/creating-mappings-bonus-coding-by-niits-sw6b/" target="_blank">1st</a>

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ['', 'M', 'MM', 'MMM'] # 0, 1000, 2000, 3000
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] # 0, 100, 200...900
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 0, 10, 20...90
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] # 0, 1, 2...9
        
        return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]      
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

각 자리수별로 가능한 모든 조합을 저장하면 바로 해당하는 로마자를 찾을 수 있다.