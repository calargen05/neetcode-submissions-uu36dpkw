class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        candidates.sort()

        def backtrack(i):
            if sum(sol) == target:
                res.append(sol.copy())
                return
            
            if sum(sol) > target:
                return
            
            for it in range(i,len(candidates)):
                if candidates[it] == candidates[it-1] and it > i:
                    continue
                sol.append(candidates[it])
                backtrack(it+1)
                sol.pop()

        backtrack(0)
        return res