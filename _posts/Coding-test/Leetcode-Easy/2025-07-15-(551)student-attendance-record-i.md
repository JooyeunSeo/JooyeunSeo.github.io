---
excerpt: "'LeetCode: Student Attendance Record I' 풀이 정리"
title: "\0551. Student Attendance Record I"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - String
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given a string `s` representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

- `'A'`: Absent.
- `'L'`: Late.
- `'P'`: Present.

The student is eligible for an attendance award if they meet **both** of the following criteria:

- The student was absent (`'A'`) for **strictly** fewer than 2 days total.
- The student was **never** late (`'L'`) for 3 or more **consecutive** days.

Return `true` *if the student is eligible for an attendance award, or* `false` *otherwise.*
<br>

**Example 1:**

- Input: s = "PPALLP"
- Output: true
- Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

**Example 2:**

- Input: s = "PPALLL"
- Output: false
- Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

**Constraints:**

- 1 <= s.length <= 1000
- `s[i]` is either `'A'`, `'L'`, or `'P'`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_count = 0

        for i in range(len(s)):
            if s[i] == "P":
                l_count = 0         # 연속 지각일 초기화
            if s[i] == "A":
                l_count = 0         # 연속 지각일 초기화
                a_count += 1        # 결석횟수 + 1
                if a_count == 2:        # 총 지각횟수 2회가 되는 순간 개근상 x
                    return False
            elif s[i] == "L":
                l_count += 1        # 연속 지각일 + 1
                if l_count == 3:        # 연속 지각일 3일이 되는 순간 개근상 x
                    return False
        
        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.48** MB \| Beats **53.08%**

"P", "A"인 경우에는 l_count를 다시 0으로 초기화하는 방식으로 연속 지각일을 체크했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/student-attendance-record-i/solutions/6926152/one-liner-solution-by-p_kanaga_shanmugam-as4v/" target="_blank">1st</a>

```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        return (s.count('A')<2) and len(s.split('LLL'))==1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

반복문을 사용하지 않아도 <mark>count()</mark>, <mark>split()</mark> 함수로 풀 수 있다. 문자열 내에 "LLL"이 있다면 split했을 때 최소 2개의 문자열로 나뉘어지기 때문에 False가 된다.