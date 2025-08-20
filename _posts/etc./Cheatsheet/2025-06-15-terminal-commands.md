---
excerpt: "터미널에서 자주 사용하는 단축키 및 명령어 정리"
title: "Terminal Shortcut Keys & Commands"
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Dir_command_in_Windows_Command_Prompt.png/500px-Dir_command_in_Windows_Command_Prompt.png"
categories:
  - Cheatsheet
tags:
  - Bash
  - Regular Expression
last_modified_at: 2025-08-19T00:30:30+09:00
---

## ⌨️ Shortcut Keys

- `Tab` : 파일 또는 디렉토리 이름 자동완성 ⭐️
- `Ctrl(⌃)` + `A` : 커서를 줄 맨 앞으로 이동 ⭐️
- `Ctrl(⌃)` + `E` : 커서를 줄 맨 끝으로 이동 ⭐️
- `Ctrl(⌃)` + `B` : 커서를 한 글자 왼쪽으로 이동
- `Ctrl(⌃)` + `F` : 커서를 한 글자 오른쪽으로 이동
- `Ctrl(⌃)` + `U` : 커서 기준 왼쪽 모두 삭제 ⭐️
- `Ctrl(⌃)` + `K` : 커서 기준 오른쪽 모두 삭제 ⭐️
- `Ctrl(⌃)` + `W` : 커서 왼쪽 방향으로 한 단어씩 삭제(스페이스 단위)
- `Ctrl(⌃)` + `Y` : 직전에 삭제한 텍스트 붙여넣기
- `Ctrl(⌃)` + `L` : 화면 전체 지움(`clear`와 동일)
- `Ctrl(⌃)` + `T` : 커서 앞 두 글자 순서 변경(오타 정정할 때 유용)
- `Ctrl(⌃)` + `C` : 현재 입력 취소 / 실행 중인 프로세스 강제 종료 ⭐️
- `Ctrl(⌃)` + `D` : 입력줄 비어 있을 때 사용 시 현재 shell 종료
- `Ctrl(⌃)` + `Z` : 실행 중인 프로세스를 백그라운드로 보내기 (일시정지)

## 📁 Directory
### pwd
- Print Working Directory
- 현재 터미널이 위치한 디렉토리 경로를 출력

### ls
- list
- 현재 디렉토리 내의 모든 파일 및 폴더 목록 출력
- 옵션
   - `-l` (long) : 자세한 정보 (권한, 소유자, 용량, 날짜 등)
   - `-a` (all) : 숨긴 파일까지 포함하여 표시

### mkdir *<font color="#ffe474">new_dir1</font>* *<font color="#ffe474">new_dir2</font>*
- Make Directory
- 해당 이름으로 새 디렉토리(들) 생성

### rmdir *<font color="#ffe474">empty_dir</font>*
- Remove Directory
- 해당 디렉토리가 비어있을 시 삭제
- 빈 폴더 정리용(실제 삭제는 `rm` 사용)

### cd *<font color="#d3a27f">path</font>*
- Change Directory
- 해당 경로의 디렉토리로 이동(현재 위치에서 접근 가능해야 함)
- cd `..` : 한 단계 상위 디렉토리
- cd `~` : 홈 디렉토리

<!---------------- ---------------->
## 📄 File
### touch *<font color="#87c4f8">new_file.txt</font>*
- 존재하지 않는 파일명 : 새 파일 생성
- 이미 존재하는 파일명 : 최근 수정 시간만 갱신

### open *<font color="#d3a27f">path</font>*
- 해당 경로를 파일 탐색기로 열기
- open `.` : 현재 디렉토리 열기

### cp *<font color="#93bf85">source</font>* *<font color="#77bbc2">destination</font>*
- Copy
- 파일이나 디렉토리를 복사
- 예시
   - cp `a.txt` `b.txt` : a.txt를 복사해서 b.txt라는 이름으로 저장(이미 존재한다면 덮어씌워짐)
   - cp `a.txt` `dir/` : dir 디렉토리 내부에 a.txt가 복사됨

### rm *<font color="#87c4f8">file1.txt</font>* *<font color="#87c4f8">file2.txt</font>*
- Remove
- 파일이나 디렉토리 삭제 (삭제하면 바로 사라짐!)
- 옵션
   - `-i` : 삭제 전 확인
   - `-r` : 해당 디렉토리 및 그 안의 모든 파일/하위 디렉토리까지 재귀 삭제 

