class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW = 0
        heightSize = len(height)
        st = 0
        end = heightSize-1
        while end>st:
            maxW = max(maxW, (min(height[st],height[end])*(end-st)))
            if height[st]>height[end]:
                end-=1
                continue
            elif height[st]<height[end]:
                st+=1
            else:
                st+=1
                end-=1
        return maxW