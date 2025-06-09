## 130. Surrounded Regions
🔗 Link: [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix<br>

<hr>

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:<br>
- Connect: A cell is connected to adjacent cells horizontally or vertically.<br>
- Region: To form a region connect every `'O'` cell.<br>
- Surround: The region is surrounded with `'X'` cells if you can connect the region with `'X'` cells and none of the region cells are on the edge of the `board`.<br>

To capture a surrounded region, replace all `'O'`s with `'X'`s in-place within the original board. You do not need to return anything.<br>


Example 1:<br>

<img src="https://github.com/user-attachments/assets/6ec1944e-4296-46e3-88ec-ddcc0ab571b4" alt="4 * 4 matrix" width="350" />

>Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]<br>
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]<br>
Explanation: In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.


Example 2:<br>
>Input: board = [["X"]]<br>
Output: [["X"]]<br>


Constraints:<br>

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `board` be empty or contain empty rows (e.g., `[]` or `[[]]`)?<br>
2. Are there any constraints on time and space complexity?<br>
3. Happy path -
   ```python
    Input: board = [
      ['X','X','X'],
      ['X','O','X'],
      ['X','X','X']
    ]

    Output: [
      ['X','X','X'],
      ['X','X','X'],
      ['X','X','X']
    ]

   ```
4. Edge case -
   ```python
    Input: board = [['O']]
    Output: [['O']]
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / DFS
   - We first mark the `'O'` regions that are **not surrounded** by `'X'` by performing DFS from the boundary cells. These are the `'O'`s that should remain unchanged.<br>

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Perform dfs on cells from the boundary and mark those cell with 'O' as well as those connected four directionally. Iterate through `board`, replace the left `'O'` with `'X'`, and set `'*'` back to `'O'`.

1) Set `rows, cols = len(board), len(board[0])`
2) Define `dfs(r, c)`
   a) Return if:
      - `r` or `c` is out of bounds
      - the current cell is not `'O'`
      ```python
      if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'O':
          return
      ```
      <br>
      
   b) Mark visited cells and go to adjacent cells four directionally<br>
      ```python
      board[r][c] = '*'
      dfs(r+1, c)
      dfs(r-1, c)
      dfs(r, c+1)
      dfs(r, c-1)
      ```
3) Perform DFS from the boundary cells (first and last rows & columns)
   ```python
   for r in range(rows):
       dfs(r, 0)
       dfs(r, cols - 1)
   for c in range(cols):
       dfs(0, c)
       dfs(rows - 1, c)
4) Replace the left `'O'` with `'X'` and restore `'*'` to `'O'`
   ```python
   for r in range(rows):
       for c in range(cols):
           if board[r][c] == 'O':
                board[r][c] = 'X'
           elif board[r][c] == '*':
                board[r][c] = 'O'
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume M is the number of rows and N is the number of columns in the `board`

- Time Complexity: O(M * N)<br>
  We traverse `board` twice and each cell is explored at most once during each traversal. <br>
- Space Complexity: O(M * N)<br>
  The recursion stack mitht take up to O(M * N) space in the worst case (e.g., all cells are `'O'`).<br>
