---
excerpt: "'LeetCode: Employees Earning More Than Their Managers' 풀이 정리"
title: "\0181. Employees Earning More Than Their Managers"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Pandas
  - SQL
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
id is the primary key (column with unique values) for this table.     
Each row of this table indicates
the ID of an employee, their name, salary, and the ID of their manager.
</pre>

Write a solution to find the employees who earn more than their managers.

Return the result table in **any order**.

The result format is in the following example.      
<br>

**Example 1:**

- Input:   
    <pre> 
    Employee table:
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
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee.rename(columns={"name": "Employee"}, inplace=True)
    
    # id를 key로, salary를 value로 하는 딕셔너리 생성
    id_to_salary = employee.set_index('id')['salary'].to_dict()
    
    # map을 사용해 각 행의 managerId에 해당하는 매니저의 salary 가져오기
    employee['managerSalary'] = employee['managerId'].map(id_to_salary)
    
    # 매니저 salary가 존재하고 자신의 salary가 더 높은 직원 선택
    employee_filtered = employee.loc[
        (employee['managerSalary'].notna()) & (employee['salary'] > employee['managerSalary']),
        ['Employee']
    ]
    return employee_filtered
```
<i class="fa-solid fa-clock"></i> Runtime: **392** ms \| Beats **80.72%**    
<i class="fa-solid fa-memory"></i> Memory: **67.62** MB \| Beats **70.68%**

id를 인덱스로 설정한 뒤, 딕셔너리에 id와 salary를 저장하고 map을 이용해 해당하는 값을 가져오는 방식이다. loc[]으로 원하는 값만 선별할 때, 'Employee' 열을 []으로 감싸야 Series가 아니라 Dataframe 타입으로 반환된다.

주의해야 할 테스트 케이스
1. managerId가 존재하지만 데이터프레임에 해당 id가 없는 경우    
2. 데이터프레임에 managerId가 없는 직원 단 한 명만 존재하는 경우
<br>

```python
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 매니저 급여를 가져오는 함수
    def get_manager_salary(manager_id):
        if pd.notna(manager_id):
            manager_salary = employee.loc[employee['id'] == manager_id, 'salary']
            return manager_salary.iloc[0] if not manager_salary.empty else None
        return None

    # name 열 이름을 Employee로 변경
    employee.rename(columns={"name": "Employee"}, inplace=True)

    # 매니저 급여를 계산한 열 추가
    employee['managerSalary'] = employee['managerId'].apply(get_manager_salary).astype('Int64')

    # 매니저보다 급여가 높은 사람을 query로 찾기
    result = employee.query('salary > managerSalary and managerSalary == managerSalary')[['Employee']]
    return result
```
<mark>query</mark>를 이용한 방법은 속도가 느렸다.


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/employees-earning-more-than-their-managers/solutions/6230576/mssql-self-join-in-sql-easy-and-detailed-72rb/" target="_blank">1st</a>

```python
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    # Merge the employee DataFrame with itself on managerId and id
    # This creates a DataFrame where each row contains data about an employee (suffix _x)
    # and their corresponding manager (suffix _y)
    merged_df = employee.merge(employee, how='left', left_on='managerId', right_on='id')
    
    # Filter the merged DataFrame to find employees whose salary is greater than their manager's salary
    # 'salary_x' refers to the employee's salary, and 'salary_y' refers to the manager's salary
    filtered_df = merged_df.query('salary_x > salary_y')
    
    # Create a new DataFrame with the names of these employees
    # 'name_x' contains the names of employees whose salary is higher than their manager's
    result_df = pd.DataFrame({'Employee': filtered_df['name_x']})
    
    return result_df

# Explanation:
# 1. The function first performs a self-join on the `employee` DataFrame to link each employee
#    with their manager using the `managerId` and `id` columns.
# 2. After the merge:
#    - The left side (employee's data) is retained as columns with a suffix `_x`.
#    - The right side (manager's data) is added as columns with a suffix `_y`.
# 3. Using the `query` method, the function filters rows where an employee's salary (`salary_x`)
#    is greater than their manager's salary (`salary_y`).
# 4. Finally, it extracts the `name_x` column (employee names) from the filtered rows
#    and returns it as a new DataFrame called `result_df`.
```
Pandas를 사용한 방법으로, 데이터베이스 자기 자신과 병합했다.

### <a href="https://leetcode.com/problems/employees-earning-more-than-their-managers/solutions/3825038/100-easy-fast-clean-solution-by-kartik_k-iq18/" target="_blank">2nd</a>

```sql
SELECT EMP.name AS Employee FROM Employee EMP,Employee MGR
WHERE EMP.managerId=MGR.id AND EMP.salary>MGR.salary
```

### <a href="" target="_blank">3rd</a>

```sql
SELECT e2.name as Employee                      -- 1. name 열 이름 변경 / 5. name 열이 어느 테이블인지 명시
FROM employee e1                                -- 2. 데이터베이스 추가
INNER JOIN employee e2 ON e1.id = e2.managerID  -- 3. INNER JOIN으로 중복 생성 후 id를 managerId에 조인
WHERE                                           -- 4. e1(매니저)와 e2(직원)의 급여 비교
e1.salary < e2.salary
```