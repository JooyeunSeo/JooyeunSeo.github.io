---
excerpt: "'LeetCode: Zigzag Conversion' 풀이 정리"
title: "\06. Zigzag Conversion"
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

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:
<pre>
string convert(string s, int numRows);
</pre>

**Example 1:**

- Input: s = "PAYPALISHIRING", numRows = 3
- Output: "PAHNAPLSIIGYIR"

**Example 2:**

- Input: s = "PAYPALISHIRING", numRows = 4
- Output: "PINALSIGYAHRPI"
- Explanation:     
    <pre>
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    </pre>

**Example 3:**

- Input: s = "A", numRows = 1
- Output: "A"

**Constraints:**

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), `','` and `'.'`.
- 1 <= numRows <= 1000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):       # 예외처리
            return s

        rows = [""] * numRows
        cur_row = 0                 # 현재 행
        direction = 1               # 1 = down, -1 = up

        for char in s:
            rows[cur_row] += char

            if cur_row == 0:                # 첫 번째 행 에서 방향 전환
                direction = 1
            elif cur_row == numRows - 1:    # 마지막 행에서 방향 전환
                direction = -1

            cur_row += direction

        return "".join(rows)
```
<i class="fa-solid fa-clock"></i> Runtime: **7** ms \| Beats **86.36%**    
<i class="fa-solid fa-memory"></i> Memory: **19.35** MB \| Beats **76.66%**    

직선일 때 아래 행으로 내려가고 대각선일 때는 올라가기 때문에 direction 변수로 방향을 전환했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/zigzag-conversion/solutions/6324425/beats-100-easier-than-you-think-by-visha-rlgh/" target="_blank">1st</a>

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        a=""
        for i in range(numRows):
            for j in range(i,len(s),2*(numRows-1)):
                a+=s[j]
                if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                    a+=s[j+2*(numRows-1)-2*i]   # 대각선 계산
        return a
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

행 기준으로 인덱스를 계산해서 건너뛰는 방법이다. `2*(numRows-1)`은 세로줄의 사이클이 된다.

s = "PAYPALISHIRING"      
numRows = 3      
{: style="color: blue;"}
<pre>
       j     j      j
i  |0|   |4|   |8 |    |12| → P   A   H   N    
i  |1| 3 |5| 7 |9 | 11 |13| → A P L S I I G   
i  |2|   |6|   |10|    |  | → Y   I   R        
</pre>

return "PAHNAPLSIIGYIR"
{: style="color: green;"}