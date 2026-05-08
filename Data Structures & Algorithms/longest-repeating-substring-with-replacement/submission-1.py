class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1


        l,r = 0, 1
        lengths = []
        chars = {}


        while r < len(s):
            if chars:
                if s[r] in chars:
                    chars[s[r]] += 1
                else:
                    chars[s[r]] = 1
                r += 1

                max_key, max_val = max(chars.items(), key=lambda item: item[1])

                if k >= (r-l) - max_val:
                    lengths.append(r-l)
                else:
                    chars[s[l]] -= 1
                    l += 1
            else:
                chars[s[l]] = 1
                
        
        return max(lengths)