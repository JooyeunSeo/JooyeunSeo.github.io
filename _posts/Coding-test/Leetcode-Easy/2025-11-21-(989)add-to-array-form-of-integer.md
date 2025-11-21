---
excerpt: "'LeetCode: Add to Array-Form of Integer' 풀이 정리"
title: "\0989. Add to Array-Form of Integer"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

The **array-form** of an integer `num` is an array representing its digits in left to right order.

- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return *the **array-form** of the integer* `num + k`.

**Example 1:**

- Input: num = [1,2,0,0], k = 34
- Output: [1,2,3,4]
- Explanation: 1200 + 34 = 1234

**Example 2:**

- Input: num = [2,7,4], k = 181
- Output: [4,5,5]
- Explanation: 274 + 181 = 455

**Example 3:**

- Input: num = [2,1,5], k = 806
- Output: [1,0,2,1]
- Explanation: 215 + 806 = 1021

**Constraints:**

- 1 <= num.length <= 10<sup>4</sup>
- 0 <= num[i] <= 9
- `num` does not contain any leading zeros except for the zero itself.
- 1 <= k <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        digit = n-1                 # 가장 작은 자릿수부터 시작
        result = []

        while k or digit >= 0:
            if digit >= 0:          # num에 아직 자릿수가 남아있을 때만 k에 더하기
                k += num[digit]
                digit -= 1
            result.append(k % 10)   # k의 현재 자리수 저장
            k //= 10                # k의 다음 자리수로 올리기

        return result[::-1]         # 리스트 뒤집어서 반환
```
<i class="fa-solid fa-clock"></i> Runtime: **11** ms \| Beats **70.60%**    
<i class="fa-solid fa-memory"></i> Memory: **18.04** MB \| Beats **92.14%**    

작은 자릿수부터 계산해서 새 리스트에 넣은 뒤, 마지막에 뒤집는 방법을 사용했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/add-to-array-form-of-integer/solutions/234488/javacpython-take-k-itself-as-a-carry-by-g9mh0/" target="_blank">1st</a>

```python
class Solution:
    def addToArrayForm(self, A, K):
        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

<mark>divmod</mark>를 사용하면 `A[i] + K`의 몫은 다음 자리로 carry되고 나머지는 배열의 기존 자리에 남게 된다.