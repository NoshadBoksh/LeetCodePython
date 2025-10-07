class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, ch):
            # Check if ch can be placed in board[r][c]
            for i in range(9):
                # Check row and column
                if board[r][i] == ch or board[i][c] == ch:
                    return False
                # Check 3x3 box
                box_row = 3 * (r // 3) + i // 3
                box_col = 3 * (c // 3) + i % 3
                if board[box_row][box_col] == ch:
                    return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in map(str, range(1, 10)):  # Try digits 1-9
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = '.'  # Undo choice
                        return False  # No valid number found
            return True  # All cells filled

        backtrack()
