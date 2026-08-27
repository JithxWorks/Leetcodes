class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - 97

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                break
        else:
            i = len(target) - 1

            while i >= 0:
                x = ord(ans[i]) - 97
                cnt[x] += 1
                ans.pop()

                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + 97))
                        cnt[c] -= 1

                        for j in range(26):
                            ans.extend([chr(j + 97)] * cnt[j])

                        return ''.join(ans)

                i -= 1

            return ""

        while i >= 0:
            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    ans.append(chr(c + 97))
                    cnt[c] -= 1

                    for j in range(26):
                        ans.extend([chr(j + 97)] * cnt[j])

                    return ''.join(ans)

            if i > 0:
                cnt[ord(ans[-1]) - 97] += 1
                ans.pop()

            i -= 1

        return ""