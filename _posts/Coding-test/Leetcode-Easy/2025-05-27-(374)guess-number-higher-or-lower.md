---
excerpt: "'LeetCode: Guess Number Higher or Lower' 풀이 정리"
title: "\0374. Guess Number Higher or Lower"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Search
---

## <i class="fa-solid fa-file-lines"></i> Description

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
- `1`: Your guess is lower than the number I picked (i.e. `num < pick`).
- `0`: your guess is equal to the number I picked (i.e. `num == pick`).  

Return *the number that I picked*.

**Example 1:**

- Input: n = 10, pick = 6
- Output: 6

**Example 2:**

- Input: n = 1, pick = 1
- Output: 1

**Example 3:**

- Input: n = 2, pick = 1
- Output: 1

**Constraints:**

- 1 <= n <= 2<sup>31</sup> - 1
- 1 <= pick <= n

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 1
        max = n

        while min <= max:
            mid = (min + max) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                min = mid + 1
            else:
                max = mid - 1
```
<i class="fa-solid fa-clock"></i> Runtime: **11** ms \| Beats **87.17%**    
<i class="fa-solid fa-memory"></i> Memory: **12.46** MB \| Beats **49.53%**

이진 탐색을 사용한 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/guess-number-higher-or-lower/solutions/2818874/python-c-java-rust-binary-search-to-halve-your-ignorance-bonus-o-0-one-liner-explained/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
from bisect import bisect_left

class Solution:
    def guessNumber(self, n):
        return bisect_left(range(n), 0, key=lambda m: -guess(m))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

파이썬 내장함수 <mark>bisect_left</mark>으로도 이진 탐색 알고리즘을 사용할 수 있다. 이 함수는 **오름차순으로 정렬**된 리스트에서 pick을 삽입할 수 있는 가장 좌측의 **인덱스**를 찾는다. `range(n)`로 0부터 n-1까지 숫자를 생성하고, key값은 `-guess(m)`가 된다. -를 붙이는 이유는 정답이 리턴값보다 더 작은 숫자일 경우 -1이 반환되고 더 큰 숫자일 경우 1이 반환되는데, 이를 반전시켜서 정렬된 리스트로 만드는 것이다.

n = 10   
pick = 6   
range(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{: style="color: blue;"}
<pre>
left   right   mid    guess(m)    -guess(m)    비교결과
0      10      5       1          -1           -1 < 0 → right
6      10      8      -1           1            1 > 0 → left
6       8      7      -1           1            1 > 0 → left
6       7      6       0           0           0 == 0 → return        
</pre>

return 6
{: style="color: green;"}