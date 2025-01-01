---
excerpt: "_config.yml 파일을 수정하여 전반적인 블로그 구성을 변경하기"
title: "Configuration"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
  - HTML
  - Ruby
---
 
`_config.yml` 파일 수정 후 저장

## <a href="https://mmistakes.github.io/minimal-mistakes/docs/configuration/" target="_blank">Site Settings</a>

```yml
minimal_mistakes_skin    : "default"
# 스킨 목록: "air", "aqua", "contrast", "dark", "dirt", "neon", "mint", "plum", "sunrise"

locale                   : "en-US"  # 기본 언어 설정(한국어는 ko-KR)
rtl                      : # 아랍어 등 RTL 언어에서 텍스트 방향을 오른쪽→왼쪽으로 변경하는 옵션(defaults: false)
title                    : "블로그 제목"
title_separator          : "-"      # '블로그 제목 - 다른 텍스트'로 구분하는 문자
subtitle                 : # 사이트 제목 아래에 표시되는 짧은 태그라인이나 부제목
name                     : "사용자 이름"
description              : "블로그를 간단히 설명하는 문구(SEO에 사용됨)"
url                      : "https://(Github ID).github.io"
baseurl                  : ""       # 블로그가 루트 디렉토리가 아닌 하위 디렉토리에서 호스팅될 경우에만 설정
repository               : "GitHub ID/Repository name"
teaser                   : "/assets/images/teaser-image.png"    # 포스트 미리보기에서 나타나는 기본 티저 이미지
logo                     : "/assets/images/logo-image.png"      # 블로그 제목 앞에 표시할 로고 이미지
masthead_title           : "사이트 상단에 간결하게 표시될 제목"         # " " 으로 생략하면 title과 같음
breadcrumbs              : # 페이지의 탐색 경로를 표시하는 옵션(defaults: false)
words_per_minute         : 200  # 독자가 콘텐츠를 읽는 평균 속도 설정(예상 읽기 시간 계산에 사용됨)
enable_copy_code_button  : true # 코드 블록에 복사 버튼 유무
copyright                : # 저작권 정보 설정(defaults: site.title)
copyright_url            : # 저작권 url 설정(defaults: site.url)
```
**comments:** [이후 관련 포스트에서 진행](#)
```yml
reCaptcha:  # Google reCaptcha 서비스 사용 시 설정(사람과 봇을 구별하는 기능으로, 이 블로그에서는 생략)
atom_feed:  # jekyll-feed 플러그인(루트 경로에서 RSS 피드 파일을 제공)의 설정으로, 기본값 그대로 설정
search                   : true # 블로그 내 검색 기능 유무(상단 네비게이션 바의 가장 오른쪽에 표시됨)
search_full_content      : true # 블로그에서 검색 시 본문 내용 중 첫 50단어만 인덱싱하는 기능
search_provider          : lunr # 블로그 내 검색 기능 제공자(lunr, algolia, google 중 택 1)
lunr:       # 기본 라이브러리로, GitHub Pages와 호환됨
  search_within_pages    : false
```

## SEO Related

[이후 관련 포스트에서 진행](#)

## Analytics

[이후 관련 포스트에서 진행](#)

## Site Author

```yml
author:
  name             : "사용자 이름"                          
  avatar           : "/assets/images/profile-image.jpg"     # 프로필 사진 
  bio              : "프로필 사진 밑 소개글"
  location         : "Republic of Korea"                    # 사용자 거주지
  email            : # 밑에서 링크로 첨부하기 때문에 생략
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope"
      url: "mailto:example@email.com"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/ID"
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      # url: "https://twitter.com/"
    - label: "Facebook"
      icon: "fab fa-fw fa-facebook-square"
      # url: "https://facebook.com/"
    - label: "Instagram"
      icon: "fab fa-fw fa-instagram"
      # url: "https://instagram.com/"
```
- 블로그 왼쪽 사이드바 위에 표시되는 프로필 영역 설정
- 프로필 링크의 아이콘은 [Font Awesome](https://fontawesome.com/v6/search?m=free)에서 가져올 수 있다
   - e.g. HTML code가 `<i class="fa-brands fa-github"></i>` → "fab fa-fw fa-github"
   - e.g. HTML code가 `<i class="fa-solid fa-envelope"></i>` → "fas fa-fw fa-envelope"
- 이메일 주소에 링크를 달기 위해서 `mailto:` 추가

## Site Footer

```yml
footer:
  links:    # Site Author와 동일
```
- 블로그 하단 부분 설정
- FEED 아이콘이 표시되는 곳

## Outputting

```yml
permalink: /:categories/:title/     # 게시물 및 페이지의 URL 형식 정의
timezone: # 블로그의 시간대 설정(defaults: 해당 컴퓨터 OS의 로컬 시간)
```

## Pagination

### jekyll-paginate

```yml
paginate: 12                # 한 페이지에서 볼 수 있는 게시물의 개수 지정(defaults: 5)
paginate_path: /page:num/   # 페이지네이션 경로 정의
```
- gem jekyll-paginate 플러그인(defaults) 사용 시 설정
- `index.html`(홈페이지) 파일에서만 작동하기 때문에 category, tag, 및 collection page 에서도 적용하려면 jekyll-paginate-v2 플러그인을 설치해야 한다.

### jekyll-paginate-v2

jekyll-paginate보다 더 강력한 기능을 가진 플러그인

# YAML Front Matter Defaults

```yml
defaults:
  # _posts(모든 포스트에 적용)
  - scope:
      path: ""
      type: posts
    values:
      layout: single        # 레이아웃
      author_profile: true  # 유저 프로필 표시
      read_time: false      # (포스트 예상 읽는 시간 끔)
      show_date: true       # 작성일 표시
      comments: true        # 댓글 시스템 활성화
      share: true           # 소셜미디어 공유 링크 표시
      related: true         # 관련 게시물 표시
      toc: true             # 목차 표시
      toc_sticky: true      # 목차 상단 고정
      sidebar:              # 왼쪽 사이드바 표시
        title: "Posts"
        nav: "docs"
      header:               # 기본 헤더 이미지
        image: /assets/images/defaults/header-main.png
  # _pages(모든 페이지에 적용)
  - scope:
      path: ""
      type: pages
    values:
      layout: single        # 레이아웃
      author_profile: true  # 유저 프로필 표시
      sidebar:              # 왼쪽 사이드바 표시
        title: "Posts"
        nav: "docs"
```
- pages나 posts의 머릿말(Front Matter)에서 지정할 구성의 기본값 정의
- 개별 페이지나 포스트에서 다른 값으로 덮어쓰지 않는 한 여기서 설정한 값이 적용됨

## etc.

기본값 그대로 둔 설정들

- **Social Sharing:** 소셜 미디어에 페이지 공유 관련 설정
- **Reading files:** Jekyll이 처리할 파일과 무시할 파일을 지정
- **Conversion:** Markdown 프로세서(defaults: kramdown), 구문 하이라이팅 도구(defaults: rouge) 지정
- **Markdown processing:** kramdown 설정
- **Sass/SCSS:** Sass/SCSS 설정
- **Plugins:** GitHub Pages로 호스팅할 경우 사용될 플러그인을 whitelist에 지정
- **HTML compression:** HTML 압축 설정