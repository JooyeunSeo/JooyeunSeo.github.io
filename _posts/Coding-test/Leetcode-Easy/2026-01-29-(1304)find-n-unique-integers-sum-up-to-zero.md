---
excerpt: "'LeetCode: Find N Unique Integers Sum up to Zero' 풀이 정리"
title: "\01304. Find N Unique Integers Sum up to Zero"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer `n`, return **any** array containing `n` **unique** integers such that they add up to `0`.

**Example 1:**

- Input: n = 5
- Output: [-7,-1,1,3,4]
- Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

**Example 2:**

- Input: n = 3
- Output: [-1,0,1]

**Example 3:**

- Input: n = 1
- Output: [0]

**Constraints:**

- 1 <= n <= 1000

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Return an array where the values are symmetric. (+x , -x).</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">If n is odd, append value 0 in your returned array.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        val = n       # 유니크한 값
        result = []

        for i in range(0, n, 2):
            if i == n-1:            # n이 홀수일 경우 마지막 값 0
                result.append(0)
            else:
                result.append(-val) # -x, x 순으로 넣기
                result.append(val)
                val -= 1

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.44** MB \| Beats **17.11%**    

큰 수부터 `(-x, x)` 쌍으로 넣어서 항상 부분합이 0이 되도록 유지했다. n이 홀수면 마지막에 0을 하나 추가하면 된다.

n = 5
{: style="color: blue;"}
<pre>
[-5,  5]               -> sum = 0
[-5,  5, -4,  4]       -> sum = 0
[-5,  5, -4,  4,  0]   -> sum = 0
</pre>

return [-5,  5, -4,  4,  0]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/solutions/7162996/2-approaches-1-line-explained-in-depth-c-n3yl/" target="_blank">1st</a>

```python
class Solution(object):
    def sumZero(self, n):
        return range(1 - n, n, 2)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

리트코드에서는 리스트가 아니어도 iterable 값이면 정답으로 인정되기 때문에 range() 만으로도 풀 수 있다. 이 나열은 수학적으로 항상 `쌍대칭`이기 때문에 전체 합이 항상 0이 된다.

### <a href="https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/solutions/7162944/wrwrw-by-la_castille-8ikn/" target="_blank">2nd</a>

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))
```
무조건 쌍대칭이 되도록 값을 나열하지 않아도 된다. 이 코드는 `1`부터 `n-1`까지의 값을 먼저 넣고, 그 합을 정확히 `0`으로 만들어주는 마지막 음수 값 하나를 맨 앞에 붙여서 보정하는 방법을 사용해다.