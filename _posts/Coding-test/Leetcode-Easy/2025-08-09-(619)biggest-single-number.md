---
excerpt: "'LeetCode: Biggest Single Number' 풀이 정리"
title: "\0619. Biggest Single Number"
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
data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})
```
<br>

Table: `MyNumbers`
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates
(In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
</pre>

A **single number** is a number that appeared only once in the `MyNumbers` table.

Find the largest **single number**. If there is no **single number**, report `null`.

The result format is in the following example.

**Example 1:**

- Input:    
    <pre>
    MyNumbers table:
    +-----+
    | num |
    +-----+
    | 8   |
    | 8   |
    | 3   |
    | 3   |
    | 1   |
    | 4   |
    | 5   |
    | 6   |
    +-----+
    </pre>
- Output:    
    <pre>
    +-----+
    | num |
    +-----+
    | 6   |
    +-----+
    </pre>
- Explanation: The single numbers are 1, 4, 5, and 6.    
Since 6 is the largest single number, we return it.

**Example 2:**

- Input:    
    <pre>
    MyNumbers table:
    +-----+
    | num |
    +-----+
    | 8   |
    | 8   |
    | 7   |
    | 7   |
    | 3   |
    | 3   |
    | 3   |
    +-----+
    </pre>
- Output:    
    <pre>
    +------+
    | num  |
    +------+
    | null |
    +------+
    </pre>
- Explanation: There are no single numbers in the input table so we return null.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    singles = my_numbers.loc[my_numbers['num'].map(counts) == 1]['num']
    
    return pd.DataFrame({'num': [singles.max()]})
```
<i class="fa-solid fa-clock"></i> Runtime: **258** ms \| Beats **91.78%**    
<i class="fa-solid fa-memory"></i> Memory: **67.39** MB \| Beats **19.83%**

<mark>value_counts()</mark>로 각 번호의 빈도수를 세는 방법을 사용했다. 한 번만 등장하는 번호가 없을 경우 NaN 값을 반환해야 하기 때문에 데이터프레임을 새로 만들었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/biggest-single-number/solutions/6935531/simplest-two-lines-of-code-using-max-and-y08b/" target="_blank">1st</a>

```python
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby('num').size().reset_index(name='count')
    singles = df[df['count']==1]['num']
    return pd.DataFrame({'num':[singles.max()]})
```
<mark>groupby()</mark>, <mark>size()</mark>와 <mark>reset_index()</mark>를 사용한 방법이다. `count`라는 열을 새로 만들어서 활용했다.

### <a href="https://leetcode.com/problems/biggest-single-number/solutions/3943685/one-line-pandas-self-explaining-by-juank-tffe/" target="_blank">2nd</a>

```python
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    return my_numbers.drop_duplicates(keep = False).max().to_frame(name = 'num')
```
<mark>drop_duplicates()</mark>으로 중복값을 제거하는 방법도 있다. 남는 행이 없어서 빈 데이터프레임이 된 경우 `max()`를 하면 NaN값이 반환된다. Series 타입이 되기 때문에 여기에 다시 `to_frame()`을 사용했다.

### <a href="https://leetcode.com/problems/biggest-single-number/solutions/3811592/sql-subquery-max-easy-to-understand-by-j-uicv/" target="_blank">3rd</a>

```sql
SELECT MAX(num) AS num      -- 6. 임시 테이블에서 num의 최댓값 구하기
FROM (
    SELECT num              -- 4. num 행만 뽑기
    FROM MyNumbers          -- 1. 테이블에서 데이터 가져오기
    GROUP BY num            -- 2. num값이 같은 행끼리 그룹화
    HAVING COUNT(num) = 1   -- 3. 그룹 크기가 1인 것만 남기기
) AS unique_numbers;        -- 5. 임시 테이블 unique_numbers 생성
```
SQL에서도 GROUP BY를 사용해서 풀 수 있다.