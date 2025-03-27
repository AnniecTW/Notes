## 97. Interleaving String
🔗  Link: [Interleaving String](https://leetcode.com/problems/interleaving-string/description/
)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given strings `s1`, `s2`, and `s3`, find whether s3 is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

 

Example 1:<br>
<img width="643" alt="interleaving string" src="https://github.com/user-attachments/assets/e020b937-a622-4a80-9617-b5155eb6b5c1" />

Input: `s1` = "aabcc", `s2` = "dbbca", `s3` = "aadbbcbcac"<br>
Output: true<br>
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:<br>

Input: `s1` = "aabcc", `s2` = "dbbca", `s3` = "aadbbbaccc"<br>
Output: false<br>
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
 
Example 3:<br>
Input: `s1` = "", `s2` = "", `s3` = ""<br>
Output: true<br>

Constraints:<br>

- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   Yes, `s1`, `s2` and `s3` can be all empty.<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `s1` = "xxyyzz", `s2` = "abc", `s3` = "axxcyybzz"; Output: false
4. Happy path - Input: `s1` = "xxyyzz", `s2` = "abc", `s3` = "axxbyyczz"; Output: true
5. Edge case - Input: `s1` = "a", `s2` = "b", `s3` = "ba"; Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String<br>
2. Dynamic programming<br>
   A 2D DP approach helps store results for substrings efficiently and avoid redundant computations. The state transition depends on previous states (`dp[i-1][j]` or `dp[i][j-1]`)
   - The space complexity can be optimized from O(m * n) to O(n) by using a 1D DP.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a 2D DP table where `dp[i][j]` represents whether `s3[:i+j]` can be formed by interleaving `s1[:i]` and `s2[:j]`.<br>

1) If `len(s1) + len(s2) != len(s3)`, return `False` since interleaving is impossible
2) Create a 2D boolean array `dp` of size `(len(s1) + 1) × (len(s2) + 1)`, initialized to `False`.
   Set `dp[0][0] = True`, representing an empty string.   
4) Iterate through the first column (`s3` consists only of `s1`)
   - update `dp[i][0] = True` if `dp[i-1][0] == True` and `s1[i-1] == s3[i-1]`
5) Iterate through the first row (`s3` consists only of `s2`)
   - update `dp[0][j] = True` if `dp[0][j-1] == True` and `s2[j-1] == s3[j-1]`
6) Use nested loop to update the rest of the dp table (interleaving case), starting from `(1, 1)`
   - update dp[i][j] based on the transition `dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])`
   - This ensures that `dp[i][j]` is `True` if:
     - The character from `s1` matches `s3`, and the previous state `dp[i-1][j]` was True.
     - Or the character from `s2` matches `s3`, and the previous state `dp[i][j-1]` was True.
8) return the value stored in `dp[len(s1)][len(s2)]`, which indicates whether `s3` can be formed by interleaving `s1` and `s2`
    
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

- Time Complexity: O(N * M)
  We iterate through the 2D DP table once, filling each cell based on previously computed values.
- Space Complexity: O(N * M)
  We store results for all substring combinations in 2D DP table.
