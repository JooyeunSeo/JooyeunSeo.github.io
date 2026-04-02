---
excerpt: "'LeetCode: Permutations II' 풀이 정리"
title: "\047. Permutations II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
---

## <i class="fa-solid fa-file-lines"></i> Description



**Example 1:**


**Example 2:**


**Example 3:**


**Constraints:**



**Follow up:** 
**Note:** This question is the same as <a href="" target="_blank">번호.제목</a>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">힌트</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path) == len(nums):          # 종료조건
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: # 같은 숫자면 바로 앞의 값 사용 여부 확인
                    continue

                visited[i] = True           # 선택
                path.append(nums[i])

                dfs(path)                   # 재귀호출

                visited[i] = False          # 복구
                path.pop()

        nums.sort()                             # [1, 1, 2]
        visited = [False] * len(nums)           # [False, False, False]
        result = []
        dfs([])

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **3** ms \| Beats **90.70%**    
<i class="fa-solid fa-memory"></i> Memory: **19.88** MB \| Beats **63.16%**    

nums를 오름차순 정렬 후 각 원소가 사용되었는지 체크하는 배열 visited를 하나 더 생성하는 방법이다. 동일 원소가 여러 개 있을 경우 가장 앞의 원소부터 순서대로 사용해야 같은 조합을 막을 수 있기 때문이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/permutations-ii/solutions/7353142/recursion-easy-solution-c-java-python-by-s2ph/" target="_blank">1st</a>

```python
class Solution:
    def permuteUnique(self, nums):
        res = []

        def backtrack(i):
            if i == len(nums):
                res.append(nums[:])
                return

            seen = set()

            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])

                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]  # backtrack

        backtrack(0)
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛\*𝑛!)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

두 원소를 swap하는 방법을 사용하기 위해 해시셋으로 중복을 제거한 코드도 참고했다.