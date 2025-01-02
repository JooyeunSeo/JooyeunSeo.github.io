---
excerpt: "'LeetCode-Palindrome Number' 풀이 정리"
title: "\09. Palindrome Number"
header:
  teaser: "/assets/images/defaults/logo-LeetCode-black.png"
categories:
  - Leetcode
tags:
  - Coding Test
  - Easy
  - Python
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `x`, return `true` if `x` is a ***palindrome***, and `false` otherwise.

*[palindrome]: An integer is a palindrome when it reads the same forward and backward.


**Example 1:**

- Input: x = 121
- Output: true
- Explanation: 121 reads as 121 from left to right and from right to left.

**Example 2:**

- Input: x = -121
- Output: false
- Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

- Input: x = 10
- Output: false
- Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

**Constraints:**

- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

**Follow up:** Could you solve it without converting the integer to a string?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 1st
        x = str(x)
        forward = x[::]
        reverse = x[::-1]
        if forward == reverse:
            return True
        else:
            return False

        # 2nd
        x = str(x)
        if x > -1:
            forward = x[::]
            reverse = x[::-1]
            if forward == reverse:
                return True
            else:
                return False
        else:
            return False
```

변수를 문자열로 변환한 뒤, 앞에서부터 하나씩 추출한 것과 뒤에서부터 하나씩 추출한 것을 비교하는 방식을 사용했다. 

1번째 코드는 매우 간단하지만 거의 꼴지 수준의 런타임을 기록했다.   
2번째는 1번째 코드에서 x가 음수인 경우를 먼저 거르고 시작하는 조건만 추가했는데 바로 3ms로 크게 단축했다.
<br>

```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:           # x가 음수이면 False 반환
            return False
        
        reverse = []
        while x > 9:
            remain = x % 10
            x = x // 10
            reverse.append(remain)
        reverse.append(x)
        if reverse == reverse[::-1]:
            return True
        else:
            return False
```

Follow up 조건에 맞춰 x를 문자열로 변환하지 않고 풀어보았다.    

|   x |   // 10 |  % 10 | reverse   |
|----:|--------:|------:|-----------|
| 272 |      27 | **2** | \[2]      |
|  27 |     *2* | **7** | [2, 7]    |
|     |         |       | [2, 7, 2] |

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="[링크](https://leetcode.com/problems/palindrome-number/solutions/4795373/why-not-1-line-of-code-python-python3-c-esxj9/)" target="_blank">1st</a>

```python
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
```

1줄짜리 코드

### <a href="[링크](https://leetcode.com/problems/palindrome-number/solutions/6044650/video-using-remainder/)" target="_blank">2nd</a>

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:         
            return False

        reverse = 0     # x 값을 거꾸로 한 값을 저장하는 변수(0으로 시작)
        xcopy = x       # 마지막에 reverse와 구분하기 위해 원래 x 값을 복사해서 저장

        while x > 0:    # x가 0이 될때까지 반복
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcopy
```     
<i class="fa-solid fa-clock"></i> **time complexity:** O(log<sub>x</sub>)  
<i class="fa-solid fa-memory"></i> **space complexity:** O(1)        

while문 계산 예시

`x` = 121    
`reverse` = 0   
`xcopy` = 121   
{: style="color: blue;"}

| reverse                                   | x               |
|-------------------------------------------|-----------------|
| (0 \* 10) + (121 % 10) = 0 + 1 = 1        | 121 // 10 = 12  |
| (1 \* 10) + (12 % 10) = 10 + 2 = 12       | 12 // 10 = 1    |
| (12 \* 10) + (1 % 10) = 120 + 1 = **121** | 1 // 10 = **0** |

`reverse` == `xcopy`      
∴ True
{: style="color: green;"}