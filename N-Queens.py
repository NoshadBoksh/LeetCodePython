class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()        # columns where queens are placed
        posDiag = set()     # positive diagonals (r + c)
        negDiag = set()     # negative diagonals (r - c)

        def backtrack(r):
            if r == n:
                # convert each row to string and add to result
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # move to next row
                backtrack(r + 1)

                # backtrack (remove queen)
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res
