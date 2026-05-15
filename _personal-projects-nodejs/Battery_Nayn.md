---
date: 2026-05-15
layout: splash
excerpt: "A cute desktop cat that reacts and moves based on your system's battery status."
title: "Battery Nayn"
header:
  teaser: "/assets/images/personal-projects/battery_nayn_ex.gif"
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: /assets/images/personal-projects/battery_nayn_ex.gif
  actions:
    - label: "Download Zip"
      url: "https://drive.google.com/uc?id=1ZwwLJQaT9UyJ7IYTTXCMmJsdJxkrYpp8&export=download" 
---

# Overview
<hr>

데스크톱 환경에서 배터리 잔량을 확인하는 것은 어려운 일이 아닙니다. 화면 상단바를 슬쩍 보기만 해도 정확한 숫자를 알 수 있습니다. 하지만 숫자를 확인하지 않아도 현재 남은 배터리가 얼마 정도인지 직관적으로 알고 싶다는 생각에서 이 애플리케이션을 제작했습니다.

BatteryNyan(배터리 냥)은 사용자의 실시간 배터리 상태를 감지하여 고양이의 몸짓으로 표현합니다. 에너지가 충분할 때는 화면 위를 활기차게 누비며 집사의 작업을 응원하지만, 에너지가 부족해질수록 점점 활동량이 줄어들다 결국 지쳐 잠든 모습을 보여줍니다. 화면 구석에서 곤히 잠든 고양이의 모습이 눈에 들어오는 순간, 사용자는 바로 충전기를 연결해야한다는 사실을 깨닫게 됩니다.

물론, 삭막한 코드와 텍스트로 가득한 모니터 화면 속에서 귀여운 고양이를 보는 것만으로도 스트레스가 해소된다는 점은 이 애플리케이션을 설치해야 할 가장 큰 이유이기도 합니다. 다크 모드에서는 하얀 고양이가, 라이트 모드에서는 검은 고양이가 여러분과 함께할 것입니다.

🐈‍⬛ **배터리 상태별 고양이 모션**
- **활발한 산책 중(80% ~ 100%):** 상하좌우 가리지 않고 화면 전체를 누비며 아주 활기차게 돌아다닙니다.
- **가벼운 산책 중(50% ~ 79%):** 활동량이 조금 줄어들어 좌우 방향으로만 산책합니다.
- **그루밍 중(31% ~ 49%):** 돌아다니는 걸 멈추고 제자리에 앉아 그루밍을 시작합니다.
- **하품하는 중(11% ~ 30%):** 이제 정말 배터리가 부족하다는 신호입니다. 고양이가 계속 하품을 하며 당신에게 충전기를 가져오라고 눈치를 줍니다.
- **딥슬립(10% 이하):** 에너지가 바닥나 결국 깊은 잠에 빠져듭니다. 고양이가 자고 있다면 지체 말고 충전기를 연결해 주세요!
<br><br><br>

# System & Interface Design
<hr>

본 프로젝트는 Electron의 IPC(Inter-Process Communication) 아키텍처를 기반으로 설계되었습니다. OS 레벨의 시스템 데이터를 수집하는 Main Process와 이를 시각화하는 Renderer Process 사이의 데이터 무결성을 보장하기 위해 고안되었습니다.

특히, 데이터 수신 직후 상태를 체크하는 단계를 배치하여 수신된 배터리 정보가 최초 데이터인지 판별합니다. 이를 통해 앱 실행 초기에 발생할 수 있는 렌더링 노이즈를 차단하고, 고양이 마스코트의 초기 위치 및 모션 설정의 안정성을 확보했습니다.

### Information Architecture

