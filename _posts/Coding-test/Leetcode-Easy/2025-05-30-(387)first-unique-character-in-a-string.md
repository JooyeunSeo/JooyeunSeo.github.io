---
excerpt: "'LeetCode: First Unique Character in a String' 풀이 정리"
title: "\0387. First Unique Character in a String"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Hash Table
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

**Example 1:**

- Input: s = "leetcode"
- Output: 0
- Explanation:   
The character 'l' at index 0 is the first character that does not occur at any other index.

**Example 2:**

- Input: s = "loveleetcode"
- Output: 2

**Example 3:**

- Input: s = "aabb"
- Output: -1

**Constraints:**

- 1 <= s.length <= 10<sup>5</sup>
- `s` consists of only lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = i
            else:
                count[s[i]] = -1

        for ch in s:
            if count[ch] != -1:
                return count[ch]
        return -1
```
<i class="fa-solid fa-clock"></i> Runtime: **73** ms \| Beats **90.75%**    
<i class="fa-solid fa-memory"></i> Memory: **15.91** MB \| Beats **12.96%**

s에서 한 번만 등장하는 문자만 인덱스를 값으로 저장하고, 중복 등장하는 순간 -1로 바꾸는 방법을 사용했다. 두 번째 반복문에서 처음에는 딕셔너리의 값을 순회하는 방법으로 확인했는데, 딕셔너리에 추가된 순서대로 적용되지 않기 때문에 문자열을 다시 순회하는 것이 더 안전했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/first-unique-character-in-a-string/solutions/6638695/master-frequency-counting-to-find-the-fi-00vj/" target="_blank">1st</a>

```python
class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(26 → 1)           

### <a href="https://leetcode.com/problems/first-unique-character-in-a-string/solutions/6520236/2-methods-beginner-freindlyjavacpython-b-jfqs/" target="_blank">2nd</a>

```python
class Solution(object):
    def firstUniqChar(self, s):
         # Create a list to store the frequency of each character
        frequency = [0] * 26  # Assuming only lowercase letters

        # Step 1: Count the frequency of each character
        for char in s:
            frequency[ord(char) - ord('a')] += 1  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25

        # Step 2: Find the first character with a frequency of 1
        for index, char in enumerate(s):
            if frequency[ord(char) - ord('a')] == 1:
                return index  # Return the index of the first unique character

        # Step 3: If no unique character is found, return -1
        return -1
```
소문자 a-z만 나오는 조건이기 때문에 사용할 수 있는 방법으로, 26칸짜리 고정 크기의 리스트를 만들어서 각 문자의 등장 횟수를 저장한 뒤, <mark>ord()</mark>를 통해 0-25 사이의 인덱스로 매핑했다.