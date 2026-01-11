---
excerpt: "'LeetCode: User Activity for the Past 30 Days I' 풀이 정리"
title: "\01141. User Activity for the Past 30 Days I"
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
data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'], [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']]
activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype({'user_id':'Int64', 'session_id':'Int64', 'activity_date':'datetime64[ns]', 'activity_type':'object'})
```
<br>

Table: `Activity`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows.
The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.
</pre>

Write a solution to find the daily active user count for a period of `30` days ending `2019-07-27` inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in **any order**.

The result format is in the following example.

Note: **Any** activity from (`'open_session'`, `'end_session'`, `'scroll_down'`, `'send_message'`) will be considered valid activity for a user to be considered active on a day.

**Example 1:**

- Input:    
    <pre>
    Activity table:
    +---------+------------+---------------+---------------+
    | user_id | session_id | activity_date | activity_type |
    +---------+------------+---------------+---------------+
    | 1       | 1          | 2019-07-20    | open_session  |
    | 1       | 1          | 2019-07-20    | scroll_down   |
    | 1       | 1          | 2019-07-20    | end_session   |
    | 2       | 4          | 2019-07-20    | open_session  |
    | 2       | 4          | 2019-07-21    | send_message  |
    | 2       | 4          | 2019-07-21    | end_session   |
    | 3       | 2          | 2019-07-21    | open_session  |
    | 3       | 2          | 2019-07-21    | send_message  |
    | 3       | 2          | 2019-07-21    | end_session   |
    | 4       | 3          | 2019-06-25    | open_session  |
    | 4       | 3          | 2019-06-25    | end_session   |
    +---------+------------+---------------+---------------+
    </pre>
- Output:    
    <pre>
    +------------+--------------+ 
    | day        | active_users |
    +------------+--------------+ 
    | 2019-07-20 | 2            |
    | 2019-07-21 | 2            |
    +------------+--------------+
    </pre>
- Explanation: Note that we do not care about days with zero active users.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # datetime 타입으로 변경 및 시작-끝 날짜 계산
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    end_day = pd.to_datetime('2019-07-27')
    start_day = end_day - pd.Timedelta(days=29)

    # 날짜 필터링
    activity = activity.loc[
        (activity['activity_date'] >= start_day) & (activity['activity_date'] <= end_day)
    ]

    # 그룹화 및 중복 제거
    df = (
        activity
        .groupby('activity_date')['user_id']
        .nunique()
        .reset_index(name='active_users')
        .rename(columns={'activity_date': 'day'})
    )

    return df
```
<i class="fa-solid fa-clock"></i> Runtime: **288** ms \| Beats **90.39%**    
<i class="fa-solid fa-memory"></i> Memory: **68.85** MB \| Beats **9.93%**    

날짜 계산을 용이하게 하기 위해 activity_date를 datetime 타입으로 변경했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/user-activity-for-the-past-30-days-i/solutions/6403426/easy-and-simple-solution-by-mayankluthya-uhyh/" target="_blank">1st</a>

```sql
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;
```
하루 단위로 그룹화한 뒤, COUNT와 DISTINCT로 하루 동안 활동한 (중복 없는)유저 수를 구할 수 있다.