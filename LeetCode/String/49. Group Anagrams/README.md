## 49. Group Anagrams
🔗  Link: [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

============================================================================================<br>
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.<br>

 

Example 1:<br>

Input: strs = ["eat","tea","tan","ate","nat","bat"]<br>

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]<br>

Explanation:<br>
There is no string in strs that can be rearranged to form "bat".<br>
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.<br>
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.<br>

Example 2:<br>

Input: strs = [""]<br>

Output: [[""]]<br>

Example 3:<br>

Input: strs = ["a"]<br>

Output: [["a"]]<br>
 

Constraints:<br>

- 1 <= strs.length <= 10<sup>4</sup>
- 0 <= strs[i].length <= 100
- `strs[i]` consists of lowercase English letters.

===========================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the string be empty?<br>
   No, at least one element in `strs`.<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: strs = ["opt","top","pot","bac","cab"]; Output: [["opt","top","pot"],["bac","cab"]]
4. Edge case - Input: strs = [[""]]; Output: [[""]]
5. Edge case - Input: strs = [["a"]]; Output: [["a"]]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String / hashing <br>
   Using a hash map to group words with the same sorted characters is a common approach.<br>
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a hash map to group words with the same sorted characters.<br>

1) Initialize a `defaultdict` (hash map) with `list` as the default value type
2) For each string in `strs`, sort the characters and use the sorted string as a key. Append the original string to the corresponding list<br>
3) Return all the values of the `defaultdict`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of characters in the string in the `strs` list and M represents the length of the list


- Time Complexity: O(M * N * log N)<br>
  For each string in `strs` (M strings), sorting each string of length N takes O(N * log N). Therefore, the total complexity is O(M * N * log N).
- Space Complexity: O(MN)<br>
  The `defaultdict` stores all the strings, and in the worst case where all strings are unique anagrams, it will store M keys, each associated with a list of up to N characters.
