class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in '([{':
                ls.append(char)
            else:
                if not ls or ls.pop() != bracket_map[char]:
                    return False
        
        return len(ls) == 0