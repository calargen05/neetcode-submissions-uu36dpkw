class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # variable declaration
        l, r = 0, len(matrix) - 1
        row = 0
        
        # loop to get the row 
        while l <= r:
            m = (l+r)//2
            
            if matrix[m][0] <= target and target <= matrix[m][len(matrix[m])-1]:
                row = m
                break
            elif matrix[m][0] < target:
                l = m+1
            else:
                r = m-1
        
        # resetting the variables to start the second binary search
        l, r = 0, len(matrix[row]) - 1

        # second loop to determine whether or not the target is in the matrix
        while l <= r:
            m = (l+r)//2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m+1
            else:
                r = m-1
        return False