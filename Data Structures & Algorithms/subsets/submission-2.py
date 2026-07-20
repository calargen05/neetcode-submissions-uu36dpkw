'''
FIRST SOLUTION

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Helper
        def backtrack(start, current):
            # append the current list (gets the empty list as well)
            res.append(list(current))
            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                # include nums[i] in the current subset and then move forward
                current.append(nums[i])
                backtrack(i+1, current)
                # then exclude nums[i] from the current subset
                current.pop()
        
        nums.sort()
        res = []
        backtrack(0,[])
        return res

'''

# SECOND SOLUTION
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # dont append nums[i]
            backtrack(i+1)

            # append nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res