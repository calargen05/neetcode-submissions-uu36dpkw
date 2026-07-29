class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        num_map = {
            2 : ['a','b','c'],
            3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r','s'],
            8 : ['t','u','v'],
            9 : ['w','x','y','z']
        }

        combs = []
        curr = []
        def dfs(i):
            if len(curr) == len(digits):
                combs.append(''.join(curr))
                return
            
            for it in range(len(num_map[int(digits[i])])):
                curr.append(num_map[int(digits[i])][it])
                dfs(i+1)
                curr.pop()
        
        dfs(0)
        return combs