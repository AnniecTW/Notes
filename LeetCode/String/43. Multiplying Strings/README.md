## 43. Multiplying String
🔗  Link: [Multiplying String](https://leetcode.com/problems/multiply-strings/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:<br>

Input: num1 = "2", num2 = "3"<br>
Output: "6"<br>

Example 2:<br>

Input: num1 = "123", num2 = "456"<br>
Output: "56088"<br>
 

Constraints:<br>

- 1 <= num1.length, num2.length <= 200
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   No, `num1` and `num2` contain at least one digit.<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `num1` = "123", `num2` = "45"; Output: "5535"
5. Edge case - Input: `num1` = "0", `num2` = "12345"; Output: "0"

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String
   It’s a type of String Manipulation Problem where we are not allowed to directly convert the input strings to integers and multiply them
3. Simulation / Math
   This problem requires us to simulate the traditional multiplication algorithm where we multiply each digit of num1 with every digit of num2 and manage carry operations.
   It involves building a result array and then filling it by breaking down the multiplications process into individual digit multiplication
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: If one of `num1` and `num2` is zero or both are, then return "0". Otherwise, mimic human mathematic calculations by multiplying each digit of `s1` with that of `s2`, and carry the ten digit number if result is more than 10.<br>

1) If one of `num1` and `nums2` is zero or both are, then return "0"
2) Initialize a list `rst` of length `len(num1) + len(num2)` with all elements 0
3) Use double for loop to multiply each digit of `num1` and `num2` by index `i` and `j`, and add the result to `rst[i + j + 1]`
   - Divide the updated result `total` and add the number to `rst[i + j] `
   - Mod `total` and store the number at `rst[i + j + 1]`
6) After traversal, transform each integer in the list `rst` into string
7) Concatenate all element in `rst` and strip the possible leading '0'
8) If `rst` is not null, return `rst`; othrrwise, return '0'
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of `s1` and M represents the length of `s2`

- Time Complexity: O(N + M)
  The initialization spends O(N) and the sliding process spends O(M - N), summing up to O(M).
- Space Complexity: O(1)
  At most 26 unique characters in the dictionary, meaning that the space used is constant and independent of N and M.
  