[![](https://mermaid.ink/img/pako:eNp1VA1P4kAQ_SubNRpMQEuLlG7iXRS9xATUAF5y15rLQqd0Y9mS7VblCP_9pttSe350E-jOvnkz82a2W7pIQ6CMLhVfx2R2FUiCT5bPS8Pd1L9bg-JayCWZbjINq8cSUjyXrUuuNagNGcEzJMdvJ7NWCSazGFbAyBVXT6cjsYx1BQIZBvJdsDEX0r9OYKFVKs2O3Kt0AVnWiDm98TNDLWSUqhVmhtiRmCuuNg3YbOzf4tkzlBmQcSqFTlUDcXM__DP28ddEYmSKKZHrZ5C6Ga5RLOl0vmH4RgxjmY2byZEjNBi74f-62AkaQYF6K3hv-aTogmtict2DGNaMKsiPGU811zCMYfG03Xfn_PycyDxJvu8alKiH_0OoTJtXRobIUwRPM6xhGqcvZMh1g_dhHSKxX_6hnkb4I3KRZdCE_RTw4j_csMKbXEhRdQhlUXxDxiDzx70WdRdQLxLQeZltJylmiZwSXTSus4i5XEIY0FrUyTtdyr7UVX-mRBngF2SkVZY8Snl4vOfE8r92uk1Ja5JLLVawdygl-F9KLLBSpkAUInxo_eEhkm-S4ibh5JJFwpXQm2os8ACasSORJOwgiqJeGLYznI8nYAdhj1tdt9p2XkSoY2avX5sUJpfSGbrRWQS1s9U9c715E2tuWBXorFg11oNiNbH1cFZ4L5qDW-MHtut2XdrGz4gIKYt4kkGbrgDvZ7Gn24IqoKajAWX4GkLE80QHNJA79Ftz-TtNV5RplaOnSvNlXPPkRtgrwfHmrGqrMhkNU-wNZb2uZ0go29JXyhzLOvEGfadvOw4q1hu06YYyu38ysAa9bt9ycTm25eza9K8Ji3C379qW63h9r295trP7B-dsjU0?type=png)](https://mermaid.live/edit#pako:eNp1VA1P4kAQ_SubNRpMQEuLlG7iXRS9xATUAF5y15rLQqd0Y9mS7VblCP_9pttSe350E-jOvnkz82a2W7pIQ6CMLhVfx2R2FUiCT5bPS8Pd1L9bg-JayCWZbjINq8cSUjyXrUuuNagNGcEzJMdvJ7NWCSazGFbAyBVXT6cjsYx1BQIZBvJdsDEX0r9OYKFVKs2O3Kt0AVnWiDm98TNDLWSUqhVmhtiRmCuuNg3YbOzf4tkzlBmQcSqFTlUDcXM__DP28ddEYmSKKZHrZ5C6Ga5RLOl0vmH4RgxjmY2byZEjNBi74f-62AkaQYF6K3hv-aTogmtict2DGNaMKsiPGU811zCMYfG03Xfn_PycyDxJvu8alKiH_0OoTJtXRobIUwRPM6xhGqcvZMh1g_dhHSKxX_6hnkb4I3KRZdCE_RTw4j_csMKbXEhRdQhlUXxDxiDzx70WdRdQLxLQeZltJylmiZwSXTSus4i5XEIY0FrUyTtdyr7UVX-mRBngF2SkVZY8Snl4vOfE8r92uk1Ja5JLLVawdygl-F9KLLBSpkAUInxo_eEhkm-S4ibh5JJFwpXQm2os8ACasSORJOwgiqJeGLYznI8nYAdhj1tdt9p2XkSoY2avX5sUJpfSGbrRWQS1s9U9c715E2tuWBXorFg11oNiNbH1cFZ4L5qDW-MHtut2XdrGz4gIKYt4kkGbrgDvZ7Gn24IqoKajAWX4GkLE80QHNJA79Ftz-TtNV5RplaOnSvNlXPPkRtgrwfHmrGqrMhkNU-wNZb2uZ0go29JXyhzLOvEGfadvOw4q1hu06YYyu38ysAa9bt9ycTm25eza9K8Ji3C379qW63h9r295trP7B-dsjU0)

# Implementation
<hr>

### Tech Stack

- **Framework:** Electron
- **Programming Language:** JavaScript (Node.js 기반)
- **Library:** systeminformation (실시간 하드웨어 데이터 획득)
- **Packaging:** electron-builder
- **UI/UX:** HTML5, CSS3 (투명 윈도우, 마우스 이벤트 관통 등)

### Key Implementation Details

1. **시스템 테마 감지 및 에셋 동적 매핑**    
사용자의 OS 설정이 다크 모드인지 라이트 모드인지에 따라 고양이의 가독성을 높이기 위해 아이콘과 고양이 색상을 실시간으로 변경합니다. `nativeTheme` 모듈을 활용하여 상태 변화를 감지하고, 에셋 파일명 뒤에 `_dark` 또는 `_light` 접미사를 붙여 동적으로 경로를 지정했습니다.
2. **투명 윈도우 및 마우스 이벤트 관통**      
고양이가 화면 위에 떠 있지만 다른 작업을 방해하지 않도록 하는 것이 핵심이었습니다. Electron의 `transparent: true` 옵션과 함께 `win.setIgnoreMouseEvents(true, { forward: true })` 설정을 활용하여, 고양이 이미지가 없는 빈 공간은 마우스 클릭이 통과하여 뒤쪽의 창이 선택되도록 구현했습니다.
3. **배터리 구간별 상태 Transition**        
systeminformation 라이브러리를 통해 10초 주기로 배터리 level 값을 가져옵니다. 수집된 배터리 잔량은 미리 정의된 5단계 임계값(Thresholds)에 따라 걷기, 그루밍, 하품, 수면 등의 상태로 매핑됩니다.
4. **랜덤 모션**      
고양이가 걷는 도중 벽에 부딪히거나, 일정 확률`(Math.random() < 0.005)`에 도달하면 방향을 정하는 함수가 호출됩니다. (`requestAnimationFrame`은 보통 초당 60번 실행되기 때문에 60 \* 0.005 = 0.3, 즉 평균적으로 약 3.3초마다 한 번 꼴로 고양이가 다음 방향을 결정하게 됩니다.)     
이 때 상/하/좌/우(또는 좌/우) 중 하나의 방향을 무작위로 선택하여 예측 불가능한 움직임을 구현했습니다.    
<br><br><br>

# Problem Solving Process
<hr>

### Problem 1. 고양이 드래그 시 잔상 발생 및 위치 이탈 문제

초기 구현 시 고양이를 드래그하면 반투명한 잔상이 생기거나 마우스를 뗀 후에도 커서에 고양이가 붙어 다니는 현상이 발생했습니다.

### Solution

- HTML5의 기본 draggable 속성 대신, Electron의 `-webkit-app-region: drag`와 마우스 이벤트 리스너(mousedown, mousemove, mouseup)를 결합했습니다.
- 클릭한 순간의 오프셋 값을 계산하여 윈도우 위치를 직접 업데이트함으로써 부드러운 드래그를 구현했습니다.

---------------

### Problem 2. 고양이 가출(화면 밖 이탈) 문제

고양이를 화면 구석으로 드래그하다가 실수로 화면 밖으로 완전히 밀어버리면 다시 불러올 방법이 없었습니다.

### Solution

- 사전 방지: 드래그 이벤트 발생 시 `screen.getPrimaryDisplay()`를 통해 화면의 유효 해상도를 계산하고, 고양이가 화면 경계선을 넘지 못하도록 좌표 제한(Clamping) 로직을 추가했습니다.
- 사후 대처: 만약의 상황을 대비해 시스템 트레이(Tray) 메뉴에 'Bring to Center' 기능을 추가하여, 클릭 한 번으로 고양이를 화면 중앙 좌표로 즉시 이동시키도록 조치했습니다.

----------------

### Problem 3. 초기 실행 시 모션 튐 현상

앱을 실행하는 찰나에 실제 배터리 잔량과는 무관하게 80% ~ 100% 상태의 모션이 짧게 출력되었다가 뒤늦게 현재 잔량에 맞는 모션으로 급격히 바뀌는 결함이 발견되었습니다.

원인은 아래 두 가지였습니다.
- 비동기 데이터 수신 지연: Electron의 메인 프로세스가 OS로부터 배터리 정보를 취득해 IPC로 전송하는 속도보다, 렌더러 프로세스가 HTML/JS를 로드하고 화면을 그리는 속도가 더 빨라 발생하는 시동 시점의 데이터 공백이 원인이었습니다.
- 잘못된 기본값 가정: 기존 로직은 배터리 변수가 초기값(100)을 가지고 시작했기에, 실제 데이터가 도착하기 전까지는 시스템이 100% 상태라고 판단하여 기본 애니메이션을 먼저 실행하는 허점이 있었습니다.

### Solution

- 데이터 수신 전 렌더링 원천 차단: 배터리 변수의 초기값을 null로 명시하고, `CSS display: none`을 기본값으로 설정했습니다. 유효한 배터리 데이터가 도착하기 전까지는 고양이 객체를 화면에 노출하지 않고 위치 계산도 유예하도록 수정했습니다.
- 초기화 플래그를 통한 강제 업데이트: 배터리 정보를 처음 수신하는 시점을 `isFirstTime`로 판별하여, 데이터가 들어오는 즉시 화면 중앙 좌표 계산과 해당 잔량에 맞는 모션 할당을 동시에 수행합니다. 이를 통해 사용자에게는 데이터 로딩이 완료된 '정제된 첫 프레임'만 노출되도록 안정성을 확보했습니다.
<br><br><br>

# Result
<hr>

<div style="width: 90%;">{% include video id="1192492400" provider="vimeo" %}</div>
<br><br><br>

# Future Improvements
<hr>

- **고양이 코스튬 기능**         
고양이를 모자나 리본 등으로 코스튬할 수 있는 기능 추가
- **다양한 시스템 데이터와의 연동**        
배터리 수치뿐만 아니라 CPU 점유율이나 메모리 사용량에 따라 고양이의 속도가 빨라지는 등의 기능 추가
<br><br><br>

# Conclusion
<hr>

간단한 아이디어에서 시작한 프로젝트였지만, 웹 기술(JS/HTML/CSS)이 어떻게 OS 레벨의 데이터와 만나 실제 사용 가능한 유틸리티가 되는지 깊이 있게 배울 수 있는 시간이었습니다.

작은 고양이 한 마리가 화면 위에 있는 것만으로도 코딩 시간이 훨씬 즐거워지는 경험을 했습니다. 앞으로도 일상의 불편함을 귀엽고 재미있게 해결하는 프로젝트를 계속 이어가고 싶습니다.
<br>

### assets & resources

**Sound Effect:** <a href="https://pixabay.com/ko/sound-effects/%ec%9e%90%ec%97%b0-purring-cat-156459/" target="_blank">https://pixabay.com/ko/sound-effects/%ec%9e%90%ec%97%b0-purring-cat-156459/</a>      
**Sound Effect:** <a href="https://pixabay.com/ko/sound-effects/%ec%9e%90%ec%97%b0-cat-meow-1-fx-306178/" target="_blank">https://pixabay.com/ko/sound-effects/%ec%9e%90%ec%97%b0-cat-meow-1-fx-306178/</a>         
**Icon**: <a href="https://www.flaticon.com/free-icons/kitty" target="_blank">Kitty icons created by kornkun - Flaticon</a>    
**Assets:** <https://last-tick.itch.io/animated-pixel-kittens-cats-32x32>
{: .small}

<b>Posted on:</b> {{ page.date | date: "%B %d, %Y" }}