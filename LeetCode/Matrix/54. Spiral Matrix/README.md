## 54. Spiral Matrix
🔗 Link: [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix<br>

<hr>

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.<br>

 

Example 1:<br>
![spiral1](https://github.com/user-attachments/assets/ab472b8c-5541-43a3-a8e9-82e60cd2b46c)


>Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]<br>
Output: [1,2,3,6,9,8,7,4,5]<br>


Example 2:<br>
![spiral](https://github.com/user-attachments/assets/5476ddac-b6e7-4d09-b22a-28f09783d917)


>Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]<br>
Output: [1,2,3,4,8,12,11,10,9,5,6,7]<br>


Constraints:<br>

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can matrix be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any constraints on modifying the input matrix?<br>
3. Any requirements on time/space complexity?<br>
4. Happy path -
   ```python
    Input: matrix = [
      [1,2,0],
      [3,4,5],
      [6,7,8]
    ]

    Output: [1,2,0,5,8,7,6,3,4]

   ```
5. Edge case -
   ```python
    Input: matrix = [[1]]
    Output: [1]
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix Traversal / Simulation
   - This is a classic simulation problem where we move in 4 directions (right, down, left, up) in a controlled loop.
   - Either we modify the input matrix to track visited cells, or we use a set to avoid modifying it.

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Simulate spiral movement using direction vectors and mark visited cells to avoid re-visiting. <br>

1) Set `res = []` and `r, c , dr, dc = 0, 0, 0, 1`
3) Set `m = len(matrix), n = len(matrix[0])`
4) Iterate through the matrix and use `dr` and `dc` to calculate the next position.
   Append the values to `res` and mark the visited cells while iteration
   ```python
   for _ in range(m * n):
       res.append(matrix[r][c])
       matrix[r][c] = "!"

       # next position
       nr, nc = r + dr, c + dc
5) If the next position is out of boundaries or has been visited, shift the direction with (dr, dc) = (dc, -dr), which simulates turning right, then move inwards
   ```python
       if not 0 <= nr < m or not 0 <= nc < n or matrix[nr][nc] == "!":
           dr, dc = dc, -dr

       r += dr
       c += dc
6) Return `res`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume M is the number of rows and N is the number of columns in the matrix.

- Time Complexity: O(M * N)<br>
  Each cell is visted exactly once.<br>
- Space Complexity: O(1)<br>
  O(1) if modifying the matrix in-place (uses no extra data structure).<br>
  O(M × N) if using a set() to track visited cells (but this avoids modifying input, which is often safer in real-world cases).
