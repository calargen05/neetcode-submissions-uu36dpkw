class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bank = {}
        for n in nums:
            if n in bank.keys():
                bank[n] += 1
            else:
                bank[n] = 1
        
        for k in bank.keys():
            if bank[k] == 1:
                return k