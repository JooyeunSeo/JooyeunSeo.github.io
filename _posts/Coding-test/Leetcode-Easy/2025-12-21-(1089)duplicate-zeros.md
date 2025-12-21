---
excerpt: "'LeetCode: Duplicate Zeros' 풀이 정리"
title: "\01089. Duplicate Zeros"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

**Note** that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

**Example 1:**

- Input: arr = [1,0,2,3,0,4,5,0]
- Output: [1,0,0,2,3,0,0,4]
- Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

**Example 2:**

- Input: arr = [1,2,3]
- Output: [1,2,3]
- Explanation: After calling your function, the input array is modified to: [1,2,3]

**Constraints:**

- 1 <= arr.length <= 1<sup>04</sup>
- 0 <= arr[i] <= 9

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">This is a great introductory problem for understanding and working with the concept of in-place operations. The problem statement clearly states that we are to modify the array in-place. That does not mean we cannot use another array. We just don't have to return anything.</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">A better way to solve this would be without using additional space. The only reason the problem statement allows you to make modifications in place is that it hints at avoiding any additional memory.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">The main problem with not using additional memory is that we might override elements due to the zero duplication requirement of the problem statement. How do we get around that?</span></u>

💡 **Hint 4:**   
<u><span style="color:#F5F5F5">If we had enough space available, we would be able to accommodate all the elements properly. The new length would be the original length of the array plus the number of zeros. Can we use this information somehow to solve the problem?</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = n - 1               # 원본 배열 마지막 인덱스 -> 읽기
        j = i + arr.count(0)    # 결과 배열 마지막 인덱스 -> 쓰기

        while i >= 0:
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
                i -= 1
                j -= 1
            else:
                if j < n:
                    arr[j] = 0
                if j-1 < n:
                    arr[j-1] = 0
                i -= 1
                j -= 2
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.46** MB \| Beats **99.58%**    

앞에서부터 채우는 것보다 뒤에서 앞으로 가는 것이 훨씬 인덱스 관리에 수월했다.

arr = [1,0,2,3,0,4,5,0]
{: style="color: blue;"}
<pre>
arr  1  0  2  3  0  4  5  0
                          i
vir  1  0  0  2  3  0  0  4  5  0  0
                                   j
------------------------------------
                       i     j(move)
                    i     j(write)
                 i  j(write)
              i  j(write)
           i  j(write)
        ij(write)
     ij(write)
arr  1  0  0  2  3  0  0  4      
</pre>

arr = [1,0,0,2,3,0,0,4]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/duplicate-zeros/solutions/322576/python-3-real-in-place-solution-by-rokan-hzpw/" target="_blank">1st</a>

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

포인터를 두 개 쓰지 않아도 풀 수 있다.