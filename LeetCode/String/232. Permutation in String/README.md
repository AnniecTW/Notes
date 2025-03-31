## 232. Permutation in String
🔗 Link: [Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)<br>
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
1. String / Sliding window + Hash map
   - Sliding Window: Efficiently traverses a string by maintaining a fixed-size window, making updates rather than rebuilding from scratch each time
   - Hash Map (or Counter): Keeps track of character frequencies to compare two substrings' compositions
   - Optimization: Removing keys with 0 frequency helps reduce unnecessary comparisons

   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a dictionary to record the number of each character in `s1`, and traverse each substring of length `len(s1)`in `s2` with a sliding window approach to check if it is a permutation of `s1`.<br>

1) If the length of `s2` is less than `s1`, `s2` can never contain a permutation of `s1`, so return false
2) Use a dictionary `count_s1` to record the frequency of each character in `s1`
3) Initialize a dictionary `count_s2` to record the frequency of each character in the first substring of length `len(s1)` in `s2` 
4) Compare `count_s1` and `count_s2`: If they are equal, return true; otherwise, continue the next step
5) Traverse each substring of length `len(s1)` in `s2` by moving the window one character at a time (using ptr `i` and `j`)
   - For each step, remove the leftmost charecter (pointed by `i`) from `count_s2` and add the new rightmost character (pointed by `j`)
   - If the frequency of any character in `count_s2` becomes `0`, remove it from the dictionary 
   - Compare `count_s1` and `count_s2` after each move: If they are equal, return true; otherwise, continue the sliding window
6) Return fasle if no valid substring is found
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of `s1` and M represents the length of `s2`

- Time Complexity: O(N + M)<br>
  The initialization spends O(N) and the sliding process spends O(M - N), summing up to O(M).
- Space Complexity: O(1)<br>
  At most 26 unique characters in the dictionary, meaning that the space used is constant and independent of N and M.
  
