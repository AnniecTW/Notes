## 33. Search in Rotated Sorted Array
🔗 Link: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

============================================================================================<br>
There is an integer array `nums` sorted in ascending order (with distinct values).<br>

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.<br>

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in nums.<br>

You must write an algorithm with O(log n) runtime complexity.<br>



 

Example 1:<br>

Input: nums = [4,5,6,7,0,1,2], target = 0<br>
Output: 4<br>

Example 2:<br>

Input: nums = [4,5,6,7,0,1,2], target = 3<br>
Output: -1<br>

Example 3:<br>

Input: nums = [1], target = 0<br>
Output: -1<br>

Constraints:<br>

- 1 <= nums.length <= 5000
- -10<sup>4</sup> < nums[i], target < 10<sup>4</sup>
- All the values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `nums` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Are there duplicate intergers in `nums`?<br>
4. Happy path - Input: `nums` = [1,2,3,4,0], target = 0; Output: 3
5. Edge case - Input: `nums` = [-1], target = 2; Output: -1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Array / Binary Search
   - Binary Search with boundaries adjustment
   - Key idea: One part of the array (left or right of `mid`) is always sorted even after rotation
   - Decision making based on where the `target` lies in relation to that sorted portion

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We use a modified binary search to find the target in O(log n) time. At each iteration, one side of the mid element must be sorted.<br>
              We can check whether the target lies in the sorted half and move our boundaries accordingly.

1) Initialize `left = 0` and `right = len(nums) - 1` 
2) While `left <= right`, repeat the following steps<br>
   a) calculate the middle index `mid` using `mid = (left + right) // 2`<br>
   b) If `nums[mid]` is equal to `target`, return `mid`<br>
   c) If `nums[left] <= nums[mid]`, indicating the left half is sorted, check whether target is in this part<br>
     i) If so, set `right = mid - 1`<br>
     ii) Otherwise, set `left = mid + 1`<br>
   d) If the right half is sorted, check whether the target is in it<br>
     i) If so, set `left = mid + 1`<br>
     ii) Otherwise, set `right = mid - 1`<br>
3) Return `-1` if the target is not found
    
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
  
