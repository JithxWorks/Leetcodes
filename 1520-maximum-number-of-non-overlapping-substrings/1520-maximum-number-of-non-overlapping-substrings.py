class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i in range(n):
            c = ord(s[i]) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try to create a valid interval from each character's first occurrence
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]

            j = left
            valid = True

            while j <= right:
                x = ord(s[j]) - ord('a')

                # This character appeared before our left boundary.
                # So we cannot make a valid substring starting at left.
                if first[x] < left:
                    valid = False
                    break

                # We must include all occurrences of this character.
                right = max(right, last[x])

                j += 1

            if valid:
                intervals.append((right, left))

        # Sort by ending position
        intervals.sort()

        ans = []
        prev_end = -1

        for right, left in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans