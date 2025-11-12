---
excerpt: "'LeetCode: DI String Match' 풀이 정리"
title: "\0942. DI String Match"
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
  - Greedy
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

A permutation `perm` of `n + 1` integers of all the integers in the range `[0, n]` can be represented as a string `s` of length `n` where:

- `s[i] == 'I'` `if perm[i] < perm[i + 1]`, and
- `s[i] == 'D'` `if perm[i] > perm[i + 1]`.

Given a string `s`, reconstruct the permutation `perm` and return it. If there are multiple valid permutations perm, return **any of them**.

**Example 1:**

- Input: s = "IDID"
- Output: [0,4,1,3,2]

**Example 2:**

- Input: s = "III"
- Output: [0,1,2,3]

**Example 3:**

- Input: s = "DDI"
- Output: [3,2,0,1]

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- `s[i]` is either `'I'` or `'D'`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        valueI, valueD = 0, len(s)
        result = []

        for ch in s:
            if ch == 'I':
                result.append(valueI)
                valueI += 1
            else:
                result.append(valueD)
                valueD -= 1

        result.append(valueI)
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **2** ms \| Beats **70.98%**    
<i class="fa-solid fa-memory"></i> Memory: **18.62** MB \| Beats **78.87%**    

'I'가 나오면 최솟값인 0부터, 'D'가 나오면 최댓값인 len(s)으로 시작하여 valueI나 valueD에서 1씩 더하거나 뺀다. s 순회를 마치면 valueI == valueD 이 되기 때문에 두 값 중 아무거나 하나를 넣으면 완료된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/di-string-match/solutions/194904/cjavapython-straight-forward-by-lee215-77a9/" target="_blank">1st</a>

```python
class Solution:
    def diStringMatch(self, S):
        left = right = 0
        res = [0]
        for i in S:
            if i == "I":                # 이전보다 증가
                right += 1
                res.append(right)
            else:                       # 이전보다 감소
                left -= 1
                res.append(left)
        return [i - left for i in res]
```
<i class="fa-solid fa-clock"></i> 𝑂(𝑛)      
<i class="fa-solid fa-memory"></i> 𝑂(𝑛)     

인접한 원소들끼리의 차이를 상대적인 높이값으로 나타내는 방법이다. 순회를 마친 뒤 left(최솟값)는 음수가 되기 때문에, 모든 값을 -left만큼 이동시켜서 최솟값이 0이 되도록 조정한다. 위의 코드와 출발점이 다르기 때문에 결과도 다른 패턴으로 나오지만 모두 정답으로 인정된다.