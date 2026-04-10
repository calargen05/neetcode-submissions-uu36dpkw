class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = ''
        for char in s:
            if self.opening(char):
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if not self.closing_char(top, char):
                        return False
                else:
                    return False
        return not stack

    
    def opening(self, ch: str) -> bool:
        if ch == '(' or ch == '[' or ch == '{':
            return True
        return False
    
    def closing_char(self, ch1: str, ch2: str) -> bool:
        if ch1 == '(' and ch2 == ')':
            return True
        elif ch1 == '[' and ch2 == ']':
            return True
        elif ch1 == '{' and ch2 == '}':
            return True
        else:
            return False