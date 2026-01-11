---
excerpt: "'LeetCode: Customers Who Never Order' 풀이 정리"
title: "\0183. Customers Who Never Order"
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
data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
```
<br>

Table: `Customers`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.    
Each row of this table indicates the ID and name of a customer.   
</pre>

Table: `Orders`
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.   
customerId is a foreign key (reference columns) of the ID from the Customers table.   
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.   
</pre>

Write a solution to find all customers who never order anything.

Return the result table in **any order**.

The result format is in the following example.   
<br>

**Example 1:**

- Input: 
    <pre>
    Customers table:
    +----+-------+
    | id | name  |
    +----+-------+
    | 1  | Joe   |
    | 2  | Henry |
    | 3  | Sam   |
    | 4  | Max   |
    +----+-------+
    
    Orders table:
    +----+------------+
    | id | customerId |
    +----+------------+
    | 1  | 3          |
    | 2  | 1          |
    +----+------------+
    </pre>
- Output: 
    <pre>
    +-----------+
    | Customers |
    +-----------+
    | Henry     |
    | Max       |
    +-----------+
    </pre>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # customers["id"] = [1, 2, 3, 4]의 값들이 orders["customerId"] = [3, 1] 에 없으면(~ 적용) True
    customer_no_order = customers[~customers["id"].isin(orders["customerId"])]

    # name 열 이름 변경
    customer_no_order.rename(columns={"name": "Customers"}, inplace=True)

    # id 열 제거
    customer_no_order.drop(columns="id", inplace=True)

    return customer_no_order
```
<i class="fa-solid fa-clock"></i> Runtime: **338** ms \| Beats **86.20%**    
<i class="fa-solid fa-memory"></i> Memory: **67.02** MB \| Beats **52.65%**

Pandas의 <mark>.isin()</mark>으로 필터링했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/customers-who-never-order/solutions/3848456/easy-pandas-2-methods-with-detailed-expl-4esq/" target="_blank">1st</a>

```python
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the customers DataFrame with the orders DataFrame using a left join on 'id' and 'customerId'
    merged_df = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    
    # Use the 'customerId' column to create a boolean mask for customers who never placed any orders
    mask = merged_df['customerId'].isna()
    
    # Filter the rows using the boolean mask
    result_df = merged_df[mask]
    
    # Select only the 'name' column from the result DataFrame and rename it as 'Customers'
    result_df = result_df[['name']].rename(columns={'name': 'Customers'})
    
    return result_df
```
Pandas의 merge로 푸는 방법도 참고했다. 위와 반대로 <mark>.isna()</mark>로 NaN값을 찾는다. 참고로 rename에서 필요한 행만 선택해서 데이터프레임을 만들면 drop을 따로 쓸 필요가 없는 것을 알게 됐다.

### <a href="" target="_blank">2nd</a>

```sql
SELECT name as Customers  -- 3. 결과 출력(name 행 이름 변경)
from Customers
where id not in (         -- 2. customers에서 id가 orders.customerId에 없는 행 필터링
    select customerId     -- 1. orders에서 customerId 행 가져오기
    from Orders
);
```