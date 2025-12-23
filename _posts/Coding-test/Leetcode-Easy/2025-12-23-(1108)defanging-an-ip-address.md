---
excerpt: "'LeetCode: Defanging an IP Address' 풀이 정리"
title: "\01108. Defanging an IP Address"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a valid (IPv4) IP `address`, return a defanged version of that IP address.

A *defanged IP address* replaces every period `"."` with `"[.]"`.

**Example 1:**

- Input: address = "1.1.1.1"
- Output: "1[.]1[.]1[.]1"

**Example 2:**

- Input: address = "255.100.50.0"
- Output: "255[.]100[.]50[.]0"

**Constraints:**

- The given `address` is a valid IPv4 address.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []
        for c in address:
            if c == ".":
                result.append("[.]")
            else:
                result.append(c)
        return "".join(result)
```
<i class="fa-solid fa-clock"></i> Runtime: **29** ms \| Beats **93.39%**    
<i class="fa-solid fa-memory"></i> Memory: **17.10** MB \| Beats **99.65%**    

`replace(".", "[.]")`로 바로 리턴할 수도 있지만, 리스트를 따로 만들어서 저장하는 위 방법이 훨씬 빨랐다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/defanging-an-ip-address/solutions/328895/javapython-3-3-one-liners-one-wo-lib-w-a-gnxc/" target="_blank">1st</a>

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
    def defangIPaddr(self, address: str) -> str:
        return re.sub('\.', '[.]', address)
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

`split()`이나 `re.sub()`를 이용하는 방법도 참고했다.