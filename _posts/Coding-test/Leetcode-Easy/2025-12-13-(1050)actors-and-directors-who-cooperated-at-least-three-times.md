---
excerpt: "'LeetCode: Actors and Directors Who Cooperated At Least Three Times' 풀이 정리"
title: "\01050. Actors and Directors Who Cooperated At Least Three Times"
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
data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})
```
<br>

Table: `ActorDirector`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
</pre>

Write a solution to find all the pairs `(actor_id, director_id)` where the actor has cooperated with the director at least three times.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    ActorDirector table:
    +-------------+-------------+-------------+
    | actor_id    | director_id | timestamp   |
    +-------------+-------------+-------------+
    | 1           | 1           | 0           |
    | 1           | 1           | 1           |
    | 1           | 1           | 2           |
    | 1           | 2           | 3           |
    | 1           | 2           | 4           |
    | 2           | 1           | 5           |
    | 2           | 1           | 6           |
    +-------------+-------------+-------------+
    </pre>
- Output:    
    <pre>
    +-------------+-------------+
    | actor_id    | director_id |
    +-------------+-------------+
    | 1           | 1           |
    +-------------+-------------+
    </pre>
- Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    filtered_pairs = df[df['count'] >= 3]
    return filtered_pairs[['actor_id', 'director_id']]
```
<i class="fa-solid fa-clock"></i> Runtime: **273** ms \| Beats **77.23%**    
<i class="fa-solid fa-memory"></i> Memory: **67.50** MB \| Beats **90.81%**    

groupby()와 size()로 개수를 센 뒤 reset_index()로 새 컬럼을 만들어서 결과를 저장했다. 그 후 3 이상인 그룹만 필터링하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/solutions/7273424/pandas-groupby-and-filter-ts-95-92-by-sp-vfdc/" target="_blank">1st</a>

```python
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'
                      ].size().reset_index()
   
    return actor_director[actor_director.timestamp >= 3].iloc[:,[0,1]]
```

### <a href="" target="_blank">2nd</a>

```sql
select actor_id,director_id
from ActorDirector 
group by actor_id,director_id
Having count(timestamp)>=3;
```