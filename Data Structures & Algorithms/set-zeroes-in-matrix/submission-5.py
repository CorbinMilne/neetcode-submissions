class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROW, COL = len(matrix), len(matrix[0])

        first_row_zero = False #first row originally contains 0
        first_col_zero = False #first col originally contains 0

        for i in range(ROW):
            if matrix[i][0] == 0:
                first_col_zero = True

        for i in range(COL):
            if matrix[0][i] == 0:
                first_row_zero = True

        #skip first row and first col since we use them as markers above
        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(COL):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(ROW):
                matrix[i][0] = 0

        
        