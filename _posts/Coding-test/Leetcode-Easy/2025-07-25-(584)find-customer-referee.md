---
excerpt: "'LeetCode: Find Customer Referee' 풀이 정리"
title: "\0584. Find Customer Referee"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Pandas
  - MySQL
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})
```
<br>

Table: `Customer`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates
the id of a customer, their name, and the id of the customer who referred them.
</pre>

Find the names of the customer that are either:

- **referred by** any customer with `id != 2`.
- **not referred by** any customer.
- Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:
    <pre>
    Customer table:
    +----+------+------------+
    | id | name | referee_id |
    +----+------+------------+
    | 1  | Will | null       |
    | 2  | Jane | null       |
    | 3  | Alex | 2          |
    | 4  | Bill | null       |
    | 5  | Zack | 1          |
    | 6  | Mark | 2          |
    +----+------+------------+
    </pre>
- Output:
    <pre>
    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+
    </pre>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Be careful of the NULL value</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # NaN 값은 0으로 변환
    return customer[customer["referee_id"].fillna(0) != 2][["name"]]
```
<i class="fa-solid fa-clock"></i> Runtime: **274** ms \| Beats **83.58%**    
<i class="fa-solid fa-memory"></i> Memory: **66.79** MB \| Beats **92.63%**

referee_id 열의 값이 2가 아닌 경우에 모두 해당하기 때문에 NaN 값을 0으로 변경했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-customer-referee/solutions/6930118/simple-1-line-pandas-code-for-where-cond-88af/" target="_blank">1st</a>

```python
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer['referee_id']!=2) | (customer['referee_id'].isna())][['name']]
```
`|` 연산자로 두 조건을 필터링했다.

### <a href="https://leetcode.com/problems/find-customer-referee/solutions/3789317/easy-solution-mysql-by-ankur_chhillar-fr5n/" target="_blank">2nd</a>

```sql
select name from customer
where referee_id != 2 or referee_id is null;
```
MySQL 버전이다.