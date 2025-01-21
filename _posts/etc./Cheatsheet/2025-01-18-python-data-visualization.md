---
excerpt: "Python에서 데이터를 시각화하는 Matplotlib, Plotly, Seaborn 라이브러리 정리"
title: "Python Data Science: Data Visualization"
header:
  teaser: "https://www.ft.com/__origami/service/image/v2/images/raw/ftcms%3A347ece48-0f69-11e9-a3aa-118c761d2745?source=ig"
categories:
  - Cheatsheet
tags:
  - Python
  - Pandas
  - Matplotlib
  - Plotly
  - Seaborn
last_modified_at: 2025-01-21T14:30:30+09:00
---

<div class="notice--info" markdown="1">
💡 **Google Colab**에서 작업한다면 해당 라이브러리들을 따로 설치할 필요가 없지만, 업데이트가 필요할 수 있다.

```bash
%pip install --upgrade plotly
```
</div>

## Matplotlib

> **Matplotlib(맷플롯립)**   
> - 정적인 이미지 형식의 그래프를 만드는 파이썬 라이브러리로, Pandas와 잘 맞는다.
> - 그래프의 세부 요소를 세밀하게 제어할 수 있어 보고서, 논문 등에 사용
> - <a href="https://matplotlib.org/cheatsheets/#matplotlib-cheatsheets-and-handouts" target="_blank">Matplotlib cheatsheets and handouts</a>에서 요약본 pdf 다운로드
> 
> ```bash 
> pip install matplotlib            # 터미널에서 설치
> ```
> ```python
> import matplotlib.pyplot as plt
> ```

<br>

### GRAPHS

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
<br>
💡 **서로 다른 타입의 차트를 한 차트에 겹쳐서 표시할 수 있다.**
</div>

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html" target="_blank">pyplot.plot()</a>

- 꺾은선형 차트 생성
- 현재 활성화된 가로(x)축과 세로(y)축 순서대로 원하는 데이터 전달
- 차트를 스타일링하려면 먼저 스타일 지정 후, plot 함수로 차트 생성
- 파라미터
   - **linewidth:** 선 굵기 지정
   - **label:** 선에 이름 붙이기
   - **color:** 선 색상 지정
   - **linewidth:** 선 굵기 지정
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
- 현재 활성화된 가로(x)축과 세로(y)축 순서대로 원하는 데이터 전달
- 파라미터
   - **alpha:** 점의 투명도(중첩된 데이터의 시각화를 용이하게 만들기)
   - **size:** 점의 사이즈

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html" target="_blank">pyplot.bar()</a>

- 막대 차트 생성
- 현재 활성화된 가로(x)축과 세로(y)축 순서대로 원하는 데이터 전달

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html" target="_blank">pyplot.show()</a>

- 차트 생성 메소드를 호출한 위치의 바로 아래에 차트를 표시(현재까지 그려진 모든 플롯의 결과를 화면에 출력)
- 주피터와 같은 대화형 노트북이 아닌 곳에서 차트 생성시 유용하다.

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html" target="_blank">pyplot.imshow()</a>

- 이미지 데이터를 시각화하여 플롯에 그리는 역할
- 파라미터
   - **cmap:** 컬러 맵을 지정(e.g. `gray`는 색상 팔레트를 그레이스케일로 설정해서 흑백 이미지 출력)

<br><br>

### STYLE

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html" target="_blank">pyplot.title()</a>

- 차트 제목 설정

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html" target="_blank">pyplot.figure()</a>

- 차트 사이즈 조정
- 파라미터
   - **figsize:** (너비, 높이) 값을 튜플로 전달
   - **dpi:** 해상도 조절

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html" target="_blank">pyplot.grid()</a>

- 차트 위에 회색 격자를 겹쳐서 표시
- 파라미터
   - **color:** 격자선 색 지정
   - **linestyle:** 격자선 스타일 지정

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks" target="_blank">pyplot.xticks()</a>, <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html" target="_blank">pyplot.yticks()</a>

