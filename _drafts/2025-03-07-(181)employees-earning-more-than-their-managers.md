---
excerpt: "'LeetCode-Employees Earning More Than Their Managers' 풀이 정리"
title: "\0181. Employees Earning More Than Their Managers"
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
data = [[1, 'Joe', 70000, 3],
        [2, 'Henry', 80000, 4],
        [3, 'Sam', 60000, None],
        [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
```
<br>

Table: `Employee`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
</pre>
id is the primary key (column with unique values) for this table.     
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
<br>

Write a solution to find the employees who earn more than their managers.   
Return the result table in **any order**.   
The result format is in the following example.   

**Example 1:**

- Input:   
    <pre> 
    +----+-------+--------+-----------+
    | id | name  | salary | managerId |
    +----+-------+--------+-----------+
    | 1  | Joe   | 70000  | 3         |
    | 2  | Henry | 80000  | 4         |
    | 3  | Sam   | 60000  | Null      |
    | 4  | Max   | 90000  | Null      |
    +----+-------+--------+-----------+
    </pre>
- Output:  
    <pre>
    +----------+
    | Employee |
    +----------+
    | Joe      |
    +----------+
    </pre>
- Explanation: Joe is the only employee who earns more than his manager.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python

```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **0**    
<i class="fa-solid fa-memory"></i> Memory: **0** MB \| Beats **0**


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python

```
<i class="fa-solid fa-clock"></i> **time complexity:**     
<i class="fa-solid fa-memory"></i> **space complexity:**            

### <a href="" target="_blank">2nd</a>

```python

```
<i class="fa-solid fa-clock"></i> **time complexity:**             
<i class="fa-solid fa-memory"></i> **space complexity:**     



{: style="color: blue;"}
{: style="color: green;"}

𝑂(𝑛)
𝑂(𝑛<sup>2</sup>)
𝑂(log𝑛)
𝑚
𝑥