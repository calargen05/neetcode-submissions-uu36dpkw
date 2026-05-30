class Solution:
    def myPow(self, x: float, n: int) -> float:
        original = x
        if n > 0:
            for i in range(1,n):
                x = x * original
            return x
        elif n < 0:
            x = 1
            for i in range(abs(n)):
                x = x / original
            return x
        else:
            return 1