---
excerpt: "'LeetCode: Not Boring Movies' 풀이 정리"
title: "\0620. Not Boring Movies"
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
data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})
```
<br>

Table: `Cinema`
<pre>
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
</pre>

Write a solution to report the movies with an odd-numbered ID and a description that is not `"boring"`.

Return the result table ordered by `rating` **in descending order.**

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Cinema table:
    +----+------------+-------------+--------+
    | id | movie      | description | rating |
    +----+------------+-------------+--------+
    | 1  | War        | great 3D    | 8.9    |
    | 2  | Science    | fiction     | 8.5    |
    | 3  | irish      | boring      | 6.2    |
    | 4  | Ice song   | Fantacy     | 8.6    |
    | 5  | House card | Interesting | 9.1    |
    +----+------------+-------------+--------+
    </pre>
- Output:    
    <pre>
    +----+------------+-------------+--------+
    | id | movie      | description | rating |
    +----+------------+-------------+--------+
    | 5  | House card | Interesting | 9.1    |
    | 1  | War        | great 3D    | 8.9    |
    +----+------------+-------------+--------+
    </pre>
- Explanation:    
We have three movies with odd-numbered IDs: 1, 3, and 5.    
The movie with ID = 3 is boring so we do not include it in the answer.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    filtered_movies = cinema.loc[(cinema.id % 2 == 1) & (cinema.description != 'boring')]
    return filtered_movies.sort_values(by='rating', ascending=False)
```
<i class="fa-solid fa-clock"></i> Runtime: **238** ms \| Beats **97.74%**    
<i class="fa-solid fa-memory"></i> Memory: **67.16** MB \| Beats **64.28%**

<mark>sort_values()</mark>에서 ascending을 False로 설정하면 내림차순 정렬을 할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/not-boring-movies/solutions/3983631/use-slicing-ignore-people-asking-you-to-work-out-whether-there-s-a-remainder-after-dividing-by-2/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[::2][cinema.description != 'boring'].sort_values('rating', ascending=False)
```
id가 1부터 시작해서 중간에 빠진 숫자없이 정렬되어있다고 보장할 수 있다면 이 방법도 사용할 수 있다.

### <a href="https://leetcode.com/problems/not-boring-movies/solutions/3839979/100-easy-fast-clean-solution-by-kartik_k-1ejq/" target="_blank">2nd</a>

```sql
SELECT *                        -- 3. 필터링된 행에서 모든 열 선택
FROM Cinema                     -- 1. 테이블 불러오기
WHERE MOD(id, 2) = 1            -- 2. 조건에 맞는 행만 필터링
  AND description <> 'boring'   -- (<> 는 표준 SQL에서 '같지 않다'는 뜻)
ORDER BY rating DESC;           -- 4. rating 열 기준으로 내림차순
```