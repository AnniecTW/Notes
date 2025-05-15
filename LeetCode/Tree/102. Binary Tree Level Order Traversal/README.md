## 102. Binary Tree Level Order Traversal
🔗 Link: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).<br>


Example 1:<br>
![tree1](https://github.com/user-attachments/assets/151d9a0f-2ee3-4548-a28b-6e3d7dd043c2)

Input: root = [3,9,20,null,null,15,7]<br>
Output: [[3],[9,20],[15,7]]<br>


Example 2:<br>
![invert2-tree](https://github.com/user-attachments/assets/aa1055b5-fd9d-4f12-a235-5609cb340722)

Input: root = [1]<br>
Output: [[1]]<br>


Example 3:<br>

Input: root = []<br>
Output: []<br>

Constraints:<br>

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [0, null, 1]; Output: [[0], [1]]
4. Edge case - Input: `root` = [0]; Output: [[0]]
5. Edge case - Input: `root` = []; Output: []

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Breadth-First Search
   Use a queue to perform BFS and collect nodes level by level. After processing each level, append the list of node values to the result.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a queue to traverse the tree level by level, storing values for each level in a temporary list

1) If `root` is empty, return `[]`
2) Initialize `res = []` and `queue = deque([root])`
3) While `queue` is not empty:<br>
   a) Set `level_size = len(queue)` to control the number of interatations for the current level<br>
   b) Initialize `level = []` to store nodes for current level<br>
   c) Iterate `level_size` times:<br>
      &ensp;&ensp;i) pop a node from `queue`, and append `node.val` to `level`<br>
      &ensp;&ensp;ii) if `node` has left child, append it to queue<br>
      &ensp;&ensp;iii) if `node` has right child, append it to queue<br>
   d) append `level` to `res` after finishing iteration for the current level<br>
4) Return `res`<br>
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes

- Time Complexity: O(N)<br>
  Every node is visited exactly once.<br>
- Space Complexity: O(N)<br>
  In the worst case, e.g. full binary tree, the queue may store up to N/2 nodes at the last level<br>

