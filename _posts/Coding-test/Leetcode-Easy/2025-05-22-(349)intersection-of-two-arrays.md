---
excerpt: "'LeetCode: Intersection of Two Arrays' 풀이 정리"
title: "\0349. Intersection of Two Arrays"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - set()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given two integer arrays `nums1` and `nums2`, return an *array of their* intersection. Each element in the result must be **unique** and you may return the result in **any order**.

*[intersection]: The intersection of two arrays is defined as the set of elements that are present in both arrays.

**Example 1:**

- Input: nums1 = [1,2,2,1], nums2 = [2,2]
- Output: [2]

**Example 2:**

- Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
- Output: [9,4]
- Explanation: [4,9] is also accepted.

**Constraints:**

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.49** MB \| Beats **87.67%**

중복 없이 값을 저장하며 연산이 빠른 set()을 사용했다. 두 리스트를 set 타입으로 변경한 뒤, 두 set의 교집합을 구했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/intersection-of-two-arrays/solutions/4850780/99-beats-hashmap-easy-explanation-dry-ru-0is3/" target="_blank">1st</a>

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}               # nums1의 숫자들을 키로 저장
        for num in nums1:
            mp[num] = mp.get(num, 0) + 1  # 키가 딕셔너리에 있으면 해당 값에 +1, 없으면 0 저장
        
        result = []
        for num in nums2:     # nums2에 있는 숫자 중 mp에 있는 것만 결과에 추가
            if num in mp:
                result.append(num)
                del mp[num]
        
        return result
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛+𝑚) ← 두 리스트   
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛) ← 딕셔너리     

이 솔루션은 nums1에서 각 원소가 등장할 때마다 카운트를 하는데, 사실 이 문제에서는 해당 값이 리스트에 있는지만 확인하면 되기 때문에 비효율적인 것 같다.