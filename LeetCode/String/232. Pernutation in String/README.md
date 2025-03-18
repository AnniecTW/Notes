## 232. Pernutation in String
🔗  Link: [Pernutation in String](https://leetcode.com/problems/permutation-in-string/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.<br>

 

Example 1:<br>

Input: s1 = "ab", s2 = "eidbaooo"<br>
Output: true<br>
Explanation: s2 contains one permutation of s1 ("ba").<br>

Example 2:<br>

Input: s1 = "ab", s2 = "eidboaoo"<br>
Output: false<br>
 

Constraints:<br>

- 1 <= s1.length, s2.length <= 10<sup>4</sup>
- `s1` and `s2` consist of lowercase English letters.

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   No, `s1` and `s2` consist of at least one character.<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `s1` = "eee", `s2` = "beetle"; Output: false
4. Happy path - Input: `s1` = "ebe", `s2` = "beetle"; Output: true
5. Edge case - Input: `s1` = "ee", `s2` = "e"; Output: false

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String <br>

   
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
