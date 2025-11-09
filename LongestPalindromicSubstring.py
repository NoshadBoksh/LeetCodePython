class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            odd_pal = expand_from_center(i, i)
            even_pal = expand_from_center(i, i + 1)

            curr_longest = odd_pal if len(odd_pal) > len(even_pal) else even_pal

            if len(curr_longest) > len(longest):
                longest = curr_longest

        return longest
