class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If character already in set, move left pointer to remove duplicates
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character to set
            char_set.add(s[right])

            # Update max_length if needed
            max_length = max(max_length, right - left + 1)

        return max_length
