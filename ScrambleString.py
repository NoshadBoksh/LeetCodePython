class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # memoization cache to avoid recomputation
        memo = {}

        def dfs(a, b):
            # if we've seen this pair before, return cached result
            if (a, b) in memo:
                return memo[(a, b)]

            # if strings are identical, they are trivially scrambled versions
            if a == b:
                memo[(a, b)] = True
                return True

            # if sorted characters don't match, impossible to be scrambled
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)
            # try every possible split position
            for i in range(1, n):
                # case 1: no swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # case 2: swapped
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
