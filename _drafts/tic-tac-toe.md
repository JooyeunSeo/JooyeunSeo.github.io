---
layout: splash
excerpt: "Play tic tac toe game on the 3 x 3 board against a friend or the AI."
title: "Tic Tac Toe"
header:
  teaser: "https://images.unsplash.com/photo-1695009327063-e50668c30d32?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: https://images.unsplash.com/photo-1695009327063-e50668c30d32?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/%ED%98%B8%EB%B0%95%EA%B3%BC-%EC%A1%B0%EB%A1%B1%EB%B0%95%EC%9D%84-%EC%96%B9%EC%9D%80-%EB%82%98%EB%AC%B4-%ED%85%8C%EC%9D%B4%EB%B8%94-nWFdL88mKuQ)"
  actions:
    - label: "Download Zip"
      url: "https://github.com/JooyeunSeo/JooyeunSeo.github.io/raw/main/download/Tic_Tac_Toe.zip"
    - label: "Try now"
      url: "https://dynamic-web-page-2bzr.onrender.com/morse_code_converter"
---

# Intro

*100개의 프로젝트로 Python 개발 완전 정복* 부트캠프에서 진행하는 전문 포트폴리오 프로젝트의 과제로 틱택토 게임을 구현해보았다. 다른 사람과 함께 플레이하거나, 컴퓨터와 플레이하는 두 가지 모드로 구성되어 있다. 컴퓨터는 미니맥스 알고리즘에 따라 항상 최선의 선택을 하도록 구현했다. 

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
   - 어느 한 플레이어가 종료를 요청
<br><br><br>

# Design

- 게임판의 상태를 텍스트로 출력
   - 2차원 리스트로 게임판을 생성한다.
   - 새 게임이 시작되면 먼저 모든 칸을 빈 칸(`" "`)으로 초기화한다.
   - 빈 칸이 남아있는지 확인하려면 게임판 전체를 확인하고 True/False 반환한다.
   - 둘 중 한 플레이어가 승리했는지 확인하려면 8가지의 승리 상황과 같은지 확인한다.
- 게임 루프
   1. 원하는 모드 및 선공할 플레이어를 선택한다.
      - 1p의 경우 사람이 선공/후공 선택 권한 소유
   2. 게임판의 현재 상태를 출력하고 다음 플레이어가 빈 칸 중 하나를 선택한다.
      - 사람: 원하는 칸의 행과 열 번호를 순서대로 입력 (e.g. 23)
      - 컴퓨터: 알고리즘을 통해 행과 열 번호를 선택
   3. 입력을 확인한다.
      - 사람이 게임 **종료 요청**(`"00"`)을 입력했을 경우, 루프 종료
      - 이미 선택된 칸을 고르거나 양식에 맞지 않게 입력한 경우, 메시지와 함께 다시 입력하도록 안내
      - 빈 칸 중 하나가 선택됐을 경우, 해당 위치에 기호를 표시하고 게임판을 업데이트
   4. 업데이트된 게임판을 확인한다.
      - 현재 플레이어가 승리했는지 확인 → **승리 상황**인 경우, 승리한 플레이어에 대한 메시지를 출력하고 루프 종료
      - 게임판에 빈 칸이 남았는지 확인 → **게임판이 가득**찬 경우, 무승부 메시지를 출력하고 루프 종료
      - 종료 조건이 아닐 경우, 다른 플레이어에게 턴 넘기기 
   5. 게임이 종료될 때까지 루프를 무한 반복한다.
<br><br><br>

# Implementation

### Language

파이썬

### Coding


<br><br>

### Computer AI

<a href="https://en.wikipedia.org/wiki/Minimax" target="_blank">Minimax algorithm(최소극대화 알고리즘)</a>을 활용해서 알고리즘을 만들었다. 이 규칙은 상대가 항상 나를 가장 불리하게 만드는 최적의 선택을 한다는 가정하에 내 차례에서 가장 좋은 선택을 하는 원리다. 틱택토, 체스, 오델로 등 2인이 플레이하는 게임에 널리 쓰이는 알고리즘이기 때문에 이 프로젝트에 적용시켜 보았다. 알고리즘이 잘 작동한다면 사람이 아무리 완벽히 플레이해도 AI를 이길 수 없다(비기는 것까지만 가능). 아래의 유투브를 참고해서 알고리즘을 이해하고 코드를 작성했다.

<div style="width: 50%;">
    <iframe src="https://www.youtube.com/embed/Bk9hlNZc6sE?start=3580" frameborder="0" allowfullscreen></iframe>
</div>
<br>

컴퓨터는 사람을 이기기 위해 다음과 같은 논리를 따른다.

**X(컴퓨터):** 이길 확률을 *최대화(Maximize)*하는 수를 선택   
**O(사람):** 컴퓨터는 사람이 항상 컴퓨터가 이길 가능성을 *최소화(Minimize)*하는 최적의 수를 둔다고 가정   
<br>

**루프**
1. 현재 게임판 상태가 종료 조건에 속하지 않을 경우 게임판을 파이썬 내장 모듈 copy로 deep copy한다(실제 게임에 사용되는 게임판에 표시하면 안 되기 때문).
2. 복사된 게임판에서 아래의 순서를 따른다.
   1. 보드의 각 칸을 순회하며 빈 칸을 수집
   2. 각 칸마다 기호를 표시한 후 재귀 호출하는 것을 반복
      - 해당 칸에 수를 뒀을 경우 가능한 모든 다음 상황에 대해 살펴보는 것
      - 모든 케이스마다 점수를 부여
   3. 게임판이 종료 조건을 만족하는 상태가 됐을 때 재귀 호출 스탑
