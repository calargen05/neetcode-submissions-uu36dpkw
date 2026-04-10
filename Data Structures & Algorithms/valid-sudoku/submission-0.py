class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashrow = defaultdict(set)
        hashcol = defaultdict(set)
        hashbox = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in hashrow[row] or board[row][col] in hashcol[col] or board[row][col] in hashbox[(row // 3, col // 3)]:
                    return False
                
                hashrow[row].add(board[row][col])
                hashcol[col].add(board[row][col])
                hashbox[(row//3,col//3)].add(board[row][col])
        
        return True