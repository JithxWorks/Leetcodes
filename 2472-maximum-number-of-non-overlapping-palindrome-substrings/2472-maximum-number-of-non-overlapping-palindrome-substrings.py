class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)

        # pal[l][r] tells whether s[l:r+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length <= 2:
                        pal[l][r] = True
                    else:
                        pal[l][r] = pal[l + 1][r - 1]

        # dp[i] = maximum number of palindromes
        # using first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't use a palindrome ending here
            dp[i] = dp[i - 1]

            # Try every palindrome ending at i - 1
            for j in range(i - k + 1):
                if i - j >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]