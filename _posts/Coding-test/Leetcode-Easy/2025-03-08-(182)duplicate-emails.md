---
excerpt: "'LeetCode: Duplicate Emails' 풀이 정리"
title: "\0182. Duplicate Emails"
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
data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})
```
<br>

Table: `Person`
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.    
Each row of this table contains an email.
The emails will not contain uppercase letters.
</pre>

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in **any order**.

The result format is in the following example.      
<br>

**Example 1:**

- Input:   
    <pre> 
    Person table:
    +----+---------+
    | id | email   |
    +----+---------+
    | 1  | a@b.com |
    | 2  | c@d.com |
    | 3  | a@b.com |
    +----+---------+
    </pre>
- Output:  
    <pre>
    +---------+
    | Email   |
    +---------+
    | a@b.com |
    +---------+
    </pre>
- Explanation: a@b.com is repeated two times.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # email 행 이름 변경
    person.rename(columns={"email": "Email"}, inplace=True)

    # 고유한 email 제거 및 중복 email은 첫 번째만 남기고 제거
    email_filtered = person[person.duplicated(subset=["Email"], keep=False)].drop_duplicates(subset=["Email"], keep="first")

    # id 열 제거
    email_filtered.drop(columns=["id"], inplace=True)
    
    return email_filtered
```
<i class="fa-solid fa-clock"></i> Runtime: **431** ms \| Beats **62.94%**    
<i class="fa-solid fa-memory"></i> Memory: **66.17** MB \| Beats **88.33%**

먼저 `.duplicated()`에 `keep=False`로 중복되지 않은 이메일만 False로 만들어서 없앤 후, `.drop_duplicates()`에 `keep="first"`로 중복 이메일의 첫 번째만 남기고 모두 지우는 방식으로 해결했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/duplicate-emails/solutions/6236441/mssqloraclepythondata-identifying-duplic-8hzi/" target="_blank">1st</a>

```python
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    """
    This function identifies duplicate email addresses in a given DataFrame.
    
    Parameters:
    - person: A pandas DataFrame containing at least one column named 'email'.

    Returns:
    - A DataFrame containing unique duplicate email addresses.
    """
    
    # Use `duplicated` to find rows where the 'email' value is duplicated.
    # `duplicated('email')` returns True for rows where 'email' has already appeared earlier in the DataFrame.
    # `loc` filters only those rows where `duplicated` evaluates to True.
    duplicate_rows = person.loc[person.duplicated('email') == True]
    
    # Select the 'email' column and drop duplicate email entries to ensure unique duplicates are listed.
    result = duplicate_rows[['email']].drop_duplicates(keep='first')
    
    return result
```

### <a href="" target="_blank">2nd</a>

```sql
# 1
SELECT email from Person  
group by email              -- 이메일을 기준으로 그룹화
having count(email) > 1;    -- 그룹화된 데이터 중 이메일이 두 번 이상 나타나는 경우만 선택

# 2.
SELECT DISTINCT(p1.email) from Person p1, Person p2 -- 테이블을 자기 자신과 조인 / DISTINCT로 중복 제거
where p1.id <> p2.id AND p1.email = p2.email;       -- 자기 자신과 비교시 id가 다르게 조건 추가 후
                                                    -- 이메일이 같은 두 사람 찾기

# 3. 
SELECT DISTINCT(p1.email) from 
Person p1 JOIN Person p2 ON
p1.email = p2.email AND p1.id <> p2.id;
```