- x축, y축을 구성
- 파라미터
   - **ticks:**
      - x축, y축 눈금의 위치(빈 리스트 전달 시 모든 눈금 제거)
      - NumPy의 <a href="https://jooyeunseo.github.io/cheatsheet/python-numpy/#arange" target="_blank">.arange()</a> 활용 가능(e.g. `np.arange(1900, 2025, step=5)`)
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

- 현재 활성화된 축이 아닌 특정 Axes 객체의 x축, y축에 제목을 추가
- 한 차트에서 여러 축을 표시해야 할 때 사용

#### <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html" target="_blank">Axes.invert_xaxis()</a>, <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html" target="_blank">Axes.invert_yaxis()</a>

- x축, y축을 반전(작은 값→큰 값에서 큰 값→작은 값으로 순서 변경)


### SETTINGS

#### <a href="https://matplotlib.org/stable/api/legend_api.html" target="_blank">.legend()</a>

- 각 데이터 시리즈의 레이블을 수집하여 범례를 생성
- 그래프 오른쪽 위(기본값)에 각 라인의 색상, 이름과 함께 표시됨
- 파라미터
   - **fontsize:** 글자 크기 조절
   - **handles:**
      - 범례에 표시하고 싶은 객체만 리스트로 전달
      - plot 객체가 반환하는 **튜플**에서 **첫 번째 값**(선, 점 등 그래프에 보여질 객체)만 handles에 전달됨    
          ```python
          ...

          black_line, = plt.plot( ... )    # 라인 객체 1 저장(, = 으로 반환값의 첫 번째 값만 저장)
          white_line, = plt.plot( ... )    # 라인 객체 2 저장(같은 축에 선을 하나 더 그림)

          plt.legend(handles=[black_line, white_line], fontsize=18)
          plt.show()
          ```  
      - `.legend()`로 자동 생성하는 범례보다 더 세밀하게 제어할 수 있고, 생성한 객체에서 속성 변경으로 스타일을 관리할 수 있다.

#### <a href="https://matplotlib.org/stable/api/dates_api.html" target="_blank">.dates</a>

- 맷플롯립의 날짜 표시 기능을 담당
- 차트의 축을 보기 쉽게 큰 눈금과 작은 눈금을 추가하는 로케이터를 추가할 수 있다.
<br><br>

```python
import matplotlib.dates as mdates

years = mdates.YearLocator()              # 연도를 찾는 로케이터
months = mdates.MonthLocator()            # 월을 찾는 로케이터
years_fmt = mdates.DateFormatter('%Y')    # 날짜를 표시하는 방식을 지정(e.g. '%Y'는 연도를 2025로 표시)
```

- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html" target="_blank">Axis.set_major_locator()</a>:** 큰 눈금의 위치 설정
- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html" target="_blank">Axis.set_major_formatter()</a>:** 큰 눈금에 날짜를 표시하는 형식 지정
- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html" target="_blank">Axis.set_minor_locator()</a>:** 작은 눈금의 위치 설정
- **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html" target="_blank">Axis.set_minor_formatter()</a>:** 작은 눈금에 날짜를 표시하는 형식 지정

--------------------------------------------

<br><br>

## Plotly

> **Plotly(플로틀리)**   
> Zoom, Pan, Hover, Toggle 등을 수행할 수 있는 대화형 그래프를 생성하는 파이썬 라이브러리
>
> ```bash 
> pip install plotly             # 터미널에서 설치
> pip install ipywidgets         # 주피터 노트북에서 사용할 경우 그래프를 제대로 표시하기 위해 권장
> ```
> ```python
> import plotly.express as px
> ```

<br>

### GRAPHS

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.bar.html" target="_blank">express.bar()</a>

