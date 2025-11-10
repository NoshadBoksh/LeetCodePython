class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine sign
        sign = -1 if x < 0 else 1
        x *= sign  # make x positive for easier reversal
        
        # Reverse digits
        rev = 0
        while x != 0:
            pop = x % 10       # take the last digit
            x //= 10           # remove last digit
            rev = rev * 10 + pop  # append digit to reversed number
        
        # Apply sign
        rev *= sign
        
        # Check for overflow
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        
        return rev
