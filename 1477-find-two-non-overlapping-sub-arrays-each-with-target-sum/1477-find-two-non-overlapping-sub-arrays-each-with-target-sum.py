class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        best = [float('inf')] * n

        left = 0
        curr = 0
        ans = float('inf')

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                # Previous non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Best subarray ending at or before right
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                if right > 0:
                    best[right] = best[right - 1]

        if ans == float('inf'):
            return -1

        return ans