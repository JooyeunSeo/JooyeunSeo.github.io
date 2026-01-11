---
excerpt: "'LeetCode: Employee Bonus' 풀이 정리"
title: "\0577. Employee Bonus"
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
data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype({'empId':'Int64', 'name':'object', 'supervisor':'Int64', 'salary':'Int64'})
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId':'Int64', 'bonus':'Int64'})
```
<br>

Table: `Employee`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee
in addition to their salary and the id of their manager.
</pre>

Table: `Bonus`
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.
</pre>

Write a solution to report the name and bonus amount of each employee with a bonus **less than** `1000`.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

- Input:
    <pre>
    Employee table:
    +-------+--------+------------+--------+
    | empId | name   | supervisor | salary |
    +-------+--------+------------+--------+
    | 3     | Brad   | null       | 4000   |
    | 1     | John   | 3          | 1000   |
    | 2     | Dan    | 3          | 2000   |
    | 4     | Thomas | 3          | 4000   |
    +-------+--------+------------+--------+
    Bonus table:
    +-------+-------+
    | empId | bonus |
    +-------+-------+
    | 2     | 500   |
    | 4     | 2000  |
    +-------+-------+
    </pre>
- Output:
    <pre>
    +------+-------+
    | name | bonus |
    +------+-------+
    | Brad | null  |
    | John | null  |
    | Dan  | 500   |
    +------+-------+
    </pre>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">If the EmpId in table Employee has no match in table Bonus, we consider that the corresponding bonus is null and null is smaller than 1000.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Inner join is the default join, we can solve the mismatching problem by using outer join.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # empId 열을 기준으로 두 데이터프레임 병합, Bonus에서 매칭되는 값 없으면 NaN으로 채우기
    merged_df = employee.merge(bonus, on="empId", how="left")

    # 보너스가 1000 이하인 행만 필터링(NaN 값은 0으로 조정)
    bonus_under_1000 = merged_df.loc[merged_df['bonus'].fillna(0) < 1000]

    # 필요없는 열 삭제
    bonus_under_1000.drop(columns=["empId", "supervisor", "salary"], inplace=True)

    return bonus_under_1000
```
<i class="fa-solid fa-clock"></i> Runtime: **322** ms \| Beats **81.32%**    
<i class="fa-solid fa-memory"></i> Memory: **68.33** MB \| Beats **73.77%**

**NaN** 값을 0으로 바꾸는 방법으로 보너스가 1000 이하인 행만 필터링했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/employee-bonus/solutions/5652487/pandas-100-working-solution/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join on the 'empId' column
    merged_df = pd.merge(employee, bonus, on='empId', how='left')
    
    # Filter rows where bonus is less than 1000 or is NaN
    result = merged_df[(merged_df['bonus'] < 1000) | (merged_df['bonus'].isna())]
    
    # Select only the 'name' and 'bonus' columns
    return result[['name', 'bonus']]    
```
`|` 연산자로 보너스가 1000 이하거나 **NaN** 값인 행을 필터링하는 방법도 있다. 또 필요없는 열을 <mark>drop()</mark>하는 대신 필요한 행만 포함해서 리턴해도 된다.

### <a href="https://leetcode.com/problems/employee-bonus/solutions/6984729/employee-bonus-by-saktheesh_a-5es1/" target="_blank">2nd</a>

```sql
SELECT e.name,b.bonus                 -- 4. 필요한 열만 선택
FROM employee e                       -- 1. employee 테이블을 기본으로 설정(별칭 e)
left join bonus b                     -- 2. employee에 bonus 테이블을 붙임
on e.empId=b.empId                    --    (empId가 일치하는 값만, bonus에 empId가 없으면 NULL)
where bonus<1000 or b.bonus is NULL   -- 3. 두 조건 중 하나에 일치하는 값만 선택
```
SQL의 `LEFT JOIN`이 Pandas의 merge에 대응된다.
