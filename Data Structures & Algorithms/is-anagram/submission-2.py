class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = ''.join(sorted(s))
        new_t = ''.join(sorted(t))

        if new_t == new_s:
            return True
        return False