---
date: 2025-03-23
layout: splash
excerpt: "Inspired by the classic arcade video game released in 1976 by Atari, Inc. <br>Bounce a ball with a paddle to break all the bricks."
title: "Breakout"
header:
  teaser: "https://images.unsplash.com/photo-1558244661-d248897f7bc4?q=80&w=2957&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  overlay_color: "#000"
  overlay_filter: "0.4"
  overlay_image: https://images.unsplash.com/photo-1558244661-d248897f7bc4?q=80&w=2957&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/blue-red-and-white-artwork-lQT_bOWtysE)"
  actions:
    - label: "Download Zip"
      url: "https://drive.google.com/uc?id=1s0-E6TCHegkuxGf8axxG5Kqs2O9QI-iV&export=download" 
---
**Note:** The file is large, so Google Drive may display a warning before download. This is normal.

---

# Intro

Python의 turtle 라이브러리리를 이용해서 만든 벽돌깨기 게임이다. 부트캠프 *100개의 프로젝트로 Python 개발 완전 정복* 의 22일차에서 만들었던 Pong 게임을 많이 응용해야 했다.   
움직이는 공을 패들로 받아서 화면의 모든 벽돌을 깨면 다음 레벨로 넘어가고, 각 레벨마다 4개의 아이템이 랜덤한 블록에 생성된다. 아이템 종류는 '생명 1개 추가', '점수 2배 적용', '패들 길이 연장', '공 파워 증가'가 있다. 공이 튕기는 횟수가 많아질수록 가속도가 조금씩 붙고, 공을 잃어서 속도가 리셋되어도 레벨이 높을수록 기본 속도값이 높기 때문에 점점 난이도가 올라가는 구조다.
주어진 생명 3개와 여러 아이템을 이용해서 최대한 높은 레벨과 점수를 기록하는 것을 목표로 한다.
<br><br><br>

# Design

- GUI 및 UX
   - turtle 라이브러리로 GUI 구성
   - 키보드 입력
      - 왼쪽, 오른쪽 방향키로 패들을 양 옆으로 이동한다.
      - 스페이스바로 게임을 시작한다.
      - 게임오버 시 r키로 게임을 다시 시작할 수 있다. 
   - 색상 변화
      - 아이템 효과가 적용 중인 객체의 색을 흰색에서 노란색으로 변경한다.
      - 아이템 지속 시간이 끝나면 객체의 색을 다시 기본 흰색으로 변경한다.
- 클래스 구조
   - Game: 게임 진행을 담당하는 메인 클래스로, turtle 스크린과 모든 객체들을 관리한다.
   - Menu: 화면 상단에 현재 보유 중인 생명, 레벨, 점수를 표시하는 객체를 관리한다.
   - Bar: 공을 받는 패들 객체와 관련 함수에 해당한다. 
   - Ball: 공 객체와 관련 함수에 해당한다.
   - Block: 벽돌 객체와 아이템 객체를 생성한다.
- 충돌
   - 공이 화면 가장자리(왼쪽, 오른쪽, 상단 벽)에 닿으면 반대 방향으로 튕긴다.
   - 공이 패들에 닿으면 위치에 따라 적절한 방향으로 튕긴다.
   - 공이 벽돌에 닿으면 위치에 따라 적절한 방향으로 튕긴다.
   - 공이 화면 하단에 닿으면 해당 공을 잃은 것으로 간주하고 생명을 1개 잃는다.
- 벽돌 1개를 깰 때마다 10점씩 추가한다.
- 생명은 최대 3개까지 보유 가능하며, 공을 한 번 잃을 때마다 하나씩 줄어든다.
- 아이템 효과
   1. Life up: 생명을 1개 늘린다(이미 최대치를 보유한 경우 스킵).
   2. Double score: 벽돌을 1개 깰 때마다 점수를 2배씩 올린다.
   3. Bar extention: 패들의 길이를 늘린다.
   4. Ball power up: 공이 한 번에 블럭을 2개씩 깬다.
- while문 반복
   - `ready`: True, `gameover`: False로 초기화하고 시작한다.
   - `ready` 상태가 True이면 공을 날리기 전 대기하는 단계로, 패들만 움직일 수 있고 공은 패들 위에 붙은 상태를 유지한다.
   - 공을 날리면 `ready`가 False로 바뀌고 움직이는 공을 패들로 받을 수 있다.
   - 화면의 모든 벽돌을 깨면 다음 레벨로 넘어가고 다시 벽돌이 리셋된다.
   - 공을 패들로 받지 못하고 놓치면 생명을 1개 잃는다.
      - 생명이 1개 이상 남아있다면 `ready`가 다시 True로 바뀌고 대기 상태로 전환
      - 남은 생명이 0개라면 `gameover` 상태를 True로 변경
   - `gameover` 상태에서 restart하면 `ready`가 True로 바뀌고 생명, 레벨, 점수와 벽돌 세트 및 각종 수치를 초기화한다.
