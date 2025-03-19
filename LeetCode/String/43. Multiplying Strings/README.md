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
1. String<br>
   It’s a type of String Manipulation Problem where we are not allowed to directly convert the input strings to integers and multiply them.
2. Simulation / Math<br>
   This problem requires us to simulate the traditional multiplication algorithm where we multiply each digit of num1 with every digit of num2 and manage carry operations.
   It involves building a result array and then filling it by breaking down the multiplications process into individual digit multiplication.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: If either `num1` or `nums2` is zero, return "0". Otherwise, mimic the human calculation process by multiplying each digit of `num1` with each digit of `nums2`, storing the results in a list `rst` and handling carry operations.<br>

1) If either `num1` or `nums2` is zero, return "0"
2) Initialize a list `rst` of length `len(num1) + len(num2)` with all elements `0`. This array stores the intermediate results of multiplication
3) Use nested loop to multiply each digit of `num1` and `num2`
   - Outer loop: Iterate `i` from the last index of `num1` to the first
   - Inner loop: Iterate `j` from the last index of `num2` to the first
   a) Multiply `num1[i]` by `nums[2]` and add the product to `rst[i + j + 1]` to be current `total`
   b) Update `rst[i + j]` by adding the quotient of `total // 10` (carry)
   c) Update `rst[i + j + 1]` by  setting it to `total % 10` (remainder)
6) Convert each element of the list `rst` to a string
7) Concatenate all element of `rst` and remove leading `'0'`
8) If `rst` is non-empty, return it; othrrwise, return `'0'`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of `num1` and M represents the length of `num2`

- Time Complexity: O(N * M)
- Space Complexity: O(N + M)
