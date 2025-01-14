---
excerpt: "Python의 Pandas 라이브러리 정리"
title: "Python Data Science: Pandas"
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/512px-Pandas_logo.svg.png"
categories:
  - Cheatsheet
tags:
  - Python
  - Pandas
last_modified_at: 2025-01-14T14:45:30+09:00
---

> **Pandas**    
> 표 형태(스프레드 시트 등)의 데이터 분석에 효과적인 파이썬 라이브러리    
> ```python
> import pandas as pd
> ```
> <br>
> **CSV**    
> 표 형태의 데이터를 대표하는 일반적인 방식으로, 쉼표로 값을 분류
> ```python
> data = pd.read_csv("weather_data.csv")    # 판다스로 CSV 파일 읽기
> ```
>> **weather_data.csv**   
>> day,temp,condition    
>> Monday,12,Sunny   
>> Tuesday,14,Rain   
>> Wednesday,15,Rain   
>> Thursday,14,Cloudy   
>> Friday,21,Sunny   
>> Saturday,22,Sunny   
>> Sunday,24,Sunny   

## Table

Pandas의 **DataFrame 클래스**로 <mark>표</mark> 전체를 출력할 수 있다.

```python
print(data)     # 데이터프레임 출력(첫 번째 행은 자동으로 각 열의 제목이 된다)
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
</pre>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html" target="_blank">DataFrame.to_dict()</a>

```python
data_dict = data.to_dict()                  # 데이터프레임 클래스의 객체를 딕셔너리로 변환
print(data_dict)
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
{
  'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
  'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
  'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
}
</pre>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html" target="_blank">DataFrame.to_csv()</a>

```python
data_dict = {                                 # 파이썬으로 딕셔너리 생성
    "students": ["Amy", "Ben", "Carter"],
    "scores": [76, 56, 65]
}
score_data = pd.DataFrame(data_dict)          # 딕셔너리를 판다스 데이터프레임 객체로 변환
score_data.to_csv("new_data.csv")             # 데이터프레임 객체를 CSV 파일로 변환
```
<br>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html" target="_blank">DataFrame.iterrows()</a>

```python
for (index, row) in score_data.iterrows():        # 위에서 생성한 score_data의 각 행의 (index, row) 튜플 반복 출력
    print(index)
    print(row)
    
for (index, row) in score_data.iterrows(): 
    if row.scores > 60:                           # 조건에 맞는 행의 특정 열만 반복 출력
        print(row.students)
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
0
students    Amy
scores       76
Name: 0, dtype: object
1
students    Ben
scores       56
Name: 1, dtype: object
2
students    Carter
scores          65
Name: 2, dtype: object


Amy
Carter
</pre>


## Column

데이터프레임(전체 표)에서 추출한 단일 <mark>열</mark>은 Pandas의 **Series 클래스**의 객체가 된다.

```python
print(data["temp"])   # 시리즈 출력하는 방법1
print(data.temp)      # 시리즈 출력하는 방법2
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
</pre>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html" target="_blank">Series.to_list()</a>

```python
temp_list = data["temp"].to_list()      # temp 열을 리스트로 변환
print(temp_list)
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
[12, 14, 15, 14, 21, 22, 24]
</pre>

## Row

Pandas의 DataFrame과 Series 클래스로 표의 특정 <mark>행</mark>만 출력할 수 있다.

```python
print(data[data["day"] == "Monday"])    # 데이터프레임과 시리즈로 표의 특정 행 출력
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
      day  temp condition
0  Monday    12     Sunny
</pre>

1. 전체 표에서 검색하는 것이 있는 열 찾기
2. 열에서 검색하는 것과 같은 값이 있는 행을 체크
<br><br>

