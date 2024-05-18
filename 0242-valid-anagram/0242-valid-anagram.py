from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in d:
                d[j] -= 1
                if d[j] == 0:
                    del d[j]
            else:
                return False
        return len(d) == 0