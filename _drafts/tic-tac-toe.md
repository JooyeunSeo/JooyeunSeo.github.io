---
layout: splash
excerpt: "Play tic tac toe game on 3 x 3 board with your friend or computer."
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
    > 8가지 승리 상황   
    > ■■■&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□□■   
    > □□□&nbsp;&nbsp;&nbsp;&nbsp;■■■&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□■□   
    > □□□&nbsp;&nbsp;&nbsp;&nbsp;□□□&nbsp;&nbsp;&nbsp;&nbsp;■■■&nbsp;&nbsp;&nbsp;&nbsp;■□□&nbsp;&nbsp;&nbsp;&nbsp;□■□&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;□□■&nbsp;&nbsp;&nbsp;&nbsp;■□□   
- 아래의 종료 조건 중 하나가 충족될 때까지 계속된다.
   - 한 플레이어가 먼저 승리
   - 더 이상 빈칸이 남지 않은 상황(무승부)
   - 플레이어가 종료 요청
<br><br>

사용자는 게임 시작 시 **1p** 또는 **2p** 중 하나를 선택할 수 있다.   

- 1p: 컴퓨터와 플레이하게 되며, 컴퓨터는 알고리즘에 따라 최선의 선택을 하도록 만들었다.   
- 2p: 다른 사람과 함께 플레이할 수 있다.
<br><br><br>

# Design

- 게임판의 상태를 텍스트로 출력
   - 2차원 리스트로 게임판을 생성한다.
   - 새 게임이 시작되면 먼저 모든 칸을 빈 칸으로 초기화(빈 칸은 `*` 기호로 표시)한다.
   - 빈 칸이 남아있는지 확인하려면 게임판 전체를 확인하고 True/False 반환한다.
   - 둘 중 한 플레이어가 승리했는지 확인하려면 8가지의 승리 상황과 같은지 확인한다.
- 게임 루프
   1. 원하는 표시(O 또는 X) 및 선공할 플레이어를 선택한다.
      - 1p: 사람이 선택
      - 2p: 첫 번째 플레이어가 선택
   2. 게임판의 현재 상태를 출력하고 다음 플레이어가 빈 칸 중 하나를 선택한다.
      - 사람: 원하는 빈 칸의 행과 열 번호를 입력
      - 컴퓨터: 알고리즘을 통해 행과 열 번호를 선택
   3. 입력을 확인한다.
      1. 사람이 게임 **종료 요청**(`0 0`)을 입력했을 경우, 바로 루프 종료
      2. 빈 칸 중 하나가 선택됐을 경우, 해당 위치에 기호를 표시하고 게임판을 업데이트한다.
   4. 업데이트된 게임판을 확인한다.
      1. 현재 플레이어가 승리했는지 확인 → **승리 상황**인 경우, 승리한 플레이어에 대한 메시지를 출력하고 루프 종료
      2. 게임판에 빈 칸이 남았는지 확인 → **게임판이 가득**찬 경우, 무승부 메시지를 출력하고 루프 종료
   5. 게임이 종료될 때까지 루프를 무한 반복
<br><br><br>

# Implementation

### Language



### Coding

<br><br><br>

# Result

<br><br><br>

# Future Improvements

<br><br><br>

# Conclusion

<br><br><br>



<https://tictactoefree.com/kr/gisa/maebeon-tiktaekto-igineun-bangbeob>   
<https://tictactoefree.com/kr/gyuchik>   
<https://tictactoefree.com/kr/gisa/tiktakto-du-beonjjae-sijak-igi>  
<https://www.youtube.com/watch?v=trKjYdBASyQ>