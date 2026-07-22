class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        coord = []

        # get the zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    coord.append((i,j))
        
        for c in coord:
            self.setZeros(matrix, c[0], c[1])
        

    def setZeros(self, matrix, y, x):
        # set column
        for i in range(len(matrix)):
            matrix[i][x] = 0
        
        # set row
        for i in range(len(matrix[y])):
            matrix[y][i] = 0