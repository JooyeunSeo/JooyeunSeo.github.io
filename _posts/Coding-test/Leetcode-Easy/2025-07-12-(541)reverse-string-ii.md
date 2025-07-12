---
excerpt: "'LeetCode: Reverse String II' 풀이 정리"
title: "\0541. Reverse String II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
  - String
  - Slicing
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s` and an integer `k`, reverse the first k characters for every `2k` characters counting from the start of the string.

If there are fewer than `k` characters left, reverse all of them. If there are less than `2k` but greater than or equal to `k` characters, then reverse the first `k` characters and leave the other as original.

**Example 1:**

- Input: s = "abcdefg", k = 2
- Output: "bacdfeg"

**Example 2:**

- Input: s = "abcd", k = 2
- Output: "bacd"

**Constraints:**

- 1 <= s.length <= 10<sup>4</sup>
- `s` consists of only lowercase English letters.
- 1 <= k <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        n = len(s)
        i = 0

        while i < n:
            slicing = min(i+k, n)   # i + k가 인덱스를 벗어날 경우 마지막 인덱스까지만 슬라이싱
            s[i:slicing] = s[i:slicing][::-1] # 슬라이싱한 부분을 뒤집은 후 원본에 붙여넣기
            i += 2 * k
        
        return "".join(s)
```
<i class="fa-solid fa-clock"></i> Runtime: **2** ms \| Beats **61.59%**    
<i class="fa-solid fa-memory"></i> Memory: **12.84** MB \| Beats **5.12%**

파이썬으로 풀 때는 문자열을 리스트로 변경한 후 슬라이싱을 이용하는 방법이 가장 간편한 것 같다. 슬라이싱 된 부분은 복사본이기 때문에 원본 리스트 위치에 다시 덮어씌워야 한다.

s = "abcdefg"   
k = 3
{: style="color: blue;"}
<pre>
i   s[i:slicing][::-1]             [a, b, c, d, e, f, g, h]
0   s[0:3][::-1]  =   [c, b, a]    [c, b, a, d, e, f, g, h]
6   s[6:8][::-1]  =   [h, g]       [c, b, a, d, e, f, h, g]
</pre>

return "cbadefhg"
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/reverse-string-ii/solutions/6672786/master-the-safe-way-to-reverse-every-2k-xh431/" target="_blank">1st</a>

```python
class Solution(object):
    def reverseStr(self, s, k):
        n = len(s)
        s = list(s)

        for i in range(0, n, 2 * k):
            s[i:i + k] = reversed(s[i:i + k])

        return "".join(s)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)       

사실 파이썬 슬라이싱에서는 `i + k`가 인덱스 범위를 초과해도 에러를 일으키지 않고 그냥 끝까지 슬라이스하기 때문에 `min(i+k, n)`을 생략해도 된다.

### <a href="https://leetcode.com/problems/reverse-string-ii/solutions/4112683/easy-to-understand-python-solution-to-re-oj32/" target="_blank">2nd</a>

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        for i in range(0, len(l), 2 * k):
            start = i
            end = min(i + k - 1, len(l) - 1) 
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1

        return ''.join(l)
```
두 개의 포인터를 이용한 방식이다.

s = "abcdefg"   
k = 3
{: style="color: blue;"}
<pre>
i   start   end              [a, b, c, d, e, f, g, h]
0     0   <  2    l[0]↔︎l[2]  [c, b, a, d, e, f, g, h]
      1  >=  1    
6     6   <  7    l[6]↔︎l[7]  [c, b, a, d, e, f, h, g]
      7   >  6    
</pre>

return "cbadefhg"
{: style="color: green;"}