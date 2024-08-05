class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        if l1==0:
            return word2
        if l2==0:
            return word1
        i,j=0,0
        merged=""
        while l1 and l2:
            merged+=word1[i]
            merged+=word2[j]
            l1-=1
            l2-=1
            i+=1
            j+=1
            
        if l1:
            merged+=word1[-l1:]
        if l2:
            merged+=word2[-l2:]
        return merged