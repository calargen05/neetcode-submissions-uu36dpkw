class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        def backtrack(i):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for it in range(len(nums)):
                if nums[it] in sol:
                    continue

                sol.append(nums[it])
                backtrack(it+1)
                sol.pop()
        
        backtrack(0)
        return res