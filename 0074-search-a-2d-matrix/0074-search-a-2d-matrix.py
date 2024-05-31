class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Check if the target is out of the matrix's range
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        st = 0
        end = len(matrix[0]) - 1
        k = 0
        
        # Find the row where the target might be located
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                k = i
                break
        
        # Binary search within the row
        while end >= st:
            mid = (st + end) // 2
            if matrix[k][mid] == target:
                return True
            elif matrix[k][mid] < target:
                st = mid + 1
            else:
                end = mid - 1
        
        return False