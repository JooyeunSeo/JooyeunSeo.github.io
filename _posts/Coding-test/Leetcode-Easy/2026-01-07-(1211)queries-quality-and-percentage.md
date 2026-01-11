---
excerpt: "'LeetCode: Queries Quality and Percentage' 풀이 정리"
title: "\01211. Queries Quality and Percentage"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Database
  - Pandas
  - SQL
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype({'query_name':'object', 'result':'object', 'position':'Int64', 'rating':'Int64'})
```
<br>

Table: `Queries`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
</pre>

We define query `quality` as:

- The average of the ratio between query rating and its position.

We also define `poor query percentage` as:

- The percentage of all queries with rating less than 3.

Write a solution to find each `query_name`, the `quality` and `poor_query_percentage`.

Both `quality` and `poor_query_percentage` should be **rounded to 2 decimal places.**

Return the result table in **any order.**

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Queries table:
    +------------+-------------------+----------+--------+
    | query_name | result            | position | rating |
    +------------+-------------------+----------+--------+
    | Dog        | Golden Retriever  | 1        | 5      |
    | Dog        | German Shepherd   | 2        | 5      |
    | Dog        | Mule              | 200      | 1      |
    | Cat        | Shirazi           | 5        | 2      |
    | Cat        | Siamese           | 3        | 3      |
    | Cat        | Sphynx            | 7        | 4      |
    +------------+-------------------+----------+--------+
    </pre>
- Output:    
    <pre>
    +------------+---------+-----------------------+
    | query_name | quality | poor_query_percentage |
    +------------+---------+-----------------------+
    | Dog        | 2.50    | 33.33                 |
    | Cat        | 0.66    | 33.33                 |
    +------------+---------+-----------------------+
    </pre>
- Explanation:       
Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50      
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33      
Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66     
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33     

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # SQL식 반올림
    eps = 1e-8

    queries['ratio'] = queries['rating'] / queries['position']
    queries['poor'] = (queries['rating'] < 3) * 100
    
    df = (
        queries
        .groupby('query_name', sort=False)
        .agg(
            quality=( 'ratio', lambda x: x.mean() + eps ),
            poor_query_percentage=( 'poor', lambda x: x.mean() + eps )
        )
        .round(2)
        .reset_index()
    )

    return df
```
<i class="fa-solid fa-clock"></i> Runtime: **323** ms \| Beats **38.37%**    
<i class="fa-solid fa-memory"></i> Memory: **68.18** MB \| Beats **28.10%**    

pandas와 sql에서 `5`일 때 반올림하는 방식이 살짝 다른데 리트코드에서는 sql 기준으로 채점하기 때문에 통과하지 못하는 문제가 있었다. 예를 들어 0.325의 경우 pandas 또는 python에서는 **가장 가까운 짝수**로 보내기 때문에 0.32가 되지만, sql에서는 **무조건** 올리기 때문에 0.33이 된다.      
판다스로 푼 유저들은 보통 테스트를 통과하기 위해 epsilon을 더하는 꼼수를 가장 많이 사용하는 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/queries-quality-and-percentage/solutions/5167355/pandas-3-lines-counter-ts-81-51-by-spaul-mjkl/" target="_blank">1st</a>

```python
round2 = lambda x: round(x + 1e-9, 2)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:

    queries['quality'] = queries.rating/queries.position
    queries['poor_query_percentage'] = (queries.rating < 3)*100

    return queries.groupby('query_name')[['quality',
          'poor_query_percentage']].mean().apply(round2).reset_index()
```
내가 제출했던 코드보다 더 효율이 좋은 코드를 참고했다.

### <a href="https://leetcode.com/problems/queries-quality-and-percentage/solutions/7347956/very-easy-sol-with-logic-explaination-by-asp8/" target="_blank">2nd</a>

```sql
SELECT query_name, 
    ROUND(AVG(rating/position),2) AS quality,
    ROUND((SUM(CASE WHEN rating<3 THEN 1 ELSE 0 END) / count(*)) * 100,2) AS poor_query_percentage
FROM queries
GROUP BY query_name
```