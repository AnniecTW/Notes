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
1. Can `board` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any constraints on time/space complexity?<br>
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
1. Matrix / Backtracking / DFS
   - We can first mark the cells which aren't captured by performing dfs on cells on edges, and then find those cells connected four directonally.<br>
     The left unmarked cells are not captured and should be changed to `'X'`.<br>

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Perform dfs on cells on edges and mark those cell with 'O' as well as those connected four directionally. Iterate through `board`, replace the left `'O'` with `'X'`, and set `'*'` back to `'O'`.

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
5) Defince `dfs(r, c ,i)` for backtracking
   a) Base case: If we finish looking for the last character, return `True`<br>
   b) Prune if
      - `r` and `c` are out of bounds
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

Assume M is the nubmer of rows, N is the number of columns of `board`, and L is the length of `word`

- Time Complexity: O(M * N * 3<sup>L</sup>)<br>
  For each of the M * N cells, we may start a DFS. At each step in the DFS, we can explore up to 3 directions (can't revisit the previous cell), and the maximum depth of the DFS is `L` (the length of the `word`). So, the overall time complexity is O(M * N * 3<sup>L</sup>). <br>
- Space Complexity: O(L)<br>
  The recursion stack and `visited` set both take up to O(L) space in the worst case. If we can modify the `board`, we can eliminate the `visited` set entirely and mark visited cells in-place (e.g., replacing with '#' temporarily), which reduces memory usage.<br>
