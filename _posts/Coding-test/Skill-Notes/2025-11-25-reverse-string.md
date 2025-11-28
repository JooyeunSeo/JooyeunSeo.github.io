---
excerpt: "문자열을 반대로 뒤집는 다양한 방법"
title: "Reverse String"
header:
  teaser: "https://cdn.pixabay.com/photo/2018/02/21/17/36/programming-3170992_1280.png"
categories:
  - Skill-Notes
tags:
  - Python
  - String
last_modified_at: 2025-11-25T19:43:27+09:00
---

## slicing
```python
txt = "Hello World"
print(txt[::-1])      # 오른쪽 끝에서 왼쪽 끝으로 한 칸씩 이동해서 새로운 문자열 생성
```
<i class="fa-solid fa-right-from-bracket"></i> dlroW olleH

## reverse + join

```python
txt = "Hello World"
txt_list = list(txt)      # 리스트 타입으로 변환 필수
txt_list.reverse()        # 리스트 원본을 in-place로 뒤집는 함수
print(''.join(txt_list))  # join으로 다시 합치기
```
<i class="fa-solid fa-right-from-bracket"></i> dlroW olleH

## revsersed + join

```python
txt = "Hello World"
txt_reversed = reversed(txt)            # iterator한 객체를 반환
print(''.join(reversed(txt_reversed)))  # join으로 다시 합치기
```
<i class="fa-solid fa-right-from-bracket"></i> dlroW olleH

## forloop

```python
txt = "Hello World"
temp_list = []
for i in range(len(txt)-1, -1, -1):     # 끝에서부터 처음까지 한 칸씩 거꾸로 이동
    temp_list.append(txt[i])
print(''.join(temp_list))
```
<i class="fa-solid fa-right-from-bracket"></i> dlroW olleH

## while

```python
txt = "Hello World"
txt_list = list(txt)
temp_list = []
while len(txt_list) > 0:
    temp_list.append(txt_list.pop())
print("".join(temp_list))
```
<i class="fa-solid fa-right-from-bracket"></i> dlroW olleH