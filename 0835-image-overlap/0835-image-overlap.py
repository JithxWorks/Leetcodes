class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = []
        ones2 = []

        # Store positions of all 1s
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))

                if img2[i][j] == 1:
                    ones2.append((i, j))

        count = {}

        # Count translations
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)

                if shift not in count:
                    count[shift] = 0

                count[shift] += 1

        # Maximum number of overlapping 1s
        if not count:
            return 0

        return max(count.values())