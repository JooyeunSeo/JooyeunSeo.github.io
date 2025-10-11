---
excerpt: "'LeetCode: Lemonade Change' 풀이 정리"
title: "\0860. Lemonade Change"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Array
  - Greedy
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the i<sup>th</sup> customer pays, return `true` *if you can provide every customer with the correct change, or* `false` *otherwise*.

**Example 1:**

- Input: bills = [5,5,5,10,20]
- Output: true
- Explanation:     
From the first 3 customers, we collect three $5 bills in order.    
From the fourth customer, we collect a $10 bill and give back a $5.    
From the fifth customer, we give a $10 bill and a $5 bill.    
Since all customers got correct change, we output true.

**Example 2:**

- Input: bills = [5,5,10,10,20]
- Output: false
- Explanation:     
From the first two customers in order, we collect two $5 bills.    
For the next two customers in order, we collect a $10 bill and give back a $5 bill.    
For the last customer, we can not give the change of $15 back because we only have two $10 bills.    
Since not every customer received the correct change, the answer is false.

**Constraints:**

- 1 <= bills.length <= 10<sup>5</sup>
- `bills[i]` is either `5`, `10`, or `20`.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0                            # 5$ 개수
        ten = 0                             # 10$ 개수

        for b in bills:
            if b == 5:                      # no change
                five += 1                   
            elif b == 10:
                if five > 0:                
                    five -= 1               # change = 5x1
                    ten += 1
                else:
                    return False
            elif b == 20:
                if five > 0 and ten > 0:    
                    five -= 1               # change = 10x1 + 5x1
                    ten -= 1
                elif five > 2:              
                    five -= 3               # change = 5x3
                else:
                    return False

        return True
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **15.17** MB \| Beats **89.63%**

15달러를 거슬러줘야할 때 단위가 큰 10달러부터 우선 소진하도록 조건을 설정했다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/lemonade-change/solutions/143719/cjavapython-straight-forward-by-lee215-w58k/" target="_blank">1st</a>

```python
    def lemonadeChange(self, bills):
        five = ten = 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five, ten = five - 1, ten + 1
            elif ten > 0: five, ten = five - 1, ten - 1
            else: five -= 3
            if five < 0: return False
        return True
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)          

if문 조건을 바꿔서 길이를 좀 더 짧게 만든 코드도 참고했다.