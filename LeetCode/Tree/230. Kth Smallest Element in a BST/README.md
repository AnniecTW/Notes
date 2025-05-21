## 230. Kth Smallest Element in a BST
🔗 Link: [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.<br>


Example 1:<br>
![kthtree1](https://github.com/user-attachments/assets/87943b8e-c78f-4e94-a1a9-b04a70c609d9)


Input: root = [3,1,4,null,2], k = 1<br>
Output: 1<br>


Example 2:<br>
![kthtree2](https://github.com/user-attachments/assets/96f5604c-4b52-44ab-b84a-47024a267817)


Input: root = [5,3,6,2,4,null,null,1], k = 3<br>
Output: 3<br>


Constraints:<br>

- The number of nodes in the tree is n.
- 1 <= k <= n <= 10<sup>4</sup>
- 0 <= Node.val <= 10<sup>4</sup>

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be `None`?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [0, 1, 2], k = 3; Output: 2
4. Edge case - Input: `root` = [0, 1], k = 1; Output: 0
5. Edge case - Input: `root` = [0], k = 1;; Output: 0

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Binary Search Tree / In-order traversal
   Since a valid BST requires all nodes in the left subtree < root < all nodes in the right subtree, we can count the number of nodes visited during an in-order traversal, which visits nodes in ascending order in a BST.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use in-order traversal to visit nodes in ascending order. Keep a counter of nodes have been visited. When the counter reaches `k`, recourd the current node value as the result.<br>

1) Initialize `self.count = 0` and `self.result = None`
   a) Define a helper function `inOrder(node)`:<br>
   b) If `node is None` or `self.result is not None`, return early<br>
   c) Recurse into the left subtree: `inOrder(node.left)`<br>
   d) Increment counter: `self.count += 1`<br>
   e) If `self.count == k`, set `self.result = node.val` and return<br>
   f) Recurse into right subtree: `inOrder(node.right)`<br>
3) Call `inOrder(root)` to start the traversal from the root<br>
4) Return `self.result`


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


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
  In the worst case (when `k == N` or the tree is unbalanced), we may visit all nodes.<br>
- Space Complexity: O(H)<br>
  The recursion stack takes up O(H) space.<br>
  In the best case (balanced BST), H = log(N). <br> 
  In the worst case (completely unbalanced BST), H = N. <br>

