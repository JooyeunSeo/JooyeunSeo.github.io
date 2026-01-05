---
excerpt: "'LeetCode: Maximum Number of Balloons' 풀이 정리"
title: "\01189. Maximum Number of Balloons"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Hash Table
  - String
  - Counting
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)
- Input: text = "nlaebolko"
- Output: 1

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)
- Input: text = "loonbalxballpoon"
- Output: 2

**Example 3:**

- Input: text = "leetcode"
- Output: 0

**Constraints:**

- 1 <= text.length <= 1<sup>04</sup>
- text consists of lower case English letters only.

**Follow up:** 
**Note:** This question is the same as <a href="https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/" target="_blank">2287. Rearrange Characters to Make Target String.</a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Count the frequency of letters in the given string.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Find the letter than can make the minimum number of instances of the word "balloon".</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_count = {'b': 0, 'a': 0, 'n': 0, 'l': 0, 'o': 0}
    
        for c in text:
            if c in letter_count:
                letter_count[c] += 1
        
        letter_count['l'] //= 2
        letter_count['o'] //= 2

        return min(letter_count.values())
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.25** MB \| Beats **91.07%**    

문자 `b, a, n, l, o`가 키로 들어있는 해시 테이블을 미리 생성하는 방법이 가장 빨랐다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/maximum-number-of-balloons/solutions/7440334/understandable-2-line-find-min-count-of-4yeyh/" target="_blank">1st</a>

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = {c: text.count(c) for c in text}
        return min(m.get('b', 0), m.get('a', 0), m.get('l', 0)//2, m.get('o', 0)//2, m.get('n', 0))
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

### <a href="https://leetcode.com/problems/maximum-number-of-balloons/solutions/1460763/python-short-counter-solution-explained-x4psc/" target="_blank">2nd</a>

```python
class Solution:
    def maxNumberOfBalloons(self, text):
        cnt = Counter(text)
        return min(cnt["b"], cnt["a"], cnt["l"]//2, cnt["o"]//2, cnt["n"])
```