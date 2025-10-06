class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # base index to calculate valid substring lengths
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # push index of '('
            else:
                stack.pop()  # pop the last '(' index
                if not stack:
                    # if stack is empty, push current index as base
                    stack.append(i)
                else:
                    # length of current valid substring
                    max_len = max(max_len, i - stack[-1])

        return max_len
