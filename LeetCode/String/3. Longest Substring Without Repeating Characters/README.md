## 3. Longest Substring Without Repeating Characters
🔗  Link: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given a string `s`, find the length of the longest substring without duplicate characters.

 
Example 1:<br>

Input: s = "abcabcbb"<br>
Output: 3<br>
Explanation: The answer is "abc", with the length of 3.<br>

Example 2:<br>

Input: s = "bbbbb"<br>
Output: 1<br>
Explanation: The answer is "b", with the length of 1.<br>

Example 3:<br>

Input: s = "pwwkew"<br>
Output: 3<br>
Explanation: The answer is "wke", with the length of 3.<br>
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.<br>
 

Constraints:

- 0 <= `s.length` <= 5 * 10<sup>4</sup>
- `s` consists of English letters, digits, symbols and spaces.

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: s = "ab"; Output: "ab"
4. Edge case - Input: s = "aaa"; Output: "a"
5. Edge case - Input: s = ""; Output: ""
6. Edge case - Input: s = " "; Output: " "

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String, Sliding Window<br>
   This problem follows the general pattern of "finding the longest/shortest subarray/substring that meets a certain condition", which is a common Sliding Window problem.<br>
   - Use a sliding window approach to efficiently track substrings
   - Use a set for quick lookup of repeating characters
   - Two pointers adjust dynamically to maintain a valid substring

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a sliding window technique with a set to keep track of unique characters in the current window and update the longest non-repeating substring found.<br>

1) Iterate through each character in string `s`, adding it to the set `seen`.
   - If a duplicate character is found in `seen`, remove characters from the left side of the window until no duplicates remain
2) Update the `longest` variable to store the maximum length found
   - use `fromcenter(i, i)` to find the longest odd-length palindrome
   - use `fromcenter(i, i+1)` to find the longest even-length palindrome
   - compare both result and update the starting and ending indices of the longest palindrome found so far
3) Return `longest`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of characters in the string and M represents the number of unique characters in the substring


- Time Complexity: O(N)
- Space Complexity: O(N)
