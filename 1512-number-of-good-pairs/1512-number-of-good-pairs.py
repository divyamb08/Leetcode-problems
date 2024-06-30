class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        res = 0
        for i in d:
            if len(d[i])<2:
                continue
            for j in range(len(d[i])):
                if j+1<len(d[i]):
                    for k in range(j+1, len(d[i])):
                        res+=1
                        
        return res
                    
                