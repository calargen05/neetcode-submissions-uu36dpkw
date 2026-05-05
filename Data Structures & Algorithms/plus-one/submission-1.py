class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for n in digits:
            s += str(n)
        
        add = int(s) + 1
        add = str(add)
        res = []
        for d in add:
            res.append(int(d))
        
        return res