---
excerpt: "'LeetCode: Sales Analysis III' 풀이 정리"
title: "\01084. Sales Analysis III"
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
data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype({'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})
data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype({'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})
```
<br>

Table: `Product`
<pre>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
</pre>

Table: `Sales`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
</pre>

Write a solution to report the **products** that were **only** sold in the first quarter of `2019`. That is, between `2019-01-01` and `2019-03-31` inclusive.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Product table:
    +------------+--------------+------------+
    | product_id | product_name | unit_price |
    +------------+--------------+------------+
    | 1          | S8           | 1000       |
    | 2          | G4           | 800        |
    | 3          | iPhone       | 1400       |
    +------------+--------------+------------+
    Sales table:
    +-----------+------------+----------+------------+----------+-------+
    | seller_id | product_id | buyer_id | sale_date  | quantity | price |
    +-----------+------------+----------+------------+----------+-------+
    | 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
    | 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
    | 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
    | 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
    +-----------+------------+----------+------------+----------+-------+
    </pre>
- Output:    
    <pre>
    +-------------+--------------+
    | product_id  | product_name |
    +-------------+--------------+
    | 1           | S8           |
    +-------------+--------------+
    </pre>
- Explanation:      
The product with id 1 was only sold in the spring of 2019.     
The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.    
The product with id 3 was sold after spring 2019.    
We return only product 1 as it is the product that was only sold in the spring of 2019. 

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # 1. product와 sales를 product_id 열 기준으로 병합
    merged = product.merge(sales, on='product_id')

    # 2. sale_date를 datetime 타입으로 변환
    merged['sale_date'] = pd.to_datetime(merged['sale_date'])

    # 3. 상품별 최초 판매일 / 마지막 판매일 계산
    period = merged.groupby('product_id')['sale_date'].agg(min_date='min', max_date='max')

    # 4. 판매 기간이 전부 2019년 1분기 안에 있는 상품만 선택
    valid_products = period[
        (period['min_date'] >= '2019-01-01') & (period['max_date'] <= '2019-03-31')
    ].index

    # 5. 상품 테이블에서 해당 상품만 리포트
    result = product.loc[ product['product_id'].isin(valid_products), ['product_id', 'product_name'] ]

    return result
```
<i class="fa-solid fa-clock"></i> Runtime: **348** ms \| Beats **79.47%**    
<i class="fa-solid fa-memory"></i> Memory: **70.42** MB \| Beats **18.98%**    

두 테이블을 먼저 merge하는 방법은 효율이 떨어졌다. Sales 테이블에서 먼저 `product_id`를 기준으로 groupby()하고 `sale_date`가 조건에 맞는 상품만 찾은 뒤, 해당 상품만 Product에서 찾는 방법이 훨씬 빠르다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/sales-analysis-iii/solutions/3952868/easy-pandas-sollution-beats-99-by-grzego-pvmg/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # Group the 'sales' DataFrame by 'product_id' and calculate the minimum and maximum sale dates for each product
    sales = sales.groupby('product_id')['sale_date'].agg(['min', 'max']).reset_index()
    
    # Filter the sales data to include only records with sale dates between January 1, 2019, and March 31, 2019
    sales = sales[(sales['min'] >= '2019-01-01') & (sales['max'] <= '2019-03-31')]
    
    # Merge the filtered sales data with the 'product' DataFrame based on 'product_id', keeping only 'product_id' and 'product_name' columns
    result = pd.merge(sales, product, on='product_id', how='inner')[['product_id', 'product_name']]
    
    # Return the resulting DataFrame
    return result
```
날짜를 datetime으로 바꾸지 않아도 리트코드의 테스트 데이터가 `YYYY-MM-DD`으로 깨끗하게 통일되어 있기 때문에 문제없이 통과되는 것 같다.

### <a href="https://leetcode.com/problems/sales-analysis-iii/solutions/7347886/very-simple-sol-with-logic-explaination-tqkfn/" target="_blank">2nd</a>

```sql
SELECT p.product_id ,p.product_name
FROM product p
JOIN sales s
    ON p.product_id=s.product_id
GROUP BY p.product_id,p.product_name
HAVING MIN(s.sale_date)>= '2019-01-01' AND MAX(s.sale_date)<= '2019-03-31'
```
GROUP BY + HAVING을 사용한 쿼리다.