---
excerpt: "디지털 논리회로를 구성하는 논리 게이트 정리"
title: "Digital Logic Gate"
toc: false
header:
  teaser: "https://images.unsplash.com/photo-1537151377170-9c19a791bbea?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
categories:
  - Cheatsheet
last_modified_at: 2025-02-18T00:30:30+09:00
---
<br>

|  Type  | Distinctive<br>Shape   |  Boolean<br>Algebra  | Truth Table<br>A, B → Q | Explanation |
|:------:|:----------------------:|:--------------------:|:-----------------------:|---------|
| **Buffer** | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Buffer_ANSI_Labelled.svg/120px-Buffer_ANSI_Labelled.svg.png) | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5ebb239b453149a6dedba8f18670ce9a9390c08)  |  <font color="Red">0</font> → <font color="Red">0</font><br><font color="Blue">1</font> → <font color="Blue">1</font>  | 입력을 그대로 복사 |
|   **NOT**  |  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/NOT_ANSI_Labelled.svg/120px-NOT_ANSI_Labelled.svg.png)      | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/92efef0e89bdc77f6a848764195ef5b9d9bfcc6a)  |  <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Blue">1</font> → <font color="Red">0</font>   | 논리적 부정을 수행 |
|   **AND**  |  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/AND_ANSI_Labelled.svg/120px-AND_ANSI_Labelled.svg.png)    | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/75a90e903f21f11a0f4ab3caca1e6943ba7a9849)<br>(![](https://wikimedia.org/api/rest_v1/media/math/render/svg/74954195333a8593163b93a9688695b8dc74da55)) |  <font color="Red">0</font>, <font color="Red">0</font> → <font color="Red">0</font><br><font color="Red">0</font>, <font color="Blue">1</font> → <font color="Red">0</font><br><font color="Blue">1</font>, <font color="Red">0</font> → <font color="Red">0</font><br><font color="Blue">1</font>, <font color="Blue">1</font> → <font color="Blue">1</font>  | 논리적 곱을 수행<br>입력이 모두 1인 경우에만 출력이 1 |
|**OR<br>**(inverter)|  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/OR_ANSI_Labelled.svg/120px-OR_ANSI_Labelled.svg.png)     | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4279cdbd3cb8ec4c3423065d9a7d83a82cfc89e3)<br>(![](https://wikimedia.org/api/rest_v1/media/math/render/svg/9b9c9c90857c12727201dd9e47a4e7c8658fdbc5)) |  <font color="Red">0</font>, <font color="Red">0</font> → <font color="Red">0</font><br><font color="Red">0</font>, <font color="Blue">1</font> → <font color="Blue">1</font><br><font color="Blue">1</font>, <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Blue">1</font>, <font color="Blue">1</font> → <font color="Blue">1</font>  | 논리적 합을 수행<br>입력 중 어느 한 개 이상이 1인 경우 출력이 1 |
|**NAND**<br>(AND-NOT)|  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/NAND_ANSI_Labelled.svg/120px-NAND_ANSI_Labelled.svg.png)   | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/225f35bb78e90b9126458f1bc6bf1ed3f0724bbf)   |  <font color="Red">0</font>, <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Red">0</font>, <font color="Blue">1</font> → <font color="Blue">1</font><br><font color="Blue">1</font>, <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Blue">1</font>, <font color="Blue">1</font> → <font color="Red">0</font>  | 논리적 곱의 보수를 수행<br>입력 중 어느 한 개 이상이 0인 경우 출력이 0<br>입력이 모두 1인 경우에만 출력이 0 |
|**NOR**<br>(OR-NOT)|  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/NOR_ANSI_Labelled.svg/120px-NOR_ANSI_Labelled.svg.png)    | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/08840f8e2022f127fc459d801a8f8ce93f65f55a)   |  <font color="Red">0</font>, <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Red">0</font>, <font color="Blue">1</font> → <font color="Red">0</font><br><font color="Blue">1</font>, <font color="Red">0</font> → <font color="Red">0</font><br><font color="Blue">1</font>, <font color="Blue">1</font> → <font color="Red">0</font>  | 논리적 합의 보수를 수행<br>입력 중 어느 한 개 이상이 1이면 출력이 0<br>입력이 모두 0인 경우에만 출력이 1 |
|**XOR**<br>(exclusive-OR)|  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/XOR_ANSI_Labelled.svg/120px-XOR_ANSI_Labelled.svg.png)    | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/f0512d6bdd29ff000dea0bf68b853618dcaabc3e)   |  <font color="Red">0</font>, <font color="Red">0</font> → <font color="Red">0</font><br><font color="Red">0</font>, <font color="Blue">1</font> → <font color="Blue">1</font><br><font color="Blue">1</font>, <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Blue">1</font>, <font color="Blue">1</font> → <font color="Red">0</font>  | 배타적 논리합을 수행<br>두 개의 입력이 서로 다르면 출력이 1, 같으면 출력이 0 |
|**XNOR**<br>(exclusive-NOR)|  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/XNOR_ANSI_Labelled.svg/120px-XNOR_ANSI_Labelled.svg.png)   | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a925c0f94e91b108609068c5ceae7c671db84d9)   |  <font color="Red">0</font>, <font color="Red">0</font> → <font color="Blue">1</font><br><font color="Red">0</font>, <font color="Blue">1</font> → <font color="Red">0</font><br><font color="Blue">1</font>, <font color="Red">0</font> → <font color="Red">0</font><br><font color="Blue">1</font>, <font color="Blue">1</font> → <font color="Blue">1</font>  | 배타적 논리합의 보수를 수행(XOR-NOT)<br>두 개의 입력이 서로 다르면 출력이 0, 같으면 출력이 1 |






<br><br>
<center>References</center>

1. "Logic gate" *From Wikipedia: the free encyclopedia*, 18 Feb. 2025, https://en.wikipedia.org/wiki/Logic_gate
1. 손진곤, 『이산수학』, 한국방송통신대학교출판문화원, 2023
{: .small}
