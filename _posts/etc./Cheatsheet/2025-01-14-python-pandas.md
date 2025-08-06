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
  - Data Science
last_modified_at: 2025-08-06T14:30:30+09:00
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

## ▦ Table

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
for (index, row) in score_data.iterrows():   # 위에서 생성한 score_data의 각 행의 (index, row) 튜플 반복 출력
    print(index)
    print(row)
    
for (index, row) in score_data.iterrows(): 
    if row.scores > 60:                      # 조건에 맞는 행의 특정 열만 반복 출력
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

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas-dataframe-merge" target="_blank">DataFrame.merge()</a>

- 두 개의 데이터프레임을 하나의 특정 열에 병합
   - `left dataframe`과 `right dataframe`으로 분류
   - `left.merge(right, ...)` 또는 `pd.merge(left, right, ...)` 으로 작성 가능
- 파라미터
   - **right:** 데이터프레임 또는 시리즈
   - **on:** 두 데이터프레임에 공통으로 존재하는 열 또는 열의 리스트
   - **left_on**, **right_on:** 서로 다른 열을 기준으로 병합할 경우 각각 left, right에서 기준이 되는 열을 지정
   - **how:** join하는 방식 지정
      - `'inner'` : 양쪽에 모두 존재하는 키만 포함, 일치하는 값이 없는 행은 제거(기본값)
      - `'outer'` : 양쪽의 모든 행을 포함, 양쪽에서 모두 일치하는 값이 없으면 NaN로 채움
      - `'left'` : left의 모든 행을 포함, right에서 일치하는 값이 없으면 NaN로 채움
      - `'right'` : right의 모든 행을 포함, left에서 일치하는 값이 없으면 NaN로 채움
      - `'cross'` : 양쪽의 모든 가능한 조합을 생성
   - **suffixes:** 중복된 열 이름을 구별하기 위한 접미사(기본값은 `('_x', '_y')`, 각각 left와 right의 중복 열 이름에 붙임)

<div class="notice--info" markdown="1">

💡 **기본키(primary key)**

- 테이블의 각 행을 고유하게 식별하는 열 또는 열의 조합
- 중복이 없고, NULL 값을 가질 수 없다.

💡 **외래키(foreign key)**

- 한 테이블의 열이 다른 테이블의 *기본키*를 참조할 때 사용
- 두 테이블 간의 관계를 형성
<br>

| Student ID | Name  | Age |
|------------|-------|-----|
|         1  | Amy   | 23  |
|         2  | Brown | 31  |
|         3  | Clack | 28  |

<u>Students 데이터프레임</u>

기본키: Student ID(각 학생을 고유하게 식별)
<br><br>
↑

| Course ID | Course Name | Student ID |
|-----------|-------------|------------|
| 1324      | Science     | 1          |
| 6235      | Math        | 1          |
| 9122      | Art         | 2          |

<u>Courses 데이터프레임</u>

기본키: Course ID(각 강의를 고유하게 식별)    
외래키: Student ID(Students 데이터프레임의 기본키를 참조, 각 강의가 어떤 학생과 연결되는지 나타냄)
</div>

## ▥ Column

데이터프레임(전체 표)에서 추출한 단일 <mark>열</mark>은 Pandas의 **Series 클래스**의 객체가 된다.

```python
print(data["temp"])   # [] 표기법
print(data.temp)      # . 표기법
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

<div class="notice--info" markdown="1">
💡 **`[]` 와 `[[]]` 의 차이**

- data**[**"temp"**]** : data의 temp 열을 Series로 반환
- data**[[**"temp"**]]** : data의 temp 열을 DataFrame으로 반환(1열짜리 새로운 DataFrame 객체)
</div>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html" target="_blank">Series.to_frame()</a>

- **이중 대괄호** 대신 해당 메서드로도 Series → DataFrame 변환 가능

```python
temp_df = data["temp"].to_frame()      # Series 구조인 temp 열을 1열짜리 DataFrame으로 변환
print(temp_df)
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
   temp
0    12
1    14
2    15
3    14
4    21
5    22
6    24
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

## ▤ Row

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

## ✅ Methods

Data Science에 활용할 수 있는 판다스 메소드 정리

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html" target="_blank">DataFrame.loc[]</a>

