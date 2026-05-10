class Solution:
    def mySqrt(self, x: int) -> int:
        w = 1
        while w ** 2 <= x:
            w += 1
        return w - 1