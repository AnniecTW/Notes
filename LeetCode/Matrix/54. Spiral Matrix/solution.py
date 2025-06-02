class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        r, c , dr, dc = 0, 0, 0, 1
        res = []

        for _ in range(m * n):
            res.append(matrix[r][c])
            matrix[r][c] = "!"

            # next position
            nr, nc = r + dr, c + dc

            if not 0 <= nr < m or not 0 <= nc < n or matrix[nr][nc] == "!":
                dr, dc = dc, -dr

            r += dr
            c += dc
        
        return res
            
