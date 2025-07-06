---
excerpt: "'LeetCode: Pascal's Triangle' 풀이 정리"
title: "\0118. Pascal's Triangle"
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
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example 1:**

- Input: numRows = 5
- Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

**Example 2:**

- Input: numRows = 1
- Output: [[1]]

**Constraints:**

- 1 <= numRows <= 30

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []       # 최종 출력

        for row in range(numRows):          # 각 행을 차례로 순환
            row_list = []                     # 행의 원소를 담는 리스트(다음 행을 만들기 전에 항상 초기화)
            for col in range(row + 1):        # 행의 원소를 차례로 순환
                if col == 0 or col == row:    # 행의 첫 번째(col == 0)와 마지막(col == row)은 1
                    row_list.append(1)        
                else:
                    row_list.append(output[row-1][col-1] + output[row-1][col])  # 바로 위 행의 두 항목 합

            output.append(row_list)           # 완성된 행을 최종 결과 리스트에 추가

        return output
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.49** MB \| Beats **51.71%**

파스칼의 삼각형 문제를 c++로 본 적이 있어서 금방 풀 수 있었다. 코드로 구현할 때는 삼각형을 가운데 정렬한 것보다 왼쪽으로 정렬했을 때가 더 이해하기 쉬운 것 같다.

numRows = 5
{: style="color: blue;"}

<pre>
                     [
numRows=1, output[0]  [1],
numRows=2, output[1]  [1, 1],
numRows=3, output[2]  [1, 2, 1],      output[1][0] + output[1][1] = 1+1 = 2
numRows=4, output[3]  [1, 3, 3, 1],
numRows=5, output[4]  [1, 4, 6, 4, 1]
                      ]
</pre>

output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/pascals-triangle/solutions/6209724/video-adding-0-at-the-both-sides-python-javascript-java-c/" target="_blank">1st</a>

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]                             # 첫 번째 행

        for _ in range(numRows - 1):            # 두 번째 행부터 시작
            dummy_row = [0] + res[-1] + [0]     # 이전 행에 0을 양쪽에 추가한 새로운 더미 행 생성
            row = []                            # 현재 행 저장

            for i in range(len(res[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i+1])   # 두 인접 항목을 더해서 새로운 항목 생성
            res.append(row)
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)      
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛<sup>2</sup>)  

각 행의 맨 앞과 맨 뒤에 0을 더한다는 아이디어를 사용한 답안이다. 0은 1에 더해도 그대로 1이 되기 때문에 결과에 전혀 영향을 주지 않고, 두 인접 항목을 더하는 연산을 일괄 적용할 수 있다.


### <a href="https://leetcode.com/problems/pascals-triangle/solutions/4016203/three-approachesbeginner-friendlyfull-ex-c39l/" target="_blank">2nd</a>

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)                 # 이전 행을 재귀호출
        newRow = [1] * numRows                                # 새 행 생성
        
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i] # 중간 요소들 계산
        
        prevRows.append(newRow)                               # 현재 행을 추가
        return prevRows                                       # 현재까지 완성된 전체 목록 반환
```
재귀 호출을 이용한 방법