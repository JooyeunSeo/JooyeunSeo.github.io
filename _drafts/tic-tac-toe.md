---
layout: splash
excerpt: "fff"
title: "Tic Tac Toe"
header:
  teaser: "https://images.unsplash.com/photo-1695009327063-e50668c30d32?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://images.unsplash.com/photo-1695009327063-e50668c30d32?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%ED%98%B8%EB%B0%95%EA%B3%BC-%EC%A1%B0%EB%A1%B1%EB%B0%95%EC%9D%84-%EC%96%B9%EC%9D%80-%EB%82%98%EB%AC%B4-%ED%85%8C%EC%9D%B4%EB%B8%94-nWFdL88mKuQ)"
  actions:
    - label: "Download Zip"
      url: "https://github.com/JooyeunSeo/JooyeunSeo.github.io/raw/main/download/Morse_Code_Converter.zip"
    - label: "Try now"
      url: "https://dynamic-web-page-2bzr.onrender.com/morse_code_converter"
---

# Intro

*100개의 프로젝트로 Python 개발 완전 정복* 부트캠프에서 진행하는 전문 포트폴리오 프로젝트의 과제로 틱택토 게임을 구현해보았다. 

틱택토는 오목과 비슷한 보드게임으로, **규칙**은 다음과 같다.

- 두 명의 플레이어가 3x3 격자판에 번갈아가며 각자 자신의 표시(O 또는 X)를 기록한다.
- 같은 표시를 가로, 세로, 또는 대각선 상에 일직선으로 놓으면 승리한다.
- 한 플레이어가 먼저 승리하거나 더 이상 빈칸이 남지 않아 비길 때까지 계속된다.

**승리 상황**은 아래와 같이 8가지 경우의 수가 있다.

■■■&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□□■   
□□□&nbsp;&nbsp;&nbsp;&nbsp;■■■&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□■□   
□□□&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;■■■&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;■□□   

게임 시작 시 1p 또는 2p 중 하나를 선택한다.

<br><br><br>

# Analysis

- 게임 시작 시 1p 또는 2p 중 하나를 선택한다.
   - 1p를 고를시 컴퓨터와 플레이하게 되며, 선공은 무작위로 선택한다.
   - 
- 플레이어는 사용자와 컴퓨터이고 각각 O와 X 기호를 사용
- 빈 칸의 행, 열 좌표를 입력하여 기호를 표시 (사용자는 사용자 입력, 컴퓨터는 랜덤 선택)
- 승리, 무승부 또는 종료 요청이면 게임이 종료 (종료 요청은 사용자가 “0 0” 입력시 발생)
- 게임판을 텍스트로 출력하여 게임 진행
<br><br><br>

# 설계 Design 구조, 데이터, 인터페이스, UI 정의

- 2차원 리스트를 사용하여 게임판을 생성하고 각각의 칸을 빈칸으로 초기화
    - 빈칸에 대한 지정한 기호(*)를 사용
- 게임판에 빈칸이 남아있는지 확인
    - 게임판 전체를 확인하고 True/False 반환
- 둘 중 한 플레이어가 승리했는지 확인
    - 8가지의 승리 상황에 따른 가능성을 확인
    - 각각의 행, 열과 두 개의 대각선 방향을 확인


- 게임판의 현재 상태를 출력
- 게임을 시작
    - 무작위로 선공할 플레이어를 선택
- 게임 루프를 기동(1/3)
    - 게임판의 현재 상태를 출력하고 다음 플레이어가 빈칸을 선택
    - 루프는 사용자 또는 컴퓨터가 다음 말의 위치를 결정해줄 때까지 계속 대기


- 게임 루프를 기동(2/3)
    - 플레이어가 선택할 빈칸의 위치(행과 열 번호)를 입력받음
        - 사용자일 경우 사용자 입력을 통해 행과 열 번호를 입력받음
        - 컴퓨터일 경우 무작위로 행과 열 번호를 선택
    - 플레이어가 선택한 위치에 기호를 표시하고 게임판을 업데이트


- 게임 루프를 기동(3/3)
    - 현재 플레이어가 승리했는지 확인
        - 승리 상황인 경우, 승리한 플레이어에 대한 메시지를 출력하고 게임 루프를 종료
    - 게임판에 빈칸이 남아있는지 확인
        - 게임판이 가득찬 경우, 무승부 메시지를 출력하고 게임 루프를 종료
    - 게임이 종료될 때까지 게임 루프를 무한 반복


# 구현 Implementation 언어 선택, 코딩 규칙 정의, 프로그램 작성

<br><br><br>


# Future Improvements

<br><br><br>

# Conclusion

<br><br><br>