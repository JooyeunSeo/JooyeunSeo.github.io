---
excerpt: "'LeetCode: Search in Rotated Sorted Array' 풀이 정리"
title: "\033. Search in Rotated Sorted Array"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
---

## <i class="fa-solid fa-file-lines"></i> Description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

- Input: nums = [4,5,6,7,0,1,2], target = 0
- Output: 4

**Example 2:**

- Input: nums = [4,5,6,7,0,1,2], target = 3
- Output: -1

**Example 3:**

- Input: nums = [1], target = 0
- Output: -1

**Constraints:**

- 1 <= nums.length <= 5000
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- All values of nums are **unique**.
- `nums` is an ascending array that is possibly rotated.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l, r = 0, n
        
        while l <= r:
            m = (l + r) // 2          # 중간값
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:            # 왼쪽이 정렬되고
                if nums[l] <= target < nums[m]:   # 정렬된 왼쪽 범위에 target 존재
                    r = m - 1
                else:
                    l = m + 1                     # 오른쪽 범위에 target 존재
            elif nums[m] <= nums[r]:            # 오른쪽이 정렬되고
                if nums[m] < target <= nums[r]:   # 정렬된 오른쪽 범위에 target 존재
                    l = m + 1
                else:                             # 왼쪽 범위에 target 존재
                    r = m - 1
        
        return -1
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.50** MB \| Beats **30.45%**    

이진 탐색으로 두 포인터의 가운데를 찾으면, 최소한 한 쪽은 정렬되어 있다는 규칙을 이용할 수 있다. target이 속한 정렬된 범위를 찾을 때까지 포인터 m의 왼쪽 또는 오른쪽으로 이동하며 탐색하면 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="" target="_blank">1st</a>

```c++
class Solution {
public:
    int search(int A[], int n, int target) {
        int lo=0,hi=n-1;
        // find the index of the smallest value using binary search.
        // Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
        // Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
        while(lo<hi){
            int mid=(lo+hi)/2;
            if(A[mid]>A[hi]) lo=mid+1;
            else hi=mid;
        }
        // lo==hi is the index of the smallest value and also the number of places rotated.
        int rot=lo;
        lo=0;hi=n-1;

        // The usual binary search and accounting for rotation.
        while(lo<=hi){
            int mid=(lo+hi)/2;
            int realmid=(mid+rot)%n;
            if(A[realmid]==target)return realmid;
            if(A[realmid]<target)lo=mid+1;
            else hi=mid-1;
        }
        return -1;
    }
};
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

최소값의 위치(회전된 시작점)를 먼저 찾은 후, 정렬된 배열처럼 인덱스를 보정하는 방법이다.