- 데이터프레임의 특정 행과 열을 라벨(이름)으로 선택
- `df.loc["행 라벨", "열 라벨"]` 으로 표기
  - **행 라벨**은 인덱스, **열 라벨**(선택사항)은 열 이름 또는 열 이름들의 리스트
  - 선택된 부분만 시리즈 형태로 반환됨(데이터프레임으로 반환하려면 각 행과 열 라벨을 다시 리스트로 감싸기)
- <mark style='background-color: LightYellow'>⚠️ 파이썬 슬라이싱처럼 인덱스 범위를 지정 가능하나, loc는 시작과 끝 숫자가 모두 포함됨</mark>
- 인덱스 대신 특정 열의 값(이름, 점수 등)을 기준으로 접근하려면 조건 명시 필요
- 둘 이상의 조건을 만족하는 행만 출력하려면 비트 연산자 <mark>&</mark> 사용
   - e.g. `new_data = df.loc[ (df.column_a == 0) & (df.column_b != 0) ]`
   - 비트 연산자의 우선순위가 비교 연산자보다 먼저이기 때문에, 비교 연산자에 괄호 필요

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html" target="_blank">DataFrame.iloc[]</a>

- 데이터프레임의 특정 행과 열을 위치(인덱스 번호)로 선택
- 인덱스 번호는 첫 번째 행, 열부터 **0**으로 시작
- `df.iloc["행 번호", "열 번호"]` 으로 표기
- <mark style='background-color: LightYellow'>⚠️ loc와 달리 일반 슬라이싱처럼 끝 숫자가 포함되지 않음</mark>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html" target="_blank">DataFrame.shape</a>

- 데이터프레임의 차원(행, 열 등)의 개수를 나타내는 튜플 반환
- NumPy에서 <a href="ndarray.shape" target="_blank">ndarray.shape</a>도 가능

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html" target="_blank">DataFrame.empty</a>

- 해당 데이터프레임이나 시리즈가 비어있다면 True를 반환
- NaN 값만 있을 경우 비어있지 않은 것으로 간주되기 때문에 `.dropna()` 뒤에 붙여서 사용

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html" target="_blank">DataFrame.columns</a>

- 속성만 사용했을 때는 데이터프레임의 모든 열의 이름을 반환
- 속성에 리스트로 열 이름들을 할당하면 데이터프레임의 열 이름 변경 가능
   - `df.columns = ['열1', '열2', ...]`
   - 리스트의 길이와 실제 열 개수 일치시키기

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html" target="_blank">DataFrame.rename()</a>

- 데이터프레임의 열 또는 행의 이름 변경
- 파라미터
   - **axis:** `0` 또는 axis 대신 `'index'`는 **행** 이름 변경, `1` 또는 axis 대신`'columns'`는 **열** 이름 변경
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html" target="_blank">DataFrame.describe()</a>

- 데이터프레임의 여러 통계(count, ean, std, min, 25%, 50%, 75%, max)를 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html" target="_blank">DataFrame.info()</a>

- 데이터프레임에 대한 간결한 정보를 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html" target="_blank">DataFrame.head()</a>,   <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html" target="_blank">DataFrame.tail()</a>

- 데이터프레임의 상위, 하위 5개 행(기본값)만 출력
- 파라미터 **n**에 값을 전달하여 원하는 개수만큼 출력 가능

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html" target="_blank">DataFrame.sample()</a>

- 파라미터 **n**에 전달한 개수만큼의 행을 무작위로 골라서 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html" target="_blank">DataFrame.query()</a>

- 여러 조건을 필터링하여 만족하는 부분 집합 생성
- `.loc[]`과 `&` 연산자를 사용하는 것과 같다(`.query()`에서는 연산자 대신 `and` 키워드).

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html" target="_blank">DataFrame.drop()</a>

- 데이터프레임에서 특정 열이나 행을 제거
- 파라미터
   - **axis:** `0`(기본값)은 행 단위, `1`은 열 단위
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html" target="_blank">DataFrame.duplicated()</a>

