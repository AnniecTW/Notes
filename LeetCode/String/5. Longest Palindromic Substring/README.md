## 5. Longest Palindromic Substring
🔗  Link: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given a string `s`, return the longest palindromic substring in `s`.<br>

 

Example 1:<br>

Input: s = "babad"<br>
Output: "bab"<br>
Explanation: "aba" is also a valid answer.<br>

Example 2:<br>

Input: s = "cbbd"<br>
Output: "bb"<br>
 

Constraints:<br>

- 1 <= s.length <= 1000<br>
- `s` consist of only digits and English letters.

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   No, at least one character.<br>
2. Any requirements on time/space complexity?<br>
3. Is single char a palindromic substring?<br>
   Yes, it can be considered a palindromic substring.<br>
4. Happy path - Input: s = "banana"; Output: "anana"
5. Edge case - Input: s = "aBc"; Output: "a", "B", or "c"
6. Edge case - Input: s = "a"; Output: "a"

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String (Palindrome-related) <br>
   A common strategy for solving it is the Expand Around Center approach, where we check for the longest palindromic substring by expanding outward from both odd-length and even-length centers.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Traverse each char in the string `s` and find the longest palindromic substring by expanding form both odd-length and even-length centers separately.<br>

1) If `s` is empty or has only one char, return `s` directly.
2) Define a function `fromcenter(left, right)`, which expands outward from the given indices while the characters are the same, keeping track of the longest palindromic substring found.
3) Iterate through each char in `s`, treating it as a center:
   - use `fromcenter(i, i)` to find the longest odd-length palindrome
   - use `fromcenter(i, i+1)` to find the longest even-length palindrome
   - compare both result and update the starting and ending indices of the longest palindrome found so far
4) Return the longest palindromic substring
    
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


- Time Complexity: O(N<sup>2</sup>)
- Space Complexity: O(1)
