## 124. Binary Tree Maximum Path Sum
🔗 Link: [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Binary Tree<br>

<hr>

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.<br>

The path sum of a path is the sum of the node's values in the path.<br>

Given the root of a binary tree, return the maximum path sum of any non-empty path.<br>


Example 1:<br>


<img src="https://github.com/user-attachments/assets/2cc70b12-1e1f-421a-b6f6-bd3a04e105d9" alt="binary tree" width="200" />

>Input: root = [1,2,3]<br>
Output: 6<br>
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.<br>


Example 2:<br>

<img src="https://github.com/user-attachments/assets/ab48d7b7-0692-4985-9548-03878d0832e3" alt="binary tree" width="250" />

>Input: root = [-10,9,20,null,null,15,7]<br>
Output: 42<br>
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.<br>


Constraints:<br>

- The number of nodes in the tree is in the range [1, 3 * 10<sup>4</sup>].
- -1000 <= Node.val <= 1000

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [1,2,3,4,6]; Output: 12<br>
4. Edge case - Input: `root` = [1]; Output: 1<br>

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Depth-First Search
   - Use DFS to traverse the tree while keeping track of the maximum path sum seen so far. One key detail is that we separately track the maximum path sum **through** the current node and the value to **return** to its parent.<br>
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use DFS to track two values — the maximum path sum that goes through the current node (can include both left and right), and the maximum path sum that can be returned to its parent (can only include one side).

1) Initialize `ans = float('-inf')`
2) Define function `dfs(node)`:<br>
   a) If `node` is `None`, return `0`<br>
   b) Recursively call `left = dfs(node.left)` and `right = dfs(node.right)`<br>
   c) Compute the maximum path sum through the current node:<br>
      ```python
      # can take both left and right
      cur_max = max(left, 0) + max(right, 0) + node.val
      ans = max(ans, cur_max)
      ```
   d) Compute the maximum path sum to return to parent:<br>
      ```python
      # can only take one side
      return max(left, right, 0) + node.val
      ```
3) Call `dfs(root)`
4) Return `ans`
    
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

