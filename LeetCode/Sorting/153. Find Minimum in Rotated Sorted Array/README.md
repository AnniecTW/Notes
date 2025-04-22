## 153. Find Minimum in Rotated Sorted Array
🔗 Link: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

============================================================================================<br>
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.
Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.<br>

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.<br>

You must write an algorithm that runs in O(log n) time.<br>



 

Example 1:<br>

Input: nums = [3,4,5,1,2]<br>
Output: 1<br>
Explanation: The original array was [1,2,3,4,5] rotated 3 times.<br>


Example 2:<br>

Input: nums = [4,5,6,7,0,1,2]<br>
Output: 0<br>
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.<br>


Example 3:<br>

Input: nums = [11,13,15,17]<br>
Output: 11<br>
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.<br>


Constraints:<br>

- 1 <= nums.length <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between 1 and n times.
===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `nums` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Are there duplicate intergers in `nums`?<br>
4. Happy path - Input: `nums` = [1,2,3,4,0]; Output: 0
5. Edge case - Input: `nums` = [-1]; Output: -1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Array / Binary Search
   - Use binary search to locate the minimum element in a rotated sorted array
   - Key idea: One part of the array (left or right of `mid`) must be sorted
   - Decision making based on comparison between `nums[mid]` and `nums[right]`

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We use a modified binary search to find the minimum in O(log n) time. At each iteration, one side of the mid element must contain the minimum.<br>
              We can check which side the target lies in and move our boundaries accordingly.

1) Initialize `left = 0` and `right = len(nums) - 1` 
2) While `left < right`, repeat the following steps<br>
   - calculate the middle index `mid` using `mid = (left + right) // 2`<br>
   - If `nums[mid]` is equal to `target`, return `mid`<br>
   - If `nums[mid] > nums[right]`, the minimum is in the right half (excluding `mid`): set `left = mid + 1`<br>
   - Else, the minimum is in the left half (including `mid`): set `right = mid`<br>
3) When the loop ends, `left == right` and points to the minimun. Return `nums[left]`
    
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
  
