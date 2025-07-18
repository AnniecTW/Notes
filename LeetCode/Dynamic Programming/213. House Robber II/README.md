## 198. House Robber II
🔗 Link: [House Robber II](https://leetcode.com/problems/house-robber-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Dynamic Programming<br>

<hr>

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight *without alerting the police*.<br>

Example 1:<br>

>Input: nums = [2,3,2]<br>
Output: 3<br>
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.<br>

Example 2:<br>

>Input: nums = [1,2,3,1]<br>
Output: 4<br>
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.<br>

Example 3:<br>

>Input: nums = [1,2,3]<br>
Output: 3<br>


Constraints:<br>

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `nums` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any constraints on time/space complexity?<br>
3. Happy path -
   ```python
    nums = [4,7,2,3,5]
    Output: 10 # Total amount you can rob = 7(house 2) + 3(house 4) = 10.
   ```
4. Edge case -
   ```python
    Input: nums = [3, 4]
    Output: 4
   ```
5. Edge case -
   ```python
    Input: nums = [3]
    Output: 3
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Dynamic Programming
   - Since we can't rob both the first and last houses, we split the problem into two cases
   - 1. Robbing from the first house to the second-to-last house
     2. Robbing from the second house to the last house
   - As House Robber, we run the dynamic programming solution on both cases and return the maximum of the two results
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We use dynamic programming to transit two types of states day by day. We conduct two calculations without the first day or the last day separately and compare them

1) Edge case: 
   ```python
   if len(nums) == 1:
       return nums[0]
2) Define `dp(houses)`:
   - Initialize `rob, skip = 0, 0`
   - Iterate through `houses` array, update two states: `rob, skip = skip + house, max(rob, skip)`
   - Rreturn `max(rob, skip)` since we can either rob or skip on the last day
3) Return `max(dp(nums[:-1]), dp(nums[1:]))` ( without the first day or the last day separately )
   
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of `nums`

- Time Complexity: O(N)<br>
  We pass through `nums` twice with `dp` function, so it takes O(N) time. <br>
- Space Complexity: O(1)<br>
  We use only two variables to transit the states.
