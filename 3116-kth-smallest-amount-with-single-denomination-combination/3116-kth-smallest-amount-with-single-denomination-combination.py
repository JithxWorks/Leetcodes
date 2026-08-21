class Solution:
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        n = len(coins)

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                value = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        value = lcm(value, coins[i])

                        if value > x:
                            valid = False
                            break

                if not valid:
                    continue

                cnt = x // value

                if bits % 2 == 1:
                    total += cnt
                else:
                    total -= cnt

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left