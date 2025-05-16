## 98. Validate Binary Search Tree
🔗 Link: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).<br>

A valid BST is defined as follows:<br>

- The left subtree of a node contains only nodes with keys less than the node's key.<br>
- The right subtree of a node contains only nodes with keys greater than the node's key.<br>
- Both the left and right subtrees must also be binary search trees.<br><br>


Example 1:<br>
![tree1](https://github.com/user-attachments/assets/1ac75ba6-6e5d-4a2e-8254-0e56c805a18a)


Input: root = [2,1,3]<br>
Output: true<br>


Example 2:<br>
![tree2](https://github.com/user-attachments/assets/0661e387-4c7a-49a6-9169-b796903d44f4)


Input: root = [5,1,4,null,null,3,6]<br>
Output: false<br>
Explanation: The root node's value is 5 but its right child's value is 4.<br>


Constraints:<br>

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>].
- -2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Are there duplicate values in the tree?
4. Happy path - Input: `root` = [0, null, 1]; Output: true
5. Edge case - Input: `root` = [1,0]; Output: false
6. Edge case - Input: `root` = [0]; Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Binary Search Tree / Validity Check Using Ranges
   Since a valid BST requires all nodes in the left subtree < root < all nodes in the right subtree, we can recursively validate the tree by checking if each node falls within a valid range defined by its ancestors.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Recursively check if each node's value falls within a valid range defined by its position in the tree.

1) Define a helper function `valid(node, low, high)` where `low` and `high` denote the allowable range for the current node’s value.
   a) If `node` is none, return `True`<br>
   b) If `node.val` is not strictly between `low` and `high`, return `False`<br>
   c) Recursively validate the left subtree with range `(low, node.val)` and the right subtree with range `(node.val, high)`<br>
2) Call `valid(root, float('-inf'), float('inf'))` to start the recursion from the root<br>
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes, H represents the height of the tree.

- Time Complexity: O(N)<br>
  In the worst case (when the tree is a valid BST), every node is visited exactly once, resulting in O(N) time.<br>
- Space Complexity: O(H)<br>
  The recursion stack takes up O(H) space in the worst case.<br>

