class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(n):
            sum = 0
            while n > 0:
                r = n % 10
                sum += r **2
                n = n//10
            return sum
        if n == 1:
            return True
        for i in range(70):
            n = sqr(n)
            if n == 1:
                return True
        return False

        def sqr(n):
            sum = 0
            while n > 0:
                r = num % 10
                sum += r **2
                n = n//10
            return sum
