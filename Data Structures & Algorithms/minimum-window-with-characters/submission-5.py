class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        if len(s) < len(t):
            return ""
        
        letters = Counter(t)
        
        res = ''
        count = 0
        while res == '':
            l,r = 0, len(t) - 1 + count
            if r == len(s):
                break
            while r < len(s):
                d = Counter(s[l:r+1])
                c = 0
                if self.contains(dict(letters), dict(d)):
                    res = s[l:r+1]
                l += 1
                r += 1
            count += 1
        return res

    def contains(self,dict1,dict2):
        for k in dict1.keys():
            if k in dict2.keys():
                if dict2[k] < dict1[k]:
                    return False
            else:
                return False
        return True