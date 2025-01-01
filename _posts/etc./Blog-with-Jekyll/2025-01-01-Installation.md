---
excerpt: "Github Pages와 Jekyll 및 minimal-mistakes 테마로 블로그 호스팅 및 설정하기"
title: "Github Pages & Jekyll Installation"
header:
  teaser: "https://jekyllrb.com/img/logo-2x.png"
categories:
  - Jekyll
tags:
  - Github Pages
  - HTML
  - Ruby
---

## Github Pages Hosting

1. GitHub Pages로 사용할 Repository 생성
   - 레포지토리 이름은 **(Github ID).github.io** 으로 설정
   - `https://(Github ID).github.io` 주소로 호스팅
2. git으로 로컬에 클론
   1. `code`에서 HTTPS 링크 복사
   2. 프로젝트를 다운받을 위치의 로컬 폴더를 우클릭해서 터미널을 열고 명령어 입력
       ```bash
       git clone (Repository URL)
       ```
3. VS Code 등의 편집기에서 클론된 폴더를 열어서 작업 가능

## Jekyll(지킬)

<a href="https://jekyllrb.com/" target="_blank">
  <img src="https://jekyllrb-ko.github.io/img/octojekyll.png" width="30%" alt="Jekyll webpage Link">
</a>

- 마크다운 파일로 작성하면 자동으로 HTML로 변환되기 때문에 쉽게 웹사이트를 꾸밀 수 있다
- Ruby로 만든 정적 웹사이트 생성기

## Jekyll Installation (macOS)

### 🛑 Ruby

1. Homebrew로 최신 버전 설치
    ```bash
    brew install ruby
    ```
2. 설치한 최신 버전을 사용하도록 경로 추가 후 연결
    ```bash
    echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
3. 최신 버전이 출력되는지 확인
   ```bash
   ruby --version
   ```

### 🧪 Jekyll

1. ruby의 패키지 관리 도구 RubyGems로 jekyll과 bundler 설치
    ```bash
    gem install jekyll bundler
    ```
2. 버전 확인
    ```bash
    jekyll -v
    bundler -v
    ```

## minimal-mistake Theme Installation

<a href="https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/" target="_blank">docs Link</a>      
<a href="https://github.com/mmistakes/minimal-mistakes" target="_blank">Github Repository Link</a>  

1. 레포지토리의 `code`에서 `Download ZIP` 으로 파일을 내려받은 후 압축 해제
2. 필요한 파일들만 복사해서 내 Github 레포지토리를 클론한 프로젝트의 최상단에 붙여넣기
3. `/assets` 안에 `/images` 폴더 생성 (이미지 저장용)

| files to Copy     | [files to Remove](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/#remove-the-unnecessary)            |
|-------------------|---------------------------------|
| /_data            | .editorconfig                   |
| /_includes        | .gitattributes                  |
| /_layouts         | .github                         |
| /_sass            | /docs                           |
| /assets           | /test                           |
| /docs/_drafts     | CHANGELOG.md                    |
| /docs/_pages      | minimal-mistakes-jekyll.gemspec |
| /docs/_posts      | README.md                       |
| .gitignore        | screenshot-layouts.png          |
| Gemfile           | screenshot.png                  |
| Rakefile          |                                 |
| LICENSE           |                                 |
| index.html        |                                 |
| package-lock.json |                                 |
| package.json      |                                 |
| _config.yml       |                                 |
| .travis.yml       |                                 |
| staticman.yml     |                                 |

## Setting at Local

### <a href="https://mmistakes.github.io/minimal-mistakes/docs/installation/#install-dependencies" target="_blank">Install dependencies</a>

```
source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

# gem "github-pages", group: :jekyll_plugins

# To upgrade, run `bundle update`.

gem "jekyll"
gem "minimal-mistakes-jekyll"

# The following plugins are automatically loaded by the theme-gem:
#   gem "jekyll-paginate"
#   gem "jekyll-sitemap"
#   gem "jekyll-gist"
#   gem "jekyll-feed"
#   gem "jekyll-include-cache"
#
# If you have any other plugins, put them here!
# Cf. https://jekyllrb.com/docs/plugins/installation/
group :jekyll_plugins do
end
```

1. `Gemfile` 파일의 원래 내용을 지우고 양식 붙여넣기
2. `# gem "github-pages", group: :jekyll_plugins` 주석 해제
3. `# The following plugins are automatically loaded by the theme-gem:` 밑 5개의 플러그인 주석 해제
4. `group :jekyll_plugins do` - `end` 안으로 주석 해제한 플러그인 5개를 이동
5. 파일 저장 후 VS Code의 터미널에서 변화 적용
    ```bash
    bundle install
    ```
<br>

### Run Jekyll

```bash
bundle exec jekyll serve
```
- Github에 Push하기 전 로컬 서버에서 미리 실행해서 확인할 수 있다.
- 로컬 서버 주소: http://127.0.0.1:4000/
- 서버 정지: `ctrl` + `c`
- **--livereload** 명령어 추가
   - 소스파일에서 변경사항이 생길 때마다 페이지 자동 새로고침
   - 예외로 `_config.yml` 파일을 변경할 경우에는 서버 정지 후 재실행 필요
- **--drafts** 명령어 추가
   - `/_drafts` 안에 있는 포스트까지 함께 로컬 서버에서 확인 가능
   - 실제 웹 서버에서는 나타나지 않기 때문에 게시물을 임시 저장하는 용도로 사용

### ⚠️ Errors

csv was loaded from the standard library, but will no longer be part of the default gems starting from Ruby 3.4.0.    
base64 was loaded from the standard library, but will no longer be part of the default gems starting from Ruby 3.4.0.   
{: style="color: red;" .small}

1. `Gemfile` 파일에 코드 추가 후 저장
    ```
    gem 'csv'
    gem 'base64'
    ```
2. gem 설치
    ```bash
    bundle install
    ```
<br>

cannot load such file -- webrick (LoadError)
{: style="color: red;" .small}
1. ruby 3.0.0 버전 이후부터 webrick 추가 필요
    ```bash
    bundle add webrick
    ```
2. gem 설치
    ```bash
    bundle install
    ```
<br>

ERROR '/favicon.ico' not found.
{: style="color: red;" .small}

1. 아래 사이트 중 한 곳에서 원하는 파비콘 생성
   + <https://www.favicon.cc/> (직접 픽셀에 점을 찍어서 파비콘을 제작하는 사이트)
   + <https://realfavicongenerator.net/>
2. `/assets` 안에 파비콘 파일 넣기
3. `/_iucludes` → `/head` → `custom.html`에 코드 추가
    ```html
    <link rel="icon" type="image/png" href="/assets/favicon.ico">
    ```
4. 웹 브라우저의 탭에서 사이트 제목 옆에 파비콘이 적용됐는지 확인하기

## git push

변경사항을 모두 git에 add
```bash
git add .
```
<br>

git에 커밋
```bash
git commit -m 'Commit message'
```
<br>

Github Pages 레포지토리로 push
```bash
git push
```