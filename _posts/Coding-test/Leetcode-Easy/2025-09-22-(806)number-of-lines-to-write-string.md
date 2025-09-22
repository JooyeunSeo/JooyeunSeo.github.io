---
excerpt: "'LeetCode: Number of Lines To Write String' 풀이 정리"
title: "\0806. Number of Lines To Write String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - String
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given a string `s` of lowercase English letters and an array `widths` denoting **how many pixels wide** each lowercase English letter is. Specifically, `widths[0]` is the width of `'a'`, `widths[1]` is the width of `'b'`, and so on.

You are trying to write `s` across several lines, where **each line is no longer than** `100` **pixels**. Starting at the beginning of `s`, write as many letters on the first line such that the total width does not exceed `100` pixels. Then, from where you stopped in `s`, continue writing as many letters as you can on the second line. Continue this process until you have written all of `s`.

Return *an array* `result` *of length 2 where:*

- `result[0]` *is the total number of lines.*
- `result[1]` *is the width of the last line in pixels.*

**Example 1:**

- Input:     
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],     
s = "abcdefghijklmnopqrstuvwxyz"
- Output: [3,60]
- Explanation: You can write s as follows:    
abcdefghij  // 100 pixels wide    
klmnopqrst  // 100 pixels wide    
uvwxyz      // 60 pixels wide    
There are a total of 3 lines, and the last line is 60 pixels wide.

**Example 2:**

- Input:     
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],    
s = "bbbcccdddaaa"
- Output: [2,4]
- Explanation: You can write s as follows:    
bbbcccdddaa  // 98 pixels wide    
a            // 4 pixels wide    
There are a total of 2 lines, and the last line is 4 pixels wide.

**Constraints:**

- widths.length == 26
- 2 <= widths[i] <= 10
- 1 <= s.length <= 1000
- `s` contains only lowercase English letters.


## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1           # total lines
        current = 0         # wide of current line

        for ch in s:
            pixel = widths[ord(ch) - 97]    # ord('a') = 97

            if current + pixel > 100:
                lines += 1
                current = pixel
            else:
                current += pixel

        return [lines, current]
```
<i class="fa-solid fa-clock"></i> Runtime: **8** ms \| Beats **97.27%**    
<i class="fa-solid fa-memory"></i> Memory: **12.45** MB \| Beats **56.82%**

각 문자의 아스키코드 값을 이용하여 widths의 인덱스 값을 계산했다. 만약 현재 라인의 픽셀 수가 정확히 100일 때 s가 끝날 경우 다음 라인으로 넘어가지 않고 그대로 멈춘다는 것을 유의해야 했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/number-of-lines-to-write-string/solutions/120666/easy-solution-6-lines-cjavapython-by-lee-uodn/" target="_blank">1st</a>

```python
    def numberOfcurs(self, widths, S):
        res, cur = 1, 0
        for i in S:
            width = widths[ord(i) - ord('a')]
            res += 1 if cur + width > 100 else 0              # 라인
            cur = width if cur + width > 100 else cur + width # 현재 너비
        return [res, cur]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

좀 더 보기 좋게 정돈된 코드가 있어서 참고했다.