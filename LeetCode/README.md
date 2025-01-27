6. Zigzag Conversion

🔗 Link: Zigzag Conversion
💡 Difficulty: Medium
🛠️ Topics: String

=======================================================================================

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P A H N
A P L S I I G
Y I R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P I N
A L S I G
Y A H R
P I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
=======================================================================================

UMPIRE Method:

Understand

Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
Verify that you and the interviewer are aligned on the expected inputs and outputs.
Can the string s be empty?
Yes, the string s can be empty. The function should be able to handle this case gracefully, typically by returning an empty string as the output since there would be no characters to process.
In cases where numRows is greater than the length of the string, should the extra rows just be empty?
Yes
Are there any time or space complexity constraints I should be aware of?
an optimal solution would have O(n) in both time and space complexity
Match

See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
String
The core task requires transforming the input string into a new format based on a specific pattern, which is a common string manipulation operation.
Plan

Sketch visualizations and write pseudocode
Walk through a high level implementation with an existing diagram
General Idea: Simulate the writing of a given string s in a zigzag pattern across a specified number of rows (numRows), and then concatenate the text in each row to form a new string that represents the zigzag pattern read line by line.

Base Case Check: If numRows is 1 or the length of the string s is less than or equal to numRows, there is no actual zigzag pattern to create, so the original string is returned as is.

Row Initialization: A list called rows is created with numRows empty strings. Each string in the list corresponds to a row in the zigzag pattern.

Zigzag Construction: The code iterates over each character in the input string s. The current row index idx is incremented or decremented based on the current direction of the zigzag pattern. The step variable controls the direction; it is set to 1 to move "down" the rows and -1 to move "up".

If the current row idx is 0, it means we're at the top row, so the direction is set to move down.
If the current row idx is numRows - 1, it means we're at the bottom row, so the direction is set to move up.
Character Appending: As the characters are read from the input string, they are appended to the corresponding string in rows based on the current row index idx.

Final String Formation: After the zigzag pattern has been created in the rows list, the strings in each row are concatenated together in order to form the final string. The join() function is used to concatenate all strings in rows into a single string.

Implement

Implement the solution (make sure to know what level of detail the interviewer wants)
see solution.py

Review

Re-check that your algorithm solves the problem by running through important examples
Go through it as if you are debugging it, assuming there is a bug
Evaluate

Finish by giving space and run-time complexity
Discuss any pros and cons of the solution
Assume N is the length of the input string s.

Time Complexity: O(N)
Space Complexity: O(N)
