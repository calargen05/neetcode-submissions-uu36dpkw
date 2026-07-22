class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        #sorted_test = []
        nums.sort()
        def backtrack(i):
            if i == len(nums) and sol[:] not in res:
                res.append(sol[:])
                #sorted_test.append(sol[:])
                return

            for it in range(i,len(nums)):
                #sorted_sol = sorted(sol)
                if sol.copy() not in res:# and sorted_sol not in sorted_test:
                    res.append(sol[:])
                    #sorted_test.append(sorted_sol)

                sol.append(nums[it])
                backtrack(it+1)
                sol.pop()
        
        backtrack(0)
        return res