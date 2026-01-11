---
excerpt: "'LeetCode: Triangle Judgement' 풀이 정리"
title: "\0610. Triangle Judgement"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Pandas
  - SQL
  - Math
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x':'Int64', 'y':'Int64', 'z':'Int64'})
```
<br>

Table: `Triangle`
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
</pre>

Report for every three line segments whether they can form a triangle.

Return the result table in **any order.**

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Triangle table:
    +----+----+----+
    | x  | y  | z  |
    +----+----+----+
    | 13 | 15 | 30 |
    | 10 | 20 | 15 |
    +----+----+----+
    </pre>
- Output:    
    <pre>
    +----+----+----+----------+
    | x  | y  | z  | triangle |
    +----+----+----+----------+
    | 13 | 15 | 30 | No       |
    | 10 | 20 | 15 | Yes      |
    +----+----+----+----------+
    </pre>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = (
        (triangle['x'] + triangle['y'] > triangle['z']) &
        (triangle['x'] + triangle['z'] > triangle['y']) &
        (triangle['y'] + triangle['z'] > triangle['x'])).map({True: 'Yes', False: 'No'}
    )
    
    return triangle
```
<i class="fa-solid fa-clock"></i> Runtime: **255** ms \| Beats **94.68%**    
<i class="fa-solid fa-memory"></i> Memory: **67.22** MB \| Beats **5.72%**

삼각형이 되려면 모든 변이 나머지 두 변의 합보다 짧아야 한다. <mark>map()</mark>을 사용하면 Series의 각 요소에 대해 딕셔너리로 매핑하여 변환 작업이 가능하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/triangle-judgement/solutions/6935436/simple-code-by-creating-a-user-defined-function/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def check_triangle(x,y,z):
        if (x+y>z) & (y+z>x) & (z+x>y):
            return "Yes"
        else:
            return "No"
    
    triangle['triangle'] = triangle.apply(lambda row: check_triangle(row['x'],row['y'],row['z']),axis=1)
    return triangle
```
map() 대신 <mark>apply()</mark>를 사용하는 방법도 있다.

### <a href="https://leetcode.com/problems/triangle-judgement/solutions/6983522/using-select-and-case/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">2nd</a>

```sql
SELECT x, y, z, 
    CASE
    WHEN (x+y) > z and (x+z) > y and (y+z) > x then 'Yes' else 'No'
    END AS 'triangle'
FROM Triangle
```
CASE WHEN 사용

```sql
SELECT *, 
    IF(x+y>z and y+z>x and z+x>y, "Yes", "No") AS triangle
FROM Triangle
```
IF() 함수 구문 사용