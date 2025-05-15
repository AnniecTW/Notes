## 105. Construct Binary Tree from Preorder and Inorder Traversal
🔗 Link: [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.<br>


Example 1:<br>
![tree](https://github.com/user-attachments/assets/b441219d-5823-4c00-a4c1-7bd9905846dc)


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]<br>
Output: [3,9,20,null,null,15,7]<br>


Example 2:<br>

Input: preorder = [-1], inorder = [-1]<br>
Output: [-1]<br>


Constraints:<br>

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `preorder` or `inorder` be null?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `preorder` = [1,2,3], `inorder` = [2,1,3]; Output: [2,1,3]
4. Edge case - Input: `preorder` = [0,1], `inorder` = [1,0]; Output: [0,1]
5. Edge case - Input: `preorder` = [1], `inorder` = [1]; Output: [1]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / In-order and pre-order traversal / Hash map
   Mapping values to their indices in the in-order array allows quick lookup of a node’s position, which helps determine the range of left and right subtrees.
   Then build the tree by consuming nodes from the pre-order array, which always provides the root node before its children.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Map values to their indices in the in-order array to quickly determine the range of the left and right subtrees. 
              Then create new nodes from the pre-order array and recursively build their left and right subtrees based on the in-order range.

1) Create map `mapping` to map the index and value in `inorder` array
2) Transform `preorder` to a deque `preOrder` for later iteration
3) Define `build(start, end)` function works as follows<br>
   a) If `start` > `end`, indicating the index if out of range and has no node, so return `None` <br>
   b) Initialize `node` as a TreeNode with the first element in `preOrder` array as a value passed in<br>
   c) Access the node's index through `mapping` and store in `mid`<br>
   d) Recursively set the left and right child and narrow down the range to `build(start, mid - 1)` and `build(mid + 1, end)` separately
   e) Finally return `node`
5) Call the `build` function with the initial range`(0, len(preorder) - 1)` and return the result
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes in `preorder` or `inorder`

- Time Complexity: O(N)<br>
  Every node is visited exactly once.
- Space Complexity: O(N)<br>
  Recursion stack takes up to O(N) space in the worst case (unbalanced tree). Also, We use a deque to hold the preorder list for efficient popleft operations.