### mv *<font color="#93bf85">source</font>* *<font color="#77bbc2">destination</font>*
- move
- 파일이나 디렉토리를 이동하거나 이름 변경
- 예시
   - mv `a.txt` `b.txt` : a.txt를 b.txt라는 이름으로 변경
   - mv `a.txt` `dir/` : a.txt를 dir 디렉토리 내부로 이동

### cat *<font color="#87c4f8">file.txt</font>*
- Concatenate
- 해당 파일(주로 텍스트 파일)의 내용 출력

### chmod
- Change Mode
- 파일이나 디렉토리의 권한 지정 및 변경

### chown
- Change Owner
- 파일이나 디렉토리의 소유자 변경

<!---------------- ---------------->
## 📚 Text Processing
### head *<font color="#87c4f8">file.txt</font>*&nbsp;&nbsp;&nbsp;<br>tail *<font color="#87c4f8">file.txt</font>*
- 파일의 앞부분/뒷부분만 출력(default: 10줄)
- 여러 개의 파일 출력 가능
- 옵션
   - `-n` `num` : 처음/마지막 num 개의 줄 출력
   - tail `-f` : 내용이 변경될 때마다 실시간으로 출력(tail에만 존재, 로그 파일에서 활용)

### find *<font color="#d3a27f">path</font>* *<font color="#ffd090">options</font>* *<font color="#ffc4ff">pattern</font>*
- 해당 경로에서 조건에 맞는 패턴을 가진 파일이나 디렉토리를 검색
- 조건자 옵션
   - `-type` : 파일 또는 디렉토리 이름 기준 검색(e.g. `"file.txt"`)
   - `-iname` : 대소문자 구분 없이 이름 검색(e.g. `"*.jpg"`)
   - `-type` : 대상 종류 지정(e.g. `f`: 파일, `d`: 디렉토리)
   - `-size` : 크기 조건 검색(e.g. `+1M`, `-100k`)
   - `-exec` : 찾은 결과에 명령어 실행

### grep *<font color="#ffd090">options</font>* *<font color="#d7bce4">"keyword"</font>* *<font color="#87c4f8">file.txt</font>*
- Global Regular Expression Print
- 해당 파일(주로 텍스트 파일)에서 검색어가 포함된 줄을 검색
- `*.txt` : 현재 디렉토리에서 검색어가 포함된 모든 txt 파일을 검색
- `| grep` 조합은 원하는 정보만 걸러내기 위해 자주 사용됨
   - **ls** `-al` `|` **grep** `"\.log$"` : 확장자가 .log인 파일만 출력
   - **cat** `file.txt` `|` **grep** `"ERROR"` : 파일에서 "ERROR"가 포함된 줄만 출력
- 옵션
   - `-n` : 매칭된 줄 번호를 함께 출력
   - `-i` : 대소문자 구분 없이 검색 (insensitive)
   - `-r` : 하위 디렉토리까지 재귀 검색
   - `-v` : 해당 패턴이 없는 줄만 검색
   - `-c` : 매칭된 줄의 수만 출력
   - `-E` : 기본 grep보다 더 복잡한 정규 표현식 문법(ERE) 지원
   - `-F` : Fixed Strings 모드로, 정규 표현식 없이 문자열 그대로 검색

<!---------------- ---------------->
## 📌 Environment Variables
### export *<font color="#ffafaf">VAR=value</font>*
- 사용자 환경변수(대문자)를 전역 변수로 설정
- 현재 셸 및 자식 프로세스에서 사용 가능하며, 터미널 종료시 사라짐
- 등록 후 사용 가능한 명령어
   - **echo** <font color="#ffafaf">$</font>`VAR` : 해당 환경변수 값 출력
   - **env** : 현재 export된 모든 환경변수 목록 출력
   - **unset** : 변수나 환경변수, 함수 등을 셸에서 삭제
      - unset `VAR` : 환경변수 삭제
      - unset `-f` `myFunc` : 셸 함수 삭제
- 설정을 영구적으로 적용하려면 설정 파일에 등록 필요
   1. **echo** <font color="#ffafaf">$</font>`SHELL` : 현재 사용하는 셸 확인
   2. 설정 파일 열기(**nano**, **vim** 등의 편집기 사용)
      - bash : `~/.bash_profile`, `~/.bashrc`
      - zsh : `~/.zshrc`
   3. 가장 아래에 `export VAR=value` 추가
   4. **source** `~/.filename` : 저장 후 설정 적용

