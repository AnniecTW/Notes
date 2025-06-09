## 79. Word Search
🔗 Link: [Word Search](https://leetcode.com/problems/word-search/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix / Backtracking<br>

<hr>

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.<br>


Example 1:<br>
<img src="https://github.com/user-attachments/assets/528ef70d-2fa5-4912-951a-021dda4e73e7" alt="9 * 9 matrix" width="300" />

>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"<br>
Output: true<br>


Example 2:<br>
<img src="https://github.com/user-attachments/assets/214e91ef-d409-45ff-acc2-4a374994d211" alt="4 * 4 matrix" width="300"/>

>Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"<br>
Output: true<br>

Example 3:<br>
<img src="https://github.com/user-attachments/assets/1a26ceb0-1b7c-4b36-aa6b-b182e304c34e" alt="4 * 4 matrix" width="300"/>

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
1. Can `board` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any constraints on time/space complexity?<br>
3. Can I modify the orginal matrix, or should I treat it as read-only?
4. Happy path -
   ```python
    Input: board = [
      ['A','A','B'],
      ['B','D','E'],
      ['C','F','A']
    ], word = 'ABC'

    Output: true

   ```
5. Edge case -
   ```python
    Input: board = [['A']], word = 'A'
    Output: true
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / Backtracking / DFS
   - We use dfs/backtracking to look for a valid path that contains the target word cell by cell.
2. Pruning
   - Before finding a valid path, we first check if the nubmer of the first character is greater than the last one.<br>
     If so, we reverse the word to prevent unnecessary searching. Imagine the following `board` and `word`:
     ```python
     ["B","B","B","B"]
     ["B","B","B","B"]
     ["B","B","C","A"]

     word = "BBBBBBBBAA"
     ```
     If we start from end(`A`) rather than beginning(`B`), we can immediately return `False` in many positions.

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: To prune unnecessary operations, we reverse `word` if the number of the last letter is greater than the first one. Then we iterate through each cell and use dfs to find a valid path.<br>

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
