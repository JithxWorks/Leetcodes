class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[i] = maximum number of characters
        # that can be matched exactly from word1[i:]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = suf[i + 1] + 1
                j -= 1
            else:
                suf[i] = suf[i + 1]

        ans = []
        pos = 0
        mismatch = False

        for j in range(m):
            while pos < n:

                # Exact match
                if word1[pos] == word2[j]:
                    ans.append(pos)
                    pos += 1
                    break

                # Use the one allowed mismatch
                remaining = m - j - 1

                if not mismatch and suf[pos + 1] >= remaining:
                    ans.append(pos)
                    pos += 1
                    mismatch = True
                    break

                pos += 1

            else:
                return []

        return ans