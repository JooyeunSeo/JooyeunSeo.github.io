---
excerpt: "'LeetCode: Classes With at Least 5 Students' 풀이 정리"
title: "\0596. Classes With at Least 5 Students"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Pandas
  - SQL 
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
```
<br>

Table: `Courses`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
</pre>

Write a solution to find all the classes that have **at least five students.**

Return the result table in **any order.**

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Courses table:
    +---------+----------+
    | student | class    |
    +---------+----------+
    | A       | Math     |
    | B       | English  |
    | C       | Math     |
    | D       | Biology  |
    | E       | Math     |
    | F       | Computer |
    | G       | Math     |
    | H       | Math     |
    | I       | Math     |
    +---------+----------+
    </pre>
- Output:    
    <pre>
    +---------+
    | class   |
    +---------+
    | Math    |
    +---------+
    </pre>
- Explanation: 
   - Math has 6 students, so we include it.
   - English has 1 student, so we do not include it.
   - Biology has 1 student, so we do not include it.
   - Computer has 1 student, so we do not include it.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    groups = courses.groupby('class', as_index=False).count()
    return groups[groups['student'] >= 5][['class']]
```
<i class="fa-solid fa-clock"></i> Runtime: **255** ms \| Beats **88.53%**    
<i class="fa-solid fa-memory"></i> Memory: **68.06** MB \| Beats **62.98%**

groupby()와 count()를 사용했다. 

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/classes-with-at-least-5-students/solutions/6931551/simplest-pandas-code-using-group-by-and-mv8z7/" target="_blank">1st</a>

```python
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['class'].size().reset_index(name='count')
    return df[df['count']>=5][['class']]
```
count() 대신 <mark>size()</mark>로 그룹별 행 갯수를 셀 수도 있다.

### <a href="https://leetcode.com/problems/classes-with-at-least-5-students/solutions/3912758/pandas-one-liner-solution-beats-95-detai-rrik/" target="_blank">2nd</a>

```python
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses['class'].value_counts()[(courses['class'].value_counts()>4)].index.to_frame()
```
<mark>value_counts()</mark>로 class 열에서 각 클래스가 등장한 횟수를 셀 경우 클래스 이름은 인덱스로, 등장 횟수는 값으로 반환된다. 5 이상만 필터링한 후 인덱스만 가져와서 이를 DataFrame으로 변환했다. 참고로 `courses['class'].value_counts()`까지를 변수에 저장하면 함수 중복 호출을 줄일 수 있다.

### <a href="" target="_blank">3rd</a>

```sql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
```
SQL에서는 GROUP BY와 HAVING을 사용한다.