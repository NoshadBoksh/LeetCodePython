class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        
        # dp[i][j] = number of ways s[:i] can form t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty t
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]
