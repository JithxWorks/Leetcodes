class Solution:
    def totalNumbers(self, digits):
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            need = [a, b, c]
            available = digits[:]

            possible = True

            for d in need:
                if d in available:
                    available.remove(d)
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count