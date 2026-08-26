class Solution:
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            if ones == k:
                while s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                if ans == "" or len(curr) < len(ans):
                    ans = curr
                elif len(curr) == len(ans) and curr < ans:
                    ans = curr

                ones -= 1
                left += 1

        return ans