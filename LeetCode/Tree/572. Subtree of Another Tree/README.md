## 572. Subtree of Another Tree
🔗 Link: [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Tree<br>

<hr>

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of root with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.<br>


Example 1:<br>
![subtree1-tree](https://github.com/user-attachments/assets/e5809621-10cc-400c-87bc-21904bd4be7b)


Input: root = [3,4,5,1,2], subRoot = [4,1,2]<br>
Output: true<br>


Example 2:<br>
![subtree2-tree](https://github.com/user-attachments/assets/531ab984-c59e-41cc-9877-a4ad4280bcae)


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]<br>
Output: false<br>


Constraints:<br>

- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10<sup>4</sup> <= root.val <= 10<sup>4</sup>
- -10<sup>4</sup> <= subRoot.val <= 10<sup>4</sup>

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `root` or `subRoot` be empty?
2. Any requirements on time/space complexity?
3. Happy path - Input: `root` = [0, null, 1], `subRoot` = [0, 1]; Output: false
4. Edge case - Input: `root` = [1, 1], `subRoot` = [1]; Output: true
5. Edge case - Input: `root` = [1], `subRoot` = [1]; Output: true

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Tree / Recursion
   Use an inner recursive function to check if two trees are identical. If current `root` and `subRoot` are not identical, continue outer recursion into left and right children of current `root`
2. Serialization / Stringify
   Transform both `root` and `subRoot` into string representations, simply check if the string of `subRoot` is a substring of `root`
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

#### Recursion
General Idea: Recursively check if two trees are identical. If the current `root` doesn't match `subRoot`, recursively check its left and right children

1) Define a helper function `isSame(r, s)`:<br>
   a) If both `r` and `s` are `None`, return `True`<br>
      // Both trees finished traversing at the same time → same structure and values so far<br>
      
   b) If only one is `None`, return `False`<br>
      // One tree ended early → not the same structure
   
   c) If `r.val != s.val`, return `False`<br>
   d) Recursively check left and right subtrees: `isSame(r.left, s.left) and isSame(r.right, s.right)`<br>

3) In main function:<br>
   a) If `root` is `None`, return `False` (can't contain `subRoot`)<br>  
   b) If `isSame(root, subRoot)` is `True`, return `True`<br>  
   c) Else, recursively check `root.left` and `root.right`<br>  

4) Return whether `subRoot` is found as a subtree in either branch

===========================================================================================
#### Serialization
General Idea: Serialize both trees using preorder traversal (including null markers), and check if the serialized `subRoot` string is a substring of `root`

1) Define a function to serialize a tree using preorder traversal with null markers (`#`)
2) Serialize both `root` and `subRoot`
3) Check if `subRoot_serialized` is a substring of `root_serialized`
4) Return the result
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes in `root`, M represents the number of nodes in `subRoot`, H1 represents the height of tree `root`, and H2 represents the height of tree `subRoot` 

#### Recursion
- Time Complexity: O(N * M)<br>
  For each of the N nodes in `root`, we may compare up to M nodes in `subRoot`.
- Space Complexity: O(max(H1, H2))<br>
 Due to recursive call stack, space used is proportional to the height of the trees
===========================================================================================
#### Serialization
- Time Complexity: O(N * M)<br>
  Each node is visited once during serialization, and substring search is O(N + M) with KMP or similar (naive is O(N * M))
- Space Complexity: O(N + M)<br>
  Storing serialized strings of both trees.
