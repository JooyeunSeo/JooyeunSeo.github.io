---
excerpt: "'LeetCode-Combine Two Tables' 풀이 정리"
title: "\0175. Combine Two Tables"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Pandas
  - MySQL
---

## <i class="fa-solid fa-file-lines"></i> Description

**Pandas Schema**
```python
data = [[1, 'Wang', 'Allen'],
        [2, 'Alice', 'Bob']]
person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
data = [[1, 2, 'New York City', 'New York'],
        [2, 3, 'Leetcode', 'California']]
address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})
```
<br>

Table: `Person`
<pre>
+-------------+---------+    
| Column Name | Type    |    
+-------------+---------+    
| personId    | int     |    
| lastName    | varchar |    
| firstName   | varchar |    
+-------------+---------+
</pre>
personId is the primary key (column with unique values) for this table.    
This table contains information about the ID of some persons and their first and last names.   
<br>

Table: `Address`  
<pre>
+-------------+---------+    
| Column Name | Type    |    
+-------------+---------+    
| addressId   | int     |    
| personId    | int     |    
| city        | varchar |    
| state       | varchar |    
+-------------+---------+ 
</pre>
addressId is the primary key (column with unique values) for this table.    
Each row of this table contains information about the city and state of one person with ID = PersonId.     
<br>

Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

**Example 1:**

- Input:    
    <pre>
    Person table:    
    +----------+----------+-----------+ 
    | personId | lastName | firstName | 
    +----------+----------+-----------+ 
    | 1        | Wang     | Allen     | 
    | 2        | Alice    | Bob       | 
    +----------+----------+-----------+ 
     
    Address table:    
    +-----------+----------+---------------+------------+ 
    | addressId | personId | city          | state      | 
    +-----------+----------+---------------+------------+ 
    | 1         | 2        | New York City | New York   | 
    | 2         | 3        | Leetcode      | California | 
    +-----------+----------+---------------+------------+
    </pre>  
- Output:   
    <pre>  
    +-----------+----------+---------------+----------+    
    | firstName | lastName | city          | state    |    
    +-----------+----------+---------------+----------+    
    | Allen     | Wang     | Null          | Null     |    
    | Bob       | Alice    | New York City | New York |    
    +-----------+----------+---------------+----------+    
    </pre>  
- Explanation:   
There is no address in the address table for the personId = 1 so we return null in their city and state.   
addressId = 1 contains information about the address of personId = 2.   


## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # address에서 addressId를 미리 생략
    address_filtered = address[['personId', 'city', 'state']]
    
    # personId를 기준으로 머지
    merged_df = person.merge(address_filtered, on="personId", how="left")
    
    # personId 열을 제거하고 lastName과 firstName 순서 재배치
    merged_df.drop(columns="personId", inplace=True)
    merged_df = merged_df[['firstName', 'lastName', 'city', 'state']]
    
    return merged_df
```
<i class="fa-solid fa-clock"></i> Runtime: **485** ms \| Beats **47.55%**    
<i class="fa-solid fa-memory"></i> Memory: **67.85** MB \| Beats **59.87%**

SQL은 잘 몰라서 Pandas의 <mark>merge</mark>로 풀었다. how 파라미터를 left 또는 right로 설정해줘야 일치하는 값이 없는 행이 제거되지 않고 null 값이 들어가게 된다. 또 두 테이블을 바로 병합하는 것보다 병합에 필요없는 행을 미리 제거하는 것이 훨씬 빨랐다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/combine-two-tables/solutions/6228473/mssql-oracle-pythondata-joining-person-and-address-data-with-sql-simple-solution/" target="_blank">1st</a>

```python
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    # Perform a left join on personId
    # This merges the 'person' and 'address' DataFrames using a left join on the 'personId' column.
    # Left Join: Includes all rows from the 'person' DataFrame and the matching rows from the 'address' DataFrame.
    # If there is no match, the result will contain NaN for columns from the 'address' DataFrame.
    merged = pd.merge(person, address, how='left', on='personId')

    # Select and reorder the required columns
    # This selects the columns 'firstName', 'lastName', 'city', and 'state' from the merged DataFrame.
    # The 'copy()' method is used to create a copy of the selected columns to avoid modifying the original DataFrame.
    res = merged[['firstName', 'lastName', 'city', 'state']].copy()

    # Return the resulting DataFrame
    return res 
```
Pandas의 merge를 이용했지만 조금 다른 방식으로 푼 답안도 참고했다. 병합 후 필요없는 행을 <mark>drop</mark>하는 대신 원하는 행만 순서대로 재배치한 후 복사본을 반환했다.

### <a href="https://leetcode.com/problems/combine-two-tables/solutions/2593063/2-ways-to-write-the-same-query-using-lef-zmfk/" target="_blank">2nd</a>

```sql
SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P LEFT JOIN Address A
on P.personId = A.personId
```

```sql
SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A USING (personId)
```
MySQL로 푸는 것이 더 빠른 것 같아서 참고했다. Pandas의 merge에서 how 파라미터를 left로 설정한 것과 비슷하게 personId를 기준으로 `LEFT JOIN`하는 것이 포인트다.   
첫 번째 쿼리는 <mark>ON</mark> 조건을 사용하여 P.personId와 A.personId가 일치하는 경우에만 Address 테이블의 데이터를 가져오는 방식이다.   
두 번째 쿼리는 <mark>USING</mark> 문법을 사용하여 personId(동일한 열 이름)를 기준으로 조인한다.