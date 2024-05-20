class Solution:
    def isPalindrome(self, s: str) -> bool:
        st= ""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        a=0
        b=len(st)-1
        while(b>a):
            if st[a]!=st[b]:
                return False
            a+=1
            b-=1
        return True