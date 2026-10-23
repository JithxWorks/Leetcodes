class Solution(object):
    def sortPermutation(self, nums):
        ans = 0
        found = False

        for i in range(len(nums)):
            if nums[i] != i:
                if not found:
                    ans = nums[i]
                    found = True
                else:
                    ans &= nums[i]

        return ans
