---
excerpt: "minimal-mistake 테마의 레이아웃"
title: "Layouts"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
---

## <a href="https://mmistakes.github.io/minimal-mistakes/docs/layouts/#single-layout" target="_blank">Single layout</a>

```yml
---
excerpt: "미리보기와 검색 결과에서 나타나는 요약 문구" # 미설정시 본문에서 첫 100단어 자동추출
title: "포스트 제목"
layout: single    # 레이아웃 설정
classes: wide     # 컨텐츠 부분의 가로폭을 넓히는 옵션(목차가 맨 위에 고정됨) 
comments: true    # 댓글 시스템 옵션
share: true       # 소셜미디어 공유 링크 표시 옵션
related: true     # 관련 게시물 표시 옵션
toc: true         # 목차 표시 옵션
categories:       # 카테고리
  - 카테고리1
tags:             # 태그
  - 태그1
  - 태그2
---
```
- 보통 '왼쪽 사이드바 + 메인 컨텐츠' 조합으로 사용하는 레이아웃
- 포스트 형식에 사용됨

### toc: true

*[toc]: Table of Contents

- 페이지 내의 제목과 하위 제목을 기반으로 자동으로 목차를 생성하는 옵션
- 블로그 포스트나 긴 문서에서 사용됨
- 그 밖의 파라미터
   - **toc_label:** 목차 제목(defaults: `_data` → `ui-text.yml`의 `toc_label` 값)
   - **toc_icon:** 목차 아이콘(defaults: Font Awesome의 file-alt 아이콘)
   - **toc_sticky:** 목차 화면 상단 고정 여부(defaults: `false`)

### Social sharing links

- 포스트 맨 밑에 위치한 소셜미디어 공유 링크 옵션
- 링크의 순서나 색깔 및 아이콘 등을 변경할 수 있다.<br><br>

```html
<section class="page__share">
  <h4 class="page__share-title">{% raw %}{{ site.data.ui-text[site.locale].share_on_label | default: "Share on" }}{% endraw %}</h4>

  <!-- Facebook -->
  ...

  <!-- LinkedIn -->
  ...

  <!-- Add Reddit button -->
  <a href="https://www.reddit.com/submit?url={% raw %}{{ page.url | absolute_url | url_encode }}&title={{ page.title | url_encode }}"{% endraw %}
     class="btn btn--reddit"
     onclick="window.open(this.href, 'window', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;"
     title="{% raw %}{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }}{% endraw %} Reddit">
    <i class="fab fa-fw fa-reddit" aria-hidden="true"></i>
    <span> Reddit</span>
  </a>
```
- `/_includes` → `social-share.html`에서 버튼을 추가한 예시
- Font awesome 아이콘 사용
<br><br>

```scss
  $buttoncolors:
  (primary, $primary-color),
  (inverse, #fff),
  (light-outline, transparent),
  (success, $success-color),
  (warning, $warning-color),
  (danger, $danger-color),
  (info, $info-color),
  (facebook, $facebook-color),
  (twitter, $twitter-color),
  (linkedin, $linkedin-color),
  /* Add reddit-color */
  (reddit, $reddit-color);
```
- `/_sass` → `/minimal-mistakes` → `_buttons.scss`에서 새로 만든 버튼에 색상 추가
- `_variables.scss`에 셋팅되어 있는 reddit-color를 사용했으나, 직접 색상코드로 지정도 가능

## Archive layout