- 중복된 행(이미 *모든* 요소들의 값이 같은 행이 존재)을 `True`로 표시하여 반환(원본 데이터프레임을 변경하지 않음)
- `.duplicated()`앞에 <mark>~</mark>(논리 부정) 연산자를 붙이면 중복되지 않은 고유한 값만 남게 된다.
- `.values.any()` 앞에 연결해서 중복값이 있는지 확인할 수 있다(`False`를 반환해야 하나도 없다는 뜻).
<!-- values 속성은 numpy 링크 -->
- 파라미터
   - **subset:** 중복을 판단할 때 고려할 단일 열 또는 여러 열의 리스트 전달(기본값은 `None`, 즉 모든 열)
   - **keep:** 
      - `'first'`: 중복 데이터 중 처음만 남기고 이후의 항목들을 중복(True)으로 표시(기본값)
      - `'last'`: 중복 데이터 중 마지막만 남기고 이전의 항목들을 중복(True)으로 표시
      - `False`: 중복 데이터 전부를 중복(True)으로 표시

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html" target="_blank">DataFrame.drop_duplicates()</a>

- 중복된 항목을 삭제한 새로운 데이터프레임 반환
- 파라미터
   - **subset** (중복 항목을 더 정확히 걸러내기 위해 지정해야 할 때도 있음)
   - **keep**
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html" target="_blank">DataFrame.isin()</a>

- 특정 열의 값이 주어진 값들과 일치하는지 확인(`True`인 행만 출력)
- **values** 파라미터에 리스트, 시리즈, 데이터프레임, 딕셔너리 등으로 전달

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html" target="_blank">DataFrame.isna()</a>

- NaN(Not a Number)값일 경우 True를 반환
- NaN 값은 누락된 데이터(빈 셀)나 정크 데이터(숫자 대신 문자열을 포함하는 셀)를 뜻함
- `.values.any()` 앞에 연결해서 NaN 값이 있는지 확인할 수 있다(`False`를 반환해야 하나도 없다는 뜻).  

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html" target="_blank">DataFrame.notna()</a>

- NaN 값일 아닐 경우 True를 반환
- isna()의 반대

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html" target="_blank">DataFrame.dropna()</a>

- 필요없는 행(NaN 값이 포함된)을 제거한 새 데이터프레임 생성
- 새로 생성된 데이터는 변수에 저장해야 한다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html" target="_blank">DataFrame.fillna()</a>

- NaN 값을 원하는 값으로 변경
- 파라미터
   - **value:** 원하는 값(e.g. 0)
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html" target="_blank">DataFrame.any()</a>

- 지정된 범위 내의 값들 중 하나라도 조건을 만족한다면 `True`를, 아니면 `False`를 반환
- 다른 함수 뒤에 연결하여 많이 사용됨

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html" target="_blank">DataFrame.insert()</a>

- 데이터프레임의 지정된 위치에 새 열을 추가
- 파라미터
   - **loc:** 열이 삽입될 위치의 인덱스
   - **column:** 열 이름(라벨)
   - **value:** 삽입할 열 데이터
   - **allow_duplicates:** 중복된 열 이름 허용 여부

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html" target="_blank">DataFrame.stack()</a>

- 데이터프레임의 열을 행(인덱스)으로 쌓음(Series 타입으로 결과 반환)
- MultiIndex(다중 인덱스) 구조로 변함
- 파라미터
   - **level:** 스택을 수행할 레벨 지정(기본값은 마지막 레벨인 `-1`)
   - **dropna:** 결측값 제거 여부(기본값은 `True`)

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index" target="_blank">DataFrame.set_index()</a>

- 지정한 열 또는 배열을 데이터프레임의 인덱스로 설정
- 파라미터
   - **keys:** 단일 열이나 배열 또는 리스트로 여러 개의 열 전달
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영 

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html" target="_blank">DataFrame.reset_index()</a>

- 인덱스를 일반 열로 되돌림
- Series를 DataFrame으로 변환할 수 있음
- 기본 숫자 인덱스(0, 1, 2,...)가 부여됨
- 파라미터
   - **drop:** `False`(기본값)는 인덱스를 일반 열로 되돌림, `True`는 인덱스를 완전히 삭제
   - **level:** 다중 인덱스일 때 특정 계층 인덱스만 리셋(나머지는 유지)
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영 

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html" target="_blank">DataFrame.pivot()</a>

- 주어진 인덱스, 열 값으로 데이터프레임을 새로 재구성
- 값이 누락된 항목에는 자동으로 NaN 값이 들어간다.
- 동일한 index/column 조합이 2개 이상이면 ValueError 발생
- 파라미터
   - **index:** 행의 범주
   - **columns:** 열의 범주
   - **values:** 새로운 셀에 들어갈 값의 범주

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html" target="_blank">DataFrame.pivot_table()</a>

