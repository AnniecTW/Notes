## 297. Serialize and Deserialize Binary Tree
🔗 Link: [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Binary Tree<br>

<hr>

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.<br>

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.<br>

Clarification: The input/output format is the same as [how LeetCode serializes a binary tree](https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.<br>


Example 1:<br>


<img src="https://github.com/user-attachments/assets/8e385a89-787e-4a30-ba1f-e71674601815" alt="binary tree" width="250" />

>Input: root = [1,2,3,null,null,4,5]<br>
Output: [1,2,3,null,null,4,5]<br>


Example 2:<br>


>Input: root = []<br>
Output: []<br>


Constraints:<br>

- The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
- -1000 <= Node.val <= 1000

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input tree be empty? ((e.g. `root = None`))<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [1,null,3,4,6]; Output: [1,null,3,4,6]<br>
4. Edge case - Input: `root` = []; Output: []<br>

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / PreOrder traversal / Depth-First Search
   - Use PreOrder to serialize (`root -> left -> right`), which preserves structure
   - Use **DFS** to deserialize by recursively rebuilding the tree from the list
   - Using PreOrder ensures we can correctly reconstruct the tree structure with a simple DFS
  
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use preOrder traversal to serialize the tree and DFS to rebuild it.

#### Serialization:<br>
1) Define `preOrder(root)`<br>
   a) If `root` is `None`, return `['#']` (represents null node)<br>
   b) Otherwise, return `[str(root.val)] + preOrder(root.left) + preOrder(root.right)`
2) Join the list with commas: `Return ','.join(preOrder(root))`<br>
   
#### Deserialization:<br>
3) Convert input string to deque: `vals = deque(data.split(','))`
4) Define recursive `dfs()` to rebuild the tree
   a) Pop the first value from `vals`
   b) If it’s `'#'`, return `None`
   c) Create a `TreeNode` with the current value
   d) Recursively build `left` and `right` subtrees
   e) Return the current node

    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes.

- Time Complexity: O(N)<br>
  Each node is visited once.<br>
- Space Complexity: O(N)<br>
  It costs O(N) to store the list.
