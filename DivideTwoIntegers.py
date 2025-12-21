class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # determine sign
        negative = (dividend < 0) != (divisor < 0)

        # work with positives
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        return max(INT_MIN, min(INT_MAX, result))
