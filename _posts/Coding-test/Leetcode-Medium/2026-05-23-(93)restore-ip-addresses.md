---
excerpt: "'LeetCode: Restore IP Addresses' 풀이 정리"
title: "\093. Restore IP Addresses"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
  - Backtracking
---

## <i class="fa-solid fa-file-lines"></i> Description

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

- For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return all possible valid IP addresses that can be formed by inserting dots into `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

**Example 1:**

- Input: s = "25525511135"
- Output: ["255.255.11.135","255.255.111.35"]

**Example 2:**

- Input: s = "0000"
- Output: ["0.0.0.0"]

**Example 3:**

- Input: s = "101023"
- Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

**Constraints:**

- 1 <= s.length <= 20
- `s` consists of digits only.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, partition):
            if start == len(s) and partition == 4:                              # 주소 완성
                res.append(".".join(digits))
                return
            
            remaining_chars = len(s) - start
            remaining_parts = 4 - partition
            if not remaining_parts <= remaining_chars <= remaining_parts * 3:   # 조기 종료
                return

            for end in range(start, min(start + 3, len(s))):                    # 1~3자리 정수
                segment = s[start:end+1]
                if segment == "0" or (segment[0] != "0" and int(segment) <= 255):
                    digits.append(segment)
                    backtrack(end + 1, partition + 1)
                    digits.pop()

        res, digits = [], []
        backtrack(0, 0)       # s에서 현재 사용할 글자 위치, 지금까지 만든 조각 개수
        return res
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.35** MB \| Beats **68.18%**    

현재 만든 segment(최소 1자리에서 최대 3자리)를 digits에 저장하고, digits가 모든 조건(s를 모두 사용, 4조각 완성)을 통과했을 경우 유효한 IP 주소로 추가할 수 있다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/restore-ip-addresses/solutions/7699974/python3-optimal-recursive-backtrack-appr-79l8/" target="_blank">1st</a>

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def backtrack(i: int, curr: list, segment: int):
            if segment == 4:
                if i == n:
                    res.append(".".join(curr))
                return
            
            for j in range(i, i+3):
                if j < n:
                    sub = s[i: j+1]
                    if len(sub) > 1 and sub[0] == '0':
                        break
                    if int(sub) <= 255:
                        curr.append(sub)
                        backtrack(j+1, curr, segment+1)
                        curr.pop()
            return

        backtrack(0, [], 0)

        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(3<sup>4</sup>\*4=1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    