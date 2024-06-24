class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return True
        flag = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                if flag == 0:
                    flag = 1
                    continue
                if flag==-1:
                    return False
                continue
            if nums[i]<nums[i-1]:
                if flag == 0:
                    flag = -1
                if flag == 1:
                    return False
                continue
        return True