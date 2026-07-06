class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        while '' in words:
            words.remove('')
        return len(words[-1])