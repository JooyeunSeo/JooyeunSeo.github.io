---
excerpt: "Python에서 데이터를 시각화하는 Matplotlib 라이브러리 정리"
title: "Python Data Science: Data Visualization"
header:
  teaser: ""
categories:
  - Cheatsheet
tags:
  - Python
  - NumPy
  - Matplotlib
last_modified_at: 2025-02-01T15:37:30+09:00
---

## Matplotlib

> **Matplotlib(맷플롯립)**   
> 차트와 그래프를 만드는 파이썬 라이브러리 중 하나로, Pandas와 잘 맞는다.
> ```python
> import matplotlib.pyplot as plt
> ```

<br>

### CHARTS

<div class="notice--info" markdown="1">
💡 **여러 개의 열(판다스 데이터프레임)을 한 차트에 표시하려면 for문으로 원하는 횟수만큼 차트 생성 메소드 호출**

```python
# e.g. 다중 선형 차트 생성
for column in df.columns:
    plt.plot(df.index, df[column], linewidth=2, label=df[column].name)
```
<br>
💡 **단위가 다른 두 개의 개별 축을 한 차트에 표시하기**
1. **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html" target="_blank">plt.gca()</a>** 으로 현재 활성화된 축(subplot) 가져오기(변수에 저장하여 1번째 Axes 객체 생성)   
2. 1번째 Axes와 동일한 x축을 공유하면 **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html" target="_blank">Axes.twinx()</a>**, 동일한 y축을 공유하면 **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twiny.html" target="_blank">Axes.twiny()</a>** 으로 2번째 Axes 생성
3. 두 개의 축에 대해 각각 차트 생성 메소드 차트 호출   

```python
# e.g. 동일한 x축을 공유하는 두 y축
ax1 = plt.gca()                # gca = Get Current Axes
ax2 = ax1.twinx()

ax1.plot(x-data, y-data-a)     # 공유하는 축은 똑같이 설정
ax2.plot(x-data, y-data-b)
```
</div>

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html" target="_blank">pyplot.plot()</a>

- 꺾은선형 차트 생성
- 현재 활성화된 가로(x)축과 세로(y)축 순서대로 원하는 데이터 전달
- 차트를 스타일링하려면 먼저 스타일 지정 후, plot 함수로 차트 생성
- 파라미터
   - **linewidth:** 선 굵기 지정
   - **label:** 선에 이름 붙이기
   - **color:** 선 색상 지정
   - **linestyle:** 선 스타일 지정
      - `'solid'` 또는 `'-'` → ───────
      - `'dashed'` 또는 `'--'` → ── ── ──
      - `'dotted'` 또는 `':'` → ············
      - `'dashdot'` 또는 `'-.'` → ─·─·─·─·─·
      - `'None'` 또는 `''` → (선 없음)
   - **marker:** 선이 꺾이는 지점을 표시하는 도형 스타일 지정
      - `'.'` → •
      - `','` → ·
      - `'o'` → ●
      - `'s'` → ■
      - `'^'` → ▲
      - `'v'` → ▼
      - `'<'` → ◀
      - `'>'` → ▶
      - `'x'` → ×
      - `'None'` 또는 `''` → (마커 없음)


#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html" target="_blank">pyplot.scatter()</a>

- 점을 찍어 각 데이터의 값을 나타내는 산점도 차트 생성
- 마커 크기와 색상을 변경 가능

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html" target="_blank">pyplot.bar()</a>

- 막대 차트 생성

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html" target="_blank">pyplot.show()</a>

- 차트 생성 메소드를 호출한 위치의 바로 아래에 차트를 표시
- 주피터와 같은 대화형 노트북이 아닌 곳에서 차트 생성시 유용하다.

<br><br>

### STYLE

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html" target="_blank">pyplot.figure()</a>

- 차트 사이즈 조정
- 파라미터
   - **figsize:** (너비, 높이) 값을 튜플로 전달
   - **dpi:** 해상도 조절

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks" target="_blank">pyplot.xticks()</a>, <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html" target="_blank">pyplot.yticks()</a>

