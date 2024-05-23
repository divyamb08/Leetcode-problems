class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = collections.defaultdict(int)
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count[s[r]]
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)

        return res
        