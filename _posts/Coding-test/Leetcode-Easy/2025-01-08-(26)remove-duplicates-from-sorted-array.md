---
excerpt: "'LeetCode: Remove Duplicates from Sorted Array' 풀이 정리"
title: "\026. Remove Duplicates from Sorted Array"
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

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates <a href="https://ko.wikipedia.org/wiki/%EC%A0%9C%EC%9E%90%EB%A6%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98" target="_blank">**in-place**</a> such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.
<br><br>

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

- Input: nums = [1,1,2]
- Output: 2, nums = [1,2,\_]
- Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.    
It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

- Input: nums = [0,0,1,1,1,2,2,3,3,4]
- Output: 5, nums = [0,1,2,3,4,\_,\_,\_,\_,\_]
- Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.    
It does not matter what you leave beyond the returned k (hence they are underscores).

**Constraints:**

- 1 <= nums.length <= 3 \* 10<sup>4</sup>
- -100 <= nums[i] <= 100
- `nums` is sorted in non-decreasing order.

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned, what is their positioning in the array when the given array is sorted? Look at the image below for the answer. If we know the position of one of the elements, do we also know the positioning of all the duplicate elements?</span></u>

![](https://assets.leetcode.com/uploads/2019/10/20/hint_rem_dup.png)

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">We need to modify the array in-place and the size of the final array would potentially be smaller than the size of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Essentially, once an element is encountered, you simply need to <b>bypass</b> its duplicates and move on to the next unique element.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq_p = 0      # 같은 숫자를 가진 원소들 중 맨 앞 원소의 인덱스(고유 원소에 카운트됨)
        curr_p = 1      # 현재 가리키는 원소의 인덱스(nums[0]는 무조건 고유 원소이므로 nums[1]부터 시작)
        
        for curr_p in range(1, len(nums)):
            if nums[curr_p] != nums[uniq_p]:    # curr_p가 가리키는 원소가 uniq_p가 가리키는 원소와 불일치하면
                uniq_p += 1                     # uniq_p의 인덱스에 +1 해서 한 칸 옮기기 
                nums[uniq_p] = nums[curr_p]     # curr_p가 가리키는 원소값을 uniq_p가 가리키는 자리에 넣기 

        k = uniq_p + 1  # 0부터 카운트했기 때문에 고유 원소의 개수는 +1 해야 한다
        return k                      
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.87** MB \| Beats **20.32%**

두 개의 포인터(고유 원소를 가리키는 포인터와 현재 노드를 가리키는 포인터)가 필요하다.

`nums` = \[0,0,1,2,2,3,3]     
`uniq_p` = 0     
`curr_p` = 1    
{: style="color: blue;"}

|nums\[curr_p] |\[0]<br>0 |\[1]<br>0 |\[2]<br>1 |\[3]<br>2 |\[4]<br>2 |\[5]<br>3 |\[6]<br>3 |
|:------------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| curr_p = 1   |   **0**  |    (0)   |     1    |     2    |     2    |     3    |     3    |
| curr_p = 2   |     0    |  **0→1** |    (1)   |     2    |     2    |     3    |     3    |
| curr_p = 3   |     0    |     1    |  **1→2** |    (2)   |     2    |     3    |     3    |
| curr_p = 4   |     0    |     1    |   **2**  |     2    |    (2)   |     3    |     3    |
| curr_p = 5   |     0    |     1    |     2    |  **2→3** |     2    |    (3)   |     3    |
| curr_p = 6   |     0    |     1    |     2    |   **3**  |     2    |     3    |    (3)   |

`k` = `uniq_p` + 1 = 3 + 1 = **4**   
`nums`= \[**0**,**1**,**2**,**3**,~~2~~,~~3~~,~~3~~]  (뒤의 원소 3개는 아무것이나 와도 상관없음)
{: style="color: green;"}

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/5540670/video-use-two-pointers-coding-exercise-b-7lap/" target="_blank">1st</a>

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)             
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)   