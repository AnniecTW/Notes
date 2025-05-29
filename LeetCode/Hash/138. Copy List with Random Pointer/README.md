## 138. Copy List with Random Pointer
🔗 Link: [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash<br>

<hr>

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.<br>

Construct a deep copy of the list. The [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list.** <br>

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.
Your code will only be given the `head` of the original linked list.<br>

 

Example 1:<br>
![e1](https://github.com/user-attachments/assets/e244005a-d49a-4e72-8990-7e1b4e8c8e06)

>Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]<br>
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]<br>


Example 2:<br>
![e2](https://github.com/user-attachments/assets/fc09b9d4-cf94-4b9d-aa73-4bef94fadd5e)

>Input: head = [[1,1],[2,1]]<br>
Output: [[1,1],[2,1]]<br>


Example 3:<br>
![e3](https://github.com/user-attachments/assets/5cd31c7f-1a8a-4468-8af6-76852ec70a24)

>Input: head = [[3,null],[3,0],[3,null]]<br>
Output: [[3,null],[3,0],[3,null]]<br>
 

Constraints:<br>

- 0 <= n <= 1000
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
- `Node.random` is `null` or is pointing to some node in the linked list.
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `head` be `None`?<br>
2. Any requirements on time/space complexity?<br>
3. Happy path - Input: head = [[1,null],[2,null]]; Output: [[1,null],[2,null]]<br>
4. Edge case - Input: head = None (i.e. empty list); Output: None<br>

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Linked List Deep Copy / Hash map
   - Store a mapping from original nodes to copied nodes to avoid making multiple copies. Requires O(N) space.
3. Linked List Deep Copy / Interweaving
   - Interleave copy nodes with original nodes to avoid extra space. Use the interleaved structure to set `random` pointers.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Interweave the old and copied lists using next pointers, which can help us get the correct nodes for next and random pointers while saving space. Then separate the two lists cleanly.<br>

1) If `head` is `None`, return `None`
2) Insert copied nodes into old nodes through iteration
   ```python
   cur = head
   while cur:
      new_node = Node(cur.val)
      new_node.next = cur.next
      cur.next = new_node
      cur = new_node.next
   ```
3) Set random node to its copied reference through iteration if the corresponding old nodes doesn't point to `None`
   ```python
   cur = head
   while cur:
       if cur.random:
          cur.next.random = cur.random.next # point to copied node
       cur = cur.next.next
   ```
4) Separate two lists cleanly by using a dummy head as the head of copied list
   ```python
   cur = head
   head_copy = Node(0) # dummy node to simplify edge case handling
   cur_copy = head_copy

   while cur:
       copy = cur.next
       cur_copy.next = copy
       cur_copy = copy
  
       cur.next = copy.next
       cur = cur.next # move to next original node
        
   return head_copy.next
   ```
5) Return `head_copy.next`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the nubmer of nodes of `head` linked list

- Time Complexity: O(N)<br>
  Three separate passes over the list.<br>
- Space Complexity: O(1)<br>
  No extra data structures (interweaving nodes in-place).
