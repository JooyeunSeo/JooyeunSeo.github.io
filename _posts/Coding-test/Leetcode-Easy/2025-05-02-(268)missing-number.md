---
excerpt: "'LeetCode: Missing Number' 풀이 정리"
title: "\0268. Missing Number"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Sorting
  - Array
  - Bitwise
  - sorted()
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array*.

**Example 1:**

- Input: nums = [3,0,1]
- Output: 2
- Explanation:   
`n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**

- Input: nums = [0,1]
- Output: 2
- Explanation:   
`n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 3:**

- Input: nums = [9,6,4,2,3,5,7,0,1]
- Output: 8
- Explanation:   
`n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

**Constraints:**

- n == nums.length
- 1 <= n <= 10<sup>4</sup>
- 0 <= nums[i] <= n
- All the numbers of `nums` are **unique**.

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
```
<i class="fa-solid fa-clock"></i> Runtime: **15** ms \| Beats **34.72%**    
<i class="fa-solid fa-memory"></i> Memory: **13.40** MB \| Beats **62.34%**

주어진 nums 상태에서 for문으로 순회하면 시간이 아주 오래걸리는데, 먼저 <mark>sorted()</mark>로 순서대로 정렬하면 중간에 빨리 빠져나올 가능성이 커지기 때문에 많이 단축할 수 있었다. 다만 Follow up에서 요구하는 시간 복잡도와 공간 복잡도에는 맞출 수 없는 방법이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/missing-number/solutions/6051524/video-using-index-numbers-by-niits-5ozc/" target="_blank">1st</a>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)             # n을 먼저 결과값에 더하고 시작

        for i in range(len(nums)):  # 인덱스 - 요소
            res += i - nums[i]
        
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

**0부터 n까지의 합**은 `n * (n + 1) // 2` 이고, **nums의 모든 원소 합**은 앞의 합에서 숫자 하나만 빠진 값이라는 것을 활용한 방법이다. 이 코드는 `(인덱스의 합 + n) - 요소의 합`을 사용했다.

nums = [3,0,1]   
res = 3
{: style="color: blue;"}
<pre>
i    nums[i]   res
0    3         3 + (0 - 3) = 0
1    0         0 + (1 - 0) = 1
2    1         1 + (2 - 1) = 2
</pre>
res = 2
{: style="color: green;"}

### <a href="https://leetcode.com/problems/missing-number/solutions/4754401/beats-98-users-4-approaches-cjavapythonj-bz73/" target="_blank">2nd</a>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return Tsum - actual_sum
```
`n * (n + 1) // 2` 공식을 그대로 사용한 방법

### <a href="https://leetcode.com/problems/missing-number/solutions/4754401/beats-98-users-4-approaches-cjavapythonj-bz73/" target="_blank">3rd</a>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0                       # 누적 XOR 값
        for i in range(1, n + 1):     # ans에 1부터 n까지 모두 XOR(0은 nums에 포함됨)
            ans ^= i
        for num in nums:              # ans와 nums의 모든 숫자들을 XOR
            ans ^= num
        return ans
```
비트 연산자 <mark>XOR</mark>(^)를 사용한 방법이다.

- `i ^ i = 0`: 같은 값끼리 XOR하면 0
- `i ^ 0 = i`: 0과 XOR하면 자기 자신
- 순서와 괄호에 상관없이 연산 가능

nums = [3,0,1]   
n = 3   
ans = 0
{: style="color: blue;"}
<pre>
XOR 1~3
0 ^= 1 → 1
1 ^= 2 → 3
3 ^= 3 → 0

nums = [3, 0, 1]
0 ^= 3 → 3
3 ^ 0 = 3
3 ^ 1 = 2
</pre>
res = 2
{: style="color: green;"}