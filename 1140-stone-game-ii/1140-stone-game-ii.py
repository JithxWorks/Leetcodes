class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                newM = max(M, X)

                # Current player gets everything remaining
                # except what the opponent can get
                opponent = dp(i + X, newM)

                best = max(best, suffix[i] - opponent)

            memo[(i, M)] = best
            return best

        return dp(0, 1)