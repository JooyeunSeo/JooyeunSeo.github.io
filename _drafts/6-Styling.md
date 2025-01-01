---
excerpt: "블로그 스타일을 구체적으로 커스텀하기"
title: "Styling"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
  - HTML
  - Ruby
---

## Width

`/_sass` → `/_minimal-mistakes` → `_variables.scss`
```scss
/*
   Grid
   ========================================================================== */
$right-sidebar-width-narrow: 180px !default;  /* default: 200px */
$right-sidebar-width: 220px !default;         /* default: 300px */
$right-sidebar-width-wide: 250px !default;    /* default: 400px */
```
- single 레이아웃에서는 게시물의 가로 너비가 너무 좁아서 더 넓게 조정했다.
- 양 옆의 사이드를 줄이는 방식으로 넓히기  

## Font Size

`/_sass` → `/_minimal-mistakes` → `_reset.scss`
```scss
html {
  /* apply a natural box layout model to all elements */
  box-sizing: border-box;
  background-color: $background-color;
  font-size: 15px;      /* Default: $doc-font-size; */

  @include breakpoint($medium) {
    font-size: 16px;    /* Default: $doc-font-size-medium; */
  }

  @include breakpoint($large) {
    font-size: 16px;    /* Default: $doc-font-size-large; */
  }

  @include breakpoint($x-large) {
    font-size: 17px;    /* Default: $doc-font-size-x-large; */
  }

  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
}
```
- 전체적으로 폰트 사이즈를 축소시킴
- 화면 크기를 여러가지로 조정하며 각 화면에 맞는 사이즈를 테스트해야 한다.

## Hyperlink Underline

`/_sass` → `/_minimal-mistakes` → `_base.scss`
```scss
/* links */

a {
  text-decoration: none;  /* remove hyperlink underline */

  &:focus {
    @extend %tab-focus;
  }

  &:visited {
    color: $link-color-visited;
  }

  &:hover {
    color: $link-color-hover;
    outline: 0;
  }
}
```
- 기본 설정은 하이퍼링크된 텍스트 밑에 밑줄이 그어진다.
- 깔끔한 디자인을 위해 밑줄 제거


## <a href="https://github.com/mmistakes/minimal-mistakes/issues/1731" target="_blank">Back to top</a>

`/_sass` → `/_minimal-mistakes` → `_sidebar.scss`
```scss
/* Add a new custom class for 'Back to top' button */
.sidebar__top {
  position: fixed;
  bottom: 1.5em;
  right: 2em;
  z-index: 10;
}

.sidebar__right {
  ...
}
```
<br>

`/_layouts` → `default.html`
```html
    <div id="footer" class="page__footer">
      ...
    </div>

    <!-- include the custom class for 'Back to top' button -->
    <aside class="sidebar__top">
      <a href="#site-nav"><i class="fas fa-circle-arrow-up fa-3x"></i></a>
    </aside>
```
- 글 어느 부분에서든 한 번에 맨 위로 올라가는 버튼 추가
- 화면 오른쪽 하단에 고정된 버튼이 나타난다.
- <a href="https://fontawesome.com/v6/search?m=free" target="_blank">Font awesome</a>에서 원하는 아이콘을 첨부하고 크기 조절하기   


## Number of Posts

`/_includes` → `nav_list`
```liquid
{% raw %}{% assign navigation = site.data.navigation[include.nav] %}{% endraw %}

{% raw %}{% assign categories_max = 0 %}{% endraw %}
{% raw %}{% for category in site.categories %}
  {% if category[1].size > categories_max %}
    {% assign categories_max = category[1].size %}
  {% endif %}
{% endfor %}{% endraw %}

{% raw %}{% assign tags_max = 0 %}{% endraw %}
{% raw %}{% for tag in site.tags %}
  {% if tag[1].size > tags_max %}
    {% assign tags_max = tag[1].size %}
  {% endif %}
{% endfor %}{% endraw %}

<nav class="nav__list">
  {% raw %}{% if page.sidebar.title %}<h3 class="nav__title" style="padding-left: 0;">{{ page.sidebar.title }}</h3>{% endif %}{% endraw %}
  <input id="ac-toc" name="accordion-toc" type="checkbox" />
  <label for="ac-toc">{{ site.data.ui-text[site.locale].menu_label | default: "Toggle Menu" }}</label>
  <ul class="nav__items">
    {% raw %}{% for nav in navigation %}
      <li>
        {% if nav.url %}
          <a href="{{ nav.url | relative_url }}"><span class="nav__sub-title">{{ nav.title }}</span></a>
        {% else %}
          <span class="nav__sub-title">{{ nav.title }}</span>
        {% endif %}

        {% if nav.children != null %}
        <ul>
          {% for child in nav.children %}
          {% assign category = site.categories[child.category] | where_exp: "item", "item.hidden != true" %}
            <li><a href="{{ child.url | relative_url }}"{% if child.url == page.url %} class="active"{% endif %}>{{ child.title }} ({{ category.size }})</a></li>
          {% endfor %}
        </ul>
        {% endif %}
      </li>
    {% endfor %}{% endraw %}
  </ul>
</nav>
```

- 파일 전체를 위와 같이 수정
- 사이드바에서 각 카테고리별 아카이브 페이지 링크 옆에 포스트 개수가 표시된다.