<br><br><br>

# Implementation

### Language

파이썬

### Coding

공이 패들 또는 벽돌과 충돌하는 순간을 감지하는 것이 이번 프로젝트에서 가장 중요한 부분이었다. 여러 방법을 시도했는데, 공(원)의 지름을 대각선으로 하는 정사각형이 공 안에 있다고 가정하고 두 사각형끼리 충돌을 계산하는 것이 가장 정확했다. 이 부분을 잘 설명한 유튜브 비디오를 보고 참고했는데, 해당 영상이 비공개로 전환되어서 그림으로 정리했다.

<img src="/assets/images/personal-projects/breakout_collision.png" width="80%">

turtle 객체의 **좌표**는 단순히 해당 객체의 중앙을 가리키기 때문에, 섬세한 충돌 감지를 위해 객체의 크기에 맞춰 좌표를 계산해야 한다.

**공의 이동**
- 공은 매번 화면이 업데이트 될 때마다 현재 좌표 `(x, y)`에 `(dx, dy)` 값만큼 더해진 새 좌표로 이동해서 마치 움직이는 것처럼 보이게 된다.
- dx, dy의 절대값이 클수록 한 번에 해당 방향으로 더 멀리(빠른 속도로) 이동하고, + 또는 - 여부에 따라 이동 방향이 결정된다.

**공 → 정사각형 좌표 계산**    
- 정사각형 한 변의 길이 `s` = √2 * r = `10√2`
   - 왼편 x좌표: 공의 x좌표 - (s / 2) 
   - 오른편 x좌표: 공의 x좌표 + (s / 2) 
   - 윗면 y좌표: 공의 y좌표 + (s / 2)
   - 아랫면 y좌표: 공의 y좌표 - (s / 2)   

**패들 및 벽돌 좌표 계산**    
- 왼편 x좌표: 패들/벽돌의 x좌표 - (가로 길이 / 2)
- 오른편 x좌표: 패들/벽돌의 x좌표 + (가로 길이 / 2)
- 윗면 y좌표: 패들/벽돌의 y좌표 + (세로 길이 / 2) 
- 아랫면 y좌표: 패들/벽돌의 y좌표 - (세로 길이 / 2)   

**공과 패들의 충돌**    
1. 패들 모서리에 충돌했는지 체크
   - '공의 좌표'와 '패들 윗면 왼쪽/오른쪽 모서리의 좌표' 사이의 거리가 (공의 반지름 + 여유 길이)보다 짧다면 모서리에 맞은 것으로 간주한다.
   - 충돌했다면 공이 패들을 파고드는 것처럼 보이지 않게 위치를 살짝 바깥으로 보정한 후, dx와 dy에 모두 `-1`씩 곱해서 방향을 반전한다.
2. 패들 윗면에 충돌했는지 체크
   - 모서리 충돌이 아닌 경우 윗면에 충돌했는지 확인해야 한다.
   - 공 안의 `정사각형`과 패들의 `직사각형`의 좌표가 아래 조건을 모두 만족하는 경우 패들 윗면에 맞은 것으로 간주한다.
      - 공의 y좌표가 특정 높이 이상
      - 정사각형의 오른편 > 패들의 왼편
      - 정사각형의 왼편 < 패들의 오른편
      - 정사각형의 윗면 > 패들의 아랫면
      - 정사각형의 아랫면 < 패들의 윗면
   - 충돌했다면 공이 패들을 파고드는 것처럼 보이지 않게 위치를 살짝 바깥으로 보정한 후, dy에 `-1`을 곱해서 방향을 반전한다.
   - 패들이 이동하는 방향에 따라 dx도 살짝 보정한다.   
   (패들이 오른쪽으로 이동 중이었다면 `+0.2`, 왼쪽으로 이동 중이었다면 `-0.2`를 더해서 공의 각도 조절)
3. 위 조건 모두 해당되지 않는다면 충돌하지 않은 것으로 간주한다.

**공과 벽돌의 충돌**   
for문으로 모든 벽돌마다 아래 조건들을 체크한다.

1. `공의 좌표`와 `벽돌의 좌표`간의 거리가 일정 수치 이하일 때만 충돌 계산 시작
2. 공 안의 `정사각형`과 벽돌의 `직사각형`의 좌표로 `delta x`와 `delta y` 계산
   - 공의 dx가 양수이면(왼쪽에서 오른쪽으로 이동 중) delta x는 정사각형의 오른편 - 직사각형의 왼편
   - 공의 dx가 음수이면(오른쪽에서 왼쪽으로 이동 중) delta x는 직사각형의 오른편 - 정사각형의 왼편
   - 공의 dy가 양수이면(아래에서 위로 이동 중) delta y는 정사각형의 윗면 - 직사각형의 아랫면 (+ 여유 길이)
   - 공의 dy가 음수이면(위에서 아래로 이동 중) delta y는 직사각형의 윗면 - 정사각형의 아랫면 (+ 여유 길이)
