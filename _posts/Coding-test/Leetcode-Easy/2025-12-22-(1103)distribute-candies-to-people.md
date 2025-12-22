---
excerpt: "'LeetCode: Distribute Candies to People' 풀이 정리"
title: "\01103. Distribute Candies to People"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Easy
tags:
  - Coding Test
  - Python
  - Math
  - Simulation
  - Weekly Contest
---

## <i class="fa-solid fa-file-lines"></i> Description

We distribute some number of `candies`, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give `n` candies to the last person.

Then, we go back to the start of the row, giving `n + 1` candies to the first person, `n + 2` candies to the second person, and so on until we give `2 * n` candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length `num_people` and sum `candies`) that represents the final distribution of candies.

**Example 1:**

- Input: candies = 7, num_people = 4
- Output: [1,2,3,1]
- Explanation:      
On the first turn, ans[0] += 1, and the array is [1,0,0,0].      
On the second turn, ans[1] += 2, and the array is [1,2,0,0].      
On the third turn, ans[2] += 3, and the array is [1,2,3,0].      
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].

**Example 2:**

- Input: candies = 10, num_people = 3
- Output: [5,2,3]
- Explanation:       
On the first turn, ans[0] += 1, and the array is [1,0,0].      
On the second turn, ans[1] += 2, and the array is [1,2,0].      
On the third turn, ans[2] += 3, and the array is [1,2,3].      
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].

**Constraints:**

- 1 <= candies <= 1<sup>09</sup>
- 1 <= num_people <= 1000

💡 **Hint 1:**   
<u><span style="color:#F5F5F5">Give candy to everyone each "turn" first [until you can't], then give candy to one person per turn.</span></u>

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        count = 1

        # 1. 모든 사람에게 사탕을 나눠줄 수 있을 때까지 반복
        while True:
            gives = (count + (count + num_people - 1)) * num_people // 2    # 이번 턴에서 모두에게 줄 사탕
            if gives > candies:
                break
            for i in range(num_people):
                result[i] += count
                count += 1
            candies -= gives

        # 2. 사탕이 떨어질 때까지 한 사람씩 나눠주기 반복
        for i in range(num_people):
            give = count if candies - count > 0 else candies
            result[i] += give
            candies -= give
            if candies == 0:
                break
            count += 1

        return result
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **17.17** MB \| Beats **99.78%**    

힌트대로 두 단계로 나누면 한 사람씩 순서대로 나눠주는 것보다 더 효율적으로 풀 수 있다. 먼저 모든 사람에게 사탕을 줄 수 있을 때까지 최대한 반복한 이후, 그 다음부터 원래 규칙대로 한 사람씩 나눠주는 방법이다. 모든 사람에게 나눠줄 사탕 갯수를 구하는 공식은 `(시작 숫자 + 끝 숫자) * 전체 인원 / 2`이다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/distribute-candies-to-people/solutions/323314/javapython3-easy-code-w-explanation-and-hl4gi/" target="_blank">1st</a>

```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = num_people * [0]
        give = 0
        while candies > 0:
            people[give % num_people] += min(candies, give + 1)
            give += 1
            candies -= give
        return people
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(√candies)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

효율적인 방법은 아니지만 %를 이용하여 깔끔하게 작성된 코드이기 때문에 참고했다. 

### <a href="https://leetcode.com/problems/distribute-candies-to-people/solutions/323364/javacpython-math-solution-and-simulation-r12t/" target="_blank">2nd</a>

```python
    def distributeCandies(self, candies, n):
        x = int(math.sqrt(candies * 2 + 0.25) - 0.5)    # 전체 지급 가능한 횟수
        res = [0] * n
        for i in xrange(n):
            m = x / n + (x % n > i)                     # 사람 i가 받는 횟수(기본횟수 + 마지막 사람 추가횟수)
            res[i] = m * (i + 1) + m * (m - 1) / 2 * n  # 사람 i가 받는 사탕(등차수열)
        res[x % n] += candies - x * (x + 1) / 2         # 배분 후 남은 사탕을 다음 사람에게 전부 지급
        return res
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛) ← num_people    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

수학 공식으로 더 간단히 풀 수도 있다. x값은 `x(x+1)/2 <= candies` 식을 변형해서 구한 것이다. 