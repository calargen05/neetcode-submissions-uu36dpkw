class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToInt(num):
            n, tens = 0, 0
            for i in range(len(num)-1,-1,-1):
                digit = ord(num[i]) - 48
                digit *= pow(10,tens)
                n += digit
                tens += 1
            return n
        
        return str(strToInt(num1) * strToInt(num2))