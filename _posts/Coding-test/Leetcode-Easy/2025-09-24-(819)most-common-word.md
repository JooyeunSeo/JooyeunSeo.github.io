---
excerpt: "'LeetCode: Most Common Word' 풀이 정리"
title: "\0819. Most Common Word"
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
  - Counting
  - Weekly Contest
  - Regular Expression
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a string `paragraph` and a string array of the banned words `banned`, return *the most frequent word that is not banne*d. It is **guaranteed** there is **at least one word** that is not banned, and that the answer is **unique**.

The words in `paragraph` are **case-insensitive** and the answer should be returned in **lowercase**.

**Note** that words can not contain punctuation symbols.

**Example 1:**

- Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
- Output: "ball"
- Explanation:    
"hit" occurs 3 times, but it is a banned word.   
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.    
Note that words in the paragraph are not case sensitive,    
that punctuation is ignored (even if adjacent to words, such as "ball,"),    
and that "hit" isn't the answer even though it occurs more because it is banned.

**Example 2:**

- Input: paragraph = "a.", banned = []
- Output: "a"

**Constraints:**

- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space `' '`, or one of the symbols: `"!?',;."`.
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- `banned[i]` consists of only lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        n = len(paragraph)
        frequent = {}
        word = ""
        max_freq = 0
        result = ""
        
        for i in range(n+1):
            if i == n or paragraph[i] == " " or not paragraph[i].isalpha():
                if word and word not in banned:
                    frequent[word] = frequent.get(word, 0) + 1
                word = ""
            elif paragraph[i].isalpha():
                word += paragraph[i].lower()

        for k, v in frequent.items():
            if v > max_freq:
                max_freq = v
                result = k
        
        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **74.34%**    
<i class="fa-solid fa-memory"></i> Memory: **12.48** MB \| Beats **60.35%**

특수문자도 공백문자처럼 단어와 단어 사이를 나누는 부분이기 때문에 한 글자씩 순회하며 단어를 완성하고 banned된 단어가 아닐 경우 딕셔너리에 넣었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/most-common-word/solutions/500772/python-3-three-lines-easy-and-explained-jfvdl/" target="_blank">1st</a>

```python
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # convert to lower case and split string into words by spaces and punctuation
        a = re.split(r'\W+', paragraph.lower())

        # make new list consisitng of words not in banned list (remove banned words)
        b = [w for w in a if w not in banned]

        # return value that counted max times in the new list
        return max(b, key = b.count)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚<sup>2</sup>) ← n: len(paragraph), m: len(b)     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚)           

정규 표현식을 이용하면 <mark>split()</mark>로 쉽게 단어끼리 분리할 수 있다. `r'\W+'`에서 `r`은 백슬래시를 이스케이프 문자가 아닌 문자로 그대로 인식하게 하며, `\W`는 단어가 아닌 구분자([^A-Za-z0-9_])를, `+`는 하나 이상 반복되는 문자를 의미한다.

### <a href="https://leetcode.com/problems/most-common-word/solutions/123854/cjavapython-easy-solution-with-explanati-mw3v/" target="_blank">2nd</a>

```python
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚)  

위의 코드보다 더 효율적으로 정규 표현식을 이용한 답안도 참고했다. 위에서 구분자를 기준으로 split했다면, `'\w+'`는 단어([A-Za-z0-9_]) 덩어리만 <mark>re.findall()</mark>로 뽑는 방식이다. split 방식은 빈 문자열이 생길 수 있지만 이 방법은 더 깔끔하다는 장점이 있다.           
추가로 `banned` 리스트를 **set** 타입으로 변경하고, **collections.Counter**로 단어 출현 빈도를 세는 딕셔너리를 만들어서 시간 효율을 높인 것도 볼 수 있었다. <mark>most_common(k)</mark>은 Counter 객체에 사용 가능한 메서드로, `(단어, 개수)` 튜플의 리스트를 개수 기준 내림차순으로 k개 반환한다.