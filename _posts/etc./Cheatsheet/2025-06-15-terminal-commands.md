---
excerpt: "터미널에서 자주 사용하는 명령어 정리"
title: "Terminal Commands"
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Dir_command_in_Windows_Command_Prompt.png/500px-Dir_command_in_Windows_Command_Prompt.png"
categories:
  - Cheatsheet
tags:
last_modified_at: YYYY-MM-DDT00:30:30+09:00
---

## Linux (MacOS)

### man *command*
- manual
- 특정 명령어에 대한 사용법과 설명이 담긴 매뉴얼 페이지 출력

### clear
- 화면 지움
- 실제로는 화면을 아래로 내려서 이전 내용이 안 보이게 만드는 것

### pwd
- print working directory
- 현재 터미널이 위치한 디렉토리 경로를 출력

### open *path*
- 해당 경로를 파일 탐색기로 열기
- open `.` : 현재 디렉토리 열기

### ls
- list
- 현재 디렉토리의 파일 및 폴더 목록 출력
- 추가 매개변수
   - `-l` (long) : 자세한 정보 (권한, 소유자, 용량, 날짜 등)
   - `-a` (all) : 숨긴 파일까지 포함하여 표시

### cd *path*
- change directory
- 해당 경로의 디렉토리로 이동(현재 위치에서 접근 가능해야 함)
- cd `..` : 한 단계 상위 디렉토리
- cd `~` : 홈 디렉토리

### find *path* *options* *pattern*
- 해당 경로에서 조건에 맞는 패턴을 가진 파일이나 디렉토리를 검색
- 조건자 옵션
   - `-type` : 파일 또는 디렉토리 이름 기준 검색(e.g. `"file.txt"`)
   - `-iname` : 대소문자 구분 없이 이름 검색(e.g. `"*.jpg"`)
   - `-type` : 대상 종류 지정(e.g. `f`: 파일, `d`: 디렉토리)
   - `-size` : 크기 조건 검색(e.g. `+1M`, `-100k`)
   - `-exec` : 찾은 결과에 명령어 실행

### grep *options* *"keyword"* *file.txt*
- global regular expression print
- 해당 파일(주로 텍스트 파일)에서 검색어가 포함된 줄을 검색
- `*.txt` : 현재 디렉토리에서 검색어가 포함된 모든 txt 파일을 검색 
- 옵션
   - `-n` : 매칭된 줄 번호를 함께 출력
   - `-i` : 대소문자 구분 없이 검색 (insensitive)
   - `-r` : 하위 디렉토리까지 재귀 검색
   - `-v` : 해당 패턴이 없는 줄만 검색
   - `-c` : 매칭된 줄의 수만 출력
   - `-E` : 기본 grep보다 더 복잡한 정규 표현식 문법(ERE) 지원
   - `-F` : Fixed Strings 모드로, 정규 표현식 없이 문자열 그대로 검색

### which *command*
- 명령어가 시스템 경로 어디에 설치되어 있는지 확인
- PATH 환경변수에 등록된 디렉토리에서 가장 먼저 발견된 실행파일 경로를 출력
- 명령어가 어느 경로에서 실행되는지, 또는 여러 버전 중 어떤 게 쓰이는지 확인할 때 사용(e.g. python)

### mkdir *new_dir*
- make directory
- 해당 이름으로 새 디렉토리 생성

### touch *new_file.txt*
- 존재하지 않는 파일명 : 새 파일 생성
- 이미 존재하는 파일명 : 최근 수정 시간만 갱신

### cat *file.txt*
- concatenate
- 해당 파일(주로 텍스트 파일)의 내용 출력

### cp *source* *destination*
- copy
- 파일이나 디렉토리를 복사
- 예시
   - cp `a.txt` `b.txt` : a.txt를 복사해서 b.txt라는 이름으로 저장(이미 존재한다면 덮어씌워짐)
   - cp `a.txt` `dir/` : dir 디렉토리 내부에 a.txt가 복사됨

