## 215. Kth Largest Element in an Array
🔗 Link: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Sorting<br>

============================================================================================<br>
Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.<br>

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.<br>

Can you solve it without sorting?<br>

 

Example 1:<br>

Input: nums = [3,2,1,5,6,4], k = 2<br>
Output: 5<br>

Example 2:<br>

Input:nums = [3,2,3,1,2,4,5,5,6], k = 4<br>
Output: 4<br>
 

Constraints:<br>

- 1 <= k <= nums.length <= 10<sup>5</sup>
- -10<sup>4</sup> < nums[i] < 10<sup>4</sup>
===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `nums` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Is it possible that the kth largest number doesn't exist? Do I need to handle that case?<br>
4. Happy path - Input: `nums` = [12,0,3,5,9], k = 2; Output: 2
5. Edge case - Input: `nums` = [-1], target = 1; Output: 0

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Array / Heap (Priority Queue)
2. Top-K Elements
   - This is a classic "Top K pattern where we need to find the k-th largest or k largest elements.
   - A common strategy is to maintain a min-heap of size K to efficiently track the K largest values as we iterate through the array.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a min-heap of size k to keep track of the k largest elements seen so far.<br>

1) Initialize an empty heap `heap = []`
2) Iterate through `nums`, and for each number
   a) Push it into the heap
   b) If the heap size exceeds k, pop the smallest element (ensure the heap keeps only the k largest elements)
6) Return `heap[0]` (the smallest among the k largest elements → i.e. the kth largest overall)
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of nums, and K is the size of the heap

- Time Complexity: O(Nlog K)<br>
  We perform `heappush()` and possibly `heappop()` for each of the N elements, and each operation costs O(log K) time.<br>
- Space Complexity: O(K)
  The heap size is maintained at most K elements<br>

- Pros:<br>
  Efficient even when N is large and K is small.<br>
  Python’s `heapq` is easy to use and handles edge cases well.<br>
- Cons:<br>
  If K is close to N, Quickselect is more efficient (which has average O(N) time and O(1) space).<br>
  Doesn’t provide the fully sorted order, only the Kth largest.<br>
