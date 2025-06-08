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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build tire
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []
        rows, cols = len(board), len(board[0])

        # dfs for searching characters in word
        def dfs(r, c, cur, word):
            if not (0 <= r < rows) or not (0 <= c < cols) or board[r][c] not in cur or board[r][c] == '*':
                return

            letter = board[r][c]
            word += letter
            next_node = cur[letter]
            path.append(letter)

            if next_node.get('end'):
                res.append(word)
                del next_node['end']

            board[r][c] = '*'

            dfs(r + 1, c, next_node, word)
            dfs(r, c + 1, next_node, word)
            dfs(r - 1, c, next_node, word)
            dfs(r, c - 1, next_node, word)

            board[r][c] = letter

            # pruning
            if not next_node:
                del cur[letter]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, "")
        return res
