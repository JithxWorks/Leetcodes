class Solution:
    def numberOfSets(self, n, k):
        MOD = 1000000007

        dp = [[0] * (k + 1) for _ in range(n)]

        # 0 segments: always exactly 1 way
        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(1, n):
                # Add dp[i-1][j-1] to the possible
                # starting positions of the last segment
                prefix = (prefix + dp[i - 1][j - 1]) % MOD

                # Case 1: don't use point i
                # Case 2: last segment ends at i
                dp[i][j] = (dp[i - 1][j] + prefix) % MOD

        return dp[n - 1][k]