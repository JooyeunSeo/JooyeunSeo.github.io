---
excerpt: "'LeetCode: Simplify Path' 풀이 정리"
title: "\071. Simplify Path"
header:
  teaser: "https://assets.leetcode.com/static_assets/public/images/LeetCode_Sharing.png"
categories:
  - Leetcode-Medium
tags:
  - Coding Test
  - Python
  - String
  - Stack
---

## <i class="fa-solid fa-file-lines"></i> Description

You are given an absolute path for a Unix-style file system, which always begins with a slash `'/'`. Your task is to transform this absolute path into its **simplified canonical path.**

The rules of a Unix-style file system are as follows:

- A single period `'.'` represents the current directory.
- A double period `'..'` represents the previous/parent directory.
- Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single slash `'/'`.
- Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, `'...'` and `'....'` are valid directory or file names.

The simplified canonical path should follow these rules:

- The path must start with a single slash `'/'`.
- Directories within the path must be separated by exactly one slash `'/'`.
- The path must not end with a slash `'/'`, unless it is the root directory.
- The path must not have any single or double periods (`'.'` and `'..'`) used to denote current or parent directories.

Return the **simplified canonical path.**

**Example 1:**

- Input: path = "/home/"
- Output: "/home"
- Explanation: The trailing slash should be removed.

**Example 2:**

- Input: path = "/home//foo/"
- Output: "/home/foo"
- Explanation: Multiple consecutive slashes are replaced by a single one.

**Example 3:**

- Input: path = "/home/user/Documents/../Pictures"
- Output: "/home/user/Pictures"
- Explanation: A double period `".."` refers to the directory up a level (the parent directory).

**Example 4:**

- Input: path = "/../"
- Output: "/"
- Explanation: Going one level up from the root directory is not possible.

**Example 5:**

- Input: path = "/.../a/../b/c/../d/./"
- Output: "/.../b/d"
- Explanation: `"..."` is a valid name for a directory in this problem.

**Constraints:**

- 1 <= path.length <= 3000
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
- `path` is a valid absolute Unix path.

## <i class="fa-solid fa-cloud-arrow-up"></i> Submitted Code

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for d in path.split('/'):
            if not d or d == '.':     # 슬래쉬 여러 개인 부분이나 현재 디렉토리는 무시
                continue
            elif d == "..":           # 상위 디렉토리는 스택에서 하나 제거하거나 스택이 비었으면 무시
                if stack:
                    stack.pop()
            else:                     # 일반 디렉토리는 추가
                stack.append(d)
        
        return '/' + '/'.join(stack)  # 맨 앞에 슬래쉬 추가 및 모든 디렉토리 슬래쉬로 연결
```
<i class="fa-solid fa-clock"></i> Runtime: **0** ms \| Beats **100.00%**    
<i class="fa-solid fa-memory"></i> Memory: **19.26** MB \| Beats **66.02%**    

`"//"` 부분은 split('/')으로 나누면 하나의 공백이 된다.

## <i class="fa-solid fa-flask"></i> Other Solutions

### <a href="https://leetcode.com/problems/simplify-path/solutions/1050573/python-short-stack-solution-explained-by-spnp/" target="_blank">1st</a>

```python
class Solution:
    def simplifyPath(self, path):
        stack = []
        for elem in path.split("/"):
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".", "", ".."]:
                stack.append(elem)
                
        return "/" + "/".join(stack)
```
<i class="fa-solid fa-clock"></i> **time complexity:** 𝑂(𝑛)    
<i class="fa-solid fa-memory"></i> **space complexity:** 𝑂(𝑛)    

위의 코드보다 더 간략하게 줄인 코드도 참고했다.