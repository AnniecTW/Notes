## 79. Word Search
🔗 Link: [Word Search](https://leetcode.com/problems/word-search/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix / Backtracking<br>

<hr>

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.<br>


Example 1:<br>
<img src="https://github.com/user-attachments/assets/528ef70d-2fa5-4912-951a-021dda4e73e7" alt="9 * 9 matrix" width="250" />

>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"<br>
Output: true<br>


Example 2:<br>
<img src="https://github.com/user-attachments/assets/214e91ef-d409-45ff-acc2-4a374994d211" alt="4 * 4 matrix" width="250"/>

>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"<br>
Output: true<br>

Example 3:<br>
<img src="https://github.com/user-attachments/assets/1a26ceb0-1b7c-4b36-aa6b-b182e304c34e" alt="4 * 4 matrix" width="250"/>

>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"<br>
Output: false<br>


Constraints:<br>

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

**Follow up**: Could you use search pruning to make your solution faster with a larger board?

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `matrix` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any constraints on time/space complexity?<br>
3. Happy path -
   ```python
    Input: matrix = [
      ['1','2','3'],
      ['4','5','4'],
      ['1','7','6']
    ]
    Output: 6

   ```
5. Edge case -
   ```python
    Input: board = [['1']]
    Output: 1
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Memoization / DFS
   - Since we may visited same postion from different starting nodes, we can use dfs with memoization to record the longest increasing path of explored nodes. 

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We iterate the entire `matrix` with each node as a starting point and perform DFS with memoization.

1) Set `visited = set()`
2) Set `m, n = len(board), len(board[0])`
3) Use a counter to calculate the number of each letter in `word`
   ```python
   for c in word:
       counter[c] = 1 + counter.get(c, 0)
4) If the nubmer of the first character is greater than the last charatcter in `word`, reverse the word
   ```python
    if counter[word[0]] > counter[word[-1]]:
        word = word[::-1]
5) Defince `dfs(r, c ,i)` with backtracking
   a) Base case: If we finish looking for the last character, return `True`<br>
   b) Prune if
      - `r` or `c` is out of bounds
      - current cell visited
      - current cell doesn't match the required letter in `word`
      ```python
      if not (0 <= r < m) or not (0 <= c < n) or (r, c) in visited or board[r][c] != word[i]:
          return False
      ```
      <br>
      
   c) Add `(r, c)` to `visited`, recursively explore four directions<br>
      Backtrack by removing `(r, c)`<br>
      ```python
      visited.add((r, c))
      res = (
          dfs(r - 1, c, i + 1) or
          dfs(r + 1, c, i + 1) or
          dfs(r, c - 1, i + 1) or
          dfs(r, c + 1, i + 1)
      )
      visited.remove((r, c))
      ```
   d) Return the combined result from all directions<br>
   
6) Traverse through the `board`, if the current path explored with `dfs` is found valid, return `True`
   ```python
   for row in range(m):
       for col in range(n):
           if dfs(row, col, 0):
               return True
8) If no valid path is found, return `False`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume M is the nubmer of rows, N is the number of columns of `matrix`

- Time Complexity: O(M * N * 3<sup>L</sup>)<br>
  We visit each node exactly once with the help of memoization while exploration. <br>
- Space Complexity: O(L)<br>
  O(M * N) for both maxium recursion stack depth and memoization.
