## 33. Search in Rotated Sorted Array
🔗 Link: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

============================================================================================<br>
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.<br>

You must write an algorithm with `O(log n)` runtime complexity.<br>

 

Example 1:<br>

Input: nums = [-1,0,3,5,9,12], target = 9<br>
Output: 4<br>
Explanation: 9 exists in nums and its index is 4<br>

Example 2:<br>

Input: s1 =  nums = [-1,0,3,5,9,12], target = 2<br>
Output: -1<br>
Explanation: 2 does not exist in nums so return -1<br>
 

Constraints:<br>

- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> < nums[i], target < 10<sup>4</sup>
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.
===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `nums` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Are there duplicate intergers in `nums`?<br>
4. Happy path - Input: `nums` = [-1,0,3,5,9,12], target = 0; Output: 2
5. Edge case - Input: `nums` = [-1,0,3,5,9,12], target = 2; Output: -1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Binary Search
   - The binary search strategy efficiently finds the target value in O(log N) time by repeatedly halving the search range.

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: To achieve O(log n) runtime, use binary search to deal with this problem.<br>

1) Initialize `left = 0` and `right = len(nums) - 1` 
2) While `left <= right`, repeat the following steps
   - calculate the middle index `mid` using `mid = (left + right) // 2`
   - If `nums[mid] == target`, return `mid`
   - If `target < nums[mid]`, then update `right = mid - 1` (search in the left half)
   - If `target > nums[mid]`, then update `left = mid + 1` (search in the right half)
6) Return -1 if the target is not found
    
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
  
