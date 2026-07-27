class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def recursion(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = recursion(i+1) + recursion(i+2)
            return cache[i]
        
        return recursion(0)