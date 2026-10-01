class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curr, sol = [], []
        def dfs(row):
            if row == n:
                sol.append(curr[:])
                return

            for col in range(n):
                placeholder = ['.']*n
                placeholder = ''.join(placeholder)
                curr.append(placeholder)
                if valid_position(row, col, curr):
                    curr.pop()
                    place_queen(col, curr)
                    dfs(row+1)
                    remove_queen(curr)
                else:
                    curr.pop()
        

        def valid_position(row, col, lst):
            # I need to check vertical, horizontal, and diagonals
            # horizontal
            if row > n-1 or col > n-1:
                return False

            for c in range(n):
                if curr[row][c] == 'Q':
                    return False
            
            # vertical
            for r in range(len(curr)):
                if curr[r][col] == 'Q':
                    return False
            
            # diagonal
            # up-left
            i,j = row, col
            while i >= 0 and j >= 0:
                if curr[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # up-right
            i,j = row, col
            while i >= 0 and j < n:
                if curr[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            # down-left
            i,j = row, col
            while i < len(curr) and j >= 0:
                if curr[i][j] == 'Q':
                    return False
                i += 1
                j -= 1
            
            # down-right
            i,j = row, col
            while i < len(curr) and j < n:
                if curr[i][j] == 'Q':
                    return False
                i += 1
                j += 1
            
            return True


        def place_queen(col, lst):
            before, after = col, n - (col + 1)
            bdots = ['.'] * before
            bdots = ''.join(bdots)
            bdots += 'Q'
            adots = ['.'] * after
            adots = ''.join(adots)
            bdots += adots
            lst.append(bdots)
            

        def remove_queen(lst):
            lst.pop()

        
        dfs(0)
        return sol