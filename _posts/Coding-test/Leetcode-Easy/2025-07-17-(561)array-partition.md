---
excerpt: "'LeetCode: Array Partition' 풀이 정리"
title: "\0561. Array Partition"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Greedy
  - Sorting
  - Counting Sort
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs (a1, b1), (a2, b2), ..., (a<sub>n</sub>, b<sub>n</sub>) such that the sum of min(a<sub>i</sub>, b<sub>i</sub>) for all `i` is **maximized**. Return *the maximized sum.*

**Example 1:**

- Input: nums = [1,4,3,2]
- Output: 4
- Explanation: All possible pairings (ignoring the ordering of elements) are:
   1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
   2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
   3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4

So the maximum possible sum is 4.

**Example 2:**

- Input: nums = [6,2,6,5,1,2]
- Output: 9
- Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6).    
min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

**Constraints:**

- 1 <= n <= 10<sup>4</sup>
- nums.length == `2 * n`
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Obviously, brute force won't help here. Think of something else, take some example like 1,2,3,4.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">How will you make pairs to get the result? There must be some pattern.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Did you observe that- Minimum element gets add into the result in sacrifice of maximum element.</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">Still won't able to find pairs? Sort the array and try to find the pattern.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0

        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum
```
<i class="fa-solid fa-clock"></i> Runtime: **35** ms \| Beats **78.36%**    
<i class="fa-solid fa-memory"></i> Memory: **13.78** MB \| Beats **94.68%**

총합을 최대로 만드려면 오름차순으로 정렬 후 인접한 수끼리 짝을 지어서 둘 중 최소값을 구하면 된다.


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/array-partition/solutions/102161/python-1-line-sorting-is-accepted-by-wil-rqf0/" target="_blank">1st</a>

```python
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

파이썬으로 1줄 코드를 작성할 수 있다.

### <a href="https://leetcode.com/problems/array-partition/solutions/6685962/beats-100-conquer-bucket-based-sorting-f-0t9g/" target="_blank">2nd</a>

```python
class Solution(object):
    def arrayPairSum(self, nums):
        bucket = [0] * 20001
        for x in nums:                # 각 숫자의 등장 횟수 카운팅
            bucket[x + 10000] += 1
        res = 0
        flag = True                   # 현재 값 = 짝수 인덱스 → res에 더하기
        for i in range(20001):
            while bucket[i]:
                if flag:
                    res += i - 10000
                flag = not flag       # 다음 값 = 홀수 인덱스
                bucket[i] -= 1
        return res
```
sort 없이 빈도 배열(bucket)을 이용하여 처리하기 때문에 시간 복잡도를 `𝑂(𝑛 + 20001)` 으로 줄일 수 있다. 숫자 범위만큼의 크기를 가진 버킷을 생성하고 nums의 숫자는 인덱스, 인덱스가 가리키는 값을 숫자의 등장횟수로 한다. x가 -10000일 때 `bucket[0]`, x가 0일 때 `bucket[10000]`이 된다.