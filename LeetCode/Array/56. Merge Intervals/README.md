## 56. Merge Intervals
🔗  Link: [Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array<br>

=======================================================================================<br>
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]<br>
Output: [[1,6],[8,10],[15,18]]<br>
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]<br>
Output: [[1,5]]<br>
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

- 1 <= intervals.length <= 10<sup>4</sup>
- intervals[i].length == 2
- 0 <= starti <= endi <= 10<sup>4</sup>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the `intervals` array be empty?
2. Any requirements on time/space complexity?
3. Is the given array sorted?
4. Happy path - Input: intervals = [[1,4],[4,5],[6,7]]; Output: [[1,5],[6,7]]
5. Edge case - Input: intervals = [[1,2]]; Output: [[1,2]]
6. Edge case - Input: intervals = [[1,1],[1,1]]; Output: [[1,1]]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Sort<br>
Sorting in advance can prevent unnecessary confusion. <br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Sort in advance, then decide if two intervals overlap according to the latter's `starti`.

1) Sort according to the first element in every interval
2) Track current interval that is going to be compared while traversing the `intervals` list by storing it in a variable `curr`
3) Traverse the `intervals`
    - If the first element of each interval is smaller than or equal to current interval's `endi`, meaning the two intervals overlap, append a new interval to the answer
    - The `starti` of the new interval is that of the current interval, and its `endi` is the larger one of the two `endi`s
    - Else, append current interval to the answer
    
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
- Space Complexity: O(N)
