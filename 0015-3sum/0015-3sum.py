class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            st = i+1
            end = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while(end>st):
                if (nums[i]+nums[st]+nums[end]==0):
                    res.append([nums[i],nums[st],nums[end]])
                    while st < end and nums[st] == nums[st+1]:
                        st += 1
                    while st < end and nums[end] == nums[end-1]:
                        end -= 1
                    st += 1
                    end -= 1
                elif (nums[i]+nums[st]+nums[end]>0):
                    end-=1
                    continue
                elif (nums[i]+nums[st]+nums[end]<0):
                    st+=1
                    continue

        return res