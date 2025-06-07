class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m, n = len(board), len(board[0])
        counter = {}
        for c in word:
            counter[c] = 1 + counter.get(c, 0)
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < m) or not (0 <= c < n) or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))
            res = (
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1)
            )
            visited.remove((r, c))
            return res
        
        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True
        return False
