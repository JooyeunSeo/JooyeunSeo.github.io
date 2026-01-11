---
excerpt: "'LeetCode: Product Sales Analysis I' 풀이 정리"
title: "\01068. Product Sales Analysis I"
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
data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})
data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype({'product_id':'Int64', 'product_name':'object'})
```
<br>

Table: `Sales`
<pre>
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
</pre>

Table: `Product`
<pre>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
</pre>

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Sales table:
    +---------+------------+------+----------+-------+
    | sale_id | product_id | year | quantity | price |
    +---------+------------+------+----------+-------+ 
    | 1       | 100        | 2008 | 10       | 5000  |
    | 2       | 100        | 2009 | 12       | 5000  |
    | 7       | 200        | 2011 | 15       | 9000  |
    +---------+------------+------+----------+-------+
    Product table:
    +------------+--------------+
    | product_id | product_name |
    +------------+--------------+
    | 100        | Nokia        |
    | 200        | Apple        |
    | 300        | Samsung      |
    +------------+--------------+
    </pre>
- Output:    
    <pre>
    +--------------+-------+-------+
    | product_name | year  | price |
    +--------------+-------+-------+
    | Nokia        | 2008  | 5000  |
    | Nokia        | 2009  | 5000  |
    | Apple        | 2011  | 9000  |
    +--------------+-------+-------+
    </pre>
- Explanation:     
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.     
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.      
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return product.merge(sales, on='product_id', how='inner')[['product_name', 'year', 'price']]
```
<i class="fa-solid fa-clock"></i> Runtime: **328** ms \| Beats **85.59%**    
<i class="fa-solid fa-memory"></i> Memory: **70.60** MB \| Beats **11.06%**    

product 데이터프레임을 기준으로 합치고, inner 방식으로 일치하는 값이 없는 행은 제거했다. 또 on 파라미터로 두 데이터프레임에 공통으로 존재하는 열을 명시해서 효율을 높였다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/product-sales-analysis-i/solutions/7049518/easy-sql-solution-beginner-level-in-dept-kt4n/" target="_blank">1st</a>

```sql
SELECT product_name, year, price
FROM Sales
JOIN Product USING(product_id);
```
두 테이블에 동일한 컬럼명(`product_id`)이 있을 때만 `USING`을 사용하여 해당 컬럼명을 조건으로 join할 수 있다.

### <a href="https://leetcode.com/problems/product-sales-analysis-i/solutions/6349854/easy-and-simple-solution-beginner-friend-k3fl/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">2nd</a>

```sql
SELECT p.product_name, s.year, s.price  
FROM Sales s  
JOIN Product p  
ON s.product_id = p.product_id;
```
`ON`은 두 테이블에 동일한 컬럼명이 없어도 사용 가능하고 join 조건을 다양하게 설정할 수 있다. 