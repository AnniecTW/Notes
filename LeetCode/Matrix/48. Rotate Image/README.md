## 48. Rotate Image
🔗 Link: [Rotate Image](https://leetcode.com/problems/rotate-image/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Matrix<br>

<hr>

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image [in-place](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.<br>


Example 1:<br>
<img src="https://github.com/user-attachments/assets/89d15b46-d99d-4988-827c-ce963574000e" alt="9 * 9 matrix" width="350" />

>Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]<br>
Output: [[7,4,1],[8,5,2],[9,6,3]]<br>


Example 2:<br>
<img src="https://github.com/user-attachments/assets/f8b11079-8733-48f7-967a-d304b2016c6a" alt="4 * 4 matrix" width="380"/>


>Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]<br>
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]<br>


Constraints:<br>

- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `matrix` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Is the input always a square matrix (same number of rows and columns)?<br>
3. Any requirements on time/space complexity?<br>
4. Happy path -
   ```python
    Input: matrix = [
      [1,2,0],
      [3,4,5],
      [6,7,8]
    ]

    Output: [
      [6,3,1],
      [7,4,2],
      [8,5,0]
    ]

   ```
5. Edge case -
   ```python
    Input: matrix = [[1]]
    Output: [[1]]
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / Rotate
   - To rotate a martix by 90 degrees(clockwise), we can actually just transpose and then flip it.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: First transpose the matrix. Secondly, reverse each row in it.<br>

1) Set `n = len(matrix)`
2) Transpose the matrix
   ```python
   for i in range(n):
       for j in range(i + 1, n):
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
3) Reverse each row
   ```python
   for row in matrix:
       row.reverse()

    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the dimension of an n x n square matrix

- Time Complexity: O(N²)<br>
  Transposing and reversing each row both take O(N²). <br>
- Space Complexity: O(1)<br>
  In-place rotation. <br>
