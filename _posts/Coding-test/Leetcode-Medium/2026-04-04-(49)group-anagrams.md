---
excerpt: "'LeetCode: Group Anagrams' 풀이 정리"
title: "\049. Group Anagrams"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - String
  - Sorting
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

*[anagrams]: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

**Example 1:**

- Input: strs = ["eat","tea","tan","ate","nat","bat"]
- Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
- Explanation:      
There is no string in strs that can be rearranged to form `"bat"`.       
The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.       
The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

- Input: strs = [""]
- Output: [[""]]

**Example 3:**

- Input: strs = ["a"]
- Output: [["a"]]

**Constraints:**

- 1 <= strs.length <= 10<sup>4</sup>
- 0 <= strs[i].length <= 100
- `strs[i]` consists of lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        res = []

        for w in strs:
            sorted_word = ''.join(sorted(w))
            table[sorted_word] = table.get(sorted_word, []) + [w]
        
        for v in table.values():
            res.append(v)

        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **11** ms \| Beats **84.61%**    
<i class="fa-solid fa-memory"></i> Memory: **21.83** MB \| Beats **90.11%**    

정렬한 단어를 키로 사용하는 해시 테이블을 사용했다. sorted()로 문자열을 정렬하면 리스트로 반환되기 때문에 join()으로 다시 합쳐줬다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/group-anagrams/solutions/6113105/video-create-keys-for-group-of-strings-2-tqdx/" target="_blank">1st</a>

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑘log𝑘) ← 𝑘=각 문자열 평균(최대) 길이    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛\*𝑘)    

defaultdict()은 키가 없이도 자동으로 기본값(여기서는 빈 리스트)을 생성하기 때문에 더 깔끔하게 작성할 수 있다.