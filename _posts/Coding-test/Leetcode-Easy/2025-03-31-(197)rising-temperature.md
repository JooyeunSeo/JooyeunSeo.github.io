---
excerpt: "'LeetCode: Rising Temperature' 풀이 정리"
title: "\0197. Rising Temperature"
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
data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})
```
<br>

Table: `Weather`
<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.   
There are no different rows with the same recordDate.   
This table contains information about the temperature on a certain day.
</pre>

Write a solution to find all dates' `id` with higher temperatures compared to its previous dates (yesterday).

Return the result table in **any order**.

The result format is in the following example.     
<br>

**Example 1:**

- Input:   
    <pre> 
    Weather table:
    +----+------------+-------------+
    | id | recordDate | temperature |
    +----+------------+-------------+
    | 1  | 2015-01-01 | 10          |
    | 2  | 2015-01-02 | 25          |
    | 3  | 2015-01-03 | 20          |
    | 4  | 2015-01-04 | 30          |
    +----+------------+-------------+
    </pre>
- Output:  
    <pre>
    +----+
    | id |
    +----+
    | 2  |
    | 4  |
    +----+
    </pre>
- Explanation:   
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).    
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).  


## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 날짜 값을 순서대로 정렬
    weather.sort_values(by='recordDate', inplace=True)

    # 바로 이전 행과 날짜끼리 간격을 계산한 열과 온도 차이끼리 계산한 열 추가
    weather["date_diff"] = weather["recordDate"].diff()
    weather["temp_diff"] = weather["temperature"].diff().fillna(0).astype(int)

    # 이전 행과의 날짜 간격이 1일이고 온도가 더 높은 행만 필터링
    filtered_weather = weather[(weather.date_diff == "1 days") & (weather.temp_diff > 0)]

    # id 값을 기준으로 다시 순서대로 정렬
    filtered_weather.sort_values(by='id', inplace=True)
    print(filtered_weather)

    # id 열의 이름을 변경하고 해당 열만 가져오기
    filtered_weather = filtered_weather[["id"]].rename(columns={"id": "Id"})
    return filtered_weather
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **75.67%**    
<i class="fa-solid fa-memory"></i> Memory: **68.12** MB \| Beats **14.99%**

주의해야 할 케이스
1. 날짜가 순서대로 정렬되지 않은 경우
2. 날짜가 하루보다 더 큰 간격으로 정렬된 경우

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/rising-temperature/solutions/3881503/pandas-simple-solution/" target="_blank">1st</a>

```python
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    return weather[
        (weather.temperature.diff() > 0)
      & (weather.recordDate.diff().dt.days == 1)
    ][['id']]
```
<mark>.diff()</mark>사용 후 dt.days로 해당 datetime 타입에서 일 단위 부분만 가져올 수 있다는 것을 알게 됐다.   
그리고 **id** 열의 이름이 `Expected`에 **Id**로 표시되어 있어서 이름을 바꿨는데, 굳이 그렇게 하지 않아도 통과되는 것 같다.

### <a href="" target="_blank">2nd</a>

```sql
SELECT today.id             -- 모든 조건에 맞는 행의 id 값 선택
FROM Weather yesterday      -- weather 참조1: yesterday, weather 참조2: today
CROSS JOIN Weather today    -- yesterday today의 모든 가능한 조합 생성

WHERE DATEDIFF(today.recordDate,yesterday.recordDate) = 1   -- 두 날짜의 차이(일 단위)가 1일인 경우만 선택
    AND today.temperature > yesterday.temperature;          -- 오늘의 온도가 어제보다 더 높은 날을 필터링
```
