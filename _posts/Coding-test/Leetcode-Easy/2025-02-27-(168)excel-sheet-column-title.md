---
excerpt: "'LeetCode-Excel Sheet Column Title' 풀이 정리"
title: "\0168. Excel Sheet Column Title"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - ASCII
  - divmod()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `columnNumber`, return *its corresponding column title as it appears in an Excel sheet*.

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

- Input: columnNumber = 1
- Output: "A"

**Example 2:**

- Input: columnNumber = 28
- Output: "AB"

**Example 3:**

- Input: columnNumber = 701
- Output: "ZY"

**Constraints:**

- 1 <= columnNumber <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        values = []
        convert = []

        while columnNumber > 26:
            values.append(columnNumber % 26)
            columnNumber //= 26
        values.append(columnNumber)
        
        for i in range(len(values)):
            if values[i] == 0 or values[i] == -1:       # 값이 0 또는 -1이고
                if i < len(values) - 1:                   # 마지막 값이 아닐 경우만 알파벳으로 변환
                    convert.append(chr(values[i] + 90))       # Z 또는 Y
                if i+1 <= len(values) - 1:                # 그 다음 값이 존재할 경우
                    values[i+1] -= 1                          # 다음 값에 -1 수행
            else:
                convert.append(chr(values[i] + 64))
        
        return "".join(convert[::-1])
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.58** MB \| Beats **8.23%**

<mark>chr()</mark> 함수를 이용하여 숫자에 대응하는 ASCII 문자를 반환하도록 했다. A는 65이고 Z는 90인 것을 활용했다.
이 방법의 경우 columnNumber을 26으로 나눈 나머지의 값이 0일 때 처리해야 할 부분이 많아서 코드가 복잡해졌다. 0은 현재 자리를 `Z`로 하고 그 윗 자리의 알파벳을 하나 아래로 내리는 작업을 해야 하는데, 다음 자리도 0일 경우 -1이 되어버려서 문제가 되었다. 예를 들어 `11881376`의 경우 values 리스트에 [0,0,0,0,26] 순서로 저장되기 때문에 모든 변수를 신경써야 통과할 수 있었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/excel-sheet-column-title/solutions/6280288/video-solution-by-niits-c4ir/" target="_blank">1st</a>

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            res = chr((columnNumber % 26) + ord("A")) + res
            columnNumber //= 26
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log26𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(log26𝑛)           

columnNumber에서 1을 뺀 후 26진법 계산을 하는 방식을 사용하면 훨씬 간단하게 풀 수 있다.   
(A가 1이 아니라 0부터 시작하는 것처럼 취급)   
<mark>ord()</mark> 함수는 문자의 ASCII 값을 반환하기 때문에 값을 알고있지 않을 경우 사용할 수 있다. 또 res에 값을 추가할 때 새 값을 기존 값 앞에 넣기 때문에 마지막에 반대로 뒤집을 필요가 없다.

### <a href="https://leetcode.com/problems/excel-sheet-column-title/solutions/3943071/100-recursive-iterative-2-approaches-by-fn6a9/" target="_blank">2nd</a>

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result.append(chr(65 + remainder))
        return ''.join(reversed(result))
```
<mark>divmod()</mark> 함수는 몫과 나머지를 한꺼번에 반환하는 함수다. 매개변수로 두 수를 넘기면 앞의 숫자를 뒤의 숫자로 나눈다. 여기서는 매개변수에서 -1을 빼는 것으로 숫자를 보정했다.