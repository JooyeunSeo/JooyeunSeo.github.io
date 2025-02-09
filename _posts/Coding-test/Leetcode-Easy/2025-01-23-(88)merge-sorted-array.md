---
excerpt: "'LeetCode-Merge Sorted Array' 풀이 정리"
title: "\088. Merge Sorted Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array* `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

**Example 1:**

- Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Output: [1,2,2,3,5,6]
- Explanation: The arrays we are merging are [1,2,3] and [2,5,6].    
The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.

**Example 2:**

- Input: nums1 = [1], m = 1, nums2 = [], n = 0
- Output: [1]
- Explanation: The arrays we are merging are [1] and [].    
The result of the merge is [1].

**Example 3:**

- Input: nums1 = [0], m = 0, nums2 = [1], n = 1
- Output: [1]
- Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].    
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

**Constraints:**

- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10<sup>9</sup> <= nums1[i], nums2[j] <= 10<sup>9</sup>

**Follow up:** Can you come up with an algorithm that runs in `O(m + n)` time?

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx_m = m - 1           # nums1에서 유효한 값의 마지막 인덱스
        idx_n = n - 1           # nums2의 마지막 인덱스
        idx_nums1 = m + n - 1   # nums1 전체의 마지막 인덱스

        while idx_m >= 0 and idx_n >= 0:
            if nums1[idx_m] > nums2[idx_n]:
                nums1[idx_nums1] = nums1[idx_m]
                idx_m -= 1
            else:
                nums1[idx_nums1] = nums2[idx_n]
                idx_n -= 1

            idx_nums1 -= 1

        # nums2에 남은 원소가 있으면 처리(nums1에 남은 원소가 있다면 이미 제자리에 있음)
        if idx_n >= 0:
            nums1[:idx_n + 1] = nums2[:idx_n + 1]
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.47** MB \| Beats **33.60%**

정렬된 두 개의 배열을 하나의 정렬된 배열로 병합하는 문제였다. 추가적인 메모리를 사용하지 않고 인덱스 오류 없이 포인터를 사용하기 위해 역방향(뒤에서부터) 병합을 했다.   
<br>

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m] + nums2      # nums1을 앞에서 m개까지 자른 부분과 nums2를 더한 결과를 nums1에 대체
        nums1.sort()                      # nums1을 오름차순으로 정리
```
효율은 낮지만 파이썬 슬라이싱 기능으로 쉽게 해결할 수 있는 코드도 작성해 보았다.   
`nums1[:] = nums1[:m] + nums2`로 작성했지만 `nums1[m:] = nums2`이 더 간단하다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑚+𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

내가 제출했던 코드와 비슷하지만 남은 원소를 처리하는 추가적인 코드 없이 해결한 코드여서 참고해 봤다.