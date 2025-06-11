---
excerpt: "'LeetCode: Climbing Stairs' 풀이 정리"
title: "\070. Climbing Stairs"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Fibonacci numbers
---

## <i class="fa-solid fa-file-lines"></i> Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

- Input: n = 2
- Output: 2
- Explanation: There are two ways to climb to the top.
   1. 1 step + 1 step
   2. 2 steps

**Example 2:**

- Input: n = 3
- Output: 3
- Explanation: There are three ways to climb to the top.
   1. 1 step + 1 step + 1 step
   2. 1 step + 2 steps
   3. 2 steps + 1 step

**Constraints:**

- 1 <= n <= 45
<br>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">To reach nth step, what could have been your previous steps? (Think about the step sizes)</span></u>


## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_steps = 0                 # steps 조합에서 1 step의 개수
        two_steps = 0                 # steps 조합에서 2 steps의 개수
        count = 0                     # 가능한 조합의 총 개수

        for i in range(n // 2 + 1):   # 2 steps 개수를 기준으로 반복(0개부터 n//2개까지)
            two_steps = i             
            one_steps = n - (2 * i)   # 2 steps가 i개일 때 1 step의 개수
            
            count += factorial(one_steps + two_steps) / (factorial(one_steps) * factorial(two_steps))
        
        return int(count)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.40** MB \| Beats **48.99%**

*중복된 문자* 가 포함된 n개의 문자를 *순서에 상관있게* 나열하는 **중복 순열** 공식을 사용해서 풀었다.

**n! / (1 step의 개수)! \* (2 steps의 개수)!**

팩토리얼 계산은 파이썬 math 모듈의 <mark>math.factorial()</mark>을 사용했다.


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/climbing-stairs/solutions/6162936/dynamic-programming-solution-by-niits-k9xe/" target="_blank">1st</a>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n   # n이 3보다 작거나 같으면 방법의 수가 n개이므로 바로 n을 반환

        prev1 = 3             # (n-1)개의 계단의 방법의 수(n = 3 일 때로 초기화)
        prev2 = 2             # (n-2)개의 계단의 방법의 수(n = 2 일 때로 초기화)
        cur = 0               # 현재 계산 중인 n개에서 방법의 수

        for _ in range(4, n):     # n = 4 부터 시작
            cur = prev1 + prev2   # (n-1)번째 계단의 방법의 수 + (n-2)번째 계단의 방법의 수
            prev2 = prev1
            prev1 = cur
        
        return cur
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

n개의 계단을 오르는 조합의 개수가 **피보나치 수열**과 같다는 것을 이용한 답안이다.  
n = 3 부터는 바로 앞 두 항의 합으로 이루어진다.

<pre>
n = 1  → 1 way
n = 2  → 2 ways
n = 3  → 3 ways (1 + 2)
n = 4  → 5 ways (2 + 3)
n = 5  → 8 ways (3 + 5)
...
</pre>

### <a href="https://leetcode.com/problems/climbing-stairs/solutions/3708750/4-methods-beats-100-c-java-python-beginn-bvot/" target="_blank">2nd</a>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}                       # 이미 계산된 값을 저장(memoize)하는 딕셔너리
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:            # n이 0이거나 1이면 1가지 방법 뿐이므로 1 반환
            return 1
        if n not in memo:               # n값이 memo에 없으면 값을 계산하고 저장
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]                  # n값이 memo에 있으면 바로 반환
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛) ← n개의 값을 한 번씩 계산            
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛) ← 딕셔너리에 n개의 값 저장   

재귀(**Recursion**) 호출을 사용하였는데, 재귀 호출은 같은 함수가 반복적으로 호출되어 효율이 낮기 때문에 **Memoization** 기법을 추가하여 중복 계산을 방지한 예시이다.

`n` = 5
{: style="color: blue;"}

<pre>
helper(5)
├── helper(4)
│   ├── helper(3)
│   │   ├── helper(2)
│   │   │   ├── helper(1) → 1
│   │   │   └── helper(0) → 1
│   │   └── memo[2] → 2 (saved)
│   └── memo[3] → 3 (saved)
└── memo[4] → 5 (saved)
</pre>

memo[5] = 5 + 3    
∴ `n` = 8
{: style="color: green;"}