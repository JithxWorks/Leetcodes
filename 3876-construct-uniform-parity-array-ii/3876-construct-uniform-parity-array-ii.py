class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)

        if mn % 2 == 0:
            return all(x % 2 == 0 for x in nums1)

        return True