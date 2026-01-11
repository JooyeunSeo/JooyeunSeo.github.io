---
excerpt: "'LeetCode: Big Countries' 풀이 정리"
title: "\0595. Big Countries"
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
data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})
```
<br>

Table: `World`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about 
the name of a country, the continent to which it belongs,
its area, the population, and its GDP value.
</pre>

A country is **big** if:

- it has an area of at least three million (i.e., 3000000 km<sup>2</sup>), or
- it has a population of at least twenty-five million (i.e., 25000000).

Write a solution to find the name, population, and area of the **big countries**.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    World table:
    +-------------+-----------+---------+------------+--------------+
    | name        | continent | area    | population | gdp          |
    +-------------+-----------+---------+------------+--------------+
    | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
    | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
    | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
    | Andorra     | Europe    | 468     | 78115      | 3712000000   |
    | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
    +-------------+-----------+---------+------------+--------------+
    </pre>
- Output:    
    <pre>
    +-------------+------------+---------+
    | name        | population | area    |
    +-------------+------------+---------+
    | Afghanistan | 25500100   | 652230  |
    | Algeria     | 37100000   | 2381741 |
    +-------------+------------+---------+
    </pre>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return world[['name', 'population', 'area']]
```
<i class="fa-solid fa-clock"></i> Runtime: **259** ms \| Beats **76.60%**    
<i class="fa-solid fa-memory"></i> Memory: **68.82** MB \| Beats **57.11%**

조건에 맞는 행만 출력하는 간단한 문제다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/big-countries/solutions/6871533/big-countries-sql-to-pandas-beginner-fri-p5cx/" target="_blank">1st</a>

```python
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # select name, population, area from world where area>=3000000 or population>=25000000
    return world.loc[
        (world['area'] >= 3000000) | (world['population'] >= 25000000),
        ['name', 'population', 'area']
    ]
```
<mark>loc[]</mark>을 사용해도 된다.

### <a href="https://leetcode.com/problems/big-countries/solutions/3362481/one-line-of-code-using-union-and-or/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">2nd</a>

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
```
**OR** 사용

```sql
select area,population,name
from world
where area>=3000000
union
select area,population,name
from world
where population>=25000000
```
**UNION** 사용