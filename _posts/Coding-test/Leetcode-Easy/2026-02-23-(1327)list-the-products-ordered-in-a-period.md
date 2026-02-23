---
excerpt: "'LeetCode: List the Products Ordered in a Period' 풀이 정리"
title: "\01327. List the Products Ordered in a Period"
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
data = [[1, 'Leetcode Solutions', 'Book'], [2, 'Jewels of Stringology', 'Book'], [3, 'HP', 'Laptop'], [4, 'Lenovo', 'Laptop'], [5, 'Leetcode Kit', 'T-shirt']]
products = pd.DataFrame(data, columns=['product_id', 'product_name', 'product_category']).astype({'product_id':'Int64', 'product_name':'object', 'product_category':'object'})
data = [[1, '2020-02-05', 60], [1, '2020-02-10', 70], [2, '2020-01-18', 30], [2, '2020-02-11', 80], [3, '2020-02-17', 2], [3, '2020-02-24', 3], [4, '2020-03-01', 20], [4, '2020-03-04', 30], [4, '2020-03-04', 60], [5, '2020-02-25', 50], [5, '2020-02-27', 50], [5, '2020-03-01', 50]]
orders = pd.DataFrame(data, columns=['product_id', 'order_date', 'unit']).astype({'product_id':'Int64', 'order_date':'datetime64[ns]', 'unit':'Int64'})
```
<br>

Table: `Products`
<pre>
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.
</pre>

Table: `Orders`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.
</pre>

Write a solution to get the names of products that have at least `100` units ordered in **February 2020** and their amount.

Return the result table in **any order.**

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Products table:
    +-------------+-----------------------+------------------+
    | product_id  | product_name          | product_category |
    +-------------+-----------------------+------------------+
    | 1           | Leetcode Solutions    | Book             |
    | 2           | Jewels of Stringology | Book             |
    | 3           | HP                    | Laptop           |
    | 4           | Lenovo                | Laptop           |
    | 5           | Leetcode Kit          | T-shirt          |
    +-------------+-----------------------+------------------+
    Orders table:
    +--------------+--------------+----------+
    | product_id   | order_date   | unit     |
    +--------------+--------------+----------+
    | 1            | 2020-02-05   | 60       |
    | 1            | 2020-02-10   | 70       |
    | 2            | 2020-01-18   | 30       |
    | 2            | 2020-02-11   | 80       |
    | 3            | 2020-02-17   | 2        |
    | 3            | 2020-02-24   | 3        |
    | 4            | 2020-03-01   | 20       |
    | 4            | 2020-03-04   | 30       |
    | 4            | 2020-03-04   | 60       |
    | 5            | 2020-02-25   | 50       |
    | 5            | 2020-02-27   | 50       |
    | 5            | 2020-03-01   | 50       |
    +--------------+--------------+----------+
    </pre>
- Output:    
    <pre>
    +--------------------+---------+
    | product_name       | unit    |
    +--------------------+---------+
    | Leetcode Solutions | 130     |
    | Leetcode Kit       | 100     |
    +--------------------+---------+
    </pre>
- Explanation:          
    Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
    Products with product_id = 2 is ordered in February a total of 80.
    Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
    Products with product_id = 4 was not ordered in February 2020.
    Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 테이블 병합
    df = products.merge(orders)
    
    # 2020년 2월만 필터링
    df = df.loc[(df['order_date'] >= '2020-02-01') & (df['order_date'] < '2020-03-01')]
    
    # 제품당 주문 개수
    df = df.groupby('product_name')['unit'].sum().reset_index()
    
    # unit이 100 이상인 제품만 필터링
    df = df.loc[df['unit'] >= 100]
    
    return df
```
<i class="fa-solid fa-clock"></i> Runtime: **314** ms \| Beats **85.52%**    
<i class="fa-solid fa-memory"></i> Memory: **67.97** MB \| Beats **94.80%**    

product_id 기준으로 두 테이블을 병합하고 product_name 기준으로 그룹화했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/list-the-products-ordered-in-a-period/solutions/3583495/attention-coders-efficient-sql-query-to-0bbi3/" target="_blank">1st</a>

```sql
SELECT p.product_name AS product_name, sum(o.unit) AS unit FROM Products p
JOIN Orders o USING (product_id)
WHERE YEAR(o.order_date)='2020' AND MONTH(o.order_date)='02'
GROUP BY p.product_id
HAVING SUM(o.unit)>=100
```

### <a href="https://leetcode.com/problems/list-the-products-ordered-in-a-period/solutions/7571527/finding-high-performing-products-using-d-j6rw/" target="_blank">2nd</a>

```sql
SELECT 
    p.product_name, 
    SUM(o.unit) AS unit
FROM Products p
JOIN Orders o 
    ON p.product_id = o.product_id
WHERE o.order_date BETWEEN DATE '2020-02-01' AND DATE '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
```