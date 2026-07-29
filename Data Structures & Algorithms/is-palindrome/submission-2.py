class Solution:
    def isPalindrome(self, s: str) -> bool:
        not_alnum = []
        mod_str = s.replace(' ', '').lower()

        for i in range(len(mod_str)):
            if not mod_str[i].isalnum():
                not_alnum.append(mod_str[i])
        
        for c in not_alnum:
            mod_str = mod_str.replace(c, '')


        l,r = 0, len(mod_str)-1
        while l < r:
            if mod_str[l] != mod_str[r]:
                return False
            l += 1
            r -= 1
        
        return True