---
excerpt: "'LeetCode: Longest Common Prefix' 풀이 정리"
title: "\014. Longest Common Prefix"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - String
  - Trie
---

## <i class="fa-solid fa-file-lines"></i> Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

- Input: strs = ["flower","flow","flight"]
- Output: "fl"

**Example 2:**

- Input: strs = ["dog","racecar","car"]
- Output: ""
- Explanation: There is no common prefix among the input strings.

**Constraints:**

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = min(strs, key=len)      # 리스트에서 가장 길이가 짧은 문자열 반환

        for i in range(len(common_prefix)):
            for str in strs:
                if not str.startswith(common_prefix):
                    common_prefix = common_prefix[:-1]
                    continue
        if common_prefix == "":
            return ""
        else:
            return common_prefix
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **36.88%**    
<i class="fa-solid fa-memory"></i> Memory: **12.45** MB \| Beats **19.45%**

리스트의 문자열 중 길이가 가장 짧은 문자열을 먼저 공통 접두사의 기준으로 잡았다.   

- <mark>min()</mark> 함수에 `key` 파라미터를 `len`으로 설정하면 문자열 원소를 가진 리스트에서도 min()을 사용 가능하다.  
- <mark>startswith()</mark> 함수로 각 원소가 common_prefix으로 시작하는지 알아보고, 그렇지 않다면 common_prefix에서 마지막 글자를 하나 뺀 후 다시 반복한다.  

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/longest-common-prefix/" target="_blank">1st</a>

```python
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""          # 출력값을 0으로 초기화
        v=sorted(v)     # sorted() 함수
        first=v[0]      # 리스트의 첫 번째 문자열
        last=v[-1]      # 리스트의 마지막 문자열
        for i in range(min(len(first),len(last))):  # 2개 중 더 짧은 문자열의 길이까지만 한 문자씩 비교
            if(first[i]!=last[i]):                  # 일치하지 않는 문자가 나오면 반복문 중단
                return ans
            ans+=first[i]
        return ans
```

<mark>sorted()</mark> 함수를 사용하여 리스트를 알파벳 순서로 정의하는 방법

- 이 방법으로 정렬하면 첫 번째 문자열과 마지막 문자열이 가장 큰 차이를 갖게 된다.
- 첫 번째 문자열과 마지막 문자열의 공통 접두사만 비교하면 나머지 문자열에도 적용되는 원리

`v` = \["flower", "flow", "flight"]
{: style="color: blue;"} 

sorted(`v`) = ['flight', 'flow', 'flower']    
∴ `first` = flower      
∴ `last` = flight


|i| first\[i] | last\[i] | compare | ans  |
|-|:---------:|:--------:|---------|------|                                                           
|0| f         |  f       | f == f  |  f   |
|1| l         |  l       | l == l  |  fl  | 
|2| i         |  o       | o != i  |  fl  | 

`ans` = fl
{: style="color: green;"} 

### <a href="https://leetcode.com/problems/longest-common-prefix/solutions/6032134/video-simply-create-prefix-between-2-words/" target="_blank">2st</a>

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]        # 리스트의 첫 번째 문자열
        pref_len = len(pref)  # 첫 번째 문자열의 길이

        for s in strs[1:]:                  # 리스트의 두 번째 문자열부터 루프
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:           # pref_len이 0이 될 경우 바로 종료
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛 \* 𝑚) ← {len(strs) - 1} \* 가장 긴 공통 접두사의 길이     
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(len(strs[0]))        

`strs` = \["flower", "flow", "flight"]    
`pref` = flower   
`pref_len` = 6
{: style="color: blue;"} 

💡 **<mark>Python 슬라이싱</mark>은 범위를 벗어나도 인덱스 에러없이 가능한 부분까지만 잘라낸다.**

| pref   | pref_len | s      | s[0:pref_len] | compare        |
|--------|----------|--------|---------------|----------------|
| flower | 6        | flow   | s[0:6] = flow | flower != flow |
| flowe  | 5        | \"     | s[0:5] = flow | flowe != flow  |
| flow   | 4        | \"     | s[0:4] = flow | flow == flow   |
| flow   | 4        | flight | s[0:4] = flig | flow != flig   |
| flo    | 3        | \"     | s[0:3] = fli  | flo != fli     |
| fl     | 2        | \"     | s[0:2] = fl   | fl == fl       |

`pref` = fl
{: style="color: green;"} 
