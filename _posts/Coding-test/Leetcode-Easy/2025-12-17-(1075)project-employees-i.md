---
excerpt: "'LeetCode: Project Employees I' 풀이 정리"
title: "\01075. Project Employees I"
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
data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})
```
<br>

Table: `Project`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
</pre>

Table: `Employee`
<pre>
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.
</pre>

Write an SQL query that reports the **average** experience years of all the employees for each project, **rounded to 2 digits**.

Return the result table in **any order**.

The query result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    Project table:
    +-------------+-------------+
    | project_id  | employee_id |
    +-------------+-------------+
    | 1           | 1           |
    | 1           | 2           |
    | 1           | 3           |
    | 2           | 1           |
    | 2           | 4           |
    +-------------+-------------+
    Employee table:
    +-------------+--------+------------------+
    | employee_id | name   | experience_years |
    +-------------+--------+------------------+
    | 1           | Khaled | 3                |
    | 2           | Ali    | 2                |
    | 3           | John   | 1                |
    | 4           | Doe    | 2                |
    +-------------+--------+------------------+
    </pre>
- Output:    
    <pre>
    +-------------+---------------+
    | project_id  | average_years |
    +-------------+---------------+
    | 1           | 2.00          |
    | 2           | 2.50          |
    +-------------+---------------+
    </pre>
- Explanation: The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # project df 기준으로 병합
    merged = project.merge(employee, on='employee_id')

    # project_id 기준으로 그룹화 후 experience_years 열로 평균 계산
    grouped = merged.groupby('project_id', as_index=False)['experience_years'].mean().round(2)

    return grouped.rename(columns={'experience_years': 'average_years'})
```
<i class="fa-solid fa-clock"></i> Runtime: **279** ms \| Beats **71.16%**    
<i class="fa-solid fa-memory"></i> Memory: **68.79** MB \| Beats **68.39%**    

groupby()와 mean(), round()를 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/project-employees-i/solutions/3876372/beats-100-memory-easy-mysql-solution-rou-6i71/" target="_blank">1st</a>

```sql
SELECT p.project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM Project p 
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id
```
MySQL에서도 employee_id를 기준으로 테이블을 JOIN해야 한다.