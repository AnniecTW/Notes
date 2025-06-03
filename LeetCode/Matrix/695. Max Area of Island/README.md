## 695. Max Area of Island
🔗 Link: [Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix<br>

<hr>

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.<br>

The area of an island is the number of cells with a value `1` in the island.<br>

Return the maximum area of an island in `grid`. If there is no island, return `0`.<br>

Example 1:<br>
<img src="https://github.com/user-attachments/assets/befaa2bf-5563-4cf5-9794-2ba81b30d49c" width="350" alt="maxarea1-grid">


>Input:<br>
>```python
>grid = [
>[0,0,1,0,0,0,0,1,0,0,0,0,0],
>[0,0,0,0,0,0,0,1,1,1,0,0,0],
>[0,1,1,0,1,0,0,0,0,0,0,0,0],
>[0,1,0,0,1,1,0,0,1,0,1,0,0],
>[0,1,0,0,1,1,0,0,1,1,1,0,0],
>[0,0,0,0,0,0,0,0,0,0,1,0,0],
>[0,0,0,0,0,0,0,1,1,1,0,0,0],
>[0,0,0,0,0,0,0,1,1,0,0,0,0]
>]
>```
>Output: 6<br>
>Explanation: The answer is not 11, because the island must be connected 4-directionally.<br>


Example 2:<br>

>Input: grid = [[0,0,0,0,0,0,0,0]]<br>
Output: 0<br>


Constraints:<br>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `grid` be empty or contain empty rows (e.g., [] or [[]])? If so, should we return 0?<br>
2. Should we modify the input `grid` in-place, or do we need to preserve it?<br>
3. Happy path -
   ```python
    Input: matrix = [
      [1,0,0],
      [0,1,0],
      [0,1,1]
    ]
    Output: 3
   ```
4. Edge case -
   ```python
    Input: matrix = [[0]]
    Output: 0
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / Graph
   - We can use DFS or BFS to explore the grid. Then we record the number of connected cells having 1 and keep track of the current largest number while exploring.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Choose DFS to explore each cell. When the cell value is 1, call DFS function and record the number of all connected cells having 1 until boundaries met or having 0 in 4 directions. Keep updating the largest area having been computed during exploration.<br>

1) Set `rows, cols = len(grid), len(grid[0])`
2) Set `directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]`
3) Initialize `maxArea = 0`
4) Defince DFS funtion `def dfs(r, c):`
   - If indices `r` and `c` are out of boundaries or `grid[r][c] == 0`, then `return 0`
   - Mark the cell having been visited: `grid[r][c] = 0`
   - Initialize current area `area = 1`
   - Move forward to the four direction and call DFS to accumulate the area when meeting cells having value 1
   ```python
   for dr, dc in directions:
       area += dfs(r + dr, c + dc)
   ```
   - Return `area`
5) Traverse each cell, and when encountering a `1`, call DFS to compute the island area. Update `maxArea` if the result is larger.
   ```python
   for r in range(rows):
       for c in range(cols):
           if grid[r][c] == 1:
               maxArea = max(maxArea, dfs(r, c))
6) Return `maxArea`

    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume M is the number of rows and N is the number of columns of `grid`

- Time Complexity: O(M * N)<br>
  We visit each cell exactly once, so it's O(M * N). <br>
- Space Complexity: O(M * N)<br>
  In the worst case (e.g., entire grid is filled with 1s), the recursion depth could be up to M × N. <br>
