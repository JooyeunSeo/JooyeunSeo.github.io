---
excerpt: "'LeetCode: Shortest Distance to a Character' 풀이 정리"
title: "\0821. Shortest Distance to a Character"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s` and a character `c` that occurs in `s`, return *an array of integers* `answer` *where* `answer.length == s.length` *and* `answer[i]` *is the **distance** from index* `i` *to the **closest** occurrence of character* `c` *in* `s`.

The **distance** between two indices `i` and `j` is `abs(i - j)`, where `abs` is the absolute value function.

**Example 1:**

- Input: s = "loveleetcode", c = "e"
- Output: [3,2,1,0,1,0,0,1,2,2,1,0]
- Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).    
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.   
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.    
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.    
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

**Example 2:**

- Input: s = "aaab", c = "b"
- Output: [3,2,1,0]

**Constraints:**

- 1 <= s.length <= 10<sup>4</sup>
- `s[i]` and `c` are lowercase English letters.
- It is guaranteed that `c` occurs at least once in `s`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        result = []
        
        # s 1st 순회: c가 등장하는 인덱스 모두 저장
        c_idx = [i for i in range(len(s)) if s[i] == c]
        
        # s 2nd 순회: 현재 i에서 c_idx 중 가장 가까운 거리
        for i in range(len(s)):
            min_distance = min(abs(i - j) for j in c_idx)
            result.append(min_distance)
            
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **21** ms \| Beats **40.14%**    
<i class="fa-solid fa-memory"></i> Memory: **12.45** MB \| Beats **74.65%**

매 인덱스마다 모든 c의 위치와 비교하여 가장 가까운 거리를 찾는 방법으로, 효율적이지 않지만 간단하게 풀어봤다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/shortest-distance-to-a-character/solutions/125788/cjavapython-2-pass-with-explanation-by-l-w2de/" target="_blank">1st</a>

```python
    def shortestToChar(self, S, C):
        n, pos = len(S), -float('inf')        # S의 길이, 마지막으로 체크한 C 위치
        res = [n] * n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

조금 더 효율적으로 하려면 왼쪽 → 오른쪽, 오른쪽 → 왼쪽 방향으로 총 두 번 스캔하는 방법이 있다. 이 코드에서는 두 방향을 하나로 합쳐서 한 루프 안에서 해결했다. 

s = "loveleetcode"    
c = "e"
{: style="color: blue;"}
<pre>
0  1  2  3  4  5  6  7  8  9 10 11
l  o  v  e  l  e  e  t  c  o  d  e

range(n)
i=0 : 'l' → res[0]=min(12,inf)=12
i=1 : 'o' → res[1]=12
i=2 : 'v' → res[2]=12
i=3 : 'e' → pos=3, res[3]=0
i=4 : 'l' → res[4]=min(12,1)=1
i=5 : 'e' → pos=5, res[5]=0
i=6 : 'e' → pos=6, res[6]=0
i=7 : 't' → res[7]=1
i=8 : 'c' → res[8]=2
i=9 : 'o' → res[9]=3
i=10: 'd' → res[10]=4
i=11: 'e' → pos=11, res[11]=0
res = [12, 12, 12, 0, 1, 0, 0, 1, 2, 3, 4, 0]

range(n)[::-1]
i=11: 'e' → pos=11, res[11]=0
i=10: 'd' → res[10]=min(4,1)=1
i=9 : 'o' → res[9]=min(3,2)=2
i=8 : 'c' → res[8]=min(2,3)=2
i=7 : 't' → res[7]=min(1,4)=1
i=6 : 'e' → pos=6, res[6]=0
i=5 : 'e' → pos=5, res[5]=0
i=4 : 'l' → res[4]=min(1,1)=1
i=3 : 'e' → pos=3, res[3]=0
i=2 : 'v' → res[2]=min(12,1)=1
i=1 : 'o' → res[1]=min(12,2)=2
i=0 : 'l' → res[0]=min(12,3)=3
res = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
</pre>

res = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
{: style="color: green;"}

### <a href="https://leetcode.com/problems/shortest-distance-to-a-character/solutions/6758989/master-two-pass-sweep-to-find-shortest-d-pcds/" target="_blank">2nd</a>

```python
class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        ans = [10**5] * n

        # 왼쪽 → 오른쪽 스캔
        prev = -10**5       # 가장 가까운 c 위치 초기화
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
        
        # 오른쪽 → 왼쪽 스캔
        prev = 10**5        # 가장 가까운 c 위치 초기화
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
```
위의 코드보다 조금 더 보기 쉬운 코드도 참고했다.