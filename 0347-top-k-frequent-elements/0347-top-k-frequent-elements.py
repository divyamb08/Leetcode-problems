from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        ar = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            ar[freq].append(num)
        res = []
        for i in range(len(ar) - 1, 0, -1):
            for num in ar[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
                if k == 0:
                    break
            if k == 0:
                break
        
        return res