class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        - mark entire row or col to zero if one element is zero
        - 1 pass to get all rows and cols to zero, 2nd pass to zero that
        """
        
        r_set = set()
        c_set = set()
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r_set.add(i)
                    c_set.add(j)
        
        for r in r_set:
            for j in range(n):
                matrix[r][j] = 0
        for c in c_set:
            for i in range(m):
                matrix[i][c] = 0
