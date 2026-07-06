class Solution:
    def scoreOfString(self, s: str) -> int:
        equations = []

        for i in range(0,len(s)-1):
            equations.append(abs(ord(s[i])-ord(s[i+1])))
        
        return sum(equations)