- x축, y축을 구성
- 파라미터
   - **fontsize:** 눈금의 글자 크기 조절
   - **rotation:** 눈금의 글자 기울기 조절(글씨가 길어서 서로 겹칠 경우 기울기 조정으로 해결 가능)

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html" target="_blank">pyplot.xlabel()</a>, <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html" target="_blank">pyplot.ylabel()</a>

- 현재 활성화된 x축, y축에 제목 추가
- 파라미터
   - **fontsize:** 글자 크기 조절
   - **color:** 글자 색상 지정

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html" target="_blank">pyplot.xlim()</a>, <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html" target="_blank">pyplot.ylim()</a>

- x축, y축의 상한 및 하한 설정(e.g. 값이 음수가 될 수 없는 경우 최저를 0으로 설정)
- 첫 번째 파라미터는 하한값, 두 번째 파라미터는 상한값


#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html" target="_blank">Axes.set_xlabel()</a>, <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html" target="_blank">Axes.set_ylabel()</a>

- 현재 활성화된 축이 아닌 특정 Axes 객체에 제목을 추가
- 한 차트에서 여러 축을 표시해야 할 때 사용

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html" target="_blank">pyplot.grid()</a>

- 차트 위에 회색 격자를 겹쳐서 표시
- **linestyle:** 파라미터로 점 스타일 지정 가능

### SETTINGS

#### <a href="https://matplotlib.org/stable/api/legend_api.html" target="_blank">.legend()</a>

- 각 데이터 시리즈의 레이블을 수집하여 범례를 생성
- 그래프 오른쪽 위(기본값)에 각 라인의 색상, 이름과 함께 표시됨
- **fontsize** 파라미터로 글자 크기를 조절

#### <a href="https://matplotlib.org/stable/api/dates_api.html" target="_blank">.dates</a>

- 맷플롯립의 날짜 표시 기능을 담당
- 차트의 축을 보기 쉽게 큰 눈금과 작은 눈금을 추가하는 로케이터를 추가할 수 있다.
<br><br>

```python
import matplotlib.dates as mdates

years = mdates.YearLocator()              # 연도를 찾는 로케이터
months = mdates.MonthLocator()            # 월을 찾는 로케이터
years_fmt = mdates.DateFormatter('%Y')    # 날짜를 표시하는 방식을 지정(e.g. 연도를 2025로 표시)
```

- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html" target="_blank">Axis.set_major_locator()</a>:** 큰 눈금의 위치 설정
- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html" target="_blank">Axis.set_major_formatter()</a>:** 큰 눈금에 날짜를 표시하는 형식 지정
- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html" target="_blank">Axis.set_minor_locator()</a>:** 작은 눈금의 위치 설정
- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html" target="_blank">Axis.set_minor_formatter()</a>:** 작은 눈금에 날짜를 표시하는 형식 지정


--------------------------------------------

## ppppp

> **Matplotlib(맷플롯립)**   
> 차트와 그래프를 만드는 파이썬 라이브러리 중 하나로, Pandas와 잘 맞는다.
> ```python
> import matplotlib.pyplot as plt
> ```


## ccccc

> **Matplotlib(맷플롯립)**   
> 차트와 그래프를 만드는 파이썬 라이브러리 중 하나로, Pandas와 잘 맞는다.
> ```python
> import matplotlib.pyplot as plt
> ```


<br><br>
<center>References</center>

1) Angela Yu, [Python 부트캠프 : 100개의 프로젝트로 Python 개발 완전 정복], Udemy, https://www.udemy.com/course/best-100-days-python/?couponCode=ST3MT72524   
{: .small}
2) https://matplotlib.org/stable/api/index.html



```python
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
</pre>

<a href="" target="_blank"></a>

<img src="https://github.com/dcurtis/markdown-mark/blob/master/png/208x128.png?raw=true" 
     width="10%">