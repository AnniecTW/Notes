class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def dfs(i, j):
            if memo[i][j]:  # if explored, just return value
                return memo[i][j]

            max_len = 1  # at least one step starting from this cell

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if (0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]): 
                    max_len = max(max_len, 1 + dfs(ni, nj))

            memo[i][j] = max_len  # memoization
            return max_len

        return max(dfs(i, j) for i in range(rows) for j in range(cols))
