class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s= ''.join(filter(str.isalnum,s))
        s=s.lower()
        if s==s[::-1]:
            return True
        else :
            return False 