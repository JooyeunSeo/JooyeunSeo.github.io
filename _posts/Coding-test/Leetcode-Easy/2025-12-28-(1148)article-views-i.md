---
excerpt: "'LeetCode: Article Views I' 풀이 정리"
title: "\01148. Article Views I"
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
data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})
```
<br>

Table: `Views`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
</pre>

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Views table:
    +------------+-----------+-----------+------------+
    | article_id | author_id | viewer_id | view_date  |
    +------------+-----------+-----------+------------+
    | 1          | 3         | 5         | 2019-08-01 |
    | 1          | 3         | 6         | 2019-08-02 |
    | 2          | 7         | 7         | 2019-08-01 |
    | 2          | 7         | 6         | 2019-08-02 |
    | 4          | 7         | 1         | 2019-07-22 |
    | 3          | 4         | 4         | 2019-07-21 |
    | 3          | 4         | 4         | 2019-07-21 |
    +------------+-----------+-----------+------------+
    </pre>
- Output:    
    <pre>
    +------+
    | id   |
    +------+
    | 4    |
    | 7    |
    +------+
    </pre>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[views['author_id'] == views['viewer_id']].drop_duplicates('author_id').sort_values('author_id')

    return df[['author_id']].rename(columns={'author_id': 'id'})
```
<i class="fa-solid fa-clock"></i> Runtime: **260** ms \| Beats **94.24%**    
<i class="fa-solid fa-memory"></i> Memory: **67.46** MB \| Beats **49.67%**    

author_id와 viewer_id가 동일한 행만 셀렉한 후, 중복 행을 지우고 id순으로 정렬했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/article-views-i/solutions/3852944/pandas-my-sql-very-simple-with-approach-z06jh/" target="_blank">1st</a>

```python
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id and viewer_id are the same (authors viewing their own articles)
    authors_viewed_own_articles = views[views['author_id'] == views['viewer_id']]
    
    # Get unique author_ids from the filtered data
    unique_authors = authors_viewed_own_articles['author_id'].unique()
    
    # Sort the unique author_ids in ascending order
    unique_authors = sorted(unique_authors)
    
    # Create a DataFrame with the sorted unique author_ids and rename the 'author_id' column to 'id'
    result_df = pd.DataFrame({'id': unique_authors})
    
    return result_df
```

### <a href="https://leetcode.com/problems/article-views-i/solutions/3704391/sql-simple-straight-forward-approach-by-6851s/" target="_blank">2nd</a>

```sql
select distinct author_id as id from Views
where author_id = viewer_id 
order by id;
```