---
excerpt: "'LeetCode: Long Pressed Name' 풀이 정리"
title: "\0925. Long Pressed Name"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Your friend is typing his `name` into a keyboard. Sometimes, when typing a character `c`, the key might get *long pressed*, and the character will be typed 1 or more times.

You examine the `typed` characters of the keyboard. Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

**Example 1:**

- Input: name = "alex", typed = "aaleex"
- Output: true
- Explanation: 'a' and 'e' in 'alex' were long pressed.

**Example 2:**

- Input: name = "saeed", typed = "ssaaedd"
- Output: false
- Explanation: 'e' must have been pressed twice, but it was not in the typed output.

**Constraints:**

- 1 <= name.length, typed.length <= 1000
- `name` and `typed` consist of only lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0     # name, typed 포인터

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]: # i가 순회중이고, i와 j의 원소가 같으면 둘 다 이동
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:    # j와 j-1의 원소가 같으면 long pressed
                j += 1
            else:
                return False
        
        return i == len(name)                         # i가 name을 끝까지 순회했는지 확인
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.77** MB \| Beats **59.46%**

처음에는 `name[i] == typed[j]`이고 `typed[j] == typed[j+1]`이면 i는 한 칸, j는 두 칸 이동하는 방법을 써 봤는데, 이 경우 name이 끝나기 전에 typed가 끝나버리는 문제가 발생했다(e.g. `name = "ee"`, `typed = "ee"`).     
이 코드는 먼저 포인터 i와 j를 매칭하며 한 칸씩 이동하고, name이 끝난 후 typed에 같은 문자가 반복되면 long pressed로 간주하기 때문에 안전하게 name이 먼저 끝나게 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/long-pressed-name/solutions/183994/cjavapython-two-pointers-by-lee215-kk7z/" target="_blank">1st</a>

```python
class Solution:
    def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

for문으로 typed를 순회하며 name의 포인터를 조작하는 방법도 있다.