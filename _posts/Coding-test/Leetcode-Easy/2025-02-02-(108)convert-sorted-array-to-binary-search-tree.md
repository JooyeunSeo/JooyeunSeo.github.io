---
excerpt: "'LeetCode-Convert Sorted Array to Binary Search Tree' 풀이 정리"
title: "\0108. Convert Sorted Array to Binary Search Tree"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Binary Search Tree
  - Recursion
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer array `nums` where the elements are sorted in **ascending order**, convert it to a ***height-balanced*** *binary search tree*. (A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.)

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

- Input: nums = [-10,-3,0,5,9]
- Output: [0,-3,9,-10,null,5]
- Explanation: [0,-10,5,null,-3,null,9] is also accepted:

![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

- Input: nums = [1,3]
- Output: [3,1]
- Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

**Constraints:**

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- nums is sorted in a strictly increasing order.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
```
문제 풀이의 아이디어는 **이진 탐색** 알고리즘에서 얻었다. 주어진 리스트가 이미 오름차순으로 정렬됐고, 리스트의 가운데에 위치한 원소를 루트로 하면 왼쪽의 값들(더 작은 값)은 왼쪽 서브트리, 오른쪽의 값들(더 큰 값)은 오른쪽 서브트리로 보낼 수 있기 때문에 적합한 방법이라고 생각했다. 다만 리스트를 양쪽으로 나누고, 각 부분 안에서 또 양쪽으로 나누는 형태여서 좀 헷갈리는 문제였다.

(코드에 문제가 없는데도 TreeNode 객체에서 TypeError가 계속 발생했다. 아마 나눠진 nums가 빈 리스트가 됐을 경우 None을 반환하는 부분 때문인 것 같은데, 다른 답안들도 같은 방법을 쓴 데다가 로컬 환경에서 실행하면 잘 작동되기 때문에 리트코드 자체에 문제가 있는 것 같다. Discussion에서 같은 상황을 해결한 방법들을 참고했지만 결국 제출하지 못했다. 연속 기록이 깨져서 좀 아쉽지만 포스팅만 하기로 했다.)

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/2406277/python-easily-understood-faster-than-86-less-than-83-recursion/" target="_blank">1st</a>

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
```



### <a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/2203558/python-easy-and-fast-solution/" target="_blank">2nd</a>

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
 
        def solve(left, right):
            if left > right:
              return None
            m = (left + right)//2
            return TreeNode(nums[m], solve(left,m-1), solve(m+1,right))
        return solve(0, len(nums)-1)
```