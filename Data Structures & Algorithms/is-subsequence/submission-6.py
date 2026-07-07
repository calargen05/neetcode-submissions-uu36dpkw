class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = s
        s2 = t
        count = 0
        seen = {}

        letters = {}
        for l in s1:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1

        for l in s2:
            if count < len(s1):
                if s1[count] == l:    
                    if s1[count] in seen:
                        seen[l] += 1
                    else:
                        seen[l] = 1
                    count += 1
            else:
                break
        
        return letters == seen