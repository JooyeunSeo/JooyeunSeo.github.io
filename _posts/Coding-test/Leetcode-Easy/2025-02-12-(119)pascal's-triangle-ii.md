---
excerpt: "'LeetCode: Pascal's Triangle II' 풀이 정리"
title: "\0119. Pascal's Triangle II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Pascal's triangle
  - Dynamic Programming
  - math.comb()
  - zip()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `rowIndex`, return the rowIndex<sup>th</sup> **(0-indexed)** row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example 1:**

- Input: rowIndex = 3
- Output: [1,3,3,1]

**Example 2:**

- Input: rowIndex = 0
- Output: [1]

**Example 3:**

- Input: rowIndex = 1
- Output: [1,1]

**Constraints:**

- 0 <= rowIndex <= 33

**Follow up:** Could you optimize your algorithm to use only `𝑂(rowIndex)` extra space?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last_row = []

        for row in range(rowIndex + 1):
            current_row = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    current_row.append(1)
                else:
                    current_row.append(last_row[col-1] + last_row[col])
            last_row = current_row

        return last_row
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.35** MB \| Beats **75.38%**

Follow up을 충족하는 답안을 만들기 위해서 고민했는데, 그냥 118번에서 했던 코드에서 전체 행을 모두 저장하는 대신 가장 마지막의 행만 저장하도록 바꾸는 것으로 간단하게 해결할 수 있었다.


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/pascals-triangle-ii/solutions/6403248/beats-100-in-0ms-by-arun_george-mzwy/" target="_blank">1st</a>

```python
from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)             

파스칼의 삼각형에서 각 항목을 **이항 계수**(binomial coefficient)로 표현할 수 있는 것을 활용한 답안이다. math 모듈의 <mark>math.comb()</mark> 함수를 이용했다. 반환값을 제외하면 추가적인 공간을 사용하지 않는다는 장점이 있다.

rowIndex = 4
{: style="color: blue;"}

<pre>
C(4, 0) = 4! / 0!(4 - 0)! = 4!/0!(4!) = 1
C(4, 1) = 4! / 1!(4 - 1)! = 4!/1!(3!) = 4
C(4, 2) = 4! / 2!(4 - 2)! = 4!/2!(4!) = 6
C(4, 3) = 4! / 3!(4 - 3)! = 4!/3!(1!) = 4 
C(4, 4) = 4! / 4!(4 - 4)! = 4!/4!(0!) = 1
</pre>

return [1, 4, 6, 4, 1]
{: style="color: green;"}

### <a href="https://leetcode.com/problems/pascals-triangle-ii/solutions/4173164/100-easy-optimized-by-vanamsen-uqq9/" target="_blank">2nd</a>

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]  # rowIndex가 0이면 [1]
        prev = 1   # 이전 항 값 저장
        
        for k in range(1, rowIndex + 1):                # 1부터 rowIndex까지 반복
            next_val = prev * (rowIndex - k + 1) // k   # 이항 계수 점화식 (// 연산자로 소수점 없이 값 얻기)
            res.append(next_val)
            prev = next_val                             # prev 업데이트
        
        return res
```
math 모듈없이 이항 계수를 계산한 코드다. 이항 계수 공식을 점화식으로 나타내서 이전 값을 이용해 새로운 값을 계산하는 방법이다. / 연산자로 나누면 float 형이 되기 때문에 // 연산자로 몫만 얻는 것을 볼 수 있다.

<div class="notice--info" markdown="1">
이항 계수 공식   
**C(rowIndex, k) = rowIndex! / k!(rowIndex - k)!**   
↓    
점화식   
**C(rowIndex, k) = C(rowIndex, k−1) \* (rowIndex - k + 1) / k**
</div>

### <a href="https://leetcode.com/problems/pascals-triangle-ii/solutions/6280033/video-give-me-10-minutes-how-we-think-ab-3lal/" target="_blank">3rd</a>

```python
class Solution(object):
    def getRow(self, rowIndex):
        row = [1]

        for _ in range(rowIndex):
            row = [left + right for left, right in zip([0]+row, row+[0])]
            
        return row
```
각 행의 양쪽 끝에 0을 더한다는 아이디어 + <mark>zip()</mark>을 이용한 예시다. 

rowIndex = 4
{: style="color: blue;"}

<pre>
                                    [1]          
zip([0]+[1]      , [1]+[0])       → [(0,1), (1,0)]
                                    [  1,     1  ]   
zip([0]+[1,1]    , [1,1]+[0])     → [(0,1), (1,1), (1,0)]
                                    [  1,     2,     1  ] 
zip([0]+[1,2,1]  , [1,2,1]+[0])   → [(0,1), (1,2), (2,1), (1,0)]
                                    [  1,     3,     3,     1  ]              
zip([0]+[1,3,3,1], [1,3,3,1]+[0]) → [(0,1), (1,3), (3,3), (3,1), (1,0)]
                                    [  1,     4,     6,     4,     1  ]
</pre>

return [1, 4, 6, 4, 1]
{: style="color: green;"}