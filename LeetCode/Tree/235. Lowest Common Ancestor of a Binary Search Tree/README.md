## 235. Lowest Common Ancestor of a Binary Search Tree
🔗 Link: [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/invert-binary-tree/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.<br>

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”<br>


Example 1:<br>
![binarysearchtree_improved](https://github.com/user-attachments/assets/c8610b07-11a7-4c69-97ee-aa6c7f7178e2)

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8<br>
Output: 6<br>
Explanation: The LCA of nodes 2 and 8 is 6.<br>


Example 2:<br>
![binarysearchtree_improved-2](https://github.com/user-attachments/assets/94bc5a16-210d-4524-b04d-7102373e26e3)

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4<br>
Output: 2<br>
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.<br>


Example 3:<br>
Input: root = [2,1], p = 2, q = 1<br>
Output: 2<br>

Constraints:<br>

- The number of nodes in the tree is in the range [2, 105].
- -10<sup>9</sup> <= Node.val <= 10<sup>9</sup>
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the BST be empty?
2. Any requirements on time/space complexity?
3. Will `p` and `q` always exist in BST?
4. Happy path - Input: `root` = [0,1,2], p = 1, q = 2; Output: 0
5. Edge case - Input: root = [2,1], p = 2, q = 1; Output: 2
6. Edge case - Input: root = [1,null,2], p = 2, q = 1; Output: 1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Binary Search Tree
   Use the ordered property of BST to determine which subtree to search. Since left child < root < right child, we can compare the target nodes with the current node and only visit necessary paths.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use BST property to locate the lowest common ancestor without visiting unnecessary nodes

1) Start with the root node and iterate while `root` is not `None`:<br>
   a) If `root.val` > `p.val` and `q.val`, both nodes are in the left subtree → move to `root.left`<br>
   b) If `root.val` < `p.val` and `q.val`, both nodes are in the right subtree → move to `root.right`<br>
   c) Otherwise, current `root` is between `p` and `q` or equal to one of them → this is the lowest common ancestor → return `root`<br>
   
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume H represents the height of the tree

- Time Complexity: O(H)
- Space Complexity: O(1)
