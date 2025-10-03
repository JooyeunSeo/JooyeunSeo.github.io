---
excerpt: "'LeetCode: Positions of Large Groups' 풀이 정리"
title: "\0830. Positions of Large Groups"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Weekly Contest
  - Regular Expression
---

## <i class="fa-solid fa-file-lines"></i> Description

In a string `s` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `s = "abbxxxxzyy"` has the groups `"a"`, `"bb"`, `"xxxx"`, `"z"`, and `"yy"`.

A group is identified by an interval `[start, end]`, where `start` and `end` denote the start and end indices (inclusive) of the group. In the above example, `"xxxx"` has the interval `[3,6]`.

A group is considered **large** if it has 3 or more characters.

Return *the intervals of every **large** group sorted in **increasing order by start index**.*

**Example 1:**

- Input: s = "abbxxxxzzy"
- Output: [[3,6]]
- Explanation: "xxxx" is the only large group with start index 3 and end index 6.

**Example 2:**

- Input: s = "abc"
- Output: []
- Explanation: We have groups "a", "b", and "c", none of which are large groups.

**Example 3:**

- Input: s = "abcdddeeeeaabbbcd"
- Output: [[3,5],[6,9],[12,14]]
- Explanation: The large groups are "ddd", "eeee", and "bbb".

**Constraints:**

- 1 <= s.length <= 1000
- `s` contains lowercase English letters only.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        n = len(s)
        start = 0
        result = []

        for i in range(1, n+1):
            if i == n or s[i] != s[start]:
                end = i - 1
                group_size = end - start + 1

                if group_size >= 3:
                    result.append([start, end])
                
                start = i

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.34** MB \| Beats **89.34%**

for문으로 순회하는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/positions-of-large-groups/solutions/128957/cjavapython-straight-forward-by-lee215-eriu/" target="_blank">1st</a>

```python
    def largeGroupPositions(self, S):
        i, j, N = 0, 0, len(S)    # 그룹 시작 인덱스, 그룹이 끝나기 전까지 이동하는 인덱스
        res = []
        while i < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append([i, j - 1])
            i = j
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)

while문을 사용하는 것이 더 깔끔한 것 같다.

### <a href="https://leetcode.com/problems/positions-of-large-groups/solutions/129431/oneline-python-using-regex-by-practicete-rrxy/" target="_blank">2nd</a>

```python
import re

return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]
```
파이썬의 정규 표현식 모듈 re의 <mark>finditer(pattern, string)</mark> 를 이용한 풀이도 참고했다. 이 함수는 패턴과 매치되는 모든 구간을 찾아서 iterator로 반환하며 `.start()`는 매칭된 부분의 시작 인덱스, `.end()`는 끝 인덱스(포함 안 됨)를 나타낸다.   
패턴 `'(\w)\1{2,}'`에서 `(\w)`는 문자(알파벳 대소문자, 숫자, 언더바) 하나를 그룹에 캡처해 놓는 기능을 하고, `\1`은 첫 번째 캡처 그룹과 동일한 문자를 가리킨다. `{2,}`는 바로 앞 패턴이 최소 2번 이상 반복되는 것을 의미하기 때문에 결국 같은 문자가 3번 이상 연속되는 구간을 모두 잡게 된다.