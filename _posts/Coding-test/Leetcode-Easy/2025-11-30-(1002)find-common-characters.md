---
excerpt: "'LeetCode: Find Common Characters' 풀이 정리"
title: "\01002. Find Common Characters"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string array `words`, return *an array of all characters that show up in all strings within the* `words` *(including duplicates)*. You may return the answer in **any order**.

**Example 1:**

- Input: words = ["bella","label","roller"]
- Output: ["e","l","l"]

**Example 2:**

- Input: words = ["cool","lock","cook"]
- Output: ["c","o"]

**Constraints:**

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- `words[i]` consists of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = {}
        result = []

        for i in range(len(words)):
            for ch in words[i]:
                # 키: 첫 번째 단어의 문자들 / 값: 단어 개수만큼의 길이를 가진 리스트
                if i == 0 and ch not in count:
                    count[ch] = [0] * len(words)
                # 각 단어에서 해당 문자의 등장 횟수 카운트
                if ch in count:
                    count[ch][i] += 1

        for k, v in count.items():
            min_val = min(v)          # 최소 등장 횟수로 공통 횟수 정하기
            for _ in range(min_val):
                result.append(k)

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **9** ms \| Beats **68.17%**    
<i class="fa-solid fa-memory"></i> Memory: **17.80** MB \| Beats **65.72%**    

각 키마다 len(words) 크기의 리스트가 생성되기 때문에 비효율적인 면이 있는 코드다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-common-characters/solutions/247560/python-1-line-by-lee215-u93p/" target="_blank">1st</a>

```python
class Solution:
    def commonChars(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

collections 모듈의 **Counter**와 교집합 연산 **&**을 이용하여 시간/공간 복잡도를 최적화할 수 있다. Counter 객체에 전용 메서드인 <mark>elements()</mark>를 쓰면 각 키를 값(카운터)만큼 반복해서 뽑아준다(마지막에 리스트 타입으로 변환 필요).