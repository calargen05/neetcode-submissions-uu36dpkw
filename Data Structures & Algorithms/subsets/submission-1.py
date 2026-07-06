class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Helper
        def backtrack(start, current):
            res.append(list(current))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        
        nums.sort()
        res = []
        backtrack(0,[])
        return res