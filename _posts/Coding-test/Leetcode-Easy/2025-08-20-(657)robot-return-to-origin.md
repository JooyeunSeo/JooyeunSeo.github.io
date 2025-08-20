---
excerpt: "'LeetCode: Robot Return to Origin' 풀이 정리"
title: "\0657. Robot Return to Origin"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Simulation
---

## <i class="fa-solid fa-file-lines"></i> Description

There is a robot starting at the position `(0, 0)`, the origin, on a 2D plane. Given a sequence of its moves, judge if this robot **ends up at** `(0, 0)` after it completes its moves.

You are given a string `moves` that represents the move sequence of the robot where `moves[i]` represents its i<sup>th</sup> move. Valid moves are `'R'` (right), `'L'` (left), `'U'` (up), and `'D'` (down).

Return `true` *if the robot returns to the origin after it finishes all of its moves, or* `false` *otherwise.*

**Note:** The way that the robot is "facing" is irrelevant. `'R'` will always make the robot move to the right once, `'L'` will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

**Example 1:**

- Input: moves = "UD"
- Output: true
- Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

**Example 2:**

- Input: moves = "LL"
- Output: false
- Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

**Constraints:**

- 1 <= moves.length <= 2 * 10<sup>4</sup>
- moves only contains the characters `'U'`, `'D'`, `'L'` and `'R'`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) % 2 != 0:   # 전체 무브수가 홀수면 원점으로 돌아오기 불가능
            return False

        x, y = 0, 0               # x,y 좌표 이동 수
        for m in moves:
            if m == 'R':
                x += 1
            elif m == 'L':
                x -= 1
            elif m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
        
        return True if x == 0 and y == 0 else False
```
<i class="fa-solid fa-clock"></i> Runtime: **25** ms \| Beats **71.43%**    
<i class="fa-solid fa-memory"></i> Memory: **12.57** MB \| Beats *77.52%**

오른쪽, 왼쪽, 위쪽, 아래쪽으로 이동한 횟수를 각각 카운트해도 되지만, x 좌표와 y 좌표를 나타내는 변수 두 개를 만들고 움직이는 방향에 따라 `+` 또는 `-`하는 방법을 선택했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/robot-return-to-origin/solutions/6730202/master-robot-return-check-with-simple-mo-0heh/" target="_blank">1st</a>

```python
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)          

<mark>count()</mark>를 사용하는 코드가 런타임은 더 빨랐다.