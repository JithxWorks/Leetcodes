class Solution:
    def longestSubsequence(self, nums):
        xor = 0
        nonzero = False

        for x in nums:
            xor ^= x
            if x != 0:
                nonzero = True

        if xor != 0:
            return len(nums)

        if nonzero:
            return len(nums) - 1

        return 0