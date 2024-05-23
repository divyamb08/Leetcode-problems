class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=start:
                start = d[s[i]]+1
            else:
                res = max(res, i-start+1)
            d[s[i]]=i
        return res