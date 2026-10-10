
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        operations = sum(max(0, d - limit) for d in diff)
        ans = sum(min(d, limit) ** 2 for d in diff)

        remaining = k - operations

        for d in diff:
            if d > limit:
                ans += 0

        ans -= remaining * (2 * limit - 1)

        return ans
