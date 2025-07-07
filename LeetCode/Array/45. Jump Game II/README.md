## 45. Jump Game II
🔗 Link: [Jump Game II](https://leetcode.com/problems/jump-game-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array / Greedy<br>

<hr>

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

`0 <= j <= nums[i]` and `i + j < n`<br>

Return *the minimum number of jumps to reach* `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

Example 1:<br>

>Input: nums = [2,3,1,1,4]<br>
Output: 2<br>
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.<br>


Example 2:<br>

>Input: nums = [2,3,0,1,4]<br>
Output: 2<br>


Constraints:<br>

- 1 <= nums.length <= 10<sup>4</sup>
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].


<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Is the input always valid? Is `nums` guaranteed to have at least one element?<br>
2. Any constraints on time/space complexity?<br>
3. Happy path - nums = [1,2,2,3,4]; Output: 3; Explanation: Jump 1 from index 0 to 1, then 2 steps to index 3, then 1 step to the last index.<br>
4. Edge case - nums = [4]; Output: 0; Explanation: Already at the last index, no jump needed.

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Greedy
   - We keep track of the farthest position that can be reached at each step
   - We only increment the jump count and update current reachable end when we reach the current boundary (Greedy strategy)

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Iterate through the array while tracking the farthest index that can be reached. When we reach the end of the current jump range, we increment the jump count and update the boundary to the farthest reachable index.<br>

1) Initialize last index: `last = len(nums) - 1`
2) Initialize jump count, current reachable end, and current farthest reachable position to zero.
3) Iterate `nums` from index `0` to `last - 1`:
   - Keep track of current maximum farthest position: `farthest = max(farthest, i + nums[i])`
   - If index is equal to current reachable end:
     - a) Increment jump count
     - b) Update current reachable end to current farthest reachable position
     - c) If current reachable end is larger than or equal to `last`, break the loop early
5) Return jump count
   
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of nums

- Time Complexity: O(N)<br>
  We only make a single pass through the array and perform constant-time work at each step. <br>
- Space Complexity: O(1)<br>
  We use a few variables to track the current jump range and farthest reachable index.
