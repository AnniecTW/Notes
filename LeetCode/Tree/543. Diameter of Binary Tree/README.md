## 543. Diameter of Binary Tree
🔗 Link: [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree<br>

<hr>

Given the `root` of a binary tree, return the length of the diameter of the tree.<br>

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.<br>

The **length** of a path between two nodes is represented by the number of edges between them.<br>


Example 1:<br>
<img src="https://github.com/user-attachments/assets/c9458b2e-3625-4605-af88-a200905f90b9" alt="binary tree" width="200" />

>Input: root = [1,2,3,4,5]<br>
Output: 3<br>
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].<br>


Example 2:<br>

Input: root = [1,2]<br>
Output: 1<br>


Constraints:<br>

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
- -100 <= Node.val <= 100

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [1,2,3,4,5,null,null,6,null,null,7,null,8,9]; Output: 6
4. Edge case - Input: `root` = [0,1]; Output: 1
5. Edge case - Input: `root` = [1]; Output: 0

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Depth-First Search
   Use DFS to calculate the height of each subtree. The diameter is the maximum sum of left and right subtree heights at any node.<br>
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use DFS to compute the height of each node’s left and right subtrees. At each node, compute the path length passing through it (leftHeight + rightHeight), and update the maximum diameter seen so far.

1) Initialize `dia = 0`
2) Define function `dfs(node)`:<br>
   a) If `node` is `None`, return `0`<br>
   b) Recursively compute left and right subtree heights: 
      `left = dfs(node.left)`, `right = dfs(node.right)`<br>
   c) Update diameter: `dia = max(dia, left + right)`<br>
   d) Return max height: `max(left, right) + 1`<br>
3) Call `dfs(root)`
4) Return `dia`
    
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
  In the worst case (skewed tree), recursion stack may grow to O(N).

