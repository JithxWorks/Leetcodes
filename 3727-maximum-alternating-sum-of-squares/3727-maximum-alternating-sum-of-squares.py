class Solution(object):
    def maxAlternatingSum(self, nums):
        nums = sorted(x * x for x in nums)

        n = len(nums)
        ans = 0

        for i in range(n):
            if i >= n // 2:
                ans += nums[i]
            else:
                ans -= nums[i]

        return ans