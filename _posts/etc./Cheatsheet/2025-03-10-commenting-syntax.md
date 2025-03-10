---
excerpt: "다양한 언어에서 주석 다는 방법 정리"
title: "Commenting Syntax"
header:
  teaser: "https://images.unsplash.com/photo-1617040619263-41c5a9ca7521?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
categories:
  - Cheatsheet
---

## Programming

|      Type      | Single Comment | Block Comment |
|:--------------:|:--------------:|:-------------:|
|   **Python**   |       `#`      |   `""" """`   |
| **C**, **C++** |      `//`      |    `/* */`    |
|    **Java**    |      `//`      |    `/* */`    |
|   **Kotlin**   |      `//`      |    `/* */`    |
|    **Swift**   |      `//`      |    `/* */`    |
| **JavaScript** |      `//`      |    `/* */`    |
|    **Ruby**    |       `#`      | `=begin =end` |
|     **PHP**    |     `/`, `#`   |    `/* */`    |
|      **R**     |       `#`      |               |

<br>

## Markup & Styling

|   Type   | Single Comment | Block Comment |
|:--------:|:--------------:|:-------------:|
| **HTML** |   `<!-- -->`   |               |
|  **CSS** |     `/* */`    |               |

<br>

## Database

|   Type  | Single Comment | Block Comment |
|:-------:|:--------------:|:-------------:|
| **SQL** |      `--`      |    `/* */`    |

<br>

## Templete Engine

|         Type               |           Single Comment                            |
|:--------------------------:|:---------------------------------------------------:|
|  **Jinja2** (Flask)        |               `{# #}`                               |
|      **Django**            |               `{# #}`                               |
| **Liquid** (Jekyll)        | {%raw%}`{%- comment %} {%- endcomment %}`{%endraw%} |
| **Handlebars** (JavaScript)| {%raw%}`{{!-- --}}`{%endraw%}                       |