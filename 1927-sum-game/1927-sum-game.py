class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left = 0
        right = 0
        l = 0
        r = 0

        for i in range(half):
            if num[i] == '?':
                l += 1
            else:
                left += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                r += 1
            else:
                right += int(num[i])

        diff = left - right
        qdiff = r - l

        if qdiff % 2 != 0:
            return True

        return diff != 9 * qdiff // 2