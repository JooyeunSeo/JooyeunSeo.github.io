---
excerpt: "Python 2와 3의 주의해야 할 차이점 정리"
title: "Python2 vs Python3"
header:
  teaser: "https://cdn.pixabay.com/photo/2018/02/21/17/36/programming-3170992_1280.png"
categories:
  - Skill-Notes
tags:
  - Python
last_modified_at: 2025-11-28T19:37:34+09:00
---

|                                        | Python2                                               | Python3                                                |
|:--------------------------------------:|-------------------------------------------------------|--------------------------------------------------------|
|             print<br>syntax            | statement<br>`print "Hello World"`                    | function<br>`print("Hello World")`                     |
|             int<br>division            | 5 / 2 → 2<br>(same as `//`)                           | 5 / 2 → 2.5<br>(always `float`)                        |
|                 range()                | return `list`                                         | return `iterator`                                      |
| variable<br>leakage<br>(comprehension) | x = 10<br>y = [x for x in range(5)]<br>print(x)   # 4 | x = 10<br>y = [x for x in range(5)]<br>print(x)   # 10 |
|             storage of str             | ASCII (7bits)                                         | Unicode (8bits)                                        |
|          string<br>formatting          | format<br>`"Hi, {}".format(name)`                     | f-string<br>`f"Hi, {name}"`                            |