class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        given
        - row in ascending
        - combined row ascending
        asked
        - find target
        apporahc:
        - binary search, treat matrix as array
        """

        ROW_COUNT = len(matrix)
        COL_COUNT = len(matrix[0])
        n = ROW_COUNT * COL_COUNT

        def num_to_cell(num):
            return (num//COL_COUNT, num%COL_COUNT)
        
        l, r = 0, n-1
        while l <= r:
            m = l + (r - l) // 2
            row, col = num_to_cell(m)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1

        return False
