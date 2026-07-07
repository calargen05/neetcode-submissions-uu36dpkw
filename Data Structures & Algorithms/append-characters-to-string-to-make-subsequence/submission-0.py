class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t == "":
            return 0
        if s == "":
            return len(t)

        sub = ""
        ps, pt = 0, 0

        count = 0

        while ps < len(s):
            if s[ps] == t[pt]:
                sub += s[ps]
                pt += 1
            if len(sub) == len(t):
                break
            ps += 1
        
        return len(t) - len(sub)