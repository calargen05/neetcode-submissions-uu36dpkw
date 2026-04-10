class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers to read the string
        a, b = 0, len(s)-1

        # loop to calculate whether or not the string is a palindrome
        while a < b:
            if Solution.alphaNum(self, s[a]) == False:
                a += 1
            elif Solution.alphaNum(self, s[b]) == False:
                b -= 1
            elif s[a].lower() != s[b].lower():
                return False
            else:
                a += 1
                b -= 1
        
        return True

    
    def alphaNum(self, c: str) -> bool:
        if (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')):
            return True
        return False