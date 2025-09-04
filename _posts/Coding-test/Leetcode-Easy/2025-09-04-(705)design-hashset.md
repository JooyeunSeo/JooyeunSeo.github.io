---
excerpt: "'LeetCode: Design HashSet' 풀이 정리"
title: "\0705. Design HashSet"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Hash Table
  - Linked List
  - Design
  - Hash Function
---

## <i class="fa-solid fa-file-lines"></i> Description

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

`void add(key)` Inserts the value `key` into the HashSet.
`bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
`void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

**Example 1:**

- Input   
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]   
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
- Output   
[null, null, null, true, false, null, true, null, false]   
- Explanation    
MyHashSet myHashSet = new MyHashSet();      
myHashSet.add(1);      // set = [1]      
myHashSet.add(2);      // set = [1, 2]      
myHashSet.contains(1); // return True      
myHashSet.contains(3); // return False, (not found)      
myHashSet.add(2);      // set = [1, 2]      
myHashSet.contains(2); // return True      
myHashSet.remove(2);   // set = [1]      
myHashSet.contains(2); // return False, (already removed)

**Constraints:**

- 0 <= key <= 10<sup>6</sup>
- At most 10<sup>4</sup> calls will be made to `add`, `remove`, and `contains`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class MyHashSet(object):

    def __init__(self):
        self.hashset = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hashset.get(key, False) # 값이 False거나 딕셔너리에 추가된 적 없는 key는 False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```
<i class="fa-solid fa-clock"></i> Runtime: **21** ms \| Beats **91.58%**    
<i class="fa-solid fa-memory"></i> Memory: **18.60** MB \| Beats **35.05%%**



## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/design-hashset/solutions/6736637/conquer-constant-time-set-operations-wit-ge5p/" target="_blank">1st</a>

```python
class MyHashSet(object):
    def __init__(self):
        self.a = [False] * 1000001    # from 0 to 10^6

    def add(self, key):
        self.a[key] = True

    def remove(self, key):
        self.a[key] = False

    def contains(self, key):
        return self.a[key]
```
<i class="fa-solid fa-clock"></i> **time complexity:**  all operations: 𝑂(1)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)            

딕셔너리 대신 `key`를 인덱스로 사용하는 리스트를 이용하여 푸는 방법도 있었다. 모든 원소가 False인 리스트를 key의 범위만큼의 길이로 설정한 뒤 키가 추가/삭제될 때마다 해당 인덱스의 원소를 바꿔주면 된다.

### <a href="https://leetcode.com/problems/design-hashset/solutions/6279609/best-solution-for-arrays-hashset-in-c-py-4wq2/" target="_blank">2nd</a>

```python
class MyHashSet:
    def __init__(self):
        self.n = 10000                          # 해시 버킷 개수
        self.arr = [[] for _ in range(self.n)]  # 리스트 10,000개를 가진 2차원 배열

    def add(self, key: int) -> None:
        idx = key % self.n                      # 해시 함수로 키가 들어간 버킷 위치 계산
        if key not in self.arr[idx]:            # 해당 버킷 안에 키가 없으면 추가
            self.arr[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.n
        if key in self.arr[idx]:
            self.arr[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % self.n
        return key in self.arr[idx]
```
파이썬에 내장된 `set`의 내부 동작을 간단하게 구현한 코드도 참고했다. 이 문제에서는 10,000 개의 버킷을 만들 경우 버킷당 100개 정도의 키를 넣을 수 있다.

Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]   
{: style="color: blue;"}
<pre>    
               idx   arr                    set
add(1)       →  1    arr[1] = []  → add     [1]
add(2)       →  2    arr[2] = []  → add     [1, 2]
contains(1)  →  1    arr[1] = [1] → True
contains(3)  →  3    arr[3] = []  → False
add(2)       →  2    arr[2] = [2] → x       [1, 2]
contains(2)  →  2    arr[2] = [2] → True 
remove(2)    →  2    arr[2] = [2] → remove  [1]
contains(2)  →  2    arr[2] = []  → False
</pre>

Output: [null, null, null, true, false, null, true, null, false]
{: style="color: green;"}