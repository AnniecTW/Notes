## 199. Binary Tree Right Side View
🔗 Link: [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Tree<br>

<hr>

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.<br>


Example 1:<br>
![tmpd5jn43fs-1](https://github.com/user-attachments/assets/dd34a434-c1d7-4cc3-8e7a-4b97b9251248)


Input: root = [1,2,3,null,5,null,4]<br>
Output: [1,3,4]<br>


Example 2:<br>
![tmpkpe40xeh-1](https://github.com/user-attachments/assets/8d98c183-c653-42b6-97bc-b0db18c2d359)


Input: root = [1,2,3,4,null,null,null,5]<br>
Output: [1,3,4,5]<br>


Example 3:<br>

Input: root = [1,null,3]<br>
Output: [1,3]<br>


Example 4:<br>

Input: root = []<br>
Output: []<br>

Constraints:<br>

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` be empty?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: `root` = [0, null, 1]; Output: [0, 1]
4. Happy path - Input: `root` = [0, 1]; Output: [0, 1]
5. Edge case - Input: `root` = [0]; Output: [0]
6. Edge case - Input: `root` = []; Output: []

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Breadth-First Search
   Use a queue to perform BFS and collect nodes level by level. When iterating at each level, append the rightmost node's value to the result.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a queue to traverse the tree level by level, append the first visited node's value for each level (due to right-to-left traversal) to the result

1) If `root` is empty, return `[]`
2) Initialize `res = []` and `queue = deque([root])`
3) While `queue` is not empty:<br>
   a) Set `n = len(queue)` to control the number of interatations for the current level<br>
   b) Iterate `n` times:<br>
      i) pop a node from `queue`
      ii) if current index is 0, then append `node.val` to `res`
      iii) if `node` has right child, append it to queue
      iV) if `node` has left child, append it to queue
5) Return `res`
    
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
  Every node is visited exactly once.
- Space Complexity: O(N)<br>
  In the worst case, e.g. full binary tree, the queue may store up to N/2 nodes at the last level

