---
excerpt: "'LeetCode: Shortest Completing Word' 풀이 정리"
title: "\0748. Shortest Completing Word"
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

Given a string `licensePlate` and an array of strings `words`, find the **shortest completing** word in `words`.

A **completing** word is a word that **contains all the letters** in `licensePlate`. **Ignore numbers and spaces** in `licensePlate`, and treat letters as **case insensitive**. If a letter appears more than once in `licensePlate`, then it must appear in the word the same number of times or more.

For example, if `licensePlate`` = "aBc 12c"`, then it contains letters `'a'`, `'b'` (ignoring case), and `'c'` twice. Possible **completing** words are `"abccdef"`, `"caaacab"`, and `"cbca"`.

Return *the shortest **completing** word in* `words`. It is guaranteed an answer exists. If there are multiple shortest **completing** words, return the **first** one that occurs in `words`.

**Example 1:**

- Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
- Output: "steps"
- Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.    
"step" contains 't' and 'p', but only contains 1 's'.    
"steps" contains 't', 'p', and both 's' characters.    
"stripe" is missing an 's'.    
"stepple" is missing an 's'.    
Since "steps" is the only word containing all the letters, that is the answer.

**Example 2:**

- Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
- Output: "pest"
- Explanation: licensePlate only contains the letter 's'.    
All the words contain 's', but among these "pest", "stew", and "show" are shortest.     
The answer is "pest" because it is the word that appears earliest of the 3.

**Constraints:**

- 1 <= licensePlate.length <= 7
- licensePlate contains digits, letters (uppercase or lowercase), or space `' '`.
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 15
- words[i] consists of lower case English letters.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Count only the letters (possibly converted to lowercase) of each word. If a word is shorter and the count of each letter is at least the count of that letter in the licensePlate, it is the best answer we've seen yet.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate_letters = {}          # 키:licensePlate의 알파벳, 값:알파벳의 출현빈도
        total_plate_letters = 0     # 필요한 총 글자 수(중복 포함)
        result = ""

        for ch in licensePlate:
            if ch.isalpha():
                ch = ch.lower()
                plate_letters[ch] = plate_letters.get(ch, 0) + 1
                total_plate_letters += 1

        for word in words:
            if len(word) < total_plate_letters:     # 필요한 총 글자 수보다 짧으면 제외
                continue
            
            completing = True
            for ch, cnt in plate_letters.items():
                if word.count(ch) < cnt:            # 필요한 글자가 없거나 적을 경우 제외
                    completing = False
                    break

            if completing:
                if result == "" or len(word) < len(result):
                    result = word

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.40** MB \| Beats **83.08%**

해시 테이블로 licensePlate의 알파벳과 알파벳의 출현 빈도를 세는 방법이 가장 깔끔한 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/shortest-completing-word/solutions/6741477/conquer-license-plate-completion-with-sm-jes4/" target="_blank">1st</a>

```python
import collections

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        lp = collections.Counter(c for c in licensePlate.lower() if c.isalpha())
        ans = None
        for w in words:
            cw = collections.Counter(w)
            if all(cw.get(c, 0) >= lp[c] for c in lp):
                if ans is None or len(w) < len(ans):
                    ans = w
        return ans
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑚) ← n: 전체 단어 개수, m: 가장 긴 단어 길이     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1) ← 26 alphabets          

collections 모듈의 <mark>Counter</mark>를 쓰면 딕셔너리에 값을 저장하는 과정을 빠르고 간단하게 구현할 수 있다.

licensePlate = "aBc 12c"     
words = ["abccdef", "caaacab", "cbca"]
{: style="color: blue;"}
<pre>
lp = {'c': 2, 'a': 1, 'b': 1}

w         cw                                          len
abccdef   {'c':2, 'a':1, 'b':1, 'd':1, 'e':1, 'f':1}  7   → ans
caaacab   {'a':4, 'c':2, 'b':1}                       7
cbca      {'c':2, 'b':1, 'a':1}                       4   → ans(new)
</pre>

ans = "cbca"
{: style="color: green;"}

### <a href="https://leetcode.com/problems/shortest-completing-word/solutions/276569/python-2-liner-with-explanation-by-rosta-47fx/" target="_blank">2nd</a>

```python
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pc = Counter(filter(lambda x : x.isalpha(), licensePlate.lower()))
        return min([w for w in words if Counter(w) & pc == pc], key=len) 
```
<mark>filter()</mark> 함수(괄호 안에 조건함수, 시퀀스 순으로 작성)와 <mark>&</mark> 연산자를 추가로 이용하여 더 짧은 코드를 만들 수도 있다.