- 주어진 인덱스와 열 값을 기준으로 데이터를 재구성하고, 중복된 항목은 집계 함수로 처리
- 중복된 index/column 조합이 있어도 에러 없이 처리 가능
- 파라미터
   - **index:** 행의 범주
   - **columns:** 열의 범주
   - **values:** 새로운 셀에 들어갈 값의 범주
   - **aggfunc:** 집계 함수 (e.g. `mean`(기본값), `sum`, `count`, `min`, `max` 등)

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html" target="_blank">DataFrame.groupby()</a>

- 데이터를 특정 기준으로 그룹화
- 파라미터
   - **by:** 열 이름 또는 열 이름의 리스트, 함수 등을 전달하여 그룹화 기준 정하기
   - **level:** 다중 인덱스가 있는 데이터프레임에서 특정 인덱스 레벨을 기준으로 그룹화(by와 다름)
   - **as_index:** `True`(기본값)는 by를 새 데이터프레임의 인덱스로 승격, `False`는 기존 인덱스 유지
   - **dropna:** : 결측값 계산에서 제외 여부

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html" target="_blank">DataFrame.sort_values()</a>

- 데이터프레임(또는 시리즈)를 특정 열이나 값을 기준으로 정렬
- 파라미터
   - **by:** 정렬 기준이 되는 열 이름 또는 열 이름의 리스트(Series에는 없는 파라미터)
   - **axis:** `0`(기본값)은 행 단위, `1`은 열 단위
   - **ascending:** `True`(기본값)는 오름차순, `False`는 내림차순 정렬(여러 개의 by에 리스트로 개별 지정 가능)
   - **inplace:** `False`(기본값)는 원본 데이터를 유지, `True`는 정렬 결과를 원본 데이터에 반영 
   - **key:** 정렬 기준을 원하는 함수로 지정하려는 경우 사용

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html" target="_blank">DataFrame.rolling()</a>

- 시계열(time-series) 데이터나 순차적인 데이터에서 지정된 윈도우 크기만큼 데이터를 슬라이딩하면서 계산
- **window** 파라미터에 윈도우 크기를 전달(e.g. `3`은 현재 값과 이전 2개의 값, 즉 3개의 연속된 값이 기준)
- 뒤에 `.mean()`을 연결하면 이동 평균(moving average) 생성(차트의 변화를 확인하며 적당한 window 값 찾기)
- 계산 결과는 변수에 저장하기

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html" target="_blank">DataFrame.resample()</a>

- 시계열 데이터를 새로운 시간 단위로 재조정
- <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.last.html" target="_blank">DataFrame.last()</a>로 각 단위의 가장 마지막 상태를 가져올 수 있다.
    <div class="notice--warning" markdown="1">
    ⚠️ 2.1 버전부터는 권장되지 않는 메소드로, 직접 마지막 인덱스에 접근하는 방식을 권고중
    </div>
