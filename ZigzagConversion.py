class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If only one row, the string stays the same
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array to store characters for each row
        rows = [''] * numRows

        # Start at the top row and move downward initially
        current_row = 0
        going_down = False

        # Loop through each character in the string
        for char in s:
            rows[current_row] += char

            # If we are at the top or bottom, reverse direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down depending on direction
            current_row += 1 if going_down else -1

        # Join all rows into one string
        return ''.join(rows)
