class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums)-1
        while end>=st:
            mid = (st+end)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                st=mid+1
                continue
            else:
                end = mid
                continue
        return -1
