## 73. Set Matrix Zeroes
🔗 Link: [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix<br>

<hr>

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).<br>

 

Example 1:<br>
![mat1](https://github.com/user-attachments/assets/62fbdf79-3b02-4cfb-bcf3-a6bc476de1b1)

>Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]<br>
Output: [[1,0,1],[0,0,0],[1,0,1]]<br>


Example 2:<br>
![mat2](https://github.com/user-attachments/assets/3a41b640-ef42-4452-8d7d-59314dd75f7a)

>Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]<br>
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]<br>


Constraints:<br>

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2<sup>31</sup> <= matrix[i][j] <= 2<sup>31</sup> - 1

**Follow up:**

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `matrix` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path -
   ```python
    Input: matrix = [
      [1,2,0],
      [3,4,5],
      [6,7,8]
    ]

    Output: [
      [0,0,0],
      [3,4,0],
      [6,7,0]
    ]

   ```
4. Edge case -
   ```python
    Input: matrix = [[1]]
    Output: [[1]]
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / Set
   - A straightforward approach is to use two sets to record the indices of rows and columns that contain zero(s).
2. Matrix / In-plcae replacement
   - Alternatviely, we can use the first row and column cells as markers. Before marking, we check whether the first row or column originally contained any zero and store that information in boolean flags
    
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use the first row and column as markers to record which rows and columns should be zeroed. Before modifying the matrix, use boolean flags to record whether the first row or column originally contained any zeros.<br>

1) Set `row = len(matrix), col = len(matrix[0])`
2) Iterate the first row and column and use flags to record if there are any zeros
   ```python
   fisrt_row_zero = any(matrix[0][c] == 0 for c in range(col))
   fisrt_col_zero = any(matrix[r][0] == 0 for r in range(row))
3) Iterate the rest of the matrix and mark the row or column if it contains any zero
   ```python
   for r in range(1, row):
       for c in range(1, col):
           if matrix[r][c] == 0:
               matrix[r][0] = 0
               matrix[0][c] = 0
4) Iterate again and set the row and column having marked cell to zero
   ```python
   for r in range(1, row):
       for c in range(1, col):
           if matrix[r][0] == 0 or matrix[0][c] == 0:
               matrix[r][c] = 0
5) Finally set the first row or column to zero if it contains zero
   ```python
   if fisrt_row_zero:
            for c in range(col):
                matrix[0][c] = 0
        if fisrt_col_zero:
            for r in range(row):
                matrix[r][0] = 0
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the number of rows and M is the number of columns in the matrix.

- Time Complexity: O(N * M)<br>
  We iterate through the matrix a constant number of times, so the time complexity is O(M * N)<br>
- Space Complexity: O(1)<br>
  We use the matrix cell itself as markers, so it takes up constant space.<br>
