---
excerpt: "'LeetCode: 1-bit and 2-bit Characters' 풀이 정리"
title: "\0717. 1-bit and 2-bit Characters"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
---

## <i class="fa-solid fa-file-lines"></i> Description

We have two special characters:

- The first character can be represented by one bit `0`.
- The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

**Example 1:**

- Input: bits = [1,0,0]
- Output: true
- Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

**Example 2:**

- Input: bits = [1,1,1,0]
- Output: false
- Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

**Constraints:**

- 1 <= bits.length <= 1000
- `bits[i]` is either `0` or `1`.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Keep track of where the next character starts. At the end, you want to know if you started on the last bit.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:        # 마지막 비트 이전까지 검사
            if bits[i] == 0:              # 0비트면 1칸 이동
                i += 1
            else:                         # 1비트면 2칸 이동 
                i += 2

        return i == len(bits) - 1       # i가 마지막 인덱스일 경우만 true
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.48** MB \| Beats **61.04%**

마지막 비트가 한 비트(`0`)로만 끝나는지 확인하기 위해 인덱스를 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/1-bit-and-2-bit-characters/solutions/440538/python-time-o-n-99-7-space-o-1-100-0-easy-understand-clean-full-comment/?envType=problem-list-v2&envId=2s2fta2m" target="_blank">1st</a>

```python
# Dev: Chumicat
# Date: 2019/11/30
# Submission: https://leetcode.com/submissions/detail/282638543/
# (Time, Space) Complexity : O(n), O(1)

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        :type bits: List[int]
        :rtype: bool
        """
        # Important Rules:
        # 1. If bit n is 0, bit n+1 must be a new char
        # 2. If bits end with 1, last bit must be a two bit char
        #    However, this case had been rejected by question
        # 3. If 1s in row and end with 0, 
        #    we can use count or 1s to check last char
        #    If count is even, last char is "0"
        #    If count is odd,  last char is "10"
        # Strategy:
        # 1. We don't care last element, since it must be 0.
        # 2. We check from reversed, and count 1s in a row
        # 3. Once 0 occur or list end, We stop counting
        # 4. We use count to determin result
        # 5. Since we will mod count by 2, we simplify it to bool
        ret = True
        for bit in bits[-2::-1]:
            if bit: ret = not ret
            else: break
        return ret
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

뒤에서 두 번째 원소부터 거꾸로 순회하는 방법으로, 마지막 원소 `0` 앞에 연속된 `1`의 개수를 세는 아이디어가 있어서 참고했다.

<pre>
[_, _, 0, 0] → 마지막 0 앞에 1이 0개(짝) → break                 →  true
[_, 0, 1, 0] → 마지막 0 앞에 1이 1개(홀) →  ~ret → break         → false
[0, 1, 1, 0] → 마지막 0 앞에 1이 2개(짝) →  ~ret →  ~ret → break →  true
[1, 1, 1, 0] → 마지막 0 앞에 1이 3개(홀) →  ~ret →  ~ret →  ~ret → false
</pre>