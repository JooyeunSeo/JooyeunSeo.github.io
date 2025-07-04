---
excerpt: "'LeetCode: Relative Ranks' 풀이 정리"
title: "\0506. Relative Ranks"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Sorting
  - Heap (Priority Queue)
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an integer array `score` of size `n`, where `score[i]` is the score of the i<sup>th</sup> athlete in a competition. All the scores are guaranteed to be **unique**.

The athletes are **placed** based on their scores, where the 1<sup>st</sup> place athlete has the highest score, the 2<sup>nd</sup> place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

- The 1<sup>st</sup> place athlete's rank is `"Gold Medal"`.
- The 2<sup>nd</sup> place athlete's rank is `"Silver Medal"`.
- The 3<sup>rd</sup> place athlete's rank is `"Bronze Medal"`.
- For the 4<sup>th</sup> place to the n<sup>th</sup> place athlete, their rank is their placement number   
(i.e., the x<sup>th</sup> place athlete's rank is `"x"`).

Return an array `answer` of size `n` where `answer[i]` is the **rank** of the i<sup>th</sup> athlete.

**Example 1:**

- Input: score = [5,4,3,2,1]
- Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
- Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

**Example 2:**

- Input: score = [10,3,8,9,4]
- Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
- Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

**Constraints:**

- n == score.length
- 1 <= n <= 10<sup>4</sup>
- 0 <= score[i] <= 10<sup>6</sup>
- All the values in `score` are **unique**.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
import heapq

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        max_heap = []   # 최대힙
        place = 1       # 현재 등수 저장

        for idx, s in enumerate(score):
            heapq.heappush(max_heap, (-s, idx))   # 요소의 값(음수변환)과 인덱스 함께 저장

        while max_heap:
            idx = heapq.heappop(max_heap)[1]      # 가장 큰 수가 추출됨(인덱스 값만 가져오기)

            if place == 1:
                score[idx] = "Gold Medal"
            elif place == 2:
                score[idx] = "Silver Medal"
            elif place == 3:
                score[idx] = "Bronze Medal"
            else:
                score[idx] = str(place)
    
            place += 1    # 다음 등수로 이동
    
        return score
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **39.31%**    
<i class="fa-solid fa-memory"></i> Memory: **13.40** MB \| Beats **38.32%**

파이썬 내장 모듈인 <mark>heapq</mark>로 리스트를 **최소힙**처럼 다룰 수 있다. **최대힙**으로 만들기 위해서는 `score` 값에 `-`를 붙여서 추가하는 트릭이 필요하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

<mark>sorted()</mark> 함수로 점수를 정렬한 후, 점수와 순위를 매핑하는 방법이다.

score = [10, 3, 8, 9, 4]
{: style="color: blue;"}
<pre>
sorted_score = [10, 9, 8, 4, 3]
rank_mapping = {
                 10: "Gold Medal",
                  9: "Silver Medal",
                  8: "Bronze Medal",
                  4: "4",
                  3: "5"
               }
</pre>

return ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
{: style="color: green;"}
