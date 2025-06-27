---
excerpt: "'LeetCode: Next Greater Element I' 풀이 정리"
title: "\0496. Next Greater Element I"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Stack
  - Monotonic Stack
---

## <i class="fa-solid fa-file-lines"></i> Description

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given **two distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine **the next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return *an array* `ans` *of length* `nums1.length` *such that* `ans[i]` *is **the next greater element** as described above.*

**Example 1:**

- Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
- Output: [-1,3,-1]
- Explanation: The next greater element for each value of nums1 is as follows:
   - 4 is underlined in nums2 = [1,3,<u>4</u>,2]. There is no next greater element, so the answer is -1.
   - 1 is underlined in nums2 = [<u>1</u>,3,4,2]. The next greater element is 3.
   - 2 is underlined in nums2 = [1,3,4,<u>2</u>]. There is no next greater element, so the answer is -1.

**Example 2:**

- Input: nums1 = [2,4], nums2 = [1,2,3,4]
- Output: [3,-1]
- Explanation: The next greater element for each value of nums1 is as follows:
   - 2 is underlined in nums2 = [1,<u>2</u>,3,4]. The next greater element is 3.
   - 4 is underlined in nums2 = [1,2,3,<u>4</u>]. There is no next greater element, so the answer is -1.

**Constraints:**

- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10<sup>4</sup>
- All integers in `nums1` and `nums2` are **unique**.
- All the integers of `nums1` also appear in `nums2`.

**Follow up:** Could you find an `O(nums1.length + nums2.length)` solution?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for n in nums1:
            idx = nums2.index(n)              # nums2에서 n의 위치 idx 찾기
            found = -1
            for next_val in nums2[idx+1:]:    # idx 오른쪽부터 순회
                if next_val > n:
                    found = next_val
                    break
            result.append(found)

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **26** ms \| Beats **32.63%**    
<i class="fa-solid fa-memory"></i> Memory: **12.46** MB \| Beats **99.30%**

단조 스택에 대해 처음 접해봐서 이번 문제는 선형 탐색하는 브루트 포스 알고리즘으로 풀었다. 시간 복잡도가 𝑂(𝑛\*𝑚) 이기 때문에 비효율적이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/next-greater-element-i/solutions/6664285/beats-100-master-monotonic-stack-for-nex-6ubb/" target="_blank">1st</a>

```python
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []    # 현재까지 더 큰 수를 아직 못 찾은 숫자 저장
        d = {}        # 각 숫자에 대해 그 다음 더 큰 수를 저장
        for n in nums2:
            while stack and n > stack[-1]:
                d[stack.pop()] = n    # 스택에서 pop한 값의 다음 큰 수는 n
            stack.append(n)           # n보다 더 큰 수를 찾기 위해 스택에 넣기
        
        for n in stack:   # 다음 더 큰 수가 없는 값들만 스택에 끝까지 남음
            d[n] = -1
        
        return [d[x] for x in nums1]
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)           

**단조 '감소' 스택**을 사용한 풀이 방법이다. 스택에 들어온 새로운 수가 마지막 수보다 더 크다면 마지막 수를 pop하기 때문에 값들이 점점 내림차순으로 쌓이게 된다.

nums1 = [4, 1, 2]   
nums2 = [1, 3, 4, 2]   
{: style="color: blue;"}
<pre>
nums2   stack     d               new stack
1       []        {}              [1]
3       [1] pop   {1: 3}          [3]
4       [3] pop   {1: 3, 3: 4}    [4]
2       [4]       {1: 3, 3: 4}    [4, 2]

stack loop
d[4] = -1
d[2] = -1
d = {1: 3, 3: 4, 4: -1, 2: -1}

nums1
               d[4]=-1
   d[1]=3
                      d[2]=-1
</pre>

return [-1, 3, -1]
{: style="color: green;"}