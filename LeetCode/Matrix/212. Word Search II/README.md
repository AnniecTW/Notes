## 212. Word Search II
🔗 Link: [Word Search II](https://leetcode.com/problems/word-search-ii/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Matrix / Backtracking<br>

<hr>

Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially **adjacent cells**, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.<br>


Example 1:

<img src="https://github.com/user-attachments/assets/f9ea27d2-e743-4a92-a253-6d8cea332db7" alt="4 * 4 matrix" width="300" />

>Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]<br>
Output: ["eat","oath"]<br>


Example 2:<br>

<img src="https://github.com/user-attachments/assets/de36ac7f-4b18-49f8-8549-58293f209650" alt="2 * 2 matrix" width="150"/>

>Input: board = [["a","b"],["c","d"]], words = ["abcb"]<br>
Output: []<br>


Constraints:<br>

- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10<sup>4</sup>
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `board` be empty or contain empty rows (e.g., [] or [[]])?<br>
2. Any constraints on time/space complexity?<br>
3. Can I modify the orginal matrix, or should I treat it as read-only?
4. If multiple paths for a word are found, should I record all of them in the result or keep each word unique in the result?
5. Happy path -
   ```python
    Input: matrix = [
      ['A','A','B'],
      ['B','D','E'],
      ['C','F','A']
    ], word = ['ABC', 'CFA']

    Output: ['ABC', 'CFA']

   ```
6. Edge case -
   ```python
    Input: matrix = [['A']], word = 'B'
    Output: []
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Matrix / Backtracking / DFS
   - We use dfs/backtracking to look for a valid path that contains the target word cell by cell.
2. Pruning
   - There are several words need to be searched. If the current cell doesn't contain any words' prefix, we can use **Trie** data structure to stop backtracking immediately 
   - In some situations, current word has been found. We can delete its letter(key-value pair) in **Trie** recursively to prevent repeating<br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: First use **Trie** to store all entries in words. Then iterate through each cell in `board` and call dfs to search possible paths containing valid words.<br>

1) Construct `Trie` data structure
   ```python
   class Trie:
       def __init__(self):
           self.root = {}

       def insert(self, word):
           cur = self.root

           for c in word:
               if c not in cur:
                   cur[c] = {}
               cur = cur[c]
           cur['end'] = True 
2) Build a Trie instance and insert all words
   ```python
   trie = Trie()
   for word in words:
       trie.insert(word)
3) Initialize `res = []`
4) Set `rows, cols = len(board), len(board[0])`
5) Defince `dfs(r, c ,cur, word)` for backtracking
   a) Prune if
      - `r` and `c` are out of bounds
      - current cell visited
      - current cell doesn't match the required letter in `word`
      ```python
      if not (0 <= r < rows) or not (0 <= c < cols) or board[r][c] not in cur or board[r][c] == '*':
                return
      ```
   b) If the letter is valid, concatenate it to `word`. Then go to the next node to check if it's the end of a word. If so, append `word` to `res`
      <br>
      ```python
      letter = board[r][c]
            word += letter
            next_node = cur[letter]
            path.append(letter)

            if next_node.get('end'):
                res.append(word)
                del next_node['end']
      ```
   c) Mark current cell as visited before move forward to four directions for further searching. Set back to the original value when backtracking <br>
      ```python
      board[r][c] = '*'

      dfs(r + 1, c, next_node, word)
      dfs(r, c + 1, next_node, word)
      dfs(r - 1, c, next_node, word)
      dfs(r, c - 1, next_node, word)

      board[r][c] = letter
      ```
6) Traverse through the `board`, call `dfs` to explore each cell
   ```python
   for r in range(rows):
       for c in range(cols):
           dfs(r, c, trie.root, '')
7) Return the result `res`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume M is the nubmer of rows, N is the number of columns of `board`, and L is the length of `word`

- Time Complexity: O(M * N * 3<sup>L</sup>)<br>
  For each of the M * N cells, we may start a DFS. At each step in the DFS, we can explore up to 3 directions (can't revisit the previous cell), and the maximum depth of the DFS is `L` (the length of the `word`). So, the overall time complexity is O(M * N * 3<sup>L</sup>). <br>
- Space Complexity: O(L)<br>
  The recursion stack and `visited` set both take up to O(L) space in the worst case. If we can modify the `board`, we can eliminate the `visited` set entirely and mark visited cells in-place (e.g., replacing with '#' temporarily), which reduces memory usage.<br>
