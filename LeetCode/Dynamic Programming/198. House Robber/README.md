## 198. House Robber
🔗 Link: [House Robber](https://leetcode.com/problems/house-robber/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Dynamic Programming<br>

<hr>

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the *maximum amount of money you can rob tonight without alerting the police*.

Example 1:<br>

>Input: nums = [1,2,3,1]<br>
Output: 4<br>
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).<br>
Total amount you can rob = 1 + 3 = 4.<br>



Example 2:<br>

>Input: nums = [2,7,9,3,1]<br>
Output: 12<br>
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).<br>
Total amount you can rob = 2 + 9 + 1 = 12.<br>


Constraints:<br>

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

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
    Output: 11 # Total amount you can rob = 4(house 1) + 2(house 3) + 5(house 5) = 11.
   ```
4. Edge case -
   ```python
    Input: nums = [3]
    Output: 3
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Dynamic Programming
   - we use dynamic programming to transit two types of states to the next day, which includes:
   - rob = prev_skip + nums[i]
   - skip = max(prev_rob, prev_skip)
   - This is a space-optimized version of the DP solution using state compression

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We use dynamic programming to transit two types of states day by day, and return the maximum final outcomes stored in the states.

1) Initialize `rob = nums[0]`, representing robbing on the first day
2) Initialize `skip = 0`, representing skipping on the first day
3) Iterate `nums[i]` from `i = 1` to `n`:
   - Store previous `rob` state
   - Update `rob = skip + nums[i]` since we can rob today only if skipped yesterday
   - Update `skip = max(skip, prev_rob)`. Because we can skip today no matter what, we update the maximum value stored so far.
5) Rreturn `max(skip, rob)` since we can either rob or skip on the last day
   
    
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
  We iterate through `nums` once, so it takes O(N) time. <br>
- Space Complexity: O(1)<br>
  We use only two variables to transit the states.
