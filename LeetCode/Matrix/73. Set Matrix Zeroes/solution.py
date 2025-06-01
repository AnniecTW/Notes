class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_zero = False
        first_col_has_zero = False
        m, n = len(matrix), len(matrix[0])

        # iterate first row and col to check if there's any zero
        for num in matrix[0]:
            if num == 0:
                first_row_has_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # iterate the rest part and if the cell contains zero, mark its corresponding postition in first row and col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        # set the marked rows to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # set the marked cols to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # check if the first row needs to be set as zero
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # check if the first col needs to be set as zero
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
