---
excerpt: "'LeetCode-Search Insert Position' 풀이 정리"
title: "\035. Search Insert Position"
header:
  teaser: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/LeetCode_Logo_black_with_text.svg/458px-LeetCode_Logo_black_with_text.svg.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Binary Search
---

## <i class="fa-solid fa-file-lines"></i> Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

- Input: nums = [1,3,5,6], target = 5
- Output: 2

**Example 2:**

- Input: nums = [1,3,5,6], target = 2
- Output: 1

**Example 3:**

- Input: nums = [1,3,5,6], target = 7
- Output: 4

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- `nums` contains **distinct** values sorted in **ascending** order.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_p = 0                  # 왼쪽 포인터의 인덱스
        right_p = len(nums) - 1     # 오른쪽 포인터의 인덱스

        while left_p <= right_p:    # 왼쪽 포인터가 오른쪽 포인터보다 커지면 out
            mid_p = (right_p + left_p) // 2     # 왼쪽과 오른쪽의 가운데 포인터의 인덱스

            if target == nums[mid_p]:   # target이 이미 존재하는 경우 가운데 포인터 반환
                return mid_p                
            elif target < nums[mid_p]:  # target이 mid보다 작으면 mid의 왼쪽 부분배열 탐색
                right_p = mid_p - 1
            else:                       # target이 mid보다 크면 mid의 오른쪽 부분배열 탐색
                left_p = mid_p + 1
            
        return right_p + 1          # '오른쪽 포인터 > 왼쪽 포인터'일 때 '오른쪽 포인터 + 1'에 삽입
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100%**    
<i class="fa-solid fa-memory"></i> Memory: **12.87** MB \| Beats **38.64%**

오름차순으로 정렬된 리스트에서 이진 탐색(<em>binary search</em>)을 사용했다. 이진 탐색은 이미 **정렬**된 리스트 형태에서 사용 가능한 방법으로, 리스트의 크기를 절반씩 줄여가며 주어진 탐색 키(target)와 같은 값의 원소를 찾는 원리이다.   

리스트의 크기가 n일 때 매번 루프를 실행할 때마다 절반으로 나누어 탐색하기 때문에 문제의 조건에 맞게 𝑂(log𝑛)의 시간 복잡도를 기록한다.

while문 밖의 반환값을 right_p + 1로 했는데, 그냥 left_p로 적는 것이 더 깔끔할 것 같다.
<br><br>

nums = \[1, 3, 5, 6]
{: style="color: blue;"}

<pre>
-1   0    1    2    3   4   (index)
-----------------------------------------
    [1,   3,   5,   6]      target = 5
     l    m         r       5 > 3
               lm   r       5 == 5
     
    [1,   3,   5,   6]      target = 2
     l    m         r       2 < 3
     lrm                    2 > 1
     rm   l                 while loop out
                            return r + 1 = 1
     
    [1,   3,   5,   6]      target = 0
     l    m         r       0 < 3
     lrm                    0 < 1
 r   lm                     while loop out
                            return r + 1 = 0
     
    [1,   3,   5,   6]      target = 7
     l    m         r       7 > 3
               lm   r       7 > 5
                    lrm     7 > 6
                    rm   l  while loop out
                            return r + 1 = 4
</pre>