```markdown
---
excerpt: "미리보기와 검색 결과에서 나타나는 요약 문구" # 미설정시 본문에서 첫 100단어 자동추출
entries_layout: grid  # 아카이브 페이지의 포스트들을 4개의 열을 가진 배열로 나열하는 옵션(defaults: list)
classes: wide         # 컨텐츠 부분의 가로폭을 넓히는 옵션(목차가 맨 위에 고정됨)

<!-- 모든 포스트들을 카테고리별로 분류한 아카이브 페이지 -->
title: "Posts by Category"
layout: categories
permalink: /categories/

<!-- 모든 포스트들을 태그별로 분류한 아카이브 페이지 -->
title: "Posts by Tag"
layout: tags
permalink: /tags/

<!-- 모든 포스트들을 년도별로 분류한 아카이브 페이지 -->
title: "Posts by Year"
layout: posts
permalink: /year-archive/
---
```
- single 레이아웃과 거의 비슷한 페이지 레이아웃
- 목록을 **List**(defaults) 또는 **grid**(바둑판형) 형태로 나열할 수 있다.
<br><br>

### Posts with Same Category

```markdown
---
title: "페이지 제목"
layout: archive           # 레이아웃 설정
permalink: /링크제목/       # 네비게이션의 url과 동일
---

{%raw%}{% assign category_name = "카테고리이름" %}{%endraw%}

{%raw%}{% assign filtered_posts = site.posts | where: "categories", category_name %}{%endraw%}

{%raw%}{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}{%endraw%}
```
- 한 페이지에서 특정 카테고리의 포스트만 모아서 보는 방법
- 왼쪽 사이드바의 메뉴 커스텀에 사용했다.    


### <a href="https://mmistakes.github.io/minimal-mistakes/docs/collections/" target="_blank">Working with Collections</a>

1. 원하는 컬렉션의 이름으로 폴더 생성 e.g. `/_portfolio`
2. `_config.yml`의 **Archives**에 양식 추가
    ```yml
    collections:
      portfolio:      # collection name
        output: true
        permalink: /:collection/:path/
    ```
3. `/_pages`에 `portfolio-archive.md` 추가
    ```markdown
    ---
    title: Portfolio
    layout: collection
    permalink: /portfolio/
    collection: portfolio
    entries_layout: grid
    classes: wide
    ---

    Sample document listing for the collection `_portfolio`.
    ```
    - 포트폴리오 폴더 안의 포스트들만 보여주는 아카이브 페이지
4. `/_portfolio` 안에 md 파일 생성

## Splash page layout

```markdown
---
title: "페이지 이름"
layout: splash                              # 레이아웃 이름
permalink: /splash-page/                    # permalink
excerpt: "미리보기와 검색 결과에서 나타나는 요약 문구" # 미설정시 본문에서 첫 100단어 자동추출
intro: 
  - excerpt: 'intro 문구'
feature_row:
  - image_path: 이미지 경로
    title: "이미지 밑의 제목"
    excerpt: "제목 밑 문구"
  - image_path: 이미지 경로
    title: "이미지 밑의 제목"
    excerpt: "제목 밑 문구"
feature_row2:
  - image_path: 이미지 경로
feature_row3:
  - image_path: 이미지 경로
feature_row4:
  - image_path: 이미지 경로
---

{%raw%}{% include feature_row id="intro" %}{%endraw%}                     <!-- intro를 출력 --> 

{%raw%}{% include feature_row type="center" %}{%endraw%}                  <!-- feature_row를 가운데 정렬로 출력 -->

{%raw%}{% include feature_row id="feature_row2" type="left" %}{%endraw%}  <!-- feature_row2를 왼쪽 정렬로 출력 -->

{%raw%}{% include feature_row id="feature_row3" type="right" %}{%endraw%} <!-- feature_row3을 오른쪽 정렬로 출력 -->
```
- 기본으로 넓은 가로폭을 사용하고 사이드바가 없는 레이아웃
- Feature blocks를 사용하여 이미지를 왼쪽, 오른쪽, 가운데 정렬할 수 있다.

## Home page layout

```html
---
layout: home
classes: wide
entries_layout: grid
---
```
- 블로그 왼쪽 상단의 제목을 클릭하면 연결되는 홈페이지 레이아웃
- `_config.yml`의 **pagination**에서 설정한 숫자만큼의 포스트들을 최신 순으로 나열
- 프로젝트 최상단의 `index.html`에서 설정
