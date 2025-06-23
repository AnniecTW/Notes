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

General Idea: We iterate `matrix` with each node as a starting point and perform DFS with memoization. Then we get the length of longest path by computing the maximum value stored in `memo`.

1) Edge case:
   ```python
   if not matrix or not matrix[0]:
       return 0
2) Set `rows, cols = len(matrix), len(matrix[0])`
3) Initialize `memo = [[0] * cols for _ in range(rows)]`
4) Define DFS function:
   - If the cell is visited, return it's corresponding result
   ```python
   if memo[i][j]: 
       return memo[i][j]
   ```
   - Set `max-len = 1` as at least one step starting from this cell
   - Move in four directions and update `max_len` if the condition is valid
   ```python
    max_len = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + dx, j + dy
        if (0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]): 
            max_len = max(max_len, 1 + dfs(ni, nj))
   ```
   - Memoization:
     ```python
     memo[i][j] = max_len  # memoization
     ```
   - Return `max_len`
     
5) Return `max(dfs(i, j) for i in range(rows) for j in range(cols))`
   
    
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
