---
excerpt: "'LeetCode: Reformat Department Table' 풀이 정리"
title: "\01179. Reformat Department Table"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Database
  - Pandas
  - MySQL
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype({'id':'Int64', 'revenue':'Int64', 'month':'object'})
```
<br>

Table: `Department`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
</pre>

Reformat the table such that there is a department id column and a revenue column **for each month**.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Department table:
    +------+---------+-------+
    | id   | revenue | month |
    +------+---------+-------+
    | 1    | 8000    | Jan   |
    | 2    | 9000    | Jan   |
    | 3    | 10000   | Feb   |
    | 1    | 7000    | Feb   |
    | 1    | 6000    | Mar   |
    +------+---------+-------+
    </pre>
- Output:    
    <pre>
    +------+-------------+-------------+-------------+-----+-------------+
    | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
    +------+-------------+-------------+-------------+-----+-------------+
    | 1    | 8000        | 7000        | 6000        | ... | null        |
    | 2    | 9000        | null        | null        | ... | null        |
    | 3    | null        | 10000       | null        | ... | null        |
    +------+-------------+-------------+-------------+-----+-------------+
    </pre>
- Explanation: The revenue from Apr to Dec is null.     
Note that the result table has 13 columns (1 for the department id + 12 for the months).

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # pivot
    df = department.pivot(index='id', columns='month', values='revenue')

    # pivot 후 columns에 붙은 이름(month) 제거
    df.columns.name = None

    # month_order에 따라 컬럼 순서 변경 후, 월별 컬럼 이름 변경
    df = df.reindex(columns=month_order).rename(columns={i: f'{i}_Revenue' for i in month_order})
    
    # id를 인덱스 -> 컬럼으로 다시 변경
    return df.reset_index()
```
<i class="fa-solid fa-clock"></i> Runtime: **287** ms \| Beats **95.30%**    
<i class="fa-solid fa-memory"></i> Memory: **68.33** MB \| Beats **54.55%**    

pivot으로 테이블 구조를 변경하면 컬럼이 알파벳 순서대로 나오기 때문에 미리 리스트로 순서를 지정해서 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reformat-department-table/solutions/7291485/pandas-pivot-and-add_suffix-by-spaulding-ewn9/" target="_blank">1st</a>

```python
months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:

    df = department.pivot(index = 'id',
                        columns = 'month',
                         values = 'revenue')
   
    return (df.reindex(columns = months).reset_index()
              .add_suffix('_Revenue')
              .rename(columns = {'id_Revenue': 'id'}))
```
pandas에서 `add_suffix()`를 이용하여 '_Revenue'를 접미사로 붙이는 방법도 있다.

### <a href="https://leetcode.com/problems/reformat-department-table/solutions/7347946/very-simple-with-logic-explaination-by-v-8ul2/" target="_blank">2nd</a>

```sql
# Write your MySQL query statement below

SELECT id,
    MAX(CASE WHEN month ='Jan' THEN revenue END) AS Jan_Revenue,
    MAX(CASE WHEN month ='Feb' THEN revenue END) AS Feb_Revenue,
    MAX(CASE WHEN month ='Mar' THEN revenue END) AS Mar_Revenue,
    MAX(CASE WHEN month ='Apr' THEN revenue END) AS Apr_Revenue,
    MAX(CASE WHEN month ='May' THEN revenue END) AS May_Revenue,
    MAX(CASE WHEN month ='Jun' THEN revenue END) AS Jun_Revenue,
    MAX(CASE WHEN month ='Jul' THEN revenue END) AS Jul_Revenue,
    MAX(CASE WHEN month ='Aug' THEN revenue END) AS Aug_Revenue,
    MAX(CASE WHEN month ='Sep' THEN revenue END) AS Sep_Revenue,
    MAX(CASE WHEN month ='Oct' THEN revenue END) AS Oct_Revenue,
    MAX(CASE WHEN month ='Nov' THEN revenue END) AS Nov_Revenue,
    MAX(CASE WHEN month ='Dec' THEN revenue END) AS Dec_Revenue
FROM DEPARTMENT
GROUP BY id
```
새 컬럼(e.g. Jan_Revenue)에 들어갈 값은 id 하나 + month 하나에 대응되는 단 하나의 revenue이고, `CASE WHEN`으로 만들면 나머지는 전부 NULL이 된다. 이 상태에서 GROUP BY id를 하기 위해 집계 함수가 필요한데 `MAX()`는 NULL을 자동으로 무시하고 실제 값 하나만 선택해주기 때문에 pivot 패턴에서 자주 사용된다.