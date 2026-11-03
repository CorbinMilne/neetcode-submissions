class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROW, COL = len(matrix), len(matrix[0])

        rows = set()
        cols = set()

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(ROW):
            for j in range(COL):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        
        