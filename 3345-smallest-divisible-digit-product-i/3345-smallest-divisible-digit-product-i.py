class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            product = 1
            temp = n

            if temp == 0:
                product = 0
            else:
                while temp > 0:
                    product *= temp % 10
                    temp //= 10

            if product % t == 0:
                return n

            n += 1