---
excerpt: "'LeetCode: Counting Bits' 풀이 정리"
title: "\0338. Counting Bits"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Bitwise
  - Dynamic Programming
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` *is the **number of*** `1`***'s** in the binary representation of* `i`.

**Example 1:**

- Input: n = 2
- Output: [0,1,1]
- Explanation:   
0 --> 0   
1 --> 1   
2 --> 10

**Example 2:**

- Input: n = 5
- Output: [0,1,1,2,1,2]
- Explanation:   
0 --> 0   
1 --> 1   
2 --> 10   
3 --> 11   
4 --> 100   
5 --> 101

**Constraints:**

- 0 <= n <= 10<sup>5</sup>


**Follow up:** 
- It is very easy to come up with a solution with a runtime of O(n log n).   
Can you do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">You should make use of what you have produced already.</span></u>    
💡 **Hint 2:**    
<u><span style="color:#F5F5F5">Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.</span></u>   
💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Or does the odd/even status of the number help you in calculating the number of 1s?</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        while len(result) <= n:
            result += [x + 1 for x in result]
        return result[:n + 1]
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **93.53%**    
<i class="fa-solid fa-memory"></i> Memory: **16.40** MB \| Beats **95.95%**

이진수를 순서대로 나열했을 때, 1의 갯수가 가지는 패턴을 활용했다.

n = 5
{: style="color: blue;"}
<pre>
2^0=1 → 1(1개)
2^1=2 → 2(1개) | 3(2개)
2^2=4 → 4(1개)   5(2개) |  6(2개)   7(3개)
2^3=8 → 8(1개)   9(2개)   10(2개)  11(3개) | 12(2개)  13(3개)  14(3개)  15(4개)

len    result
1     [0]        + [1]       → [0,1]
2     [0,1]      + [1,2]     → [0,1,1,2]
3     [0,1,1,2]  + [1,2,2,3] → [0,1,1,2,1,2,2,3]
                                           | slice
</pre>

result = [0,1,1,2,1,2]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)                 # 길이가 n+1인 리스트 생성(모든 원소값이 0)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)        
짝수와 홀수의 비트 패턴 규칙을 이용해서 1의 개수를 계산하는 방법이다.   
`i >> 1` 은 i를 오른쪽으로 1비트 시프트하여 마지막 자리를 제거하는데, 이는 십진수에서 `i // 2`와 같다.    
`i & 1`의 결과는 i의 가장 오른쪽 비트가 0(짝수)일 경우 0을 반환하고, 1(홀수)일 경우 1을 반환한다.   
현재의 값은 이전의 값 + 마지막 비트 로 계산하여 구할 수 있게 된다.

n = 5
{: style="color: blue;"}
<pre>
i    i >> 1        i & 1   ans[i]    ans
                                     [0,0,0,0,0,0]
1    ans[0] = 0    1       0+1 = 1   [0,1,0,0,0,0]
2    ans[1] = 1    0       1+0 = 1   [0,1,1,0,0,0]
3    ans[1] = 1    1       1+1 = 2   [0,1,1,2,0,0]
4    ans[2] = 1    0       1+0 = 1   [0,1,1,2,1,0]
5    ans[2] = 1    1       1+1 = 2   [0,1,1,2,1,2]
</pre>

result = [0,1,1,2,1,2]
{: style="color: green;"}