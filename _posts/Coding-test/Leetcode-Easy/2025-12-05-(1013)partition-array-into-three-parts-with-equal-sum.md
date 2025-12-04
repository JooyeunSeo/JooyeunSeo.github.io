---
excerpt: "'LeetCode: Partition Array Into Three Parts With Equal Sum' 풀이 정리"
title: "\01013. Partition Array Into Three Parts With Equal Sum"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Greedy
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array of integers `arr`, return `true` if we can partition the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes `i + 1 < j` with `(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])`

**Example 1:**

- Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
- Output: true
- Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

**Example 2:**

- Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
- Output: false

**Example 3:**

- Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
- Output: true
- Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

**Constraints:**

- 3 <= arr.length <= 5 * 10<sup>4</sup>
- -10<sup>4</sup> <= arr[i] <= 10<sup>4</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">If we have three parts with the same sum, what is the sum of each? If you can find the first part, can you find the second part?</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        else:
            target = sum(arr) // 3
    
        l, r = 0, len(arr)-1
        sum1st, sum3rd = arr[l], arr[r]

        while (l < r) and (r-l >= 2):
            if sum1st == sum3rd == target:
                return True
            if sum1st != target:
                l += 1
                sum1st += arr[l]
            if sum3rd != target:
                r -= 1
                sum3rd += arr[r]

        return False
```
<i class="fa-solid fa-clock"></i> Runtime: **4** ms \| Beats **78.33%**    
<i class="fa-solid fa-memory"></i> Memory: **23.31** MB \| Beats **31.30%**    

포인터 2개로 맨 앞부터 첫 번째 파트, 맨 뒤부터 세 번째 파트를 더해가는 방법을 사용했다. 두 파트 모두 target과 같고, 두 파트 사이에 원소가 하나라도 존재한다면 true가 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/solutions/6887029/very-easy-and-simple-to-understand-by-sr-ltsi/" target="_blank">1st</a>

```python
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        current_sum = 0
        partitions = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum == target:
                partitions += 1
                current_sum = 0
                # If we found two partitions and it's not the end, the rest must be the third
                if partitions == 2 and i < len(arr) - 1:
                    return True
        return False
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

포인터 두 개를 사용하지 않고 앞에서부터 한 파트씩 완성해나가도 된다.