## 74. Search a 2D Matrix
🔗 Link: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

<hr>

You are given an `m x n` integer matrix `matrix` with the following two properties:<br>

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.<br>

You must write a solution in O(log(m * n)) time complexity.<br>


Example 1:<br>
![mat](https://github.com/user-attachments/assets/288ce3cb-eb06-45d9-87c0-3e02d8246b23)

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3<br>
Output: true<br>

Example 2:<br>
![mat2](https://github.com/user-attachments/assets/2d661012-c0a0-451f-92ca-4753653f98d7)

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13<br>
Output: false<br>

Constraints:<br>

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10<sup>4</sup> < matrix[i][j], target < 10<sup>4</sup>

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `matrix` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Are there duplicate intergers in `matrix`?<br>
4. Happy path - Input: `matrix` = [[1,2],[3,4]], target = 0; Output: false
5. Edge case - Input: `matrix` = [[-1]], target = -1; Output: true
6. Edge case - Input: `matrix` = [[-1],[0]], target = 2; Output: false

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. 2D - Array / Binary Search
   - Strategy: Use Binary Search twice — first locate the correct row , then to locate the column within that row
   - Optimization: Treat the 2D matrix as a flattened 1D sorted array. Use `row = index // num_cols`, `col = index % num_cols` to map the 1D indices back to 2D coordinates.

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Since each row is sorted in non-decreasing order and each first element of a row is greater than the last of the previous row, we can treat the 2D matrix as a flattened 1D sorted array. Use standard binary search to map 1D indices back into 2D coordinates.

1) Set `m` to the number of rows and `n` to the number of columns
2) Initialize `start` to 0 and `end` to `m * n - 1`
3) While `start <= end`, repeat the following steps<br>
   - use `mid = (start + end) // 2` to calculate the middle index `mid` when stretched in a 1D array <br>
   - map `mid` to the 2D coordinates, using `row, col = mid // n, mid % n`<br>
   - If `matrix[row][col] == target`, return `true`<br>
   - If `matrix[row][col] < target`, set `start = mid + 1`<br>
   - Otherwise, set `end = mid - 1`<br>
4) Return `false` if the target is not found
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume M represents the number of rows in `matrix` and N represents the number of cols in `matrix`

- Time Complexity: O(log (M * N))<br>
  We conduct binary search on a virtual 1D array of size M * N.
- Space Complexity: O(1)
  
