---
excerpt: "'LeetCode: Find Smallest Letter Greater Than Target' 풀이 정리"
title: "\0744. Find Smallest Letter Greater Than Target"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an array of characters `letters` that is sorted in **non-decreasing order**, and a character `target`. There are **at least two different** characters in `letters`.

Return *the smallest character in* `letters` *that is lexicographically greater than* `target`. If such a character does not exist, return the first character in `letters`.

**Example 1:**

- Input: letters = ["c","f","j"], target = "a"
- Output: "c"
- Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

**Example 2:**

- Input: letters = ["c","f","j"], target = "c"
- Output: "f"
- Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

**Example 3:**

- Input: letters = ["x","x","y","y"], target = "z"
- Output: "x"
- Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

**Constraints:**

- 2 <= letters.length <= 10<sup>4</sup>
- `letters[i]` is a lowercase English letter.
- `letters` is sorted in **non-decreasing** order.
- `letters` contains at least two different characters.
- `target` is a lowercase English letter.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Try to find whether each of 26 next letters are in the given string array.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1 

        # 바로 리턴(target이 첫 번째 원소보다 작은 경우, 마지막 원소보다 크거나 갈은 경우)
        if target < letters[left] or target >= letters[right]: return letters[0]

        # 이진 탐색
        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return letters[left]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.67** MB \| Beats **63.86%**

mid 위치의 문자가 정답이 될 수 있는 후보인 경우 왼쪽에 더 작은 값이 존재할 수 있기 때문에 탐색 범위를 `왼쪽`으로 줄인다. mid에서의 문자가 정답이 될 수 없는 경우(target보다 작거나 같을 때) 탐색 범위를 `오른쪽`으로 줄인다. 이 과정을 반복하면 left는 항상 target보다 큰 문자가 시작하는 위치에 오게 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/find-smallest-letter-greater-than-target/solutions/6091711/ologn-time-o1-space-beats-100-lets-search/" target="_blank">1st</a>

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]: 
            return letters[0]

        # Binary Search
        left, right, result = 0, len(letters)-1, letters[0]
        while left <= right:
            mid = left + (right - left) // 2  # (left + right) // 2와 동일(타 언어에서 오버플로 방지)
            if target >= letters[mid]:
                result = letters[mid+1]
                left = mid + 1
            else:
                result = letters[mid]
                right = mid - 1
        
        return result         
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

변수에 정답 후보를 저장하고 정답이 나올 때까지 갱신해나가는 방법도 있다.