class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr, sol = [], []
        def isPalindrome(string):
            rev = list(string)
            rev.reverse()
            rev = ''.join(rev)
            return rev == string

        def dfs(i):
            if i == len(s):
                sol.append(curr[:])
                return
            
            for it in range(i+1, len(s)+1):
                substr = s[i:it]

                if isPalindrome(substr):
                    curr.append(substr)
                    dfs(it)
                    curr.pop()
        
        dfs(0)
        return sol
                    