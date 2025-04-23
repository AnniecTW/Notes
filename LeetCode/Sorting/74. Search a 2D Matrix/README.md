## 74. Search a 2D Matrix
🔗 Link: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

============================================================================================<br>
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
===========================================================================================<br>
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
   - Optimization: Treat the 2D matrix as a flattened 1D sorted array. Use `row = index // num_cols`, `col = index % num_cols` to map the 1D index back to 2D coordinates.

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We use a modified binary search to find the target in O(log n) time. At each iteration, one side of the mid element must be sorted.<br>
              We can check whether the target lies in the sorted half and move our boundaries accordingly.

1) Initialize `left = 0` and `right = len(nums) - 1` 
2) While `left <= right`, repeat the following steps<br>
   - calculate the middle index `mid` using `mid = (left + right) // 2`<br>
   - If `nums[mid]` is equal to `target`, return `mid`<br>
   - If `nums[left] <= nums[mid]`, indicating the left half is sorted, check whether target is in this part<br>
     - If so, set `right = mid - 1`<br>
     - Otherwise, set `left = mid + 1`<br>
   - If the right half is sorted, check whether the target is in it<br>
     - If so, set `left = mid + 1`<br>
     - Otherwise, set `right = mid - 1`<br>
3) Return `-1` if the target is not found
    
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
- Space Complexity: O(1)
  
