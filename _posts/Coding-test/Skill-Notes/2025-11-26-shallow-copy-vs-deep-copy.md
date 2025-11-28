---
excerpt: "얕은 복사와 깊은 복사의 차이"
title: "Shallow copy vs Deep copy"
header:
  teaser: "https://cdn.pixabay.com/photo/2018/02/21/17/36/programming-3170992_1280.png"
categories:
  - Skill-Notes
tags:
  - Python
last_modified_at: 2025-11-26T19:52:38+09:00
---

## Assignment (=)

```python
a = [1, 2, 3]
b = a           # 대입
b.append(4)
print(a)
print(b)
```
<i class="fa-solid fa-right-from-bracket"></i>    
[1,2,3,4]    
[1,2,3,4]

- 객체 `a`에 `b`라는 변수 이름만 하나 더 할당해서 연결하는 동작이다.
- 얕은 복사나 깊은 복사에 해당하지 않음

## Shallow Copy

```python
a = [[1, 2], [3, 4]]
b = a[:]                # 슬라이싱으로 전체를 얕은 복사
b.append([5, 6])
print(a)
print(b)

b[0].append(7)
print(a)
print(b)
```
<i class="fa-solid fa-right-from-bracket"></i>    
[[1, 2], [3, 4]]     
[[1, 2], [3, 4], [5, 6]]    

[[1, 2, 7], [3, 4]]    
[[1, 2, 7], [3, 4], [5, 6]]

- `b`는 `a`의 바깥 컨테이너만 새로운 객체로 복사하고, 내부 객체는 원본을 참조한다.
    <pre>
    a --> [[1, 2], [3, 4]]     [[1, 2], [3, 4]]
              ↕︎       ↕︎     →     ↕︎       ↕︎
    b --> [[1, 2], [3, 4]]     [[1, 2], [3, 4], [5, 6]]
                                                append
    </pre>
- `a[:]` 대신 copy 모듈의 `copy.copy(a)` 사용 가능
- `[1, 2, 3]`과 같은 단순 리스트에서는 얕은 복사를 해도 복사본이 원본에 영향을 주지 않는다.   
(내부 요소가 int처럼 불변 객체일 경우 공유는 하지만 값을 수정할 수 없기 때문)

## Deep Copy

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)   # 깊은 복사
b[0].append(7)
print(a)
print(b)
```
<i class="fa-solid fa-right-from-bracket"></i>      
[[1, 2], [3, 4]]      
[[1, 2, 7], [3, 4]]    

- `b`는 `a`의 모든 계층을 새로운 객체로 복사한다.