```python
monday = data[data.day == "Monday"]         # 월요일에 해당하는 행

monday_condition = monday.condition           # 월요일 행에서 condition 열에 접근
print(monday.condition)                       

monday_temp = monday.temp                     # 월요일 행에서 temp 열에 접근
monday_temp_F = (monday_temp * 9/5) + 32      # 섭씨를 화씨로 변환
print(monday_temp_F)
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
0    Sunny
Name: condition, dtype: object

0    53.6
Name: temp, dtype: float64
</pre>

## Data Science

데이터 사이언스에 활용할 수 있는 판다스 메소드

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html" target="_blank">DataFrame.head()</a>,   <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html" target="_blank">DataFrame.tail()</a>

- 데이터프레임의 상위, 하위 5개 행(기본값)만 출력
- 파라미터 **n**에 값을 전달하여 원하는 개수만큼 출력 가능

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html" target="_blank">DataFrame.shape</a>

- 데이터프레임의 차원(행, 열 등)의 개수를 나타내는 튜플 반환
<!-- - ndarray.shape 도 가능(링크달기) -->

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html" target="_blank">DataFrame.columns</a>

- 데이터프레임의 모든 열의 이름만 출력

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html" target="_blank">DataFrame.loc[]</a>

- [] 안에 인덱스를 넣어서 특정 행을 출력할 수 있다.
- <mark style='background-color: LightYellow'>⚠️ 파이썬 슬라이싱처럼 범위를 지정 가능하나, loc는 시작과 끝 숫자가 모두 포함됨</mark>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html" target="_blank">DataFrame.isna()</a>

- NaN(Not a Number)값을 찾는 메소드
- 누락된 데이터(빈 셀)나 정크 데이터(숫자 대신 문자열을 포함하는 셀)를 뜻함

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html" target="_blank">DataFrame.dropna()</a>

- 필요없는 행(NaN 값이 포함된)을 제거한 새 데이터프레임 생성
- 새로 생성된 데이터는 변수에 저장해야 한다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html" target="_blank">DataFrame.insert()</a>

- 데이터프레임의 지정된 위치에 새 열을 추가
- 파라미터
   - **loc:** 열이 삽입될 위치의 인덱스
   - **column:** 열 이름(라벨)
   - **value:** 삽입할 열 데이터

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html" target="_blank">DataFrame.sort_values()</a>

- 데이터프레임(또는 시리즈)를 특정 열이나 값을 기준으로 정렬
- 파라미터
   - **by:** 정렬 기준이 되는 열 이름 또는 열 이름의 리스트(Series에는 없는 파라미터)
   - **axis:** `0`(기본값)은 행 단위, `1`은 열 단위
   - **ascending:** `True`(기본값)는 오름차순, `False`는 내림차순 정렬(여러 개의 by에 리스트로 개별 지정 가능)
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영 
   - **key:** 정렬 기준을 원하는 함수로 지정하려는 경우 사용

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html" target="_blank">DataFrame.groupby()</a>

- 데이터를 특정 기준으로 그룹화
- 파라미터 **by**에 열 이름 또는 열 이름의 리스트, 함수 등의 값을 전달하여 그룹화 기준 정하기

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html" target="_blank">DataFrame.count()</a>

- 각 열(행)에서 NaN 값을 제외한 값만 카운트
- 파라미터 **axis:** 0(기본값)은 열별로 세고(행을 따라 계산)하고, 1은 행별로 셈(열을 따라 계산)
- `DataFrame.groupby()` 메소드의 뒤에 연결하면 특정 그룹의 값만 셀 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html" target="_blank">Series.mean()</a>

- 평균값을 계산
- `DataFrame.groupby()` 메소드의 뒤에 연결하면 특정 그룹의 평균값을 계산할 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html" target="_blank">Series.max()</a>,   <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html" target="_blank">Series.min()</a>

- 특정 열에서 가장 큰 값, 가장 작은 값을 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html" target="_blank">Series.idxmax()</a>,   <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html" target="_blank">Series.idxmin()</a>

- 특정 열에서 가장 큰 값, 가장 작은 값을 가진 행의 인덱스 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.add.html" target="_blank">Series.add()</a>

- == `.addition()`
- `.` 앞의 열에 파라미터로 전달한 열을 합해서 새로운 열 생성

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sub.html" target="_blank">Series.sub()</a>

- == `.subtract()`
- `.` 앞의 열에서 파라미터로 전달한 열을 빼서 새로운 열 생성

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html" target="_blank">Series.mul()</a>

- == `.multiply()`
- `.` 앞의 열에 파라미터로 전달한 열을 곱해서 새로운 열 생성

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.div.html" target="_blank">Series.div()</a>

- == `.divide()`
- `.` 앞의 열에서 파라미터로 전달한 열을 나눠서 새로운 열 생성

<br>

## <a href="https://pandas.pydata.org/docs/user_guide/options.html#options-and-settings" target="_blank">Options</a>

```python
import pandas as pd

pd.options.display.float_format = "{:,.2f}".format  # 천 단위 구분기호를 추가하고 소수점 이하 2자리로 고정
```

- Pandas의 전역 설정에 영향을 미치는 옵션 수정
- 원본 데이터에는 영향을 끼치지 않고 파이썬에서 출력되는 형식만 변경됨

<br><br>
<center>References</center>

1) Angela Yu, [Python 부트캠프 : 100개의 프로젝트로 Python 개발 완전 정복], Udemy, https://www.udemy.com/course/best-100-days-python/?couponCode=ST3MT72524   
{: .small}
<!--
```python
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
</pre>

<a href="" target="_blank">d</a>

<img src="https://github.com/dcurtis/markdown-mark/blob/master/png/208x128.png?raw=true" 
     width="10%">
-->