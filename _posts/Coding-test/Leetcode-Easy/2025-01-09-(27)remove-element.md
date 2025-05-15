---
excerpt: "'LeetCode: Remove Element' 풀이 정리"
title: "\027. Remove Element"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Two Pointers
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` <a href="https://ko.wikipedia.org/wiki/%EC%A0%9C%EC%9E%90%EB%A6%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98" target="_blank">**in-place**</a>. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.
<br><br>

**Custom Judge:**     
The judge will test your solution with the following code:
```c
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.


**Example 1:**

- Input: nums = [3,2,2,3], val = 3
- Output: 2, nums = [2,2,\_,\_]
- Explanation: Your function should return k = 2, with the first two elements of nums being 2.   
It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

- Input: nums = [0,1,2,2,3,0,4,2], val = 2
- Output: 5, nums = [0,1,4,0,3,\_,\_,\_]
- Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.   
Note that the five elements can be returned in any order.   
It does not matter what you leave beyond the returned k (hence they are underscores).

**Constraints:**

- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to remove that element per-say, right?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">We can move all the occurrences of this element to the end of the array. Use two pointers!</span></u>

![](https://assets.leetcode.com/uploads/2019/10/20/hint_remove_element.png)

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Yet another direction of thought is to consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.
</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:          # 빈 리스트일 경우 0 반환
            return 0

        front_p = 0                 # 앞에서부터 시작하는 포인터(맨 앞 원소의 인덱스로 초기화)
        back_p = len(nums) - 1      # 뒤에서부터 시작하는 포인터(맨 뒤 원소의 인덱스로 초기화)

        while front_p <= back_p:        # front_p가 back_p보다 작거나 같을때까지만 루프
            if nums[front_p] != val:    
                front_p += 1
            elif nums[front_p] == val and nums[back_p] != val:
                nums[front_p] = nums[back_p]
                front_p += 1
                back_p -= 1
            else:
                back_p -= 1             # nums[front_p] == val and nums[back_p] == val
                
        return len(nums[:front_p])      # num를 front_p의 바로 뒤까지 자른 길이(k)만큼을 반환
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **12.61** MB \| Beats **18.84%**

두 개의 포인터(앞에서부터 시작하는 포인터와 뒤에서부터 시작하는 포인터)가 필요하다.

while문을 이용해서 반복문을 생성했는데, 리스트가 비어있을 경우에 대응하기 위해 위에 따로 코드를 적어야 했다. 하지만 그냥 for문으로 하고 `range(len(nums))`로 범위를 설정하면 `range(0)`일 때 for문이 아예 실행되지 않기 때문에 더 간단해서 좋은 것 같다. 


## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-element/solutions/5468263/video-step-by-step-explanation-by-niits-eyte/" target="_blank">1st</a>

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛) ← 리스트의 크기에 비례        
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)   

두 개의 포인터가 모두 맨 앞에서부터 시작하고, 현재 포인터 `i`의 원소값과 `val`이 다를 때만 포인터 `k`를 이동하는 방식이다.   

`nums` = \[3,2,2,3]   
`val` = 3   
{: style="color: blue;"}

| start | 3<br>k<br>i        | 2<br><br><br>      | 2<br><br><br>  | 3<br><br><br>  | i = val   |
|:-----:|:------------------:|:-------------------:|:--------------:|:--------------:|-----------|
|   1   | 3<br>k<br><br>     | 2<br><br>i         | 2<br><br><br>  | 3<br><br><br>  | i ≠ val   |
|   2   | **2**<br>→<br><br> | 2<br>k<br><br>     | 2<br><br>i     | 3<br><br><br>  | i ≠ val   |
|   3   | 2<br><br><br>      | **2**<br>→<br><br> | 2<br>k<br><br> | 3<br><br>i     | i ≠ val   |
|   4   | 2<br><br><br>      | 2<br><br><br>      | 2<br>k<br><br> | 3<br><br><br>  | i = val   |

`k`= 0 + 1 + 1 = 2    
∴ `k` = 2    
{: style="color: green;"}

### <a href="https://leetcode.com/problems/remove-element/solutions/6225048/beginners-attempt-by-leetcoder974-r21u/" target="_blank">2nd</a>

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)  # 리스트에서 가장 먼저 발견한 val을 지우고 그 뒤를 한 칸씩 앞으로 이동하여 재정렬
        return len(nums)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛<sup>2</sup>)         
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)   

코드는 간단하지만, <mark>.remove()</mark> 함수는 리스트를 순회하는 원리이다.   
따라서 최악의 경우 시간 복잡도가 O(n<sup>2</sup>)이 되어 효율이 떨어진다.