### mv *source* *destination*
- move
- 파일이나 디렉토리를 이동하거나 이름 변경
- 예시
   - mv `a.txt` `b.txt` : a.txt를 b.txt라는 이름으로 변경
   - mv `a.txt` `dir/` : a.txt를 dir 디렉토리 내부로 이동

### echo
- 문자열을 출력하거나 변수 값을 표시할 때 사용
- 예시(입출력 리디렉션 기호와 함께 사용 가능)
   - echo `"hello"` : 터미널에 텍스트 출력
   - echo `"hello"` `>` `file.txt` : 해당 파일에 텍스트 덮어씌움(존재하지 않는 파일이면 새로 생성)
   - echo `"world"` `>>` `file.txt` : 해당 파일 끝에 텍스트 추가

### rm
- remove
- 파일 또는 디렉토리 삭제
- 매개변수
   - `file.txt` : 파일 삭제
   - `-r` `dir/` : 디렉토리 삭제
   - `-rf` (recursively, forcibly) : 해당 디렉토리 강제 삭제(삭제할 위치 밖에서 실행)

### export *VAR=value*
- 환경변수를 등록하거나 하위 프로세스(자식 쉘 등)에 전달(현재 셸 세션 내에서만 유효)
- 등록 후 사용 가능한 명령어
   - **echo** `$VAR` : 해당 환경변수 값 출력
   - **env** : 현재 export된 모든 환경변수 목록 출력 가능
   - **unset** : 변수나 환경변수, 함수 등을 셸에서 삭제 가능
      - unset `VAR` : 환경변수 삭제
      - unset `-f` `myFunc` : 셸 함수 삭제
- 설정을 영구적으로 적용하려면 설정 파일에 등록하기
   1. **echo** `$SHELL` : 현재 사용하는 셸 확인
   2. 설정 파일 열기(**nano**, **vim** 등의 에디터 사용)
      - bash : `~/.bash_profile`, `~/.bashrc`
      - zsh : `~/.zshrc`
   3. 가장 아래에 `export VAR=value` 추가
   4. **source** `~/.filename` : 저장 후 설정 적용

### vim *file.txt*
- 리눅스/유닉스 계열에서 가장 많이 쓰이는 텍스트 에디터
- 파일을 열고 vim 모드 진입 후 명령어 사용 가능

<div class="notice" markdown="1">
< VI 편집기의 모드 >

1. **Normal Mode(명령 모드)**   
   - `u` → 마지막 작업 실행 취소
   - `dd` → 현재 줄 삭제
   - `yy` → 현재 줄 복사
   - `p` → 붙여넣기
   - `x` → 커서 아래 문자 삭제
   - `k`/`j`/`h`/`l` → 상/하/좌/우 이동
2. **Insert Mode(입력 모드)**   
   - 명령 모드에서 아래 키 중 하나로 진입 후 입력 시작
      - `i` → 현재 위치에서 입력 시작
      - `I` → 줄 맨 앞에서 입력 시작
      - `a` → 현재 위치 뒤에서 입력
      - `A` → 줄 맨 끝에서 입력
      - `o` → 아래 줄에 새 줄 만들고 입력
      - `O` → 위 줄에 새 줄 만들고 입력
   - 입력을 마치면 `Esc` 키로 다시 명령 모드 전환
3. **Command-line Mode(명령행 모드)**
   - 명령 모드에서 `:`으로 진입 후 화면 하단에 뜨는 : 뒤에 명령어 입력 가능
      - `:w` → 저장
      - `:q` → 변경사항 없을 시 그대로 종료
      - `:wq` → 저장하고 종료
      - `:q!` → 저장 안 하고 강제 종료
      - `:set` `nu` → 좌측에 행 번호 표시
      - `:set` `nonu` → 표시된 행 번호 숨기기 
      - `:/keyword` → 해당 단어 검색
</div>