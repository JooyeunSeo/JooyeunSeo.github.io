---
excerpt: "'LeetCode: Assign Cookies' 풀이 정리"
title: "\0455. Assign Cookies"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Sorting
  - Two Pointers
  - Greedy
---

## <i class="fa-solid fa-file-lines"></i> Description

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

**Example 1:**

- Input: g = [1,2,3], s = [1,1]
- Output: 1
- Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.   
You need to output 1.

**Example 2:**

- Input: g = [1,2], s = [1,2,3]
- Output: 2
- Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children,    
You need to output 2.

**Constraints:**

- 1 <= g.length <= 3 * 10<sup>4</sup>
- 0 <= s.length <= 3 * 10<sup>4</sup>
- 1 <= g[i], s[j] <= 2<sup>31</sup> - 1

**Note:** This question is the same as <a href="https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/" target="_blank">2410: Maximum Matching of Players With Trainers.</a>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) == 0:   # 쿠키가 없으면 바로 0 반환
            return 0
        
        g.sort()          # 두 리스트 정렬
        s.sort()
        
        child = 0         # g 포인터
        cookie = 0        # s 포인터

        while child <= len(g) - 1 and cookie <= len(s) - 1:
            if s[cookie] >= g[child]:   # s가 g를 만족시킬때만 child 이동
                child += 1
            cookie += 1                 # cookie 이동

        return child
```
<i class="fa-solid fa-clock"></i> Runtime: **30** ms \| Beats **78.67%**    
<i class="fa-solid fa-memory"></i> Memory: **13.98** MB \| Beats **95.75%**

값을 오름차순으로 정렬한 뒤, 두 개의 포인터를 사용하여 Greedy 방식으로 푸는 것이 정석인 것 같다. 리스트 두 개를 정렬하기 때문에 𝑂(𝑛log𝑛 + 𝑚log𝑚)의 시간 복잡도가 소요된다.