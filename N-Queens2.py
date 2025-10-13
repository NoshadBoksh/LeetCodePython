class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0

        # sets to track columns and diagonals already under attack
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        def backtrack(r):
            # base case: all rows filled
            if r == n:
                self.count += 1
                return

            for c in range(n):
                # skip if column or diagonal already under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # choose
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                # explore next row
                backtrack(r + 1)

                # unchoose (backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return self.count
