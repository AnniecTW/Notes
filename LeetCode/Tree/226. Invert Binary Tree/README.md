## 226. Invert Binary Tree
🔗 Link: [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given the `root` of a binary tree, invert the tree, and return its root.<br>


Example 1:<br>
![invert1-tree](https://github.com/user-attachments/assets/3033ab3f-38f9-474c-bf0e-25018fdd7a39)


Input: root = [4,2,7,1,3,6,9]<br>
Output: [4,7,2,9,6,3,1]<br>

Example 2:<br>
![invert2-tree](https://github.com/user-attachments/assets/aa1055b5-fd9d-4f12-a235-5609cb340722)


Input: root = []<br>
Output: []<br>

Constraints:<br>

- The number of nodes in the tree is in the range [0, 100].
- 100 <= Node.val <= 100

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [0, null, 1]; Output: [0, 1, null]
4. Edge case - Input: `root` = [0]; Output: [0]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Recursion
   Recursively visit all nodes and swap their left and right children during traversal
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: recursively traverse the tree and swap the left and right children of each node

1) If root is `None`, return `None`
2) Recursively invert the right subtree and assign it to `root.left`
3) Recursively invert the left subtree and assign it to `root.right`
4) Return the current node (`root`)
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes, H represents the height of the tree

- Time Complexity: O(N)<br>
  Every node is visited exactly once.
- Space Complexity: O(H)
  Due to recursion stack. In the worst case (unbalanced tree), it could be O(N); in the best case (balanced tree), it is O(log N).
  
