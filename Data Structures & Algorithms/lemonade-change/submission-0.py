class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = {}
        bank[5] = 0
        bank[10] = 0

        for b in bills:
            if b in bank:
                bank[b] += 1
            else:
                bank[b] = 1
            
            if b == 10:
                if bank[5] and bank[5] >= 1:
                    bank[5] -= 1
                else:
                    return False
            if b == 20:
                if bank[5] and bank[5] >= 1 and bank[10] and bank[10] >= 1:
                    bank[5] -= 1
                    bank[10] -= 1
                elif bank[5] and bank[5] >= 3:
                    bank[5] -= 3
                else:
                    return False
        
        return True
