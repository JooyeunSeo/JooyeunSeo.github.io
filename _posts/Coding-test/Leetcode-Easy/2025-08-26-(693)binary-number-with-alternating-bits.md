---
excerpt: "'LeetCode: Binary Number with Alternating Bits' 풀이 정리"
title: "\0693. Binary Number with Alternating Bits"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Bit Manipulation
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

**Example 1:**

- Input: n = 5
- Output: true
- Explanation: The binary representation of 5 is: 101

**Example 2:**

- Input: n = 7
- Output: false
- Explanation: The binary representation of 7 is: 111.

**Example 3:**

- Input: n = 11
- Output: false
- Explanation: The binary representation of 11 is: 1011.

**Constraints:**

- 1 <= n <= 2<sup>31</sup> - 1

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1            # 가장 마지막 자리의 비트값으로 초기화
        while n != 0:
            n >>= 1             # 오른쪽으로 1비트 이동

            if n & 1 != prev:
                prev = n & 1
            else:
                return False

        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.36** MB \| Beats **77.92%**

**AND** 연산을 이용하면 마지막 자리 비트가 0, 1 중 어떤 것인지 알 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/binary-number-with-alternating-bits/solutions/6734818/master-alternating-bits-check-with-bit-t-3wjm/" target="_blank">1st</a>

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(1)   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

모든 비트를 체크하지 않고 빠르게 판별할 수 있는 방법이다. 우선 `n`과 n을 오른쪽으로 한 칸 민 `n >> 1`을 **XOR** 연산을 하면 인접한 비트가 번갈아 나타나는 숫자일 때만 전부 `1`로 나온다. 두 번째로 `x`와 `x + 1`을 **AND** 연산하면 전부 1비트일 때만 `0`이 나온다. 이진수로 `111...111`인 숫자에 1을 더하면 `1000...000`이 되는 것을 활용한 것이다.

n = 42 (101010)
{: style="color: blue;"}
<pre>
n        101010
n>>1     010101
        --------- XOR
x        111111
x+1     1000000
        -------- AND
        0000000
</pre>

return True
{: style="color: green;"}

### <a href="https://leetcode.com/problems/binary-number-with-alternating-bits/solutions/7124111/two-pointers-previous-o-logn/" target="_blank">2nd</a>

```python
class Solution(object):
    def hasAlternatingBits(self, n):
       return not (n*3) & (n*3+1) & (n*3+2)
```
또 다른 비트 트릭으로, alternating bits라면 그 세배수는 1비트가 연속해서 나타나는 성질을 활용한 방법이다(홀수라면 `...111`, 짝수라면 `...1110` 형태). 또한 인접한 3개의 수는 모두 동일한 자리에 비트 `1`이 똑같이 있는 것이 불가능하기 때문에 `(n*3) & (n*3+1) & (n*3+2)`의 결과는 `0`이 되어야 한다.

n = 42 (101010)
{: style="color: blue;"}
<pre>
n          101010   (42)

n*3       1111110  (126)
n*3+1     1111111  (127)
n*3+2    10000000  (128) 
        ---------
         00000000       
</pre>