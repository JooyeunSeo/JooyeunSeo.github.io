---
excerpt: "'LeetCode: Design HashMap' 풀이 정리"
title: "\0706. Design HashMap"
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

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the key already exists in the map, update the corresponding `value`.
- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
- `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

**Example 1:**

- Input     
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]    
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
- Output     
[null, null, null, 1, -1, null, 1, null, -1]
- Explanation     
MyHashMap myHashMap = new MyHashMap();    
myHashMap.put(1, 1); // The map is now [[1,1]]    
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]    
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]    
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]    
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)    
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]    
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]    
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

**Constraints:**

- 0 <= key, value <= 10<sup>6</sup>
- At most 10<sup>4</sup> calls will be made to `put`, `get`, and `remove`.     

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class MyHashMap(object):

    def __init__(self):
        self.hashmap = [-1] * 1000001   # 키: 인덱스, 값: -1로 초기화

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.hashmap[key]

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashmap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```
<i class="fa-solid fa-clock"></i> Runtime: **77** ms \| Beats **55.10%**    
<i class="fa-solid fa-memory"></i> Memory: **37.73** MB \| Beats **11.68%**

바로 이전 문제 **705**번과 같이 키를 인덱스로 쓰는 리스트를 생성하는 방법을 썼다. 이번에는 키-값 쌍을 저장해야 하기 때문에 해당 인덱스 위치에 값을 저장하고, 아직 키가 저장되지 않았거나 삭제된 경우 `-1`을 넣었다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/design-hashmap/solutions/6279872/video-how-we-think-about-a-solution-pyth-m16w/" target="_blank">1st</a>

```python
class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next  # 같은 버킷 안의 다음 노드 가리킴

class MyHashMap:

    def __init__(self):
        self.map = []

        for _ in range(1000):         # 해시맵(버킷 리스트) 크기를 1000으로 설정
            self.map.append(Node())     # 각 버킷에 더미 노드를 head로 삽입

    def hash(self, key):                          # 해시 함수(나머지 연산)로 키 → 버킷 인덱스 변환
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]              # 해당 버킷 찾기

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value                # 이미 키가 있으면 value 갱신
                return
            cur = cur.next                            

        cur.next = Node(key, value)                 # 키가 없으면 맨 끝에 새 노드 삽입

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val                 # 키 찾으면 값 반환
            cur = cur.next

        return -1                                   # 키가 없으면 -1 반환
        
    def remove(self, key: int) -> None:           
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next            # 키가 있다면 노드 삭제(이전 노드를 다다음으로 연결)
                return
            cur = cur.next
```
<i class="fa-solid fa-clock"></i> **time complexity:** all operations: 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑚+𝑛) ← bucket+key 개수           

**연결 리스트**로 구현하면 배열 인덱싱 방법보다 메모리 낭비가 적고 키의 범위가 유동적일 때도 사용할 수 있다는 장점이 있다.

### <a href="https://leetcode.com/problems/design-hashmap/solutions/1970885/python-basic-hashtable-implementation-by-7erg/" target="_blank">2nd</a>

```python
class MyHashMap:

    def __init__(self):
        self.BUCKET_SIZE = 1000
        # bucket[i] stores a list of (key, value)
        self.buckets = [[] for _ in range(self.BUCKET_SIZE)]

    def getBucket(self, key):
        return self.buckets[key % self.BUCKET_SIZE]

    def findIndexOfKey(self, bucket, key):
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        bucket = self.getBucket(key)
        index = self.findIndexOfKey(bucket, key)
        if index != -1:
            bucket[index][1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.getBucket(key)
        index = self.findIndexOfKey(bucket, key)
        if index == -1: return -1
        return bucket[index][1]

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        index = self.findIndexOfKey(bucket, key)
        if index == -1: return
        del bucket[index]
```
각 버킷을 연결 리스트가 아닌 배열로도 구현 가능하지만, 원소 삭제 시 그 뒤의 요소를 한 칸씩 이동해야 하기 때문에 연결 리스트보다 더 느리다는 단점이 있다.