3. 충돌 위치 순서대로 체크
   - `delta x - delta y`의 절대값이 공의 반지름 길이 이하라면, 모서리에 맞은 것으로 간주한다. → dx, dy 방향 반전
   - `delta x > delta y`이면, 벽돌의 윗면이나 아랫면에 맞은 것으로 간주한다. → dy 방향 반전
   - `delta y > delta x`이면, 벽돌의 왼편이나 오른편에 맞은 것으로 간주한다. → dx 방향 반전   

**그 외**
- 아이템 적용
   1. 1에서 48(총 벽돌 개수)의 숫자 중 4개(아이템 개수)의 숫자를 무작위로 뽑는다.
   2. 벽돌을 생성하고 리스트에 넣는 것을 48번 반복하는 와중에 리스트의 길이가 무작위 숫자에 해당될 때, 아이템 객체를 생성하여 벽돌 위에 표시
   3. 공으로 깬 벽돌에 아이템 객체가 있을 경우 15초간 해당 아이템 효과가 지속된다.
      - lifeup: `life` 값에 1 추가 후 life의 수만큼 `"♥︎ "`를 반복 출력하여 화면에 표시(예외로 지속 시간 없음)
      - doublescore: 벽돌 1개를 깰 때마다 `score`에 더하는 점수를 10에서 20으로 2배 상향
      - extendbar: 패들 객체의 가로 길이를 늘리는 비율을 5에서 7로 상향
      - powerball: 공이 한 번에 벽돌 2개씩 깰 수 있도록 파워 상향 → `power`값을 1로 초기화
         - 파워가 1일 때는 벽돌에 충돌해도 공이 튕기지 않은 채 그대로 이동하고 power값에 -1 더하기
         - 파워가 0일 때는 일반 공처럼 벽돌에 충돌하면 위치에 따라 공을 튕김
         - 벽, 패들 또는 벽돌에 충돌해서 공이 튕길 때마다 power값을 1로 재충전
   4. 아이템 객체는 1초 간 화면에 텍스트를 유지 후 삭제된다.
- 공의 속도 조절
   - dx, dy값은 각각 5(레벨 1)로 시작한다.
   - 공이 한 번 튕길 때마다 횟수를 카운트해서 20이 될 때마다 속도 10%를 상향한다(dx, dy에 1.1씩 곱하기).
   - 공을 잃을 때마다 해당 레벨의 기본 속도로 리셋된다.
   - 해당 레벨의 기본 속도는 최초 속도부터 10%씩 상향하는 것을 (해당 레벨의 숫자 - 1)번 반복한 값이다.
<br><br><br>

# Result

<div style="width: 80%;">{% include video id="1068564784" provider="vimeo" %}</div>

<br><br><br>

# Future Improvements

- **다양한 아이템**    
공을 1개 추가하거나 패들에서 총알이 나가면서 벽돌을 제거하는 등 다양한 기능의 아이템 추가된다면 더 흥미로운 게임이 될 것이다.
- **다양한 레벨 디자인**    
레벨마다 벽돌 배치를 다양하게 변경하고 장애물을 추가하여 차별성을 주는 동시에 난이도를 조절할 수 있다.
- **자신의 점수를 기록하는 리더보드 추가**   
<br><br><br>

# Conclusion

부트캠프에서 주어진 조건에 맞춰서 turtle 라이브러리로 게임을 만들어봤는데, pygame과 같이 게임 개발에 적합한 라이브러리가 아니어서 아쉬운 점이 많았다. 일단 움직임이 자연스럽지 않고 살짝 끊기는 느낌이 있는데, 공이 빨라질수록 심해져서 오래 플레이하기 불편했다. 또 다양한 애니메이션 효과를 넣고 싶어도 기능이 제한적이어서 처음에 원했던 것보다 많이 간단하게 만들어졌다. 하지만 부트캠프에서 배운 내용을 응용하고 게임의 구조를 직접 짜볼 수 있어서 많은 도움이 됐던 프로젝트였다.

### reference

**level up 사운드:** Sound Effect by <a href="https://pixabay.com/ko/users/universfield-28281460/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=143027">Universfield</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=143027">Pixabay</a>      
**item 사운드:** Sound Effect by <a href="https://pixabay.com/ko/users/liecio-3298866/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=190035">LIECIO</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=190035">Pixabay</a>    
**gameover 사운드:** Sound Effect by <a href="https://pixabay.com/ko/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=6435">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=6435">Pixabay</a>    
**app 아이콘:** <a href="https://www.flaticon.com/free-icons/bricks" title="bricks icons">Bricks icons created by BizzBox - Flaticon</a>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}