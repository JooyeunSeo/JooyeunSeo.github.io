---
excerpt: "'LeetCode: Subtract the Product and Sum of Digits of an Integer' 풀이 정리"
title: "\01281. Subtract the Product and Sum of Digits of an Integer"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.

**Example 1:**

- Input: n = 234
- Output: 15 
- Explanation:       
Product of digits = 2 * 3 * 4 = 24       
Sum of digits = 2 + 3 + 4 = 9      
Result = 24 - 9 = 15    

**Example 2:**

- Input: n = 4421
- Output: 21
- Explanation:      
Product of digits = 4 * 4 * 2 * 1 = 32     
Sum of digits = 4 + 4 + 2 + 1 = 11     
Result = 32 - 11 = 21    

**Constraints:**

- 1 <= n <= 10<sup>5</sup>

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">How to compute all digits of the number ?</span></u>

💡 **Hint 2:**   
<u><span style="color:#F5F5F5">Use modulus operator (%) to compute the last digit.</span></u>

💡 **Hint 3:**   
<u><span style="color:#F5F5F5">Generalise modulus operator idea to compute all digits.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0

        while n > 0:
            last = n % 10       # 마지막 자리 숫자
            product *= last
            sum += last
            n //= 10
        
        return product - sum
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.41** MB \| Beats **5.95%**    

% 연산으로 자릿수만큼 while문을 반복하는 방법이 가장 정석인 것 같다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/solutions/446372/javacpython-straight-forward-solution-by-ff43/" target="_blank">1st</a>

```python
from functools import reduce
import operator

class Solution:
    def subtractProductAndSum(self, n):
        A = list(map(int, str(n)))
        return reduce(operator.mul, A) - sum(A)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(log𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(1)    

정수 n을 문자열로 변경하여 푸는 방법이다. 정수 n의 자릿수는 `⌊logn⌋ + 1`개이기 때문에 위의 방법과 시간복잡도는 동일하다.