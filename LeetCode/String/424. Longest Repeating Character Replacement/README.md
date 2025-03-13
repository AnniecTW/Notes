## 5. Longest Palindromic Substring
🔗  Link: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character.<br>
You can perform this operation at most `k` times.<br>

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
- 0 <= k <= s.length<br>

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   No, at least one character in the string.<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: s = "APPLE", k = 2; Output: 4
4. Edge case - Input: s = "AB", k = 2; Output: 2
5. Edge case - Input: s = "A", k = 1 Output: 1
6. Edge case - Input: s = "A", k = 0; Output: 1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String / sliding window <br>
   Sliding Window technique is commonly used for problems that involve finding the longest/shortest/minimum/maximum substring with specific conditions.<br>
   The sliding window approach helps dynamically expand and shrink the window to find the optimal solution while keeping track of the most frequent character in the current window.<br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a sliding window with two pointers (`i` and `j`) to keep track of the current substring. 
              Keep expanding the window by moving `j` and only shrinking it by moving `i` when the window becomes invalid (i.e., we need more than k replacements to make all characters the same). 
              Update the max length whenever a valid window is found.<br>
              
1) Initialize two pointers `i` and `j` to 0 and a `longest` variable to keep track of the longest valid substring
2) While traversing the string with `j`, increase the count of the character visited in counter
3) Calculate the number of the most frequent character in the current substring `max_freq`
4) If the difference between the length of the current substring (`j - i + 1`) and `max_freq` is greater than `k`, move the pointer `i` forward and decrement the counter of the character pointed to by `i`
5) Keep updating `longest`, current valid substring length `j - i + 1` and `max_freq`
6) Return `max_freq`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of characters in the string.


- Time Complexity: O(N)
- Space Complexity: O(1)
