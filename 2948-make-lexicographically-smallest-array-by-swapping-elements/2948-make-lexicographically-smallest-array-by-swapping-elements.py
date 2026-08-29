class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        # Store (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find all values connected to this group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Original indices of this group
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            for i in range(len(indices)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans