## 1448. Count Good Nodes in Binary Tree
🔗 Link: [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Binary Tree<br>

<hr>

Given a binary tree `root`, a node X in the tree is named **good** if in the path from root to X there are no nodes with a value *greater than* X.<br>

Return the number of **good** nodes in the binary tree.<br>


Example 1:<br>

<img src="https://github.com/user-attachments/assets/b352122f-760a-44c3-a109-aba771c0cb2c" alt="binary tree" width="250" />

>Input: root = [3,1,4,3,null,1,5]<br>
Output: 4<br>
Explanation: Nodes in blue are good.<br>
Root Node (3) is always a good node.<br>
Node 4 -> (3,4) is the maximum value in the path starting from the root.<br>
Node 5 -> (3,4,5) is the maximum value in the path<br>
Node 3 -> (3,1,3) is the maximum value in the path.<br>


Example 2:<br>

<img src="https://github.com/user-attachments/assets/530b02f6-73a4-48b0-8708-74142467ae4c" alt="binary tree" width="200" />

>Input: root = [3,3,null,4,2]<br>
Output: 3<br>
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.<br>


Example 3:<br>

>Input: root = [1]<br>
Output: 1<br>
Explanation: Root is considered as good.<br>


Constraints:<br>

- The number of nodes in the binary tree is in the range [1, 10<sup>5</sup>].
- Each node's value is between [-10<sup>4</sup>, 10<sup>4</sup>].

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [1,2,3,4,2]; Output: 5
4. Edge case - Input: `root` = [1,0]; Output: 1
5. Edge case - Input: `root` = [1]; Output: 1 (Root is considered as good)

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Depth-First Search
   - Use DFS to traverse the tree while keeping track of the maximum value seen so far. Then compare the value with the current node's to check if it's good.<br>
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use DFS to track the maximum value along the path and compare it with the current node's value to determine if it's a good node.

1) Initialize `res = 0`
2) Define function `dfs(node, cur_max)`:<br>
   a) If `node` is `None`, return `0`<br>
   b) If current node value is larger than or equal to current maximum value, then increment `res` and set `cur_max` to `node.val`<br>
   c) Recursively call `dfs(node.left, cur_max)` and `dfs(node.right, cur_max)`<br>
3) Call `dfs(root, float('-inf'))`
4) Return `res`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes and H is the height of the tree.

- Time Complexity: O(N)<br>
  Every node is visited exactly once.<br>
- Space Complexity: O(H)<br>
  In a balanced tree, the recursion stack will be O(log N), but in the worst case (e.g. a skewed tree), it can grow to O(N).

