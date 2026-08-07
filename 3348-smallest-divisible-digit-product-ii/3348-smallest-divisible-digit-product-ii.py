class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        a = b = c = d = 0
        tt = t
        for p in (2, 3, 5, 7):
            while tt % p == 0:
                tt //= p
                if p == 2: a += 1
                elif p == 3: b += 1
                elif p == 5: c += 1
                else: d += 1
        if tt != 1:
            return "-1"

        # digit -> (exp2, exp3, is5, is7)
        DIGIT = [
            (0,0,0,0), (0,0,0,0), (1,0,0,0), (0,1,0,0), (2,0,0,0),
            (0,0,1,0), (1,1,0,0), (0,0,0,1), (3,0,0,0), (0,2,0,0),
        ]

        A, B = a, b
        minslots = [[0]*(B+1) for _ in range(A+1)]
        for ra in range(A+1):
            row = minslots[ra]
            for rb in range(B+1):
                best = ra + rb
                for k3 in range(0, ra + rb + 1):
                    rem_a = ra - k3
                    if rem_a < 0: rem_a = 0
                    k1 = (rem_a + 2)//3
                    rem_b = rb - k3
                    if rem_b < 0: rem_b = 0
                    k2 = (rem_b + 1)//2
                    total = k3 + k1 + k2
                    if total < best:
                        best = total
                row[rb] = best

        def feasible(rem_slots, ra, rb, rc, rd):
            if rc + rd > rem_slots:
                return False
            rem2 = rem_slots - rc - rd
            return minslots[ra][rb] <= rem2

        def fill(length, ra, rb, rc, rd):
            res = []
            append = res.append
            for i in range(length):
                rem_after = length - i - 1
                for e in range(1, 10):
                    e2, e3, e5, e7 = DIGIT[e]
                    nra = ra - e2
                    if nra < 0: nra = 0
                    nrb = rb - e3
                    if nrb < 0: nrb = 0
                    nrc = rc - e5
                    if nrc < 0: nrc = 0
                    nrd = rd - e7
                    if nrd < 0: nrd = 0
                    if feasible(rem_after, nra, nrb, nrc, nrd):
                        append(str(e))
                        ra, rb, rc, rd = nra, nrb, nrc, nrd
                        break
            return res

        n = len(num)
        zero_pos = num.find('0')
        if zero_pos == -1:
            zero_pos = n

        prefix_a = [0]*(n+1)
        prefix_b = [0]*(n+1)
        prefix_c = [0]*(n+1)
        prefix_d = [0]*(n+1)
        for i in range(n):
            dv = int(num[i])
            e2, e3, e5, e7 = DIGIT[dv]
            prefix_a[i+1] = prefix_a[i] + e2
            prefix_b[i+1] = prefix_b[i] + e3
            prefix_c[i+1] = prefix_c[i] + e5
            prefix_d[i+1] = prefix_d[i] + e7

        if zero_pos == n:
            if prefix_a[n] >= a and prefix_b[n] >= b and prefix_c[n] >= c and prefix_d[n] >= d:
                return num

        max_p = min(n-1, zero_pos)
        answer = None
        for p in range(max_p, -1, -1):
            start_digit = int(num[p]) + 1
            pa, pb, pc, pd = prefix_a[p], prefix_b[p], prefix_c[p], prefix_d[p]
            rem_slots = n - 1 - p
            for e in range(start_digit, 10):
                e2, e3, e5, e7 = DIGIT[e]
                used_a = pa + e2
                used_b = pb + e3
                used_c = pc + e5
                used_d = pd + e7
                ra = a - used_a
                if ra < 0: ra = 0
                rb = b - used_b
                if rb < 0: rb = 0
                rc = c - used_c
                if rc < 0: rc = 0
                rd = d - used_d
                if rd < 0: rd = 0
                if feasible(rem_slots, ra, rb, rc, rd):
                    suffix = fill(rem_slots, ra, rb, rc, rd)
                    answer = num[:p] + str(e) + ''.join(suffix)
                    break
            if answer is not None:
                break

        if answer is not None:
            return answer

        L_min = c + d + minslots[a][b]
        L = max(n+1, L_min)
        digits = fill(L, a, b, c, d)
        return ''.join(digits)