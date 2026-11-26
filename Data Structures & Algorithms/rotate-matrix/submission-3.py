class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def sol_reverse_transpose():
            matrix.reverse()
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        return sol_reverse_transpose()


        def sol_traverse():
            l, r = 0, len(matrix) - 1
            while l < r:
                for i in range(r-l):
                    save = matrix[l][l+i]
                    matrix[l][l+i] = matrix[r-i][l]
                    matrix[r-i][l] = matrix[r][r-i]
                    matrix[r][r-i] = matrix[l+i][r]
                    matrix[l+i][r] = save
                l += 1
                r -= 1
 
        # return sol_traverse()
