class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,e in enumerate(nums):
            if e in dict1:
                return [i, dict1[e]]
            dict1[target-e] = i