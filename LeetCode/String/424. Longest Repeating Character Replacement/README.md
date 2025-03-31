## 424. Longest Repeating Character Replacement
🔗 Link: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.<br>

 

Example 1:<br>

Input: s = "ABAB", k = 2<br>
Output: 4<br>
Explanation: Replace the two 'A's with two 'B's or vice versa.<br>

Example 2:<br>

Input: s = "AABABBA", k = 1<br>
Output: 4<br>
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".<br>
The substring "BBBB" has the longest repeating letters, which is 4.<br>
There may exists other ways to achieve this answer too.<br>
 

Constraints:<br>

- 1 <= s.length <= 10<sup>5</sup>
- `s` consists of only uppercase English letters.
- 0 <= k <= s.length
===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `s` be empty?<br>
   No, `s` contains at least one characters.<br>
2. Does `s` contain any characters other than uppercase English letters?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `s` = "ABBCC", k = 2; Output: 4
4. Edge case - Input: `s1` = "A", k = 1; Output: 1
5. Edge case - Input: `s1` = "A", k = 0; Output: 1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String / Sliding window + Hash map
   - Sliding Window: Efficiently traverses a string by maintaining a dynamcic fixed-size window, adjusting its boundaries rather than reconstructing it at each step
   - Hash Map (or Counter): Tracks frequencies within the current window to determine the remaining quota for replacements

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a dictionary to maintain characters frequencies within the current window while traversing `s`. Ensure the window size is valid by keeping the difference between the length and the frequency of the most frequent character within `k`.
Keep tracking of the longest valid substring encountered.<br>

1) Initialize `res = 1` (at least one character can always form a valid substring)
2) Initialize left pointer `i = 0`
3) Traverse `s` with right pointer `j`, maintaining a dictionary `counter` to store character frequencies in the current window
   - Compute `maxFreq`, the frequency of the most frequent characters in the window
   - If the difference between window length `j - i + 1` and `maxFreq` is larger than `k`, shrink the window by incrementing `i` and updating `counter`
5) Update `res` if the current valid window is longer than the previous maximum
7) Return `res`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of `s`

- Time Complexity: O(N)<br>
  The string is processes at most twice, with pointer `j` expanding and `i` shrinking the window.
- Space Complexity: O(1)<br>
  At most 26 unique characters in the dictionary, meaning that the space used for `counter` is constant and independent of N.
