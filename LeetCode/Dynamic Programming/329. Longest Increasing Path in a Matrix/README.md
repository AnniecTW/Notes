## 329. Longest Increasing Path in a Matrix
🔗 Link: [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Matrix / Memoization<br>

<hr>

Given an `m x n` integers `matrix`, return the length of the longest increasing path in `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).<br>


Example 1:<br>

<img src="https://github.com/user-attachments/assets/e3475fea-68c3-460b-9d84-d2e492ff5e5f" alt="9 * 9 matrix" width="250" />

>Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]<br>
Output: 4<br>
Explanation: The longest increasing path is [1, 2, 6, 9].<br>


Example 2:<br>

<img src="https://github.com/user-attachments/assets/4eee93b5-a254-4bcf-ba26-e5fb1f575684" alt="4 * 4 matrix" width="250"/>

>Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]<br>
Output: 4<br>
Explanation: The longest increasing path is [3, 4, 5, 6].<br>
Moving diagonally is not allowed.<br>


Example 3:<br>

>Input: matrix = [[1]]<br>
Output: 1<br>


Constraints:<br>

- m == board.length
- n = board[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2<sup>31</sup> - 1

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
      [1,2,3],
      [4,5,4],
      [1,7,6]
    ]
    Output: 6 # one possible path: 1 → 2 → 3 → 4 → 5 → 7

   ```
4. Edge case -
   ```python
    Input: board = [['1']]
    Output: 1
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. DFS + Memoization
   - Since the same cell might be visited multiple times from different paths, we use **DFS** to explore all valid increasing paths, and **memoization** to cache the longest path starting from each cell
   - This pattern avoids redundant computation and ensures that each cell is computed only once
   - BFS is less ideal here since we care about increasing order, not shortest path by level

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We iterate `matrix` with each node as a starting point and perform DFS with memoization. Then we get the length of longest path by computing the maximum value stored in `memo`.

1) Check if `matrix` is empty or has no rows → return 0
2) Use a memoization matrix `memo[i][j]` to store the longest increasing path starting at `(i, j)`
3) DFS logic:
4) Define DFS function:
   - If current cell's result is already computed → return memo
   - Else, try moving in four directions
   - Only move to a neighbor `(ni, nj)` if `matrix[ni][nj] > matrix[i][j]`
   - Recursively compute path from `(ni, nj)` and take the max path length
   - Memoize result for `(i, j)` before returning
5) Loop over all cells, run `dfs(i, j)`, and return the maximum value
   
    
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

- Time Complexity: O(M * N)<br>
  Each cell is visited only once due to memoization. Each DFS has at most 4 directions → still constant time per cell overall <br>
- Space Complexity: O(M * N)<br>
  `memo` uses O(M × N). Call stack may go up to O(M × N) in the worst case.
