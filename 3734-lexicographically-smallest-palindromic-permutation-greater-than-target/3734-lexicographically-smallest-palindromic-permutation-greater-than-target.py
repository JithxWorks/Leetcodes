class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # More than one odd count -> impossible
        odd = -1

        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        # Half counts
        half = [x // 2 for x in cnt]
        m = n // 2

        # --------------------------------------------------
        # Try to make the left half exactly target[:m]
        # --------------------------------------------------
        possible = True

        for i in range(m):
            x = ord(target[i]) - 97

            if half[x] == 0:
                possible = False
                break

            half[x] -= 1

        # If exact left half is possible, check its palindrome
        if possible:
            left = target[:m]

            if n % 2:
                middle = chr(odd + 97)
            else:
                middle = ""

            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate

        # --------------------------------------------------
        # Backtrack from right to left.
        #
        # Find the rightmost position where we can increase
        # target[i], while keeping target[:i] unchanged.
        # --------------------------------------------------

        # Restore the counts
        half = [x // 2 for x in cnt]

        # Remove characters used by target[:m]
        for i in range(m):
            half[ord(target[i]) - 97] -= 1

        # If a count became negative, exact target prefix
        # cannot be formed.
        #
        # Instead, build counts progressively below.
        half = [x // 2 for x in cnt]

        # Number of characters from target prefix that are usable
        used = [0] * 26

        for i in range(m):
            c = ord(target[i]) - 97

            if half[c] == 0:
                break

            half[c] -= 1
            used[c] += 1
        else:
            # The entire target left half was possible.
            # We already checked equality case above.
            pass

        # --------------------------------------------------
        # Simpler robust method:
        # Construct answer position-by-position using DFS.
        # n <= 300 and only 26 characters.
        # --------------------------------------------------

        half = [x // 2 for x in cnt]
        prefix = []

        def build_max():
            """Largest possible palindrome from current prefix."""
            left = ''.join(prefix)

            for c in range(25, -1, -1):
                left += chr(c + 97) * half[c]

            if n % 2:
                mid = chr(odd + 97)
            else:
                mid = ""

            return left + mid + left[::-1]

        def dfs(pos):
            if pos == m:
                left = ''.join(prefix)

                if n % 2:
                    mid = chr(odd + 97)
                else:
                    mid = ""

                ans = left + mid + left[::-1]

                if ans > target:
                    return ans

                return None

            # Try characters from smallest to largest.
            for c in range(26):
                if half[c] == 0:
                    continue

                ch = chr(c + 97)

                half[c] -= 1
                prefix.append(ch)

                # The largest completion from here must be > target.
                # Otherwise no completion with this prefix can work.
                if build_max() > target:
                    result = dfs(pos + 1)

                    if result is not None:
                        return result

                prefix.pop()
                half[c] += 1

            return None

        result = dfs(0)

        return result if result is not None else ""