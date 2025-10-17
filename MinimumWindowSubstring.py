class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter

        # Step 1: Count all characters needed from t
        need = Counter(t)
        have = {}
        need_count = len(need)  # how many unique characters we need to match
        have_count = 0  # how many unique characters we currently match

        # Step 2: Initialize window pointers and result variables
        res = [-1, -1]
        res_len = float("inf")
        left = 0

        # Step 3: Expand the right pointer to include characters
        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1

            # if the count of current char matches the required count, increment have_count
            if c in need and have[c] == need[c]:
                have_count += 1

            # Step 4: Contract window when we have all required chars
            while have_count == need_count:
                # update result if current window is smaller
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # try to shrink from the left
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    have_count -= 1
                left += 1

        # Step 5: Return the substring if found
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
