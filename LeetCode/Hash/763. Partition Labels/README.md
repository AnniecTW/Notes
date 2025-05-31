## 763. Partition Labels
🔗 Link: [Partition Labels](https://leetcode.com/problems/partition-labels/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash<br>

<hr>

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.<br>
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.<br>
Return a list of integers representing the size of these parts.<br>
 

Example 1:<br>

>Input: s = "ababcbacadefegdehijhklij"<br>
Output: [9,7,8]<br>
Explanation:<br>
The partition is "ababcbaca", "defegde", "hijhklij".<br>
This is a partition so that each letter appears in at most one part.<br>
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.<br>


Example 2:<br>

>Input: s = "eccbbbbdec"<br>
Output: [10]<br>

 

Constraints:<br>

- 1 <= s.length <= 500
- `s` consists of lowercase English letters.
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `s` be empty?<br>
2. Is there only one valid way to partition, or are multiple answers acceptable? If so, is returning any one valid parition sufficient?
3. Any requirements on time/space complexity?<br>
4. Happy path - Input: `s` = "dlsjgsligjhigsjg"; Output: [1, 16]
5. Edge case - Input: `s` = "cc"; Output: [2]
6. Edge case - Input: `s` = "c"; Output: [1]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String / Hash
   - Use a hash map to record the last index of each unique character in `s` and greedily choose the smallest partition that includes current start letter.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a hash map to record the last index of each unique character in `s`. Iterate through `s` and update the partition result when encounter current largest index. <br>

1) Initialize `last = {}` to record the last occurrence index of each character
2) Iterate through `s` and populate the `last` dictionary accordingly
3) Set `start = 0` and `end = 0` to definde the current partition range
4) As iterate through `s` 
   - For each character `c` at index `i`, update `end = max(end, last[c])` 
   - If `i == end`, a complete partition is found:
       a) Append `end - start + 1` to `res`<br>
       b) Update `start = i + 1` for the next partition
5) After iteration done, return `res`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of `s`

- Time Complexity: O(N)<br>
  We scan through `s` twice, once to build the hash map, once to build the partitions.<br>
- Space Complexity: O(N)<br>
  The hash map stores at most 26 characters (only lowercase letters), so it's constant space.<br>