### echo
- 문자열을 출력하거나 변수 값을 표시할 때 사용
- 예시(입출력 리디렉션 기호와 함께 사용 가능)
   - echo `"hello"` : 터미널에 텍스트 출력
   - echo `"hello"` `>` `file.txt` : 해당 파일에 텍스트 덮어씌움(존재하지 않는 파일이면 새로 생성)
   - echo `"world"` `>>` `file.txt` : 해당 파일 끝에 텍스트 추가

<!---------------- ---------------->
## ⚙️ System
### ping *<font color="#b8b4b4">ADDRESS</font>*
- Packet Internet Groper
- IP 또는 도메인의 주소를 넣어 해당 네트워크의 상태를 확인
- `Ctrl-C`로 강제 종료하기 전까지 계속 출력됨
- 옵션
   - `-c` `num` : 입력된 숫자만큼만 출력되도록 제한
   - `-i` `sec` : 전송 간격 조정(default: 1초) 

### uname
- 현 시스템의 정보 출력
- 옵션
   - `-a` : 모든 정보
   - `-c` : 커널 이름
   - `-n` : 호스트 이름
   - `-r` : 커널 릴리즈 버전
   - `-v` : 커널 빌드 정보

<!---------------- ---------------->
## ➡️ Process
### ps
- Process State
- 현재 실행 중인 프로세스와 상태를 출력
- 옵션
   - `-a` : 모든 사용자 프로세스 표시
   - `-u` : 사용자 정보 포함
   - `-x` : 터미널에 종속되지 않은 프로세스도 포함

### kill *<font color="#b8b4b4">PID</font>*
- 해당 PID(프로세스 ID, ps 명령어로 확인 가능) 프로세스 종료
- kill `-9` `PID` : 강제 종료(SIGKILL)

<!---------------- ---------------->
## etc.
### man *<font color="#b0b0af">command_name</font>*
- Manual
- 특정 명령어에 대한 사용법과 설명이 담긴 매뉴얼 페이지 출력

### history
- 지금까지 입력한 명령어 기록 목록 출력
- history `num` : 입력한 개수만큼 출력

### clear
- 화면 지움
- 실제로는 화면을 아래로 내려서 이전 내용이 안 보이게 만드는 것

### which *<font color="#b0b0af">command_name</font>*
- 명령어가 시스템 경로 어디에 설치되어 있는지 확인
- PATH 환경변수에 등록된 디렉토리에서 가장 먼저 발견된 실행파일 경로를 출력
- 명령어가 어느 경로에서 실행되는지, 또는 여러 버전 중 어떤 게 쓰이는지 확인할 때 사용(e.g. python)

### vim *<font color="#87c4f8">file.txt</font>*
- 리눅스/유닉스 계열에서 가장 많이 쓰이는 텍스트 에디터
- 파일을 열고 vim 모드 진입 후 명령어 사용 가능

<div class="notice" markdown="1">
< VI 편집기의 모드 >

1. **Normal Mode(명령 모드)**   
   - `u` = 마지막 작업 실행 취소
   - `dd` = 현재 줄 삭제
   - `yy` = 현재 줄 복사
   - `p` = 붙여넣기
   - `x` = 커서 아래 문자 삭제
   - `h`/`j`/`k`/`l` = **←**/**↓**/**↑**/**→** 이동
2. **Insert Mode(입력 모드)**   
   - 명령 모드에서 아래 키 중 하나로 진입 후 입력 시작
      - `i` = 현재 위치에서 입력 시작
      - `I` = 줄 맨 앞에서 입력 시작
      - `a` = 현재 위치 뒤에서 입력
      - `A` = 줄 맨 끝에서 입력
      - `o` = 아래 줄에 새 줄 만들고 입력
      - `O` = 위 줄에 새 줄 만들고 입력
   - 입력을 마치면 `Esc` 키로 다시 명령 모드 전환
3. **Command-line Mode(명령행 모드)**
   - 명령 모드에서 `:`으로 진입 후 화면 하단에 뜨는 : 뒤에 명령어 입력 가능
      - `:w` = 저장
      - `:q` = 변경사항 없을 시 그대로 종료
      - `:wq` = 저장하고 종료
      - `:q!` = 저장 안 하고 강제 종료
      - `:set` `nu` = 좌측에 행 번호 표시
      - `:set` `nonu` = 표시된 행 번호 숨기기 
      - `:/keyword` = 해당 단어 검색
</div>