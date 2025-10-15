class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()  # remove leading/trailing spaces
        if not s:
            return False

        def isInteger(s):
            if not s:
                return False
            if s[0] in '+-':
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in '+-':
                s = s[1:]
            if '.' not in s:
                return False
            integer_part, dot, fractional_part = s.partition('.')
            # at least one of integer_part or fractional_part must be digits
            if integer_part == '' and fractional_part == '':
                return False
            if integer_part and not integer_part.isdigit():
                return False
            if fractional_part and not fractional_part.isdigit():
                return False
            return True

        # check for exponent 'e' or 'E'
        if 'e' in s or 'E' in s:
            parts = s.split('e') if 'e' in s else s.split('E')
            if len(parts) != 2:
                return False
            base, exponent = parts
            return (isInteger(base) or isDecimal(base)) and isInteger(exponent)
        else:
            return isInteger(s) or isDecimal(s)
