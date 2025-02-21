## 739. Daily Temperatures
🔗 Link: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array<br>

=======================================================================================<br>
Given an array of integers `temperatures` represents the daily temperatures,<br>
return an array `answer` such that answer[i] is the number of days you have to wait after the `ith` day to get a warmer temperature.<br>

If there is no future day for which this is possible, keep `answer[i] == 0` instead.<br>

Example 1:<br>
Input: temperatures = [73,74,75,71,69,72,76,73]<br>
Output: [1,1,4,2,1,1,0,0]<br>

Example 2:<br>
Input: temperatures = [30,40,50,60]<br>
Output: [1,1,1,0]<br>

Example 3:<br>
Input: temperatures = [30,60,90]<br>
Output: [1,1,0]<br>
 

Constraints:<br>
- 1 <= temperatures.length <= 105<br>
- 30 <= temperatures[i] <= 100<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the temperatures array be empty?
2. Any requirements on time/space complexity?
3. Will the numbers in the array duplicate?
4. Happy path - Input: temperatures = [60,40,50,30] Output: [0,1,0,0]
5. Edge case 1 - Input: temperatures = [60,60,60] Output: [0,0,0]
6. Edge case 2 - Input: temperatures = [60,50,40] Output: [0,0,0]
7. Edge case 3 - Input: temperatures = [60] Output: [0]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Array / Stack<br>
In a monotonic stack, the strictly decreasing property is used to find the next greater element for any given element.<br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a monotonic stack to track indices of temperatures in strictly decreasing order, updating the answer when a larger temperature is encountered. If no larger temperature is found, leave the answer as zero. <br>

1) Create a stack, initialize it with a zero number.<br>
2) Initialize the `answers` array with all zeros and length equaling to the length of `temperatures`.<br>
3) Traverse the `temperatures` array from the second element to the end
    - while stack is not empty, add indices of the numbers that are smaller then the last element of the stack.<br>
    - If a larger number is encountered, `answers[index]` equals to the difference between the index of the larger number and that of the last element of the stack (Keep popping until none), where `index = s.pop()`. <br>
    - If no larger number is encountered, remain the `answers[index]` zero.
  
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py 

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the `temperatures` array.


- Time Complexity: O(N)
- Space Complexity: O(N)
