class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        # node:
        # (left_char, right_char, prefix, suffix, maximum, length)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc, lrc, lp, ls, lm, llen = a
            rc, rrc, rp, rs, rm, rlen = b

            prefix = lp
            suffix = rs
            maximum = max(lm, rm)

            if lrc == rc:
                maximum = max(maximum, ls + rp)

                # Entire left segment is same character
                if lp == llen:
                    prefix = llen + rp

                # Entire right segment is same character
                if rp == rlen:
                    suffix = rlen + ls

            return (
                lc,
                rrc,
                prefix,
                suffix,
                maximum,
                llen + rlen
            )

        def build(node, left, right):
            if left == right:
                tree[node] = (
                    s[left],   # left char
                    s[left],   # right char
                    1,         # prefix
                    1,         # suffix
                    1,         # maximum
                    1          # length
                )
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = (
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for i in range(len(queryCharacters)):
            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            answer.append(tree[1][4])

        return answer