- Pandas DataFrame을 기반으로 간단하고 빠르게 막대 차트 생성
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **x:** x축 데이터(카테고리 이름)
   - **y:** y축 데이터(수치형 데이터)
   - **color:** 색상으로 데이터를 구분하여 보여줄 열(한 막대를 값에 따라 여러 색깔로 분할할 수 있음) 
   - **color_continuous_scale:** 값에 따라 변하는 색상 스케일 <a href="https://plotly.com/python/builtin-colorscales/l" target="_blank">설정</a>
   - **orientation:** 막대 방향 지정(`'v'는 세로, `'h'`는 가로)
   - **barmode:** 막대의 표시 방식(e.g. `'group'`은 한 카테고리에 대한 여러 데이터가 옆에 나란히 배치됨)
   - **width, height:** 차트의 너비 및 높이(픽셀)
   - **hover_name:** 점 위에 마우스를 올릴 때 표시될 추가 정보

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.scatter.html" target="_blank">express.scatter()</a>

- Pandas DataFrame을 기반으로 간단하고 빠르게 산점도 차트 생성
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **x:** x축 데이터(카테고리 이름)
   - **y:** y축 데이터(수치형 데이터)
   - **size:** 각 점의 크기를 나타낼 수치형 데이터
   - **color:** 색상으로 데이터를 구별하여 보여줄 열
   - **hover_name:** 점 위에 마우스를 올릴 때 표시될 추가 정보

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.line.html" target="_blank">express.line()</a>

- Pandas DataFrame을 기반으로 간단하고 빠르게 선형 차트 생성
- <a href="https://plotly.com/python/line-charts/" target="_blank">Line Charts in Python</a> 참고
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **x:** x축 데이터(카테고리 이름)
   - **y:** y축 데이터(수치형 데이터)
   - **color:** 색상으로 데이터를 구별하여 보여줄 열(여러 개의 선을 한 차트에 표시할 수 있다.)

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.box.html" target="_blank">express.box()</a>

- Pandas DataFrame을 기반으로 간단하고 빠르게 상자 차트 생성
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **x:** x축 데이터(카테고리 이름)
   - **y:** y축 데이터(수치형 데이터)
   - **color:** 각 상자의 색상을 나타낼 데이터   
   - **notched:** 상자 위아래에 홈 추가 여부(두 박스가 겹치는지 확인하거나 중앙값의 신뢰 구간 확인에 유용)
   - **points:** 이상치(outliers, 박스를 벗어난 데이터) 표시 방법(e.g. `all`은 모든 이상치를 점으로 표시)

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.histogram.html" target="_blank">express.histogram()</a>

- 히스토그램 생성
- <a href="https://plotly.com/python/histograms/" target="_blank">Histograms in Python</a> 참고
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **x:** x축 데이터(카테고리 이름)
   - **y:** y축 데이터(수치형 데이터)
   - **nbins:** 히스토그램의 빈(bin)개수를 설정(e.g. 30일 경우 데이터를 30개의 구간으로 나눔)
   - **color:** 각 막대의 색상을 나타낼 데이터
   - **opacity:** 막대의 투명도 설정(겹치는 구간에서 투명하게 보여서 쉽게 구분할 수 있다.)
   - **barmode:** 막대의 표시 방식(e.g. `'overlay'`는 한 카테고리에 대한 여러 데이터가 겹쳐서 표시됨)
   - **histnorm:** y축 값을 퍼센트로 정규화(수치가 크게 다른 값끼리 비교할 때 유용)
   - **marginal:** 차트 위나 옆에 추가적인 그래프 제공(e.g. `'box'`는 박스 플롯 추가)

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.pie.html" target="_blank">express.pie()</a>

- Pandas DataFrame을 기반으로 간단하고 빠르게 파이 차트 생성
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **names:** 데이터프레임의 열 이름을 사용하여 파이 조각에 이름을 지정
   - **labels:** 가독성을 위해 names보다 간결하거나 읽기 쉬운 이름을 리스트 또는 딕셔너리로 전달
   - **values:** 파이 조각의 크기(비율) 지정
   - **hole:** 차트 가운데 동그랗게 빈 공간을 추가하고 크기 조절(<mark>도넛 차트</mark>로 변경됨)
   - **width, height:** 차트의 너비 및 높이(픽셀)

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.sunburst.html" target="_blank">express.sunburst()</a> 

- Pandas DataFrame을 기반으로 간단하고 빠르게 햇살형 차트 생성
- 계층적 데이터를 원형으로 시각화   
(e.g. 1번째 레벨: `'Region'`, 2번째 레벨: `'Country'`, 3번째 레벨: `'City'`, 각 섹션의 크기: `'Population'`)
- <a href="https://plotly.com/python/sunburst-charts/" target="_blank">Sunburst Charts in Python</a> 참고
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **path:** 계층적 데이터의 열 이름을 리스트로 지정
   - **values:** 각 섹션의 크기를 결정하는 데이터
   - **color** 각 섹션의 색상을 나타낼 데이터

#### <a href="https://plotly.com/python-api-reference/generated/plotly.express.choropleth.html" target="_blank">express.choropleth()</a>

- 지역 데이터를 시각화할 수 있는 색상 지도(choropleth map) 생성
- <a href="https://plotly.com/python/choropleth-maps/" target="_blank">Choropleth Maps in Python</a> 참고
- 파라미터
   - **title:** 차트 제목
   - **data_frame:** 데이터프레임 또는 딕셔너리(생략 가능)
   - **locations:** 지역을 나타내는 값이 저장된 열
   - **locationmode:** locations 값의 형식 지정
      - `'ISO-3'`: 3글자 ISO 국가 코드(기본값)
      - `'USA-states'`: 미국 주 이름
      - `'country names'`: 국가 이름
   - **hover_name:** 마우스를 올렸을 때 표시될 텍스트
   - **hover_data:** 마우스를 올렸을 때 추가로 표시할 데이터(열 이름들을 리스트로 전달 가능)
   - **color:** 각 지역의 색상을 나타낼 데이터   

#### <a href="https://plotly.com/python-api-reference/generated/generated/plotly.graph_objects.Figure.show.html?highlight=show" target="_blank">Figure.show()</a>

- 생성된 그래프 개체를 graph_objects로 표시

<br>

### STYLE

<div class="notice--info" markdown="1">
💡 그래프 생성 메소드의 파라미터에 없는 부분을 구성하려면 먼저 그래프 객체를 만든 후 필요한 메소드 호출   
</div>

#### <a href="https://plotly.com/python-api-reference/generated/generated/plotly.graph_objects.Figure.update_traces.html?highlight=update_traces" target="_blank">Figure.update_traces()</a> 

- trace는 그래프에서 데이터의 시각적 표현에 관련된 속성의 집합
- 파라미터
   - **textposition:** 텍스트 위치 변경(e.g. 파이 차트 바깥 또는 안에 포함)
   - **textinfo:** 텍스트 표시 방법 변경(e.g. 레이블과 퍼센트의 조합)

#### <a href="https://plotly.com/python-api-reference/generated/generated/plotly.graph_objects.Figure.update_layout.html?highlight=update_layout" target="_blank">Figure.update_layout()</a>  

- 그래프의 전반적인 레이아웃 설정 변경
- 파라미터
   - **title:** 그래프의 제목
   - **xaxis_title:** x축 제목
   - **yaxis_title:** y축 제목
   - **xaxis:** x축의 레이아웃 설정
      - `{'categoryorder':'min ascending'}`: 각 범주에서 가장 작은 값을 기준으로 범주를 오름차순 정렬
      - `{'categoryorder':'max ascending'}`: 각 범주에서 가장 큰 값을 기준으로 범주를 오름차순 정렬
   - **yaxis:** y축의 레이아웃 설정    
   (e.g. `dict(type="선형,로그,날짜,범주 등 스케일", showgrid="그리드 표시 여부")`)
   - **plot_bgcolor:** 그래프의 배경색
   - **paper_bgcolor:** 전체 배경색
   - **coloraxis_showscale:** 그래프 생성 시 *color_continuous_scale*로 설정한 색상 스케일 축 표시 여부
   - **legend:** 범례의 레이아웃 설정    
   (e.g. `dict(title="제목", orientation="표시 방향", x=x축 위치, y=y축 위치, xanchor="위치 기준")`)

--------------------------------------------

<br><br>

## Seaborn

> **Seaborn(씨본)**   
> Matplotlib을 기반으로 한 파이썬 라이브러리로, 더 많은 기능과 세련된 디자인을 제공
> 
> ```bash
> pip install seaborn         # 터미널에서 설치
> ```
> ```python
> import seaborn as sns       # 관례적으로 sns라는 이름으로 임포트
> ```

<br>

### GRAPHS

<div class="notice--info" markdown="1">
💡 한 차트에 여러 그래프를 그리려면 차트 생성 메소드를 원하는 만큼 호출
</div>

#### <a href="https://seaborn.pydata.org/generated/seaborn.scatterplot.html" target="_blank">.scatterplot()</a>

- 산점도 차트 생성
- 파라미터
   - **data:** 판다스 데이터프레임
   - **x:** x축 데이터로 사용할 열
   - **y:** y축 데이터로 사용할 열
   - **hue:** 지정한 값을 기준으로 점의 색상 결정(큰 값일수록 진한 색)
   - **palette:** `hue`의 색상 그라데이션을 변경할 컬러맵(colormap) 지정
   - **size:** 지정한 값을 기준으로 점의 크기 결정 

#### <a href="https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot" target="_blank">.regplot()</a>

- 산점도 + 선형 회귀선(점들 사이의 선형 관계를 나타내는 직선)을 함께 표시하는 차트 생성
- 파라미터
   - **data:** 판다스 데이터프레임
   - **x:** x축 데이터로 사용할 열
   - **y:** y축 데이터로 사용할 열
   - **lowess:**
      - Locally Weighted Scatterplot Smoothing의 약자
      - `True`로 설정하면 선형 회귀 대신 국소 회귀를 사용하여 더 부드럽고 자연스러운 추세선을 그릴 수 있다.
   - **scatter_kws:** 점의 스타일을 설정하는 딕셔너리
       - `{'alpha': 투명도(0은 투명, 1은 불투명}`
       - `{'color': 색상}`
       - `{'s': 크기}`
       - `{'marker': 모양}`
       - `{'linewidth': 테두리 두께}`
       - `{'edgecolor': 테두리 색상}`
   - **line_kws:** 회귀선의 스타일을 설정하는 딕셔너리
      - `{'color': 색상}`
      - `{'alpha': 투명도}`
      - `{'linewidth': 두께}`
      - `{'linestyle': 스타일}`

#### <a href="https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot" target="_blank">.lmplot()</a>

- `.regplot()`의 확장 형태로, 선형 회귀선이나 국소 회귀선에 대한 여러 조건 설정 가능
- 파라미터
   - **row:** 지정된 열을 기준으로 서브플롯을 생성하여 행으로 배치(가로로 나열됨)
   - **col:** 지정된 열을 기준으로 서브플롯을 생성하여 열로 배치(세로로 나열됨)
   - **aspect:** 각 플롯의 가로 세로 비율 설정
   - **hue:** 색상으로 그룹을 구분할 열 지정(row, col처럼 서브플롯을 생성하지 않고 한 차트에 모두 표시)

#### <a href="https://seaborn.pydata.org/generated/seaborn.histplot.html" target="_blank">.histplot()</a>

- 히스토그램 생성
- 데이터를 구간(bin)으로 나누고 각 구간에 포함된 데이터의 개수를 막대로 표현
- 파라미터
   - **data:** 판다스 데이터프레임
   - **x:** x축 데이터로 사용할 열(x축은 bins를 나타내고 y축은 해당 구간에 속한 데이터의 개수나 밀도가 됨)
   - **bins:** 데이터를 나누는 구간의 개수(데이터에 따라 적절히 설정해야 한다.)

#### <a href="https://seaborn.pydata.org/generated/seaborn.kdeplot.html" target="_blank">.kdeplot()</a>

- 커널 밀도 추정(Kernel Density Estimation, KDE) 그래프 생성
- 데이터의 분포를 부드러운 곡선 형태로 추정하는 데 사용
- 파라미터
   - **data:** 판다스 데이터프레임
   - **x:** x축 데이터로 사용할 열
   - **shade:** `True`로 설정하면 각 분포 아래(곡선 안쪽)를 색으로 채운다(겹치는 영역 확인에 용이).
   - **clip:** x축 값의 범위를 제한(e.g. `(0, 1)`는  KDE 곡선을 0에서 1 사이의 범위로 제한)

#### <a href="https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot" target="_blank">.boxplot()</a>

- 박스 차트 생성
- 구성 요소
   - **Box:** 데이터의 중앙 50%를 나타냄(박스의 상단은 세 번째 사분위수, 하단은 첫 번째 사분위수가 된다.)
   - **Median:** 박스 안의 가로선은 데이터의 중앙값(두 번째 사분위수)
   - **Whiskers:** 박스에서 벗어나는 선들은 데이터를 1.5배 IQR 범위 내로 확장한 부분
   - **Outliers:** 수염(Whiskers) 끝을 넘어서는 점들(원과 같은 기호로 표시)
- 파라미터
   - **data:** 판다스 데이터프레임
   - **x:** x축 데이터로 사용할 열
   - **y:** y축 데이터로 사용할 열
<br>

### STYLE

<div class="notice--info" markdown="1">
💡 Seaborn은 Matplotlib 기반이기 때문에 맷플롯립 레이어에서도 차트를 구성할 수 있다.     
💡 차트 생성 메소드가 반환하는 **<a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes" target="_blank">맷플롯립의 Axes 객체</a>**를 구성하여 스타일 지정하기    
💡 모든 차트가 아닌 특정 차트에만 스타일을 설정하려면 파이썬 `with` 키워드 사용    

```python
plt.figure(figsize=(8, 4), dpi=200)       # 1. 먼저 맷플롯립으로 차트 크기와 해상도 조절

with sns.axes_style('darkgrid'):          # (with 블록 내에서만 유효한 스타일 변경)
   ax = sns.scatterplot(data=df,             # 2. 씨본으로 Axes 객체 생성
                        x='column_a',
                        y='column_b')

   ax.set(ylim=(0, 100000),                  # 3. 맷플롯립 레이어에서 축 한계와 레이블 등 설정
          xlim=(0, 300000),
          xlabel='A',
          ylabel='B')

plt.show()                                   # 4. 맷플롯립으로 차트 출력   
```
</div>

#### <a href="https://seaborn.pydata.org/generated/seaborn.axes_style.html" target="_blank">.axes_style()</a>

- 차트의 전체적인 테마 변경
- "darkgrid", "whitegrid", "dark", "white", "ticks" 중 선택

<br><br>
<center>References</center>

1. Angela Yu, [Python 부트캠프 : 100개의 프로젝트로 Python 개발 완전 정복], Udemy, https://www.udemy.com/course/best-100-days-python/?couponCode=ST3MT72524   
2. [API Reference], https://matplotlib.org/stable/api/index.html   
3. [Python API reference for plotly], https://plotly.com/python-api-reference/     
4. [API reference], https://seaborn.pydata.org/api.html   
{: .small}
<!--
```python
```
<i class="fa-solid fa-right-from-bracket"></i>    
<pre>
</pre>

<a href="" target="_blank"></a>

<img src="https://github.com/dcurtis/markdown-mark/blob/master/png/208x128.png?raw=true" 
     width="10%"> -->