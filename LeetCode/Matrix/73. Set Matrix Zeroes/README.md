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
1. Can `m` and `n` be empty?<br>
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
5. Edge case -
   ```python
    Input: matrix = [[1]]
    Output: [[1]]
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / Set
   -  more staightforward approach is to use two sets to record the indices of rows and cols which have zero(s) inside.
2. Matrix / In-plcae replacement
   - Alternatviely, we can use the cells in first row and the first column as markers. Before mark the cells with zero in the same row or column, we have to check wether the first row or column contains zero and record it. 
    
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use Python's `collections.Counter` to count the character frequencies in `ransomNote` and `magazine`, and then compare them.<br>

1) `from collections import Counter`
2) `ransom_count = Counter(ransomNote)`
3) `magazine_count = Counter(magazine)`
4) Iterate each character (key) and its frequency (value) in `ransom_count.items()`
   - if the frequency of the corresponding character in `magazine_count` is less, return `False`
5) If all the charaters pass, return `True`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of `ransomNote`, and M is the length of `magazine`

- Time Complexity: O(N + M)<br>
  `Counter` scans through `ransomNote` and `magazine` once, resulting in linear time.<br>
- Space Complexity: O(N + M)<br>
  In the worst case, all characters are unique, so two separate counters may store up to N + M elements.<br>
  If there is only lowercase English letters, this can be considered O(1).<br>
