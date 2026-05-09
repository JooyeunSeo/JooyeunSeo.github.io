---
excerpt: "'LeetCode: Remove Duplicates from Sorted Array II' 풀이 정리"
title: "\080. Remove Duplicates from Sorted Array II"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array nums sorted in **non-decreasing order**, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**In-place**</a> such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array** <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**In-place**</a> with O(1) extra memory.

**Custom Judge:**       
The judge will test your solution with the following code:
```c
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be **accepted**.

**Example 1:**

- Input: nums = [1,1,1,2,2,3]
- Output: 5, nums = [1,1,2,2,3,\_]
- Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.        
It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

- Input: nums = [0,0,1,1,1,1,2,3,3]
- Output: 7, nums = [0,0,1,1,2,3,3,\_,\_]
- Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.         
It does not matter what you leave beyond the returned k (hence they are underscores).

**Constraints:**

- 1 <= nums.length <= 3 * 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- `nums` is sorted in **non-decreasing** order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        k = 2
        for curr in range(2, n):
            if nums[curr] != nums[k-2]:
                nums[k] = nums[curr]
                k += 1

        return k
```
<i class="fa-solid fa-clock"></i> Runtime: **86** ms \| Beats **64.49%**    
<i class="fa-solid fa-memory"></i> Memory: **22.36** MB \| Beats **24.56%**    

<a href="https://jooyeunseo.github.io/leetcode-easy/(26)remove-duplicates-from-sorted-array/" target="_blank">26. Remove Duplicates from Sorted Array</a> 번을 응용하여 중복 허용 개수를 2개까지 늘린 버전이다. 

nums = [1,1,1,2,2,3]
{: style="color: blue;"}
<pre>
[1,  1,  1,  2,  2,  3]
p-2     p,c             → 1 == 1  

[1,  1,  1,  2,  2,  3]
p-2      p   c          → 1 != 2

[1,  1,  2,  2,  2,  3]
    p-2      p   c      → 1 != 2

[1,  1,  2,  2,  2,  3]
        p-2      p   c  → 2 != 3

[1,  1,  2,  2,  3,  2]
</pre>

return 5, nums = [1,1,2,2,3,2]
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/6269804/best-solution-ever-python-java-c-c-javas-dihh/" target="_blank">1st</a>

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 0
                nums[current] = nums[i]
                current += 1
            else:
                count += 1
                if count <= 1:
                    nums[current] = nums[i]
                    current += 1
        return current
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    