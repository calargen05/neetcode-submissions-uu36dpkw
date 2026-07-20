class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sub = [], []
        n = len(nums)
        def backtrack(i):
            if sum(sub) == target:
                res.append(sub.copy())
                return
            
            if sum(sub) > target:
                return
            
            for it in range(i,n):
                sub.append(nums[it])
                backtrack(it)
                sub.pop()
        
        backtrack(0)
        return res