3. 각 케이스마다 점수를 확인하고 합산한다.
<br><br>

**점수 평가법**

가장 마지막 케이스(종료 조건이 되는 케이스)부터 점수 계산을 시작해서 위로 거슬러 올라간다.

1. 게임 종료 케이스에서는 다음과 같이 계산한다.
   - 컴퓨터가 이기는 상황: `+1`의 점수 부여
   - 컴퓨터가 지는(사람이 이기는) 상황: `-1`의 점수 부여
   - 비기는 상황: `0`의 점수 부여
2. 자식 케이스들이 있는 경우, 현재 턴에 따라 점수 계산 방식이 달라진다.
   - 다음 차례가 컴퓨터: 자식 케이스들 중 가장 높은(max) 점수를 선택
   - 다음 차례가 사람: 자식 케이스들 중 가장 낮은(min) 점수를 선택

<br>
<pre>
                                        Current Board
                                        +---+---+---+
                                        |   | O | X |
                                        +---+---+---+
                                        | O |   | X |
                                        +---+---+---+
                                        | X |   | O |
                                        +---+---+---+
                                        next: human(●) 
                                        min(+1, -1, +1) = -1

         👤Case 1                        👤Case 2                        👤Case 3
        +---+---+---+                   +---+---+---+                   +---+---+---+
        | ● | O | X |                   |   | O | X |                   |   | O | X |
        +---+---+---+                   +---+---+---+                   +---+---+---+
        | O |   | X |                   | O | ● | X |                   | O |   | X |
        +---+---+---+                   +---+---+---+                   +---+---+---+
        | X |   | O |                   | X |   | O |                   | X | ● | O |
        +---+---+---+                   +---+---+---+                   +---+---+---+
        next: com(✖)                    next: com(✖)                    next: com(✖)
        max(+1, -1) = +1                max(-1, -1) = -1                max(-1, -1) = +1

 🤖Case 1-1      🤖Case 1-2      🤖Case 2-1      🤖Case 2-2      🤖Case 3-1      🤖Case 3-2
+---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
| ● | O | X |   | ● | O | X |   | ✖ | O | X |   |   | O | X |   | ✖ | O | X |   |   | O | X |
+---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
| O | ✖ | X |   | O |   | X |   | O | ● | X |   | O | ● | X |   | O |   | X |   | O | ✖ | X |
+---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
| X |   | O |   | X | ✖ | O |   | X |   | O |   | X | ✖ | O |   | X | ● | O |   | X | ● | O |
+---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
game over       next: human(●)  next: human(●)  next: human(●)  next: human(●)  game over
(score: +1)     min(-1) = -1    min(-1) = -1    min(-1) = -1    min(-1) = -1    (score: +1)

                 👤Case 1-2-1    👤Case 2-1-1    👤Case 2-2-1    👤Case 3-1-1
                +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
                | ● | O | X |   | ✖ | O | X |   | ● | O | X |   | ✖ | O | X |
                +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
                | O | ● | X |   | O | ● | X |   | O | ● | X |   | O | ● | X |
                +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
                | X | ✖ | O |   | X | ● | O |   | X | ✖ | O |   | X | ● | O |
                +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
                game over       game over       game over       game over
                (score: -1)     (score: -1)     (score: -1)     (score: -1)
</pre><br>

**최대화/최소화 스위칭**

- 변수 `maximizing`에 bool값을 저장
   - 컴퓨터의 턴에서는 True가 되어서 가능한 케이스 중 가장 큰 점수를 고른다.
   - 사람의 턴에서는 False가 되어서 가능한 케이스 중 가장 작은 점수를 고른다.
<br><br><br>

# Result

<img src="/assets/images/personal-projects/tic_tac_toe_1.png" 
     width="60%">

AI와 easy 레벨로 겨루기 모드를 선택   
<br>

<img src="/assets/images/personal-projects/tic_tac_toe_2.png" 
     width="60%">

AI가 easy 레벨에서 랜덤으로 칸을 선택하는 모습   
<br>

<img src="/assets/images/personal-projects/tic_tac_toe_3.png" 
     width="60%">

1p 모드에서 AI를 이겼을 때(easy 레벨)   
<br>

<img src="/assets/images/personal-projects/tic_tac_toe_4.png" 
     width="60%">

1p 모드에서 무승부일 때   
<br>

<img src="/assets/images/personal-projects/tic_tac_toe_5.png" 
     width="60%">

AI가 hard 레벨에서 미니맥스 알고리즘으로 최적의 칸을 선택하는 모습   
<br>

<img src="/assets/images/personal-projects/tic_tac_toe_6.png" 
     width="60%">

1p 모드에서 AI에게 졌을 때   
<br>

<img src="/assets/images/personal-projects/tic_tac_toe_7.png" 
     width="60%">

2p 모드를 선택(올바른 값이나 빈 칸을 입력해야 게임판에 표시할 수 있는 구조)
<br>

<br><br><br>

# Future Improvements

<br><br><br>

# Conclusion

<br><br><br>



<https://tictactoefree.com/kr/gisa/maebeon-tiktaekto-igineun-bangbeob>   
<https://tictactoefree.com/kr/gyuchik>   
<https://tictactoefree.com/kr/gisa/tiktakto-du-beonjjae-sijak-igi>  
<https://www.youtube.com/watch?v=trKjYdBASyQ>


