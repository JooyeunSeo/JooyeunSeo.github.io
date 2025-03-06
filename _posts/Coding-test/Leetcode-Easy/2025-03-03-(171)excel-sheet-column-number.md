---
excerpt: "'LeetCode-Excel Sheet Column Number' 풀이 정리"
title: "\0171. Excel Sheet Column Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - ord()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return *its corresponding column number*.

For example:

A -> 1   
B -> 2   
C -> 3   
...   
Z -> 26   
AA -> 27   
AB -> 28    
...   

**Example 1:**

- Input: columnTitle = "A"
- Output: 1

**Example 2:**

- Input: columnTitle = "AB"
- Output: 28

**Example 3:**

- Input: columnTitle = "ZY"
- Output: 701

**Constraints:**

- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        i = -1                          # 자리수에 따라 지수로 곱할 값
        sum = 0                         # 모든 자리수를 더한 결과값
        for c in columnTitle[::-1]:     # 뒤에서부터 순서대로 체크
            convert = int(26 * 26**i) * (ord(c) - 64)
            sum += convert
            i += 1
        return sum
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats **77.12%**

168번의 반대 버전이기 때문에 금방 풀 수 있었다. <mark>ord()</mark> 함수로 알파벳의 아스키코드 값을 구한 뒤 64를 빼서 해당 알파벳에 해당하는 숫자를 구했다. 그리고 그 숫자에 각 자리수에 맞춰 26 * 26<sup>i</sup> 를 곱한다. 일의 자리는 26 * 26<sup>-1</sup> = 1, 십의 자리는 26 * 26<sup>0</sup> = 26, 백의 자리는 26 * 26<sup>1</sup> = 676과 같이 계산된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/excel-sheet-column-number/solutions/5980561/beginner-friendly-step-by-steps-solution-beats-100-user-in-each-solution-of-me/" target="_blank">1st</a>

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

문자열을 왼쪽부터 오른쪽으로 처리하는 방법이 더 깔끔한 것 같다.

### <a href="https://leetcode.com/problems/excel-sheet-column-number/solutions/52107/my-solutions-in-3-languages-does-any-one-have-one-line-solution-in-java-or-c/" target="_blank">2nd</a>

```python
from functools import reduce

class Solution(object):
    def titleToNumber(self, s):
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
```
`[ord(c) - 64 for c in list(s)]`를 통해 모든 알파벳을 숫자로 변환하여 리스트로 만든 후, <mark>reduce()</mark>에서 리스트의 첫 번째 값을 `x`, 두 번째 값부터 `y`로 하나씩 처리한다.