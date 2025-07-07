---
excerpt: "'LeetCode: Game Play Analysis I' 풀이 정리"
title: "\0511. Game Play Analysis I"
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
data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})
```
<br>

Table: `Activity`
<pre>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key    
(combination of columns with unique values) of this table.   
This table shows the activity of players of some games.   
Each row is a record of a player
who logged in and played a number of games (possibly 0)
before logging out on someday using some device.   
</pre>

Write a solution to find the **first login date** for each player.

Return the result table in **any order**.

The result format is in the following example.   
<br>

**Example 1:**

- Input:
    <pre>
    Activity table:
    +-----------+-----------+------------+--------------+
    | player_id | device_id | event_date | games_played |
    +-----------+-----------+------------+--------------+
    | 1         | 2         | 2016-03-01 | 5            |
    | 1         | 2         | 2016-05-02 | 6            |
    | 2         | 3         | 2017-06-25 | 1            |
    | 3         | 1         | 2016-03-02 | 0            |
    | 3         | 4         | 2018-07-03 | 5            |
    +-----------+-----------+------------+--------------+
    </pre>
- Output:
    <pre>
    +-----------+-------------+
    | player_id | first_login |
    +-----------+-------------+
    | 1         | 2016-03-01  |
    | 2         | 2017-06-25  |
    | 3         | 2016-03-02  |
    +-----------+-------------+
    </pre>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # player_id를 기준으로 그룹화하고, 각 그룹에서 event_date 값이 가장 작은 행 선택
    filter_first_lg = activity.groupby(by="player_id", as_index=False)["event_date"].min()

    # 행 이름 변경
    filter_first_lg.rename(columns={"event_date": "first_login"}, inplace=True)

    return filter_first_lg
```
<i class="fa-solid fa-clock"></i> Runtime: **277** ms \| Beats **85.82%**    
<i class="fa-solid fa-memory"></i> Memory: **67.47** MB \| Beats **98.74%**

`groupby()`와 `min()`을 사용해서 필터링했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/game-play-analysis-i/solutions/6927393/two-different-pandas-code-to-solve-this-gsu2q/" target="_blank">1st</a>

```python
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # 방법 1
    df = activity.groupby('player_id')['event_date'].min().reset_index().rename(columns={'event_date':'first_login'})

    # 방법 2
    df = activity.pivot_table(index='player_id',values='event_date',aggfunc='min').reset_index().rename(columns={'event_date':'first_login'})

    return df
```
`pivot_table()`로도 필터링할 수 있다.

### <a href="https://leetcode.com/problems/game-play-analysis-i/solutions/6667894/beginner-friendly-unlock-first-login-tra-9ih8/" target="_blank">2nd</a>

```sql
SELECT player_id, MIN(event_date) AS first_login  -- 3. 각 플레이어의 최소 날짜를 구하고 열이름 변경
FROM Activity                                     -- 1. 데이터가 있는 테이블에서
GROUP BY player_id;                               -- 2. 플레이어 id별로 그룹화
```