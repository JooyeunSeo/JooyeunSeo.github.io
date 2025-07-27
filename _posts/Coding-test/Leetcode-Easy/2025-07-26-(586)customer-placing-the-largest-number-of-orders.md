---
excerpt: "'LeetCode: Customer Placing the Largest Number of Orders' 풀이 정리"
title: "\0586. Customer Placing the Largest Number of Orders"
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
data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})
```
<br>

Table: `Orders`
<pre>
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
</pre>

Write a solution to find the `customer_number` for the customer who has placed **the largest number of orders.**

The test cases are generated so that **exactly one customer** will have placed more orders than any other customer.

The result format is in the following example.

**Example 1:**

- Input:
    <pre>
    Orders table:
    +--------------+-----------------+
    | order_number | customer_number |
    +--------------+-----------------+
    | 1            | 1               |
    | 2            | 2               |
    | 3            | 3               |
    | 4            | 3               |
    +--------------+-----------------+
    </pre>
- Output:
    <pre>
    +-----------------+
    | customer_number |
    +-----------------+
    | 3               |
    +-----------------+
    </pre>
- Explanation:      
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order.      
So the result is customer_number 3.

**Follow up:** What if more than one customer has the largest number of orders, can you find all the customer_number in this case?

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">MySQL uses a different expression to get the first records other than MSSQL's TOP expression.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # 같은 customer_number 값끼리 그룹화한 후, 그룹 내에서 order_number 열의 개수 반환
    group_count = orders.groupby("customer_number", as_index=False)[["order_number"]].count()
    
    # group_count에서 order_number 열의 값이 가장 큰 행만 필터링
    max_order = group_count["order_number"].max()
    top_customers = group_count[group_count["order_number"] == max_order]
    
    # top_customers에서 필요한 행만 리턴
    return top_customers[["customer_number"]]
```
<i class="fa-solid fa-clock"></i> Runtime: **271** ms \| Beats **87.20%**    
<i class="fa-solid fa-memory"></i> Memory: **67.32** MB \| Beats **38.86%**

마지막에 customer_number행을 반환해야 하기 때문에 그룹화할 때 `as_index`를 False로 설정해서 인덱스로 넘어가지 않도록 방지했다. 그리고 order_number 열을 이중 대괄호로 선택해서 Series로 변경되지 않고 DataFrame 구조를 유지하도록 했다. 또 테스트 케이스는 최대 주문 고객이 단 1명임을 보장하지만, 만약 공동 1등이 존재할 경우에도 사용 가능하도록 만들어봤다.

<pre>
   order_number  customer_number
0             1                1
1             2                2
2             3                3
3             4                3
</pre>
{: style="color: blue;"}
<pre>
   customer_number  order_number  (← count rows in each group)
0                1             1
1                2             1
2                3             2
                  ↓
   customer_number  order_number  (← only max value)
2                3             2
</pre>

<pre>
   customer_number
2                3
</pre>
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/solutions/6958486/easy-understanding-by-madhusudhanaraghu0-5qg6/" target="_blank">1st</a>

```python
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customer_number").count().reset_index()
    df = df.sort_values(by=["order_number"],ascending=False)
    return df.iloc[:1,:1]
```
그룹화해서 각 그룹의 열 개수를 카운팅하는 것 까지는 동일한데, 그 후 내림차순으로 정렬한 후 첫번째 행과 첫 번째 열만 선택하는 방법을 사용했다.

### <a href="https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/solutions/3863257/pandas-vs-sql-elegant-short-all-30-days-vax5k/" target="_blank">2nd</a>

```python
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()
```
<mark>mode()</mark>는 groupby 후 count하고 max값을 찾는 과정 없이 최빈값을 바로 구할 수 있고, 만약 공동 1등이 있을 경우에도 모두 반환하기 때문에 편리하다. Series 형태로 반환되기 때문에 <mark>to_frame()</mark>으로 다시 변환했는데, `orders[['customer_number']].mode()`처럼 이중 대괄호를 써도 된다.

### <a href="https://chatgpt.com/c/6884a1c9-9618-8004-b805-8c5788cc10e6" target="_blank">3rd</a>

```sql
SELECT customer_number            -- 6. customer_number 열만 보여주기 
FROM Orders                       -- 1. 테이블에서 데이터 가져오기
GROUP BY customer_number          -- 2. customer_number 값을 기준으로 그룹화
ORDER BY count(*) DESC LIMIT 1;   /* 3. 각 그룹에 대해 행 개수 집계
                                     4. 집계 결과를 기준으로 내림차순
                                     5. 상단 첫 번째 행만 남기기 */ 
```