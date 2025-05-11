## 240. Search a 2D Matrix II
🔗 Link: [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

<hr>

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:<br>

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.


Example 1:<br>
![searchgrid](https://github.com/user-attachments/assets/8261b7df-63d9-47c8-b7b7-484088e0480f)


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5<br>
Output: true<br>

Example 2:<br>
![searchgrid2](https://github.com/user-attachments/assets/98f3c195-9c60-4073-aaaf-665fc1749264)


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
1. 2D - Array / Binary Search
   - Strategy: Use Binary Search twice — first avoid the impossible row, then to locate the column within all possible rows
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We first conduct binary search on the last column, and then only dive into the rows whose last column's values are larger than target.<br>
              Then do binary search on these rows one by one. At the same time, we can narrow down the range during each search by the result of previous search.

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

Assume N represents the length of `nums`

- Time Complexity: O(log N)<br>
  Binary search halves the search space in each iteration, leading to logarithmic time complexity.
- Space Complexity: O(1)
  
