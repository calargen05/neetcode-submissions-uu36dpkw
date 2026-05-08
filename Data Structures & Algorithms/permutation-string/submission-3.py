class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1
        seen = {}
        correct = {}

        for c in s1:
            if c in correct:
                correct[c] += 1
            else:
                correct[c] = 1

        while r < len(s2):
            for i in range(l,r+1):
                if s2[i] in s1:
                    if s2[i] in seen:
                        seen[s2[i]] += 1
                    else:
                        seen[s2[i]] = 1
            if correct == seen:
                return True
            seen.clear()
            l+=1
            r+=1
        
        return False