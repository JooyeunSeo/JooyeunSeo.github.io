---
excerpt: "상단 네비게이션 메뉴와 왼쪽 사이드바 네비게이션 메뉴 커스텀하기"
title: "Navigation (Masthead & Sidebar)"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
---

`/_data` → `navigation.yml`

## <a href="https://mmistakes.github.io/minimal-mistakes/docs/navigation/" target="_blank">Masthead</a>

```yml
main:
  - title: "About"            # 소개 페이지로 연결
    url: /about/		  
  - title: "Posts"            # 포스트를 연도별로 모아놓은 페이지로 연결
    url: /year-archive/
  - title: "Categories"       # 카테고리별로 콘텐츠를 분류한 페이지로 연결
    url: /categories/
  - title: "Tags"             # 태그별로 포스트를 분류한 페이지로 연결
    url: /tags/
  - title: "Pages"            # /_pages 의 페이지들을 나열한 페이지로 연결
    url: /page-archive/
  - title: "Collections"      # 콘텐츠 유형을 그룹화한 페이지로 연결
    url: /collection-archive/
  - title: "External Link"    # 외부 웹사이트로 연결되는 링크
    url: 해당 페이지 url 링크
    target: _blank	  # 외부 링크를 새로운 탭에서 열도록 설정
```
- `/_pages`에 포함된 샘플 페이지들을 활용한 상단 네비게이션 예시
- **title:** 네비게이션에 표시될 이름
- **url:** 연결하려는 페이지에 명시된 permalink와 동일하게 작성


## <a href="https://mmistakes.github.io/minimal-mistakes/docs/layouts/#custom-sidebar-navigation-menu" target="_blank">Sidebar</a>

### Sidebar Custom

```yml
docs:
  - title: "대분류1"
    children:
      - title: "소분류1"
        url: /소분류1/
        category: "카테고리 이름"
      - title: "소분류2"
        url: /소분류2/
        category: "카테고리 이름"
  - title: "대분류2"
    children:
      - title: "소분류1"
        url: /
        category:
      - title: "소분류2"
        url: /
        category:
      - title: "소분류3"
        url: /
        category:
```
- 화면 왼쪽에 표시되는 프로필 밑에 위치하는 사이드바 예시
- 한 **대분류** title 안에 **소분류들**이 들어가는 구조
- 위와 마찬가지로 url는 연결하려는 페이지에 명시된 permalink와 동일해야 한다.

### Pull the Sidebar Links

```markdown
---
sidebar:
  title: "사이드바 제목"
  nav: docs
---
```
- 해당 YAML Front Matter를 사이드바를 활성화하려는 포스트 및 페이지에 더하기
- 여러 페이지들에서 사용될 경우 `_config.yml`에서 디폴트값으로 설정하는 것이 더 편하다.    
(<a href="https://jooyeunseo.github.io/jekyll/Configuration/#yaml-front-matter-defaults" target="_blank">YAML Front Matter Defaults</a> 설정 참조)