---
excerpt: "'LeetCode: Unique Email Addresses' 풀이 정리"
title: "\0929. Unique Email Addresses"
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

Every **valid email** consists of a **local name** and a **domain name**, separated by the `'@'` sign. Besides lowercase letters, the email may contain one or more `'.'` or `'+'`.

- For example, in `"alice@leetcode.com"`, `"alice"` is the **local name**, and `"leetcode.com"` is the **domain name**.

If you add periods `'.'` between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule **does not apply** to **domain names**.

For example, `"alice.z@leetcode.com"` and `"alicez@leetcode.com"` forward to the same email address.
If you add a plus `'+'` in the **local name**, everything after the first plus sign **will be ignored**. This allows certain emails to be filtered. Note that this rule **does not apply** to **domain names**.

- For example, `"m.y+name@email.com"` will be forwarded to `"my@email.com"`.

It is possible to use both of these rules at the same time.

Given an array of strings `emails` where we send one email to each `emails[i]`, return *the number of different addresses that actually receive mails*.

**Example 1:**

- Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
- Output: 2
- Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

**Example 2:**

- Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
- Output: 3

**Constraints:**

- 1 <= emails.length <= 100
- 1 <= emails[i].length <= 100
- `emails[i]` consist of lowercase English letters, `'+'`, `'.'` and `'@'`.
- Each `emails[i]` contains exactly one `'@'` character.
- All local and domain names are non-empty.
- Local names do not start with a `'+'` character.
- Domain names end with the `".com"` suffix.
- Domain names must contain at least one character before `".com"` suffix.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        actual_emails = set()
        for email in emails:
            local, domain = email.split('@')        # @ 기준으로 문자열 구분
            local = local.split('+')[0]             # 로컬이름에서 '+' 이후 무시
            local = local.replace('.', '')          # 로컬이름에서 '.' 제거
            actual_emails.add(f"{local}@{domain}")
        return len(actual_emails)
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **85.51%**    
<i class="fa-solid fa-memory"></i> Memory: **18.11** MB \| Beats **24.52%**

파이썬의 set() 자료형으로 효율을 높이고 split(), replace() 함수로 간단하게 문자열을 처리했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/unique-email-addresses/solutions/1488791/easy-simple-well-defined-code-for-beginn-wq83/" target="_blank">1st</a>

```python
class Solution:
def numUniqueEmails(self, emails: List[str]) -> int:
    
    res = set()
    for email in emails:
        local,domain = email.split('@')
        tmp = ""
        for c in local:
            if c==".": continue
            elif c=="+": break
            else: tmp+=c
        res.add(tmp+"@"+domain)
    
    return len(res)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)        