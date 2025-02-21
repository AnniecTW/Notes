## 435. Non-overlapping Intervals
🔗  Link: [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array<br>

=======================================================================================<br>
Given an array of `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]<br>
Output: 1<br>
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.<br>

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]<br>
Output: 2<br>
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.<br>

Example 3:

Input: intervals = [[1,2],[2,3]]<br>
Output: 0<br>
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.<br>

 

Constraints:

- 1 <= intervals.length <= 10<sup>5</sup>
- intervals[i].length == 2
- -5 * 10<sup>4</sup> <= starti < endi <= 5 * 10<sup>4</sup>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the nums array be empty?
   No, at least one item exists.
2. Any requirements on time/space complexity?
3. Is the given array sorted?
4. Happy path - Input: intervals = [[1,4],[4,5],[7,8],[6,7]]; Output: 0
5. Happy path - Input: intervals = [[1,2],[1,7],[7,8],[1,5]]; Output: 2
6. Edge case - Input: intervals = [[1,1]]; Output: 0

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Sort<br>
Sorting in advance can prevent unnecessary confusion. <br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Sort in advance, then decide if two intervals overlap according to the latter's `starti`.

1) Sort according to the first element in every interval
2) Initialize `count` to 0
3) Track current interval that is going to be compared while traversing the `intervals` list by storing it in a variable `curr`
4) Traverse the `intervals`
    - If the first element of each interval is smaller than or equal to current interval's `endi`, meaning the two intervals overlap, `count` += 1
    - `curr` is set to the interval with the smaller `end_i` to minimize the number of removals
    - Else, `curr` is set to current interval
5) return `count`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the array.


- Time Complexity: Sorting O(NlogN) + Traversal O(N) => O(NlogN)
- Space Complexity: O(1)
