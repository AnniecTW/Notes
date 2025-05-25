## 12. Integer to Roman
🔗 Link: [Integer to Roman](https://leetcode.com/problems/integer-to-roman/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash<br>

<hr>
Seven different symbols represent Roman numerals with the following values:<br>

<table>
  <tr>
    <td>Symbol</td>
    <td>Value</td>
  </tr>
  <tr>
    <td>I</td>
    <td>1</td>
  </tr>
  <tr>
    <td>V</td>
    <td>5</td>
  </tr>
  <tr>
    <td>X</td>
    <td>10</td>
  </tr>
  <tr>
    <td>L</td>
    <td>50</td>
  </tr>
  <tr>
    <td>C</td>
    <td>100</td>
  </tr>
  <tr>
    <td>D</td>
    <td>500</td>
  </tr>
  <tr>
    <td>M</td>
    <td>1000</td>
  </tr>
</table>

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:<br>
- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.<br>

Example 1:<br>

>Input: num = 3749<br>
Output: "MMMDCCXLIX"<br>
Explanation:<br>
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)<br>
 700 = DCC as 500 (D) + 100 (C) + 100 (C)<br>
  40 = XL as 10 (X) less of 50 (L)<br>
   9 = IX as 1 (I) less of 10 (X)<br>
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places<br>


Example 2:<br>

>Input: num = 58<br>
Output: "LVIII"<br>
Explanation:<br>
50 = L<br>
 8 = VIII<br>


Example 3:<br>

>Input: num = 1994<br>
Output: "MCMXCIV"<br>
Explanation:<br>
1000 = M<br>
 900 = CM<br>
  90 = XC<br>
   4 = IV<br>
 

Constraints:<br>

- 1 <= num <= 3999
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `num` be zero or negative?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: 2025; Output: MMXXV;
4. Edge case - Input: 3999; Output: MMMCMXCIX;

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Hash map / Math
   - Roman numerals are composed of symbols representing specific integer values, arranged in descending order.
   - Since the conversion follows a greedy pattern — always subtracting the largest possible value — we can use a hash map and iterate through it in descending order to build the result string.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a hash map that maps integer values to their corresponding Roman numeral symbols. Traverse the map in descending order, repeatedly subtracting values from `num` and appending symbols to the result until `num` becomes 0.<br>

1) Build a hash map in descending order:<br>
   ```python
   iToR = {
   1000: "M", 900: "CM", 500: "D", 400: "CD",
   100: "C", 90: "XC", 50: "L", 40: "XL",
   10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
   }
3) Initialize the result string: `res = ""`
4) Iterate through each key `val` in `iToR`:
   - While `num >= val`:<br>
    a) Append the Roman symbol: `res += iToR[val]`<br>
    b) Subtract the value from `num`: `num -= val`
6) Return `res` when `num` reaches 0
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


- Time Complexity: O(N + M)<br>
  The number of iterations is bounded by the input range (1–3999), and the hash map contains only 13 entries.<br>
  Although the inner while loop may run multiple times (e.g., for `num = 8`, it runs 1 time for `5` and 3 times for `1`), this total number is bounded and does not scale with input size. So overall, it's constant time.<br>
  
- Space Complexity: O(1)<br>
  The hash map has a fixed size and the result string grows linearly with the number of Roman symbols (at most around 15 for `num = 3888`), which is also bounded. So, it's constant space.<br>
