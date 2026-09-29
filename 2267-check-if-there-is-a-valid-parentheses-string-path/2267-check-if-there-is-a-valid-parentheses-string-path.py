
class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # First cell must be '('
        if grid[0][0] == ')':
            return False

        # dp[j] = set of possible balances at current row
        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                current = set()

                # Come from above
                if i > 0:
                    current.update(dp[j])

                # Come from left
                if j > 0:
                    current.update(dp[j - 1])

                # Calculate new balance
                if grid[i][j] == '(':
                    current = {balance + 1 for balance in current}
                else:
                    current = {
                        balance - 1
                        for balance in current
                        if balance > 0
                    }

                dp[j] = current

        return 0 in dp[n - 1]

