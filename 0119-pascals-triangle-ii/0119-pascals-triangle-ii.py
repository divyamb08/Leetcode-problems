class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        
        for row in range(2, rowIndex + 1):
            for idx in reversed(range(1, row)):
                ans[idx] += ans[idx - 1]
        
        return ans