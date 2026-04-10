class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        smallest = 200
        for s in strs:
            if len(s) < smallest:
                smallest = len(s)

        cp = ""
        for i in range(smallest):
            c = strs[0][i]
            for j in range(len(strs)):
                if c != strs[j][i]:
                    return cp
            cp += c
        
        return cp