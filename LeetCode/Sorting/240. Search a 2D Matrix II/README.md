## 240. Search a 2D Matrix II
🔗 Link: [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

<hr>

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:<br>

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.


Example 1:<br>
![searchgrid2](https://github.com/user-attachments/assets/98f3c195-9c60-4073-aaaf-665fc1749264)


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5<br>
Output: true<br>

Example 2:<br>
![searchgrid](https://github.com/user-attachments/assets/8261b7df-63d9-47c8-b7b7-484088e0480f)


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20<br>
Output: false<br>

Constraints:<br>

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- -10<sup>9</sup> < matrix[i][j], target < 10<sup>9</sup>
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `matrix` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Are there duplicate intergers in `matrix`?<br>
4. Happy path - Input: `matrix` = [[1,2],[3,4]], target = 3; Output: true
5. Edge case - Input: `matrix` = [[-1]], target = 2; Output: false
6. Edge case - Input: `matrix` = [[0,1,2]], target = 2; Output: true
7. Edge case - Input: `matrix` = [[0],[1],[2]] target = 2; Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. 2D Array with sorted rows and columns
   - Strategy: Since the matrix is sorted in ascending order both row-wise and column-wise, we can eliminate entire rows or columns that cannot possibly contain the target by moving strategically
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Start from the top-right corner and move left or down to gradually eliminate impossible rows or columns.<br>

1) Initialize `rows = len(matrix)` and `cols = len(matrix[0])`<br>
2) Initialize `r = 0` and `c = cols - 1`<br>
3) While `r < rows`and `c >= 0`<br>
   - If `matrix[r][c]` is equal to `target`, return `true`<br>
   - If `matrix[r][c] > target`, indicating `target` is only possible in columns smaller than column`c`. So set`c = c - 1`<br>
   - If `matrix[r][c] < target`, indicating `target` is only possible in rows larger than row`r`. So set`r = r + 1`<br>
4) If the loop ends, return `false` (target not found)
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of rows and M represents the length of columns of `matrix`

- Time Complexity: O(N + M)<br>
  At each step, we eliminate either a row or a column. In the worst case, we move all the way down and all the way left.
- Space Complexity: O(1)
  
