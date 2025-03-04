## 242. Valid Anagram
🔗 Link: [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: String<br>

=======================================================================================<br>
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.<br>

 
Example 1:<br>
Input: s = "anagram", t = "nagaram"<br>
Output: true<br>

Example 2:<br>
Input: s = "rat", t = "car"<br>
Output: false<br>

 
Constraints:
- 1 <= s.length, t.length <= 5 * 10<sup>4</sup>
- `s` and `t` consist of lowercase English letters.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the strings be empty?
2. Any requirements on time/space complexity?
3. Happy path - Input: s = "eat", t = "tea" Output: true
4. Edge case 1 - Input: s = "aaa", t = "aa" Output: false
5. Edge case 2 - Input: s = "aaa", t = "aaa" Output: true
6. Edge case 3 - Input: s = "eat", t = "tea" Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String<br>
<br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use hash maps to calculate and store the frequencies of chars in the two strings, and then compare them.
1) Import `Counter`.<br>
2) Use `Counter(string)` to construct a hash map that calculates and stores the frequency of each unique character in `string`. <br>
3) If `Counter(s)` equals to `Counter(t)`, then return `True`; otherwise, return `False`.<br>
  
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py 

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N, M represent the number of items in the `s` and `t` strings.

- Time Complexity: O(N + M)
- Space Complexity: O(1)
  
---------------------------------------------------------------------------------------------------------------------------------------------<br>
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py (Same as the previous)

### Evaluate
Assume N, M represent the number of items in the `s` and `t` strings.

- Time Complexity: O(N + M)
- Space Complexity: O(N + M)
