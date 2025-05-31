## 383. Ransom Note
🔗 Link: [Ransom Note](https://leetcode.com/problems/ransom-note/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Hash<br>

<hr>
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.<br>

 

Example 1:<br>

Input: ransomNote = "a", magazine = "b"<br>
Output: false<br>


Example 2:<br>

Input: ransomNote = "aa", magazine = "ab"<br>
Output: false<br>


Example 3:<br>

Input: ransomNote = "aa", magazine = "aab"<br>
Output: true<br>
 

Constraints:<br>

- 1 <= ransomNote.length, magazine.length <= 10<sup>5</sup>
- ransomNote and magazine consist of lowercase English letters.
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `ransomNote` or `magazine` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `ransomNote` = "cab", `magazine` = "abc"; Output: true
4. Edge case - Input: `ransomNote` = "c", `magazine` = "a"; Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. String / Counter
   - Use Python's built-in function `Counter` to calculate character frequencies efficiently, and then conduct subsequent comparison.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use Python's `collections.Counter` to count the character frequencies in `ransomNote` and `magazine`, and then compare them.<br>

1) `from collections import Counter`
2) `ransom_count = Counter(ransomNote)`
3) `magazine_count = Counter(magazine)`
4) Iterate each character (key) and its frequency (value) in `ransom_count.items()`
   - if the frequency of the corresponding character in `magazine_count` is less, return `False`
5) If all the charaters pass, return `True`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of `ransomNote`, and M is the length of `magazine`

- Time Complexity: O(N + M)<br>
  `Counter` scans through `ransomNote` and `magazine` once, resulting in linear time.<br>
- Space Complexity: O(N + M)<br>
  In the worst case, all characters are unique, so two separate counters may store up to N + M elements.<br>
  If there is only lowercase English letters, this can be considered O(1).<br>
