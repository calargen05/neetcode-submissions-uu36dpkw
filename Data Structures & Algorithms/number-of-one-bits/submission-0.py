class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(str(bin(n))[2:])
        print(str(bin(n)))
        return c['1']