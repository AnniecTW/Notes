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
   Use a inner recursive function to check if two trees are identical. If current `root` and `subRoot` are not identical, continue outer recursion into left and right children of current `root`
2. Serialization / Stringify (Optimized in run time)
   Transform tree of `root` and `subRoot` into string, simply check if the string of `subRoot` is a substring of `root`
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

#### Recursion
General Idea: Check if two trees are identical by recursion. If current `root` fails, recurse into its left and right children and check again

1) Define a recursive function `isSame(r, s)`, where `r` and `s` are two nodes passed into the function
   a) If `r` and `s` are both `None`, indicating recursion is finished on both tree, return `True` <br>
   b) If only one of the two trees completes recursion earlier than the other, indicating they are not identical, return `False`<br>
   c) If `r.val` is not equal to `s.val`, return `False`<br>
   d) If none of the above is true, recurse into the left and right children of current `root` and `subRoot` to continue comparison<br>
2) If `root` is `None` but `subRoot` exists, return `False`
3) Start with `root`, compare it to `subRoot` using function just defined.
4) Return the result if the function returns `true`; otherwise, recrurse into children of `root` and compare them with current `subRoot` using recursion function

===========================================================================================
#### Serialization
General Idea: Stringify both `root` and `subRoot`, then check if `subRoot` is a substring of `root`

1) Generate strings of `root` tree and `subRoot` tree using pre-order traversal
2) Check if string of `subRoot` is a substring of `root`, if so, then return `True`; otherwise, return `False`
    
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
  Each node in `root` can be beginning of a recursion check, and each check cause O(M) run time
- Space Complexity: O(max(H1, H2))<br>
  The space is used by recursion stack, and it depends on the height of the larger tree
===========================================================================================
#### Serialization
- Time Complexity: O(N + M)<br>
  Every node in `root` and `subRoot` is visited exactly once.
- Space Complexity: O(N + M)<br>
  Every node value in `root` and `subRoot` is stored as strings.
