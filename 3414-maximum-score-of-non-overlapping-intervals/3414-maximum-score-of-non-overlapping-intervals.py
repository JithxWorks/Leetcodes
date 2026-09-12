
class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Add original index
        arr = []
        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # Find first interval whose left > current right
        def find_next(r):
            lo = 0
            hi = n

            while lo < hi:
                mid = (lo + hi) // 2

                if starts[mid] <= r:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        # Precompute next interval
        nxt = [0] * n

        for i in range(n):
            nxt[i] = find_next(arr[i][1])

        # dp[i][k]:
        # best (score, indices) using intervals from i onward
        # with at most k intervals
        dp = [[None] * 5 for _ in range(n + 1)]

        # IMPORTANT:
        # With 0 intervals allowed, score is 0 and indices are empty
        for i in range(n + 1):
            dp[i][0] = (0, ())

        # At the end, score is 0 for every k
        for k in range(1, 5):
            dp[n][k] = (0, ())

        def better(a, b):
            if a[0] > b[0]:
                return a
            if a[0] < b[0]:
                return b

            # Same score -> lexicographically smaller indices
            if a[1] < b[1]:
                return a

            return b

        # Fill DP backwards
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Option 1: Skip current interval
                skip = dp[i + 1][k]

                # Option 2: Take current interval
                j = nxt[i]

                take_score = arr[i][2] + dp[j][k - 1][0]

                take_indices = tuple(
                    sorted((arr[i][3],) + dp[j][k - 1][1])
                )

                take = (take_score, take_indices)

                dp[i][k] = better(skip, take)

        return list(dp[0][4][1])