- 파라미터
   - **rule:** 리샘플링할 주기(연별 빈도는 `'Y'`, 월별 빈도는 `'M'` <a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects" target="_blank">등</a>)
   - **on:** 리샘플링할 열(datetime 타입이어야 한다.)

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html" target="_blank">DataFrame.diff()</a>

- "현재 행(열)의 값 - n행(열) 이전 또는 이후의 값"을 계산하여 반환(기본적으로 float 타입으로 반환)
- 계산 방향에 따라 맨 처음 또는 마지막 행(열)은 비교할 값이 없기 때문에 무조건 NaN가 된다.   
(`.fillna(0)` 등으로 값 대체하기)
- datetime 타입일 경우 차이나는 날짜 수 만큼 `n days`로 표시됨
- 파라미터
   - **periods:** n행(열) 앞의 값을 비교하기 위해 int형으로 값 전달(기본값은 1으로, 음수일 경우 뒤의 값 비교)
   - **axis:** `0`(기본값)은 행 단위, `1`은 열 단위

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html" target="_blank">DataFrame.shift()</a>

- 현재 값이 속한 행(열)을 n행(열)만큼 이동
- 이동 방향에 따라 맨 처음 또는 마지막 행(열)은 더 이동할 곳이 없기 때문에 무조건 NaN가 된다.
- 파라미터
   - **periods:** n행(열) 만큼 앞으로 이동하기 위해 int형으로 값 전달(기본값은 1으로, 음수일 경우 뒤로 이동)
   - **axis:** `0` 또는 `'index'`는 **행** 기준, `1` 또는 `'columns'`는 **열** 기준

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html" target="_blank">DataFrame.count()</a>

- 각 열(행)에서 NaN 값을 제외한 값만 카운트
- 파라미터 **axis**에서 0(기본값)은 열별로 세고(행을 따라 계산)하고, 1은 행별로 센다(열을 따라 계산).
- `.groupby()` 메소드의 뒤에 연결하면 특정 그룹의 값만 셀 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html" target="_blank">DataFrame.value_counts()</a>

- 데이터프레임의 각 행이 나타나는 빈도를 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html" target="_blank">DataFrame.agg()</a>

- 데이터프레임이나 시리즈에 대해 하나 이상의 집계 함수를 적용 가능
- 파라미터에 `{ 키(열 이름): 값(적용할 함수) }`처럼 딕셔너리로 전달하면 각 열마다 다른 함수를 적용할 수 있다.
- `.groupby()` 메소드의 뒤에 연결하면 특정 데이터프레임 열에 기반한 작업을 할 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html" target="_blank">DataFrame.sum()</a>

- 총 개수를 계산
- `.isna()` 메소드의 뒤에 연결하면 데이터프레임의 열마다 있는 NaN 값의 개수를 셀 수 있다.
- `.groupby()` 메소드의 뒤에 연결하면 특정 그룹에 속한 개수를 계산할 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html" target="_blank">DataFrame.cumsum()</a>

- 누적 합계(cumulative sum)를 계산
- 첫 번째 값은 그대로 유지되고 그 이후의 값은 이전 값과 현재 값을 누적하여 합산
- `.groupby()` 메소드의 뒤에 연결하면 특정 그룹에 대해 누적 합계를 계산할 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html" target="_blank">DataFrame.nlargest()</a>, <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html" target="_blank">DataFrame.nsmallest()</a>

- 데이터프레임에서 가장 큰 값, 가장 작은 값을 가진 행을 반환
- columns 파라미터의 기준으로 정렬된 상태로 반환된다.
- 파라미터
   - **n:** 반환할 행의 개수
   - **columns:** 기준이 되는 열

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html" target="_blank">Series.mean()</a>

- 평균값을 계산
- `.groupby()` 메소드의 뒤에 연결하면 특정 그룹의 평균값을 계산할 수 있다.

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html" target="_blank">Series.nunique()</a>

- 특정 열의 고유한 항목의 개수를 반환
- **dropna** 파라미터는 기본적으로 NA값을 제외하도록 설정됨
- 데이터프레임의 행 개수와 nunique의 값이 일치하면 중복되는 항목이나 결측값이 없다는 의미

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html" target="_blank">Series.max()</a>,   <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html" target="_blank">Series.min()</a>

- 특정 열에서 가장 큰 값, 가장 작은 값을 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html" target="_blank">Series.idxmax()</a>,   <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html" target="_blank">Series.idxmin()</a>

- 특정 열에서 가장 큰 값, 가장 작은 값을 가진 행의 인덱스 반환

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.add.html" target="_blank">Series.add()</a>, <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sub.html" target="_blank">Series.sub()</a>, <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html" target="_blank">Series.mul()</a>, <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.div.html" target="_blank">Series.div()</a>

- `.add()` == `.addition()` → a.add(b)는 a + b
- `.sub()` == `.subtract()` → a.sub(b)는 a - b
- `.mul()` == `.multiply()` → a.mul(b)는 a \* b
- `.div()`== `.divide()` → a.div(b)는 a / b
- 각 연산은 새로운 열 생성

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html" target="_blank">Series.map()</a>

- Series의 각 요소에 대해 변환 작업을 수행하여 새로운 Series를 반환
- 파라미터
   - **arg:** 매핑에 적용할 대상
      - `function`: 각 요소에 함수 적용(e.g. `lambda x: x * 2`)
      - `dictionary`: 값 치환용 딕셔너리 매핑(e.g. `{True: 'Yes', False: 'No'}`)
      - `Series`: 다른 Series 기반 매핑(index 기준)
   - **na_action:** `None`(기본값)은 NaN 값도 함수에 그대로 전달, `ignore`은 NaN 값을 전달하지 않고 유지

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html" target="_blank">Series.apply()</a>

- Series에서는 map()과 비슷하게 동작하지만, 함수 인자 전달이 더 유연하며 복잡한 연산에 적합
- 파라미터
   - **func:** 매핑에 적용할 함수
   - **args:** 함수에 위치 인자(\*args)로 전달
   - **\*\*kwargs:** 함수에 명시적 키워드(\*\*kwargs)로 전달됨

<div class="notice--info" markdown="1">
💡 **<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html" target="_blank">DataFrame.apply()</a>**에서는 `axis` 파라미터를 통해 각 **행** 또는 **열** 단위로 함수를 적용 가능
- `0`: 열 방향(기본값)
- `1`: 행 방향
</div>

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html" target="_blank">Series.astype()</a>

- 해당 데이터의 타입을 지정한 타입으로 변경(e.g. `str`)
- Series 객체의 `.str` 속성(문자열일 때만 사용 가능) 앞에 붙여서 문자열로 변환할 때 사용 가능

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html#" target="_blank">Series.str</a>

- 문자열 형식의 데이터를 조작
- **<a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html" target="_blank">.replace()</a>**
   - 해당 열의 값에 있는 특정 문자를 다른 문자로 대체
   - 공백으로 대체할 경우 제거할 수 있다.
- **<a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html" target="_blank">.split()</a>**
   - 해당 열의 값을 특정 문자를 기반으로 해서 분할
   - 파라미터
      - **pat:** 기준이 될 문자(기본값은 공백)
      - **expand:** `False`(기본값)는 리스트/시리즈 반환, `True`는 분리된 항목을 데이터프레임의 각 열로 반환

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html" target="_blank">Series.dt</a>

- datetime 형식의 데이터를 조작
- 속성
   - `.year`: 연도 추출
   - `.month`: 월 추출
   - `.day`: 일 추출
   - `.hour`: 시간 추출
   - `.minute`: 분 추출
   - `.second`: 초 추출
   - `.weekday`: 요일 추출(월요일을 `0`으로 반환)

<br>

## ✅ General Functions

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html" target="_blank">.to_datetime()</a>

- 문자열 등의 데이터 타입을 타임스탬프로 변환
- 해당 값에는 년(4자리), 월, 일, 시간 등의 정보가 있어야 한다.
- 변환 후 원래 값에 덮어씌워야 적용됨

### <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html#pandas.to_numeric" target="_blank">.to_numeric()</a>

- 데이터를 숫자(int, float)로 변환
- 숫자, 문자, 결측치가 혼합된 데이터에서 유연하게 사용 가능
- 파라미터
   - **expand:** `False`(기본값)는 리스트/시리즈 반환, `True`는 분리된 항목을 데이터프레임의 각 열로 반환
   - **errors:**
      - `'raise'`: 변환할 수 없는 값이 있으면 오류 발생(기본값)
      - `'coerce`: 변환 불가능한 값은 NaN으로 처리
      - `'ignore'`: 변환 불가능한 값은 원래 값 유지

## ✅ Index Objects

### <a href="https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex" target="_blank">.DatetimeIndex()</a>

- datetime 객체의 배열로 구성된 Pandas의 인덱스 객체
- 파라미터에 날짜값으로 이루어진 열을 전달 가능
- 속성
   - `.year`: 연도 반환
   - `.month`: 월 반환
   - `.day`: 일 반환
   - `.weekday`: 요일 반환(`0`은 월요일, `6`은 일요일)

## ✅ <a href="https://pandas.pydata.org/docs/user_guide/options.html#options-and-settings" target="_blank">Options</a>

```python
import pandas as pd

pd.options.display.float_format = "{:,.2f}".format  # 천 단위 구분기호를 추가하고 소수점 이하 2자리로 고정
```

- Pandas의 전역 설정에 영향을 미치는 옵션 수정
- 원본 데이터에는 영향을 끼치지 않고 파이썬에서 출력되는 형식만 변경됨

<br><br>
<center>References</center>

1. Angela Yu, [Python 부트캠프 : 100개의 프로젝트로 Python 개발 완전 정복], Udemy, https://www.udemy.com/course/best-100-days-python/?couponCode=ST3MT72524    
2. [API reference], https://pandas.pydata.org/docs/reference/index.html#  
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