class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        for p in details:
            if int(p[11:13]) > 60:
                senior += 1
        
        return senior