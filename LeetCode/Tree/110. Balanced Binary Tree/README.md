## 110. Balanced Binary Tree
🔗 Link: [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Binary Tree<br>

<hr>

Given a binary tree, determine if it is height-balanced.<br>

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.<br>


Example 1:<br>

<img src="https://github.com/user-attachments/assets/b070ca81-9717-46fd-81aa-2616af8e4185" alt="binary tree" width="200" />

>Input: root = [3,9,20,null,null,15,7]<br>
Output: true<br>


Example 2:<br>

<img src="https://github.com/user-attachments/assets/60154f8e-0d48-40c4-af7b-ba6eb635ef54" alt="binary tree" width="250" />

>Input: root = [1,2,2,3,3,null,null,4,4]<br>
Output: false<br>
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.<br>


Example 3:<br>

>Input: root = []<br>
Output: true<br>


Constraints:<br>

- The number of nodes in the tree is in the range [0, 5000].
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [1,2,3,4,2]; Output: true
4. Edge case - Input: `root` = [1,0,null,2]; Output: false
5. Edge case - Input: `root` = []; Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Depth-First Search
   - Use DFS traversal. At each node, compute the depths of the left and right subtrees and check if the difference is more than 1<br>
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use DFS to compute and compare the depths of left and right subtrees to determine if the tree is balanced. 

1) Define `dfs(node)` that returns `(depth, totBalanced)`.<br>
   a) If `node` is `None`, return `0, True`<br>
   b) Recursively call left and right:<br>
      ```python
      leftDepth, leftBalanced = dfs(node.left)
      rightDepth, rightBalanced = dfs(node.right)
      ```
   c) Determine if current node is balanced:
      ```python
      curBalanced = abs(left - right) <= 1
      ```
   d) Combine subtree status:
      ```python
      totBalanced = curBalanced and leftBalanced and rightBalanced
      ```
   e) Return:
      ```python
      return max(leftDepth, rightDepth) + 1, totBalanced
3) Call `d, b = dfs(root)`
4) Return `b`
    
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

