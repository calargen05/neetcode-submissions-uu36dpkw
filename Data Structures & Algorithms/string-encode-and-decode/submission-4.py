class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            output = output + str(len(i)) + '#' + i
        return output


    def decode(self, s: str) -> List[str]:
        output, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            l = int(s[i:j])
            output.append(s[j+1 : j+1+l])
            i = j+1+l
        return output


