---
excerpt: "'LeetCode: Average Selling Price' 풀이 정리"
title: "\01251. Average Selling Price"
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
data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})
```
<br>

Table: `Prices`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
</pre>

Table: `UnitsSold`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 
</pre>

Write a solution to find the average selling price for each product. `average_price` should be **rounded to 2 decimal places**. If a product does not have any sold units, its average selling price is assumed to be 0.

Return the result table in any order.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Prices table:
    +------------+------------+------------+--------+
    | product_id | start_date | end_date   | price  |
    +------------+------------+------------+--------+
    | 1          | 2019-02-17 | 2019-02-28 | 5      |
    | 1          | 2019-03-01 | 2019-03-22 | 20     |
    | 2          | 2019-02-01 | 2019-02-20 | 15     |
    | 2          | 2019-02-21 | 2019-03-31 | 30     |
    +------------+------------+------------+--------+
    UnitsSold table:
    +------------+---------------+-------+
    | product_id | purchase_date | units |
    +------------+---------------+-------+
    | 1          | 2019-02-25    | 100   |
    | 1          | 2019-03-01    | 15    |
    | 2          | 2019-02-10    | 200   |
    | 2          | 2019-03-22    | 30    |
    +------------+---------------+-------+
    </pre>
- Output:    
    <pre>
    +------------+---------------+
    | product_id | average_price |
    +------------+---------------+
    | 1          | 6.96          |
    | 2          | 16.96         |
    +------------+---------------+
    </pre>
- Explanation:         
Average selling price = Total Price of Product / Number of products sold.     
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96      
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # 테이블 join
    df = prices.merge(units_sold, on='product_id', how='left')

    # purchase_date가 실제 판매기간에 속하는 행만 필터링
    df = df.loc[ (df.purchase_date >= df.start_date) & (df.purchase_date <= df.end_date) ]

    # 해당 일자의 총 판매 액수 계산
    df['total_price'] = df.price * df.units

    # id 기준으로 그룹으로 묶은 뒤 average_price 계산을 위한 값 계산
    avg = (
        df.groupby('product_id')
        .agg(total_revenue=('total_price', 'sum'), total_units=('units', 'sum'))
    )

    # average_price 계산
    avg['average_price'] = ( avg['total_revenue'] / avg['total_units'] ).round(2)

    # 판매 기록 없는 id의 average_price 값을 0으로 처리
    result = (
        avg[['average_price']].reindex(prices['product_id'].unique()).fillna(0).reset_index()
    )

    return result
```
<i class="fa-solid fa-clock"></i> Runtime: **395** ms \| Beats **57.73%**    
<i class="fa-solid fa-memory"></i> Memory: **68.63** MB \| Beats **62.04%**    

UnitsSold에 판매 기록이 없는 product_id는 groupby할 때 아예 등장하지 않는 문제가 생긴다. 이럴 때 `reindex()`로 인덱스를 새로 덮어씌우면 값이 없는 경우 NaN로 채울 수 있다. `unique()`는 product_id가 여러 개이기 때문에 중복을 거르기 위해 필요하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```sql
SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
   u.purchase_date BETWEEN start_date AND end_date
group by product_id
```
Prices 테이블 기준으로 `LEFT JOIN`하면 Prices에 있는 모든 상품을 판매 기록에 상관 없이 무조건 결과에 포함시킬 수 있다.     
한편 `ON` 절의 두번째 조건을 WHERE 절에 쓰면 안 되는 이유는 해당 가격이 유효한 기간에 발생한 판매만 매칭하기 때문이다. 이는 LEFT JOIN을 INNER JOIN처럼 동작하게 만들어 판매 기록이 없는 상품이 사라지게 한다.