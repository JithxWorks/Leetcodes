class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Option 1: Remove everything from the front up to right
        front = right + 1

        # Option 2: Remove everything from the back up to left
        back = n - left

        # Option 3: Remove one from front and one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)