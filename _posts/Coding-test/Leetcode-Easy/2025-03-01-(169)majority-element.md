---
excerpt: "'LeetCode: Majority Element' 풀이 정리"
title: "\0169. Majority Element"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Boyer–Moore
  - Majority Vote
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an array `nums` of size `n`, return the *majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

- Input: nums = [3,2,3]
- Output: 3

**Example 2:**

- Input: nums = [2,2,1,1,1,2,2]
- Output: 2

**Constraints:**

- n == nums.length
- 1 <= n <= 5 * 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

**Follow up:** Could you solve the problem in linear time and in `O(1)` space?

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        half = len(nums) // 2 
        front = 0
        back = len(nums) - 1

        while front <= back:
            if nums.count(nums[front]) > half:
                return nums[front]
            else:
                front += 1

            if nums.count(nums[back]) > half:
                return nums[back]
            else:
                back -= 1
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **13.70** MB \| Beats **30.85**

**sort 함수**로 원소를 순서대로 정렬한 후 가운데 원소를 반환하는 방법을 가장 먼저 생각했으나 시간 복잡도가 𝑂(𝑛log𝑛)이어서 넘어갔다. **hash map**을 사용하는 방법도 좋지만 공간 복잡도가 𝑂(𝑛)이기 때문에 다른 방법을 생각해봤다.   
보이어-무어 과반수 투표 알고리즘을 몰랐었기 때문에 리스트 앞쪽과 뒷쪽에서부터 동시에 원소를 체크하며 <mark>count()</mark> 함수로 개수가 과반수 이상인지 세는 방법으로 풀었다. 비효율적인 방법일 수 있지만 과반수 이상의 원소를 찾기 때문에 금방 나와줘서 시간이 별로 안 걸렸던 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/majority-element/solutions/5845732/video-2-solutions-using-hashmap-on-space-2nv6/" target="_blank">1st</a>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0                # 후보(res) 원소와 그 후보의 개수(majority)를 0으로 초기화
        
        for n in nums:
            if majority == 0:                   # majority == 0 이면 후보가 없다는 의미
                res = n                           # 후보가 없으면 먼저 현재 원소를 후보로 설정
            
            majority += 1 if n == res else -1   # 현재 원소가 후보이면 majority+1, 아니면 majority-1
        
        return res                              # 최종적으로 후보로 남은 값이 과반수 원소
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)      
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)           

Boyer-Moore 과반수 투표 알고리즘을 이용하여 과반수를 차지하는 원소를 찾는 방법이다. 과반수가 반드시 존재하는 문제에서만 사용 가능한 방법으로, 과반수 원소는 반드시 절반 이상 등장하기 때문에 마지막에 최종 후보로 남게 되는 원리다.

nums = [2,2,1,1,1,2,2]
{: style="color: blue;"}

<pre>
n     res     majority
      0       0
2     2       1
2     2       2(+1)
1     2       1(-1)
1     2       0(-1) → out
1     1       1
2     1       0(-1) → out
2     2       1
</pre>

res = 2
{: style="color: green;"}