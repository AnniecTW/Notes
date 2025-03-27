## 76. Minimum Window Substring
🔗  Link: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

 

Example 1:<br>

Input: s = "ADOBECODEBANC", t = "ABC"<br>
Output: "BANC"<br>
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t."<br>

Example 2:<br>

Input: s = "a", t = "a"<br>
Output: "a"<br>
Explanation: The entire string s is the minimum window.<br>

Example 3:<br>
 
Input: s = "a", t = "aa"<br>
Output: ""<br>
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.<br>


Constraints:<br>

- m == s.length
- n == t.length
- 1 <= m, n <= 10<sup>5</sup>
- `s` and `t` consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   No, `s` and `t` contain at least one character.<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `s` = "LeetCodE", `t` = "eE"; Output: "etCodE"
4. Edge case - Input: `s` = "e", `t` = "eE"; Output: ""
5. Edge case - Input: `s` = "CC", `t` = "C"; Output: "C"

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String<br>
2. Sliding window<br>
   We use two pointers (left and right) to expand and contract a window efficiently.<br>
3. Hash map (Counter)<br>
   We use a hash map to track character frequencies. 
   This helps count and update required characters in `t` efficiently. <br>
   
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a counter to store the frequencies of characters in `t`. 
Use the sliding window technique to find the smallest substring in `s` that contains all characters in `t`.<br>

1) Create a counter `need` to store the frequency of characters in `t`
2) Use `toMatch` to track the number of unique characters in `t` that still need to be matched
3) Initialize `minLength = ∞` and `res = ""` to track the smallest valid substring
4) Set `left = 0` as the starting point of the sliding window
5) Expand the window with `right` pointer and store current character in `char`.
   - When `char` is in `t`, decrement `need[char]`
   - If `need[char] == 0`, it means we have matched all occurrences of `char`, so decrement `toMatch`<br>
   a) If `toMatch == 0`, it means all characters in `t` are covered in the current window
      - Update `minLength` and `res` if the length of current window `right - left + 1` is less than `minLength`
      - Try to minimize the window by moving left forward, increment `need[char]` and increment `toMatch` if `need[char] == 1` (mismatch caused)
      - Move `left` forward
8) If `minLength` was updated, return `res`; otherwise, return `''` (no valid substring found)
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of `s` and M represents the length of `t`

- Time Complexity: O(N + M)<br>
  Each character in `s` is processed at most twice. The counter `need` requires O(M) time.<br>
- Space Complexity: O(1): best case; O(N): worst case<br>
  If characters in `s` are concentrated, space complexity mainly depends on `need`, which only stores at most 52 characters.<br>
  If characters are so far in `s` that `res = s`, space complexity becomes O(N)<br>
