---
excerpt: "'LeetCode: Delete Duplicate Emails' 풀이 정리"
title: "\0196. Delete Duplicate Emails"
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
data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})
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
</pre>
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
<br>


Write a solution to **delete** all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a `DELETE` statement and not a `SELECT` one.
For Pandas users, please note that you are supposed to modify `Person` in place.

After running your script, the answer shown is the `Person` table. The driver will first compile and run your piece of code and then show the `Person` table. The final order of the `Person` table **does not matter**.

The result format is in the following example.

**Example 1:**

- Input:   
    <pre> 
    Person table:
    +----+------------------+
    | id | email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    | 3  | john@example.com |
    +----+------------------+
    </pre>
- Output:  
    <pre>
    +----+------------------+
    | id | email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    +----+------------------+
    </pre>
- Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # id를 오름차순으로 정렬
    person.sort_values(by="id", inplace=True)
    
    # 중복값 중 첫 번째만 남기고 모두 삭제
    person.drop_duplicates(subset="email", keep="first", inplace=True)
```
<i class="fa-solid fa-clock"></i> Runtime: **366** ms \| Beats **71.54%**    
<i class="fa-solid fa-memory"></i> Memory: **67.33** MB \| Beats **10.74%**

판다스의 <mark>drop_duplicates</mark>을 쓰면 간단하게 풀 수 있다. 다만 id 값의 순서가 1부터 시작하지 않는 예시에 이대로 적용하면 id 값이 더 큰 행이 남게 되는데 그럴 경우 통과가 되지 않았다. 그래서 먼저 id 열을 순서대로 정렬해야 했다.   
또 새로운 데이터프레임을 반환하지 말고 Person 데이터프레임 자체를 직접 수정해야 한다는 조건이 있기 때문에 `inplace=True` 옵션을 사용해야 한다. 이번에 알게 된 사실은 함수에 이 옵션을 사용한 값을 return하면 `None`을 반환한다는 것이다. 그래서 return하면 오히려 에러가 나게 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/delete-duplicate-emails/solutions/6317652/easy-solution-by-mayankluthyagi-0gpt/" target="_blank">1st</a>

```sql
DELETE p FROM Person p                  -- 마지막으로 p 지우기
JOIN Person p2                          -- Person에서 자기 자신을 조인
ON p.Email = p2.Email AND p.Id > p2.Id; -- 같은 이메일을 가진 행끼리 서로 연결시키고 그 중 p의 id가 더 큰 행만 남기기
```
SQL의 경우 `SELECT`를 사용하지 않는다는 조건이 있어서 JOIN과 DELETE로 푸는 것 같다.

### <a href="https://leetcode.com/problems/delete-duplicate-emails/solutions/2627589/my-sql-solution-by-_himanshu_12-cy0p/" target="_blank">2nd</a>

```sql
delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;  -- on 대신 where 사용
```
위의 솔루션과 비슷하지만 JOIN과 DELETE의 과정이 잘 설명되어있어서 참고했다.
<pre>
Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

=> From Person p1, Person p2 : it would look like:
1|john@example.com|1|john@example.com
1|john@example.com|2|bob@example.com 
1|john@example.com|3|john@example.com

2|bob@example.com|1|john@example.com
2|bob@example.com|2|bob@example.com
2|bob@example.com|3|john@example.com

3|john@example.com|1|john@example.com
3|john@example.com|2|bob@example.com
3|john@example.com|3|john@example.com

=> From Person p1, Person p2 where p1.email=p2.email and p1.id>p2.id:
It would look like:
3|john@example.com|1|john@example.com

Now delete this row's matching row in p1 using p1:  delete p1
</pre>