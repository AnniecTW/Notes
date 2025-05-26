## 36. Valid Sudoku
🔗 Link: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash<br>

<hr>
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:<br>
1. Each row must contain the digits 1-9 without repetition.<br>
2. Each column must contain the digits 1-9 without repetition.<br>
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.<br>

Note:<br>
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:<br>

![Sudoku-by-L2G-20050714 svg](https://github.com/user-attachments/assets/61d28fd2-cfc7-406b-837c-0138e201b606)
>Input:
>```python
>board = [["5","3",".",".","7",".",".",".","."]
>,["6",".",".","1","9","5",".",".","."]
>,[".","9","8",".",".",".",".","6","."]
>,["8",".",".",".","6",".",".",".","3"]
>,["4",".",".","8",".","3",".",".","1"]
>,["7",".",".",".","2",".",".",".","6"]
>,[".","6",".",".",".",".","2","8","."]
>,[".",".",".","4","1","9",".",".","5"]
>,[".",".",".",".","8",".",".","7","9"]]
>```
>Output: true<br>


Example 2:<br>

>Input:
>```python
>[["8","3",".",".","7",".",".",".","."]
>,["6",".",".","1","9","5",".",".","."]
>,[".","9","8",".",".",".",".","6","."]
>,["8",".",".",".","6",".",".",".","3"]
>,["4",".",".","8",".","3",".",".","1"]
>,["7",".",".",".","2",".",".",".","6"]
>,[".","6",".",".",".",".","2","8","."]
>,[".",".",".","4","1","9",".",".","5"]
>,[".",".",".",".","8",".",".","7","9"]]
>```
>Output: false<br>
>Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:<br>

- board.length == `9`
- board[i].length == `9`
- board[i][j] is a digit `1-9` or `'.'`.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Is a Sudoku board filled entirely with `'.'`(i.e., empty) considered valid?<br>
2. Any constraints on time/space complexity?<br>
3. Happy path - 
Input:
```python
[["7","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
Output: false<br>

4. Edge case - 
Input:
```python
[[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]]
```
>Output: true<br>

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. 2D arrays / Hash
   - Use three arrays of sets to detect duplicates in rows, column, and 3 x 3 sub-boxes
   - Use this formula `(row // 3) * 3 + (col // 3)` to calculate the box index
     
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use three arrays of sets to record existing digits and detect duplicates in rows (`rows[r]`), columns (`cols[c]`), and 3 x 3 sub-boxes (`boxes[box_idx]`)<br>

1) Initialize `rows`, `cols`, and `boxes` as `List[Set]`:
   ```python
   rows = [set() for _ in range(9)]
   cols = [set() for _ in range(9)]
   boxes = [set() for _ in range(9)]
   ```
2) Iterate the board in both rows and columns:
   ```python
   for r in range(N):<br>
       for c in range(N):
   ```
3) Set `val = board[r][c]`
4) If `val = '.'`, then skip current loop
5) Calculate the box index of each cell with `box_idx = (r // 3) * 3 + (c // 3)`
6) If `val` is in `rows[r]`, `cols[c]` or `boxes[box_idx]`, then return `False`
7) Add val to `rows[r]`, `cols[c]`, and `boxes[box_idx]`
8) Return `True` if all the cells pass

    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the number of rows of `board`, and M is the number of columns of `board`

- Time Complexity: O(1)<br>
  Since the board is fixed size (9x9), the runtime is O(1).<br>
- Space Complexity: O(N + M)<br>
  We use 9 * 3 = 27 sets for rows, cols, and boxes. In the worst case(all distinct digits), each set holds at most 9 elements. So total space is bounded and also O(1).
