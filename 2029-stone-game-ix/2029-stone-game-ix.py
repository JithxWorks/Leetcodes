class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        a, b, c = cnt

        # If there are no stones with remainder 1 or 2,
        # Alice cannot avoid making the sum divisible by 3.
        if b == 0 and c == 0:
            return False

        # If the number of remainder-0 stones is even,
        # the game effectively depends on whether one side
        # of remainders 1/2 has enough stones.
        if a % 2 == 0:
            return b > 0 and c > 0

        # When remainder-0 count is odd
        return abs(b - c) > 2