---
excerpt: "'LeetCode: Find the Town Judge' 풀이 정리"
title: "\0997. Find the Town Judge"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Graph
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties **1** and **2**.

You are given an array `trust` where trust[i] = [a<sub>i</sub>, b<sub>i</sub>] representing that the person labeled a<sub>i</sub> trusts the person labeled b<sub>i</sub>. If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

Return the *label of the town judge if the town judge exists and can be identified, or return* `-1` *otherwise.*

**Example 1:**

- Input: n = 2, trust = [[1,2]]
- Output: 2

**Example 2:**

- Input: n = 3, trust = [[1,3],[2,3]]
- Output: 3

**Example 3:**

- Input: n = 3, trust = [[1,3],[2,3],[3,1]]
- Output: -1

**Constraints:**

- 1 <= n <= 1000
- 0 <= trust.length <= 10<sup>4</sup>
- trust[i].length == 2
- All the pairs of `trust` are **unique**.
- a<sub>i</sub> != b<sub>i</sub>
- 1 <= a<sub>i</sub>, b<sub>i</sub> <= n




**Follow up:** 
**Note:** This question is the same as 번호: <a href="" target="_blank"></a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">hint</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = {n: 0 for n in range(1, n+1)}  # 모든 주민을 후보에 넣고 시작
        
        for a, b in trust:
            candidates.pop(a, None)       # a는 후보에서 탈락 (이미 탈락했다면 None 반환)
            if b in candidates:           # b가 아직 후보라면 b를 신뢰하는 사람 +1
                candidates[b] += 1
        
        for k, v in candidates.items():   # 모든 주민들이 신뢰하는 사람이 있는지 확인
            if v == n-1:
                return k
        
        return -1
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **96.29%**    
<i class="fa-solid fa-memory"></i> Memory: **21.01** MB \| Beats **15.82%**    

모든 주민들을 딕셔너리에 먼저 넣은 뒤, 누군가를 신뢰하는 주민은 빼고 신뢰받는 주민에는 카운트하는 것이 가장 깔끔하면서 모든 케이스를 커버하는 방법인 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-the-town-judge/solutions/1663344/cjavapython3javascript-everything-you-ne-ifeb/" target="_blank">1st</a>

```python
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (N+1)
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
            
        for i in range(1, len(Trusted)):
            if Trusted[i] == N-1:
                return i
        return -1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

딕셔너리 대신 인덱스를 주민의 숫자로 사용하는 리스트를 사용하는 방법도 있다.