class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # is valid by rows
        for r in range(9):
            state = set()
            for c in range(9):
                ch = board[r][c]
                if(ch == "."):
                    continue
                elif ch in state:
                    return False
                else:
                    state.add(ch)

        # is valid by cols
        for c in range(9):
            state = set()
            for r in range(9):
                ch = board[r][c]
                if(ch == "."):
                    continue
                elif ch in state:
                    return False
                else:
                    state.add(ch)

        # is valid by squares
        for i in range(3):
            for j in range(3):
                state = set()
                for r in range(3):
                    for c in range(3):
                        ch = board[3*i + r][3*j + c]
                        if(ch == "."):
                            continue
                        elif ch in state:
                            return False
                        else:
                            state.add(ch)

        return True
        # Runtime: O(n^2)